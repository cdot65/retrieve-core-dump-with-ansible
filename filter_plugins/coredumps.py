class FilterModule(object):

    def filters(self):
        return {
            'coredumps': self.coredumps,
        }

    def coredumps(self, value):
        list_of_coredumps = []
        for each in value['parsed_output']['multi-routing-engine-results']:
            for item in each['multi-routing-engine-item']:
                for directory in item['directory-list']:
                    for each in directory['directory']:
                        for each_file in each['file-information']:
                            for file_name in each_file['file-name']:
                                list_of_coredumps.append(file_name['data'])
        
        return list_of_coredumps
