using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour
{

    public int speed = 10;
    public int horizontalSpeed = 10;

    public int ID = 0;

    public int posX = -1;
    public int previousX = -1;

    public int posY;
    public int previousY;


    public void Move()
    {
        transform.Translate(Vector3.forward * horizontalSpeed * Time.deltaTime * 1);
    }


    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
            Move();

    }

}
