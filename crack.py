#!/usr/bin/env python

import crypt, sys
import optparse

parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="file", help="wordlist para bruteforce")
v = optparse.Values()
(options, args) = parser.parse_args(values=v)

try:
	if len(v.__dict__) == 0:
		print "Voce precisa passar uma wordlist!"
		sys.exit()
	wordlist = options.file
	f = open(wordlist)
	hash = raw_input("Digite o hash: ")
	tmp = hash
	tmp = tmp.split("$")
	salt = "$"+tmp[1]+"$"+tmp[2]+"$"
	for word in f.readlines():
		word = word.strip()
		print "Tentando %s"%word
		if crypt.crypt(word, salt) == hash:
			print "Senha encontrada: %s"%word
			sys.exit()
	print "Senha nao encontrada. :-("
except IOError:
	print "Arquivo inexistente, tente novamente!"
except KeyboardInterrupt:
	print "\nUsuario parou, saindo..."
