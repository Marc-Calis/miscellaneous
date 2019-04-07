import xmlrpc.client

root = 'http://%s:%d/xmlrpc/' % ("server-057.endoxa.private", 8069)
uid = xmlrpc.client.ServerProxy(root + 'common').login("odoo_demo_v12_be", "marc.calis@gmail.com", "dmn45678")
print("Logged in as %s (uid: %d)" % ("USER", uid))

print("ok")
# python3 odoo_xmlrpc.py