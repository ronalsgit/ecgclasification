import src.encryption.key as key
import res.values.value as val

def serializeData(pub_key, priv_key, data):
	encrypted_data_list = [([pub_key.encrypt(x) for x in n]) for n in data]

	encrypted_data={}
	encrypted_data['public_key'] = {'n': pub_key.n}
	encrypted_data['value'] = [([((x.ciphertext()), x.exponent) for x in n]) for n in encrypted_data_list]
	#encrypted_data['value'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_data_list]
	
	return encrypted_data

def encrypt(path, data):
	pub_key, priv_key = key.getKeys()
	encrypted_data = serializeData(pub_key, priv_key, data)

	val.savePickleFile(path, encrypted_data)
	if False: val.saveJsonFile(path, encrypted_data)

	return encrypted_data

