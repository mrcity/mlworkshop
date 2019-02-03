# Tensorflow Lite + Sceneform Android App Example

A simple Android example that demonstrates mixing object detection from camera images with an augmented reality interpretation of the scene so as to draw 3D objects on recognized objects.

## Media You Should See

See the [slide deck on SlideShare](https://www.slideshare.net/StephenWylie3/fusing-artificial-intelligence-with-augmented-reality-on-android-1-feb-2019).

See the video of the presentation at `TBD`.

## Steps to Build

Note: Steps 1 and 2 are to be run from the main Tensorflow source directory.  **Do not run** commands on this repository until you get to Step 3.

Also note that I have slightly optimized the number of steps required for you to build this project for yourself.  As such, it is not exactly the same procedure as described in the video and slides.  Specifically, these steps save you from having to build with Gradle *before* building with Bazel.

### Install Prerequisites

1. Download the Tensorflow source from [GitHub](https://github.com/tensorflow/tensorflow) or [Docker](https://www.tensorflow.org/install/docker).  If you are using Docker, pick a `devel` branch -- do not use "latest" since it will not have the source code.

2. Install Java JDK 10.  (Not 8, and not 11, possibly until Bazel gets upgraded.)  Set up `$JAVA_HOME` as an environment variable in the usual manner, and put `$JAVA_HOME/bin` on your `PATH`.

3. Follow the [Bazel steps for the TF Demo App](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android#bazel).  Ignore the part where it says you can't build Android apps with Bazel on Windows.  You can; this repo will show you how.
  
    a. [Install Bazel and Android Prerequisites](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android#install-bazel-and-android-prerequisites).
     It's easiest with the **latest version** of Android Studio.

       - You'll need at least SDK version 28.
       - Also get NDK version 19.
       - Make sure to install the latest version of Bazel. Some distributions
        ship with Bazel 0.5.4, which is too old.
       - Bazel requires Android Build Tools `28.0.3` or higher.
       - Install the latest version of the Gradle plugin.
       - You also need to install the Android Support Repository, available
        through Android Studio under `Android SDK Manager -> SDK Tools ->
        Android Support Repository`.


    b. [Edit your `WORKSPACE`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android#edit-workspace)
     in `tensorflow/` to add SDK and NDK targets.

     NOTE: As long as you have the SDK and NDK installed, the `./configure`
     script will create these rules for you. Answer "Yes" when the script asks
     to automatically configure the `./WORKSPACE`.

      - Make sure the `api_level` in `WORKSPACE` is set to an SDK version that
        you have installed.
      - By default, Android Studio will install the SDK to `~/Android/Sdk` and
        the NDK to `~/Android/Sdk/ndk-bundle`.

    c. If you didn't run `./configure` (or `python configure.py` for Windows users) as indicated in the previous step, run it from your `tensorflow/` directory in order to set up the Bazel build.

4. If you are on Windows:

    a. Install the [appropriate Visual C++ SDK](https://go.microsoft.com/fwlink/?LinkId=691126).  From this EXE (`visualcppbuildtools_full.exe`), if you are on Windows 10, choose `Windows 10 SDK` and `.NET Framework SDK`.

    b. Go to `C:\Program Files (x86)\Windows Kits\`*(version number, e.g. `10`)*`\`.  It is possible that the SDK version you installed (likely 10.0.10240) is below another one that is already installed.  If this is the case, you will need to copy the the directories underneath `Lib` and `Include` of this directory (especially `ucrt` and `um`) into the highest version SDK (first moving the originals out of the way by renaming them with a suffix, possibly) so that you will not experience dependency issues during the Bazel build.

### Build the Original Source with Bazel

Go to `tensorflow/` and run at least `bazel build //tensorflow/lite/examples/android:tflite_demo`. A few additional options are listed below, such as configuring the fat_apk_cpu flag to package support for 4 hardware variants and which C++ compiler to use. You may replace it with --config=android_arm64 on a 64-bit device and --config=android_arm for 32-bit device, but the flags are purely optional and are not required for a successful build.

  ```shell
  bazel build -c opt --cxxopt='--std=c++11' --fat_apk_cpu=x86,x86_64,arm64-v8a,armeabi-v7a \
    //tensorflow/lite/examples/android:tflite_demo
  ```
  
  If your Bazel build fails along the way, search Google to try to remedy it.  If you find the remedy didn't work, sometimes it is useful to clear the Bazel cache.
  
  1. Shutdown any running Bazel processes with `bazel suutdown`.
  
  2. Go into your user home directory (such as `C:\Users\me`) and  delete the entire `_bazel_`*(username)* directory.
  
  3. Retry your Bazel build.

### Include libtensorflow.so dependency into this code

1. Clone this repository into a location of your choosing.  It does not have to be within your Tensorflow source code repository.

2. Find the `libtensorflow.so` shared library file on your computer.  It is located:

 - deep in your user home directory where Bazel stores its temporary files, probably somewhere inside `execroot/org_tensorflow/bazel-out/android-`*(CPU architecture)*`-opt`
 - in the final APK file that gets built, if you open it as an archive -- probably inside `bazel-bin/` or also somewhere in your user directory

3. Move this file into the appropriate folder for the architecture for which the library was built -- usually this is `jniLibs/armeabi-v7a` but if you pulled it from the APK, you will probably find the name of the architecture from the folder it came from in a similar way as if it came from your user home folder as described above.

### Make It Yours

Build the app with Android Studio.  Once it installs, you might need to deal with a couple of crashes and force close issues while you grant it permissions to your camera, but upon doing this, you should be able to restart it and it should work just fine.  Also if exceptions in the logcat show that it's complaining about not finding files that appear to be in the assets/ directory, just "Rebuild All" and redeploy.

## If You Do Anything Cool With This

Let me know so I can give it a try!  Easiest way is on Twitter at [@SWebCEO](https://twitter.com/SWebCEO).

## The Final Result

![Image of the app doing object detection and putting in 3D objects](app.png?raw=true "App Working")
