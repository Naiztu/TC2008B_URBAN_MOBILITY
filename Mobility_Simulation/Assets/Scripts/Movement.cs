using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour
{

    public int speed = 10;
    public int horizontalSpeed = 10;

    public int ID = 0;

    public int posX = 0;
    public int previousX = 0;

    public int posY;
    public int previousY;

    public Vector3 currentPos;
    public Vector3 targetPos;




    public void Move()
    {

      transform.position = Vector3.Lerp(transform.position, new Vector3(posX, 0, posY), 2f);

      //transform.Translate(Vector3.Lerp(currentPos, new Vector3(0, 0, (posY + 3)), 0.1f));

      //Debug.Log("Movement - Current Pos = " + currentPos);
      //transform.position = Vector3.Lerp(transform.position, new Vector3(posX, 0, posY), 10f);

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
