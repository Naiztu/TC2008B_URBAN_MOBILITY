using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour
{

    public int speed = 10;
    public int horizontalSpeed = 10;
    public int ID = 0;
    public Vector3 limitPosition = new Vector3(0, -50, 0);
    public Vector3 limitPositionRight = new Vector3(25, 0, 0);
    public Vector3 limitPositionLeft = new Vector3(5, 0, 0);
    public int posy;
    public int previousPosy;
    public int posx = -1;
    public int previousPosx = -1;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (transform.position.y >= limitPosition.y)
        {
            Destroy(gameObject);
        }
        else
        {
            Move();

        }

    }

    public void Move()
    {
        transform.Translate(Vector3.forward * horizontalSpeed * Time.deltaTime * 1);
    }
}
