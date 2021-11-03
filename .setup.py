import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='ecedi',  
     version='0.1',
     scripts=['ecedi'] ,
     author="Marcelo Mora",
     author_email="marcelo.mora@hotmail.es",
     description="Ecuadorian electronic invoicing helper methods",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/marcelomora/ecedi",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
