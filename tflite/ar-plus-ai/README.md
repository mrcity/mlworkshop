# Tensorflow Lite + Sceneform Android App Example

A simple Android example that demonstrates mixing object detection from camera images with an augmented reality interpretation of the scene so as to draw 3D objects on recognized objects.

## Media You Should See

See the slide deck at https://www.slideshare.net/StephenWylie3/fusing-artificial-intelligence-with-augmented-reality-on-android-1-feb-2019 .

See the video of the presentation at `TBD`.

## Steps to Build

### Install Prerequisites

1. Download the Tensorflow source from GitHub or Docker.

2. Follow the [Bazel steps for the TF Demo App](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android#bazel)
  
[Install Bazel and Android Prerequisites](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android#install-bazel-and-android-prerequisites).
     It's easiest with Android Studio.

      - You'll need at least SDK version 28.
      - Make sure to install the latest version of Bazel. Some distributions
        ship with Bazel 0.5.4, which is too old.
      - Bazel requires Android Build Tools `28.0.3` or higher.
      - You also need to install the Android Support Repository, available
        through Android Studio under `Android SDK Manager -> SDK Tools ->
        Android Support Repository`.

3. [Edit your `WORKSPACE`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android#edit-workspace)
     to add SDK and NDK targets.

     NOTE: As long as you have the SDK and NDK installed, the `./configure`
     script will create these rules for you. Answer "Yes" when the script asks
     to automatically configure the `./WORKSPACE`.

      - Make sure the `api_level` in `WORKSPACE` is set to an SDK version that
        you have installed.
      - By default, Android Studio will install the SDK to `~/Android/Sdk` and
        the NDK to `~/Android/Sdk/ndk-bundle`.

4. Install Java JDK 10.  (Not 8, and not 11, possibly until Bazel gets upgraded.)

5. If you are on Windows, install the appropriate Visual C++ SDK.

### Build the Original Source with Bazel

Go to `tensorflow` and run at least `bazel build //tensorflow/lite/examples/android:tflite_demo`. A few additional options are listed below, such as configuring the fat_apk_cpu flag to package support for 4 hardware variants. You may replace it with --config=android_arm64 on a 64-bit device and --config=android_arm for 32-bit device:

  ```shell
  bazel build -c opt --cxxopt='--std=c++11' --fat_apk_cpu=x86,x86_64,arm64-v8a,armeabi-v7a \
    //tensorflow/lite/examples/android:tflite_demo
  ```

### Include libtensorflow.so dependency into this code

1. Clone this repository into a location of your choosing.  It does not have to be within your Tensorflow source code repository.

2. Find the `libtensorflow.so` shared library file on your computer.  It is located:

 - deep in your user directory where Bazel stores its temporary files, probably somewhere inside `execroot/org_tensorflow/bazel-out/android-(CPU architecture)-opt`
 - in the final APK file that gets built, if you open it as an archive -- probably inside `bazel-bin/` or also somewhere in your user directory

3. Move this file into the appropriate folder for the architecture for which the library was built -- usually this is `jniLibs/armeabi-v7a` but if you pulled it from the APK, you will probably find the name of the architecture from the folder it came from in a similar way as if it came from your user home folder as described above.

Build the app with Android Studio.  Once it installs, you might need to deal with a couple of crashes and force close issues while you grant it permissions to your camera, but upon doing this, you should be able to restart it and it should work just fine.  Also if exceptions in the logcat show that it's complaining about not finding files that appear to be in the assets/ directory, just "Rebuild All" and redeploy.
