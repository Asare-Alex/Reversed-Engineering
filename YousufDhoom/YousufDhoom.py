import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))