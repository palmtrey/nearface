import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nearface",
    version="0.1.4",
    author="Cameron Palmer",
    author_email="palmtrey779@gmail.com",
    description="A refined version of the Python library DeepFace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/palmtrey/nearface",
    packages=setuptools.find_packages(),
    scripts=['nearface/models/face-recognition-ensemble-model.txt'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.5.5',
    install_requires=["numpy>=1.14.0", "pandas>=0.23.4", "tqdm>=4.30.0", "gdown>=3.10.1", "Pillow>=5.2.0", "opencv-python>=3.4.4", "tensorflow>=1.9.0", "keras>=2.2.0", "Flask>=1.1.2", "mtcnn>=0.1.0", "retina-face>=0.0.1"]
)
