#
# Convert current docker-compose.yml to docker-compose-result.yml for
# used by MLSteam annotations
#

import yaml
from yaml import safe_dump, safe_load

class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


with open("docker-compose.yml", 'rt') as f:
    compose_file_data = safe_load(f)

for (name, service) in compose_file_data['services'].items():
    cn = service['container_name']
    compose_file_data['services'][name]['container_name'] = "${CVAT_UUID}-"+cn
    volumes = service.get('volumes')
    if volumes:
        volumes_result = []
        for volume in volumes:
            vol_src = volume.split(':')[0]
            if '/' not in vol_src:
                volume = "${CVAT_ROOT}/"+vol_src+":"+volume.split(':')[1]
            volumes_result.append(volume)
        compose_file_data['services'][name]['volumes'] = volumes_result
    envs = service.get('environment')
    if envs:
        if isinstance(envs, dict):
            envs_result = {}
            for env_key, env_value in envs.items():
                if env_key in ['DJANGO_LOG_VIEWER_HOST', 'DJANGO_LOG_VIEWER_PORT', 'DJANGO_LOG_SERVER_HOST', 'DJANGO_LOG_SERVER_PORT']:
                    continue

                envs_result.update({env_key: env_value})
            compose_file_data['services'][name]['environment'] = envs_result
            print("envs:{}".format(envs_result))

# remove volumes section
del compose_file_data['volumes']
# set network external
compose_file_data['networks']['cvat'] = { 'external': True, 'name': '${MLSTEAM_NET}' }
# set prefix url
envs = compose_file_data['services']['cvat_ui'].get('environment')
if not envs:
    envs = {}
envs.update({
    'PREFIX_URL': '${CVAT_BASE_URL}'
})
compose_file_data['services']['cvat_ui']['environment'] = envs
envs = compose_file_data['services']['cvat_server'].get('environment')
if not envs:
    envs = {}
envs.update({
    'PREFIX_URL': '${CVAT_BASE_URL}'
})
compose_file_data['services']['cvat_server']['environment'] = envs
# delete CVAT_BASE_URL env
#del compose_file_data['services']['cvat_server']['environment']['CVAT_BASE_URL']
# delete grafana
if compose_file_data['services'].get('cvat_grafana'):
    del compose_file_data['services']['cvat_grafana']
if compose_file_data['services'].get('cvat_worker_analytics_reports'):
    del compose_file_data['services']['cvat_worker_analytics_reports']
del compose_file_data['services']['cvat_vector']
del compose_file_data['services']['cvat_clickhouse']
del compose_file_data['services']['traefik']['ports']

with open('docker-compose-result.yml', 'wt') as f:
    yaml.dump(compose_file_data, f, Dumper=IndentDumper, sort_keys=False, allow_unicode=True)

