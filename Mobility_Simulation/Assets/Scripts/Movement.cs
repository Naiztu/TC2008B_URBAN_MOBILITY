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

    public int posY = 0;

    public int previousY = 0;

    public Vector3 currentPos;

    public Vector3 targetPos;

    public Agent a;

    public void Move()
    {
        a = UrbanMobility.a;
        bool flag = false;
        for (int i = 0; i < a.positions.Count; i++)
        {
            if (a.positions[i].unique_id == ID)
            {
                flag = true;
                posX =
                    a.positions[i].pos.x == 0
                        ? -4
                        : a.positions[i].pos.x == 1 ? 0 : 4;
                posY = (a.positions[i].pos.y * 5);
                break;
            }
        }
        if (a.state_num_cars == 0)
        {
            return;
        }

        if (flag)
        {
            currentPos = transform.position;
            targetPos = new Vector3(posX, 0, posY);
            transform.position =
                Vector3.Lerp(currentPos, targetPos, Time.deltaTime * 0.7f);

            // transform.position = Vector3.Lerp(currentPos, targetPos, 5f);
            previousX = posX;
            previousY = posY;
        }
        else
        {
            Destroy (gameObject);
        }
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
