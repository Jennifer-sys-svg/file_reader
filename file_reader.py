def read_and_modify_file():
    try:
        # Ask user for the input file name
        input_filename = input("Enter the name of the file you want to read: ")

        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content - for example, convert it to uppercase
        modified_content = content.upper()

        # Create a new file name
        output_filename = "modified_" + input_filename

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"\n✅ Successfully read from '{input_filename}' and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print("\n❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("\n❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
