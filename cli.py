import argparse
from main import (
    add_application,
    list_applications,
    update_application_status,
    delete_application,
    get_stats,
    search_applications,
    export_to_csv
)


def handle_add(args):
    add_application(
        args.company,
        args.position,
        args.salary,
        args.status,
        args.date,
        args.link,
        args.notes
    )
    print("Application added.")


def handle_list(args):
    applications = list_applications()

    if not applications:
        print("No applications found.")
        return

    for app in applications:
        print(f"""
ID: {app['id']}
Company: {app['company']}
Position: {app['position']}
Status: {app['application_status']}
Date: {app['date_applied']}
""")


def handle_update(args):
    update_application_status(args.id, args.status)
    print("Application updated.")


def handle_delete(args):
    delete_application(args.id)
    print("Application deleted.")

def stats_command(args):
    total, applied, rejected, accepted = get_stats()
    print(f"Total Applications: {total}")
    print(f"Applied : {applied}")
    print(f"Rejected : {rejected}")
    print(f"Accepted : {accepted}")
    if total > 0:
        response_rate = ((accepted + rejected) / total) * 100
        print(f"\nResponse Rate: %{response_rate:.1f}")
def search_command(args):
    applications = search_applications(args.q)
    if not applications:
        print("no matching applications found.")
        return
    for app in applications:
        print(f"""
ID: {app['id']}
Company: {app['company']}
Position: {app['position']}
Status: {app['application_status']}
Date: {app['date_applied']}
""")
def handler_export(args):
    export_to_csv(args.filename)
def main():

    parser = argparse.ArgumentParser(
        description="Job Application Tracker CLI"
    )

    subparsers = parser.add_subparsers()


    # ADD
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--company", required=True)
    add_parser.add_argument("--position", required=True)
    add_parser.add_argument("--status", required=True)
    add_parser.add_argument("--salary", type=int, required=True)
    add_parser.add_argument("--date", required=True)
    add_parser.add_argument("--link", required=True)
    add_parser.add_argument("--notes")
    add_parser.set_defaults(func=handle_add)


    # LIST
    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(func=handle_list)


    # UPDATE
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--status", required=True)
    update_parser.set_defaults(func=handle_update)


    # DELETE
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)
    delete_parser.set_defaults(func=handle_delete)

    #STATS
    stat_parser = subparsers.add_parser("get_stats")
    stat_parser.set_defaults(func=stats_command)

    #SEARCH
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("--q",required=True,help="Keyboard to search")
    search_parser.set_defaults(func=search_command)

    #EXPORT
    export_parser = subparsers.add_parser("export")
    export_parser.add_argument("--filename",default="applications.csv",help="File name to export")
    export_parser.set_defaults(func=handler_export)


    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()