import src.encryption.key as key
import phe as paillier
import res.values.value as val

def serializeData(pub_key, priv_key, data):
	decrypted_data= []
	try:
		for n in range(len(data['value'])):
			decrypted = []
			for x in range(len(data['value'][n])):
				answer = (paillier.EncryptedNumber(pub_key, int(data['value'][n][x][0]), int(data['value'][n][x][1])))
				decrypted.append(priv_key.decrypt(answer))
			decrypted_data.append(decrypted)
	except:
			decrypted_data = priv_key.decrypt(data)

	return decrypted_data

def decrypt(path, data):
	pub_key, priv_key = key.getKeys()
	decrypted_data = serializeData(pub_key, priv_key, data)

	if not None : val.savePickleFile(path, decrypted_data)
	if False: val.saveJsonFile(path, decrypted_data)

	return decrypted_data

