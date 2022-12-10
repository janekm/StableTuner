import os
import argparse
import glob
import shutil

def main(args):
    input_dir = args.input_dir
    output_dir = args.output_dir

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for images_dir in glob.glob(os.path.join(input_dir, "*")):
        base_prompt = os.path.basename(images_dir)
        print(f"Processing base prompt: {base_prompt}")

        for img_file in glob.glob(os.path.join(images_dir, "*.png")) + glob.glob(os.path.join(images_dir, "*.jpg")):
            img_file = os.path.basename(img_file)
            base_caption = os.path.splitext(img_file)[0]
            caption_file_name = os.path.join(images_dir, base_caption + ".txt")
            caption = ""
            with open(caption_file_name, "r") as f:
                caption = f.read().strip()
            caption = base_prompt + ", " + caption
            print(f"full caption: {caption}")
            output_file_name = os.path.join(output_dir, base_caption + ".txt")
            with open(output_file_name, "w") as f:
                f.write(caption)
            shutil.copy(os.path.join(images_dir, img_file), os.path.join(output_dir, img_file))
            img_fileb = base_caption + "b.jpg"
            shutil.copy(os.path.join(images_dir, img_fileb), os.path.join(output_dir, img_fileb))
            output_file_nameb = os.path.join(output_dir, base_caption + "b.txt")
            with open(output_file_nameb, "w") as f:
                f.write(base_prompt)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=str, help="directory containing directories of training images")
    parser.add_argument("output_dir", type=str, help="output directory")
    # parser.add_argument("--debug", action="store_true", help="debug mode")

    args = parser.parse_args()
    main(args)
