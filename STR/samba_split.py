# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    samba_cut = smb_path.lstrip('//')
    cut_index = samba_cut.find('/')
    ip = samba_cut[:cut_index]
    route = samba_cut[cut_index:]
    
    host = ip
    path = route

    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')