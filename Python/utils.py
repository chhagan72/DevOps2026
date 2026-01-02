


# def get_environment(config):
#     return config.get("app", {}).get("environment", "dev")
# env = get_environment(config)
# print(env)

def check_environment(config):
    return config.get("app", {}).get("environment", "dev")
    

def great():
    print("Welcome to DevOps automation")
    
def check_port(config):
    return config.get("server", {}).get("port")
    