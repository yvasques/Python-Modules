#!/usr/bin/env python3

def secure_archive(
        filename: str,
        action: str = "read",
        content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "write":
            with open(filename, "w") as file_obj:
                file_obj.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(filename, "r") as file_obj:
                file_content: str = file_obj.read()
            return (True, file_content)
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    res1: tuple[bool, str] = secure_archive("/not/existing/file")
    print(res1)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    res2: tuple[bool, str] = secure_archive("secretfile")
    print(res2)

    print("\nUsing 'secure_archive' to read from a regular file:")
    res3: tuple[bool, str] = secure_archive("teste.txt")
    print(res3)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if res3[0]:
        res4: tuple[bool, str] = secure_archive(
            "new_file.txt",
            action="write",
            content=res3[1]
        )
        print(res4)


if __name__ == "__main__":
    main()
