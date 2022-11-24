import phe as paillier
import res.values.value as val

def storeKeys(n_length = 2048, private_keyring = None):	
	public_key, private_key = paillier.generate_paillier_keypair(private_keyring, n_length)
	keys={}
	keys['public_key'] = {'n': public_key.n}
	keys['private_key'] = {'p': private_key.p,'q':private_key.q}

	val.savePickleFile(val.fileName.key, keys)
	return keys
	
def getKeys():
	try:
		keys = val.loadPickleFile(val.fileName.key)
	except:
		keys = storeKeys()

	pub_key=paillier.PaillierPublicKey(n=int(keys['public_key']['n']))
	priv_key=paillier.PaillierPrivateKey(pub_key,keys['private_key']['p'],keys['private_key']['q'])
	return pub_key, priv_key