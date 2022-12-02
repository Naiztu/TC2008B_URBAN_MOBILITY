using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class Spawner : MonoBehaviour
{
    public GameObject gameManager;

    public GameObject Carro;

    public GameObject AltCarro;

    int numCar;

    List<int> carIDs = new List<int>();

    public Agent a;

    // Start is called before the first frame update
    void Start()
    {
        InvokeRepeating("Create", 0.0f, 3f);
    }

    // Update is called once per frame
    void Update()
    {
        a = UrbanMobility.a;
    }

    public void Create()
    {
        for (int i = 0; i < a.positions.Count; i++)
        {
            if (!carIDs.Contains(a.positions[i].unique_id))
            {
                carIDs.Add(a.positions[i].unique_id);
                GameObject carro =
                    Instantiate(Carro,
                    new Vector3(a.positions[i].pos.x == 0
                            ? -4
                            : a.positions[i].pos.x == 1 ? 0 : 4,
                        0,
                        0),
                    Quaternion.identity);
                carro.GetComponent<Movement>().ID = a.positions[i].unique_id;
            }
        }
    }
}
