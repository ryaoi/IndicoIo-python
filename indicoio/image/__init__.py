from importlib import import_module
IMAGE_APIS = {
    name: getattr(import_module(".{0}".format(name), package="indicoio.image"), name)
        for name in [
            "content_filtering",
            "facial_features",
            "facial_localization",
            "fer",
            "image_features",
            "image_recognition"
        ]
}
globals().update(IMAGE_APIS)
