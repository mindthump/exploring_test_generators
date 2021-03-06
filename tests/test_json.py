import json
import re


def interpret_json():
    steps = ["install", "stop", "configure", "start", "agents"]
    reply = '{"status": "ok", "out": {"code": 200, "out": {"new_cluster": true, "started": 1392381649, "state": "running", "finished": null, "cluster_id": "opscenter_aft_dev_test_pool", "details": {"subrequests": {"stop": {"started": 1392381771, "state": "success", "finished": 1392381772, "cluster_id": null, "details": {"subrequests": {"10.160.255.207": {"started": 1392381771, "state": "success", "finished": 1392381772, "cluster_id": null, "details": null, "id": "4eba5737-2876-436f-bfff-62937bec6db2"}, "10.168.53.237": {"started": 1392381771, "state": "success", "finished": 1392381772, "cluster_id": null, "details": null, "id": "51c08484-ce02-4507-9e5a-f9ce8cb4c15b"}, "10.176.11.79": {"started": 1392381772, "state": "success", "finished": 1392381772, "cluster_id": null, "details": null, "id": "86a7800f-b937-4a48-8e0a-8b3380bd08be"}}}, "id": "998155b3-8383-47b0-a455-c78f6f457ea7"}, "start": {"started": 1392381772, "state": "success", "finished": 1392381802, "cluster_id": null, "details": {"subrequests": {"10.160.255.207": {"started": 1392381772, "state": "success", "finished": 1392381781, "cluster_id": null, "details": null, "id": "160c7ae2-dc0f-46a6-82c3-c85a226c702a"}, "10.168.53.237": {"started": 1392381781, "state": "success", "finished": 1392381793, "cluster_id": null, "details": null, "id": "a4f85946-2d76-4d77-b0a4-b451c405be62"}, "10.176.11.79": {"started": 1392381793, "state": "success", "finished": 1392381802, "cluster_id": null, "details": null, "id": "2b5d1125-9866-4543-9d03-c348b8f40909"}}}, "id": "24068da0-6d8c-485c-85f0-4e879427ad43"}, "agents": {"started": 1392381805, "state": "running", "finished": null, "cluster_id": null, "details": {"subrequests": {"10.160.255.207": {"started": 1392381805, "state": "success", "finished": 1392381816, "cluster_id": null, "details": "Agent successfully connected.", "id": "21d6d601-e04f-4d73-baf4-74a62397248c"}, "10.168.53.237": {"started": 1392381805, "state": "running", "finished": null, "cluster_id": null, "details": "", "id": "bd985bd3-15cb-4e40-b1a0-3a12f38ce23f"}, "10.176.11.79": {"started": 1392381805, "state": "running", "finished": null, "cluster_id": null, "details": "", "id": "d24aa0e7-6c57-49c7-848f-000e11dcc93d"}}}, "id": "96a1d6d5-a3ff-49d5-a314-8d53b88dc898"}, "configure": {"started": 1392381772, "state": "success", "finished": 1392381772, "cluster_id": null, "details": null, "id": "c5013e44-8217-43eb-b6eb-84e857ad3003"}, "install": {"started": 1392381649, "state": "success", "finished": 1392381771, "cluster_id": null, "details": {"subrequests": {"10.160.255.207": {"started": 1392381670, "state": "success", "finished": 1392381742, "cluster_id": null, "details": null, "id": "e615468a-782c-4c69-be22-a9a986bcaed6"}, "10.168.53.237": {"started": 1392381672, "state": "success", "finished": 1392381771, "cluster_id": null, "details": null, "id": "b9590c77-c1a3-4a66-851f-960235cbccfb"}, "10.176.11.79": {"started": 1392381673, "state": "success", "finished": 1392381755, "cluster_id": null, "details": null, "id": "a0b745b7-0775-4125-9bb2-bb0c9ac879e1"}}}, "id": "a247532a-11ea-43a7-abe5-2db6b5e67fc2"}}}, "id": "cc54c18f-3c3d-48a1-a09f-11370b71e93a"}}}'
    # reply = '{"status":"ok","out":{"out":{"started":1389964693,"details":{"message":"Start stage failed: Failed to start node 10.170.163.66: Timed out waiting for app to start.","subrequests":{"stop":{"cluster_id":null,"state":"success","finished":1389964784,"details":{"subrequests":{"10.170.163.66":{"cluster_id":null,"state":"success","finished":1389964784,"details":null,"id":"b55afa1a-3ad5-4c34-9a83-14192a7e90bd","started":1389964783}}},"id":"23304d7a-f27b-4ebe-a8ee-ff24dca2b8ce","started":1389964783},"install":{"cluster_id":null,"state":"success","finished":1389964783,"details":{"subrequests":{"10.170.163.66":{"cluster_id":null,"state":"success","finished":1389964783,"details":null,"id":"87059814-330e-4200-9a27-f7436fdbd2da","started":1389964718}}},"id":"a0353509-5a5b-49d9-ae11-f8c91ebfeb3a","started":1389964693},"configure":{"cluster_id":null,"state":"success","finished":1389964786,"details":null,"id":"342e2ff1-725d-4d3a-933e-f51904259ae0","started":1389964784},"agents":null,"start":{"cluster_id":null,"state":"error","finished":1389964982,"details":{"message":"Failed to start node 10.170.163.66: Timed out waiting for app to start.","subrequests":{"10.170.163.66":{"cluster_id":null,"state":"error","finished":1389964982,"details":"Timed out waiting for app to start.","id":"ae1eb23f-0480-4a65-a309-62b62cfaca7d","started":1389964786}}},"id":"c9a58024-0d08-4f23-9cff-5d9c7d42b8a6","started":1389964786}}},"finished":1389964982,"cluster_id":"provisioning_automaton_node_pool","id":"4652202f-4a3b-4bda-a649-5d961d4ba26b","state":"error","new_cluster":true},"code":200}}'
    for step in steps:
        try:
            step_details = json.loads(reply)["out"]["out"]["details"]["subrequests"][
                step
            ]
            # print("{0}: {1}".format(step, step_details))
            if step_details:
                if step_details["state"] == "error":
                    print(
                        "{0}: step_details['state'] ('{1}')".format(
                            step,
                            json.loads(reply)["out"]["out"]["details"]["subrequests"][
                                step
                            ]["details"]["message"],
                        )
                    )
                else:
                    print(
                        "{0}: {1}".format(
                            step,
                            json.loads(reply)["out"]["out"]["details"]["subrequests"][
                                step
                            ]["state"],
                        )
                    )
            else:
                print("{}: None".format(step))
        except KeyError as ke:
            print("Missing key: {0}".format(ke))
            break


interpret_json()
