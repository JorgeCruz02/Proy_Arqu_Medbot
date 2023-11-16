from view import GetUserDetailPrueba

#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def test_GetUserDetailPrueba():
    assert GetUserDetailPrueba("/login")==['prueb', 'python']
    
    
