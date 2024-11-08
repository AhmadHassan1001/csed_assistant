## Computer Networks - Lecture 01: Introduction

### Course Information

* **Instructor:** Prof. Dr. Sahar M. Ghanem, Associate Professor
* **Department:** Computer and Systems Engineering Department
* **University:** Faculty of Engineering, Alexandria University
* **Textbook:** Computer Networking: A Top-Down Approach, 8th ed., Kurose & Ross

### Course Outline

* **Grading:**
    * Attendance & Participation: 5-7%
    * Assignments & Quizzes: 40%
    * Midterm: 15%
    * Final: 40%
* **Join with Code:** 142tcab
* **Course Materials & Discussions:** MS Teams
* **Teaching Assistant:** Eng. Mohamed Essam

### Chapter 1: Computer Networks and the Internet

#### Outline

* What is the Internet?
* The Network Edge
* The Network Core
* Delay, Loss, and Throughput in Packet-Switched Networks
* Protocol Layers and Their Service Models

#### What is the Internet?

* The Internet is a **network of networks**.
* We will use the **public Internet** as the basis for our discussion. 

#### Nuts-and-Bolts Description

* The Internet interconnects **billions of computing devices** worldwide.
* These devices are called **hosts** or **end systems**.
* Estimated number of devices: 18 billion in 2017, reaching **28.5 billion by 2022**.
* End systems are connected by a network of **communication links** and **packet switches**.
* **Packet switches** forward packets received on incoming links to outgoing links.
* Common types of packet switches: **routers** and **link-layer switches**.
* The path a packet takes is called a **route** or **path**.
* **Internet Service Providers (ISPs)** provide access to the Internet.
* ISPs themselves are **networks** of packet switches and links.
* Devices on the Internet run **protocols**.
* Key protocols: **Transmission Control Protocol (TCP)** and **Internet Protocol (IP)**.
* **Internet standards** are developed by the **Internet Engineering Task Force (IETF)**.
* IETF standards documents are called **Requests for Comments (RFCs)**.
*  There are nearly **9000 RFCs**.
* Other organizations also specify standards, such as the **IEEE 802 LAN Standards Committee**.

#### Services Description

* The Internet is an **infrastructure** that provides services to **distributed applications**.
* Internet applications run on **end systems**. They do **not** run on packet switches.
* End systems provide a **socket interface**. This defines how applications request data delivery.
* The Internet provides **multiple services** to its applications.

#### What is a Protocol?

* Two or more entities need to run the same **protocol** to accomplish a task.
* **Human protocols** involve specific messages and actions based on replies or events.
* This course focuses on **computer network protocols**.
* A **protocol** defines the format and order of messages exchanged between entities, as well as actions taken during transmission and reception.

#### The Network Edge

* **End Systems:** 
    * Include **desktop computers** (PCs, Macs, Linux boxes), **servers** (Web, email), and **mobile devices** (laptops, smartphones, tablets).
    * Also include **"things"** (non-traditional devices) connected to the Internet.
    * End systems are also known as **hosts** because they host application programs.
    * Hosts are categorized as **clients** and **servers**.
    * Most servers reside in **data centers**. Google has 19 data centers worldwide, containing millions of servers.

#### Access Networks

* **Home Access:**
    * **DSL (Digital Subscriber Line):** Uses existing telephone lines. Requires a **DSL modem** and **DSLAM (Digital Subscriber Line Access Multiplexer)** in the telco's central office (CO).
        * Downstream rates: 24 Mbps and 52 Mbps.
        * Upstream rates: 3.5 Mbps and 16 Mbps.
        * Newest standard: 1 Gbps.
    * **Cable Internet:** Utilizes existing cable television infrastructure.
        * Downstream rates: 40 Mbps and 1.2 Gbps.
        * Upstream rates: 30 Mbps and 100 Mbps.
    * **Fiber to the Home (FTTH):** Provides very high speeds in the gigabit per second range.
    * **5G Fixed Wireless:**  Offers high-speed access without requiring physical cabling.

* **Enterprise/Home Access:**
    * **Ethernet:** Uses twisted-pair copper wire to connect to an **Ethernet switch**.
        * Users typically have 100 Mbps to tens of Gbps access.
        * Servers may have 1 Gbps to 10 Gbps access.
    * **WiFi (Wireless Fidelity):**  Based on IEEE 802.11 technology.
        * Requires a **WiFi access point** and a **home router**.
        * Shared transmission rate: Up to over 100 Mbps.

* **Wide-Area Wireless Access:**
    * **3G, LTE 4G, and 5G:** Uses cellular telephony infrastructure.
        * Requires a **base station**.
        * 4G: Download speeds up to 60 Mbps.
        * 5G: Even higher speeds.

#### Physical Media

* Bits travel through a series of transmitter-receiver pairs using a **physical medium**.
* Physical media are classified as **guided** or **unguided**:
    * **Guided Media:** Electromagnetic waves or optical pulses travel through a solid medium, such as fiber-optic cables, twisted-pair copper wire, or coaxial cables.
    * **Unguided Media:** Waves propagate through the atmosphere or outer space, such as in wireless LANs or satellite channels.

#### The Network Core

* The network core consists of **packet switches** (primarily **routers**).
* Routers are connected to the network edge through **access networks**.

#### Packet Switching

* End systems exchange **messages**.
* Messages are divided into **packets**.
* Packets travel through **communication links** and **packet switches**.
* Most packet switches use **store-and-forward transmission**. They receive the entire packet before forwarding it.
* **Output buffers/queues** store packets waiting to be sent on a specific link.
* Packets experience **store-and-forward delay** and **queuing delay**. Queuing delay depends on the level of **congestion**.
* **Packet loss** can occur if the buffer space is full, resulting in a dropped packet.

#### Forwarding Tables and Routing Protocols

* Routers use **forwarding tables** to determine the appropriate outgoing link for a packet.
* **IP addresses** are used to identify hosts and have a hierarchical structure.
* The destination's **IP address** is included in the packet header.
* **Routing protocols** are used to automatically set up forwarding tables.

#### Circuit Switching

* **Traditional telephone networks** are circuit-switched networks.
* **Circuit-switched networks** reserve resources (buffers, transmission rate) along a path for the duration of a communication session.
* A dedicated **end-to-end connection** is established between hosts.
* The sender can transmit data at a **guaranteed constant rate**.
* The Internet uses a **best-effort** approach to deliver packets, without guarantees.

#### Multiplexing in Circuit-Switched Networks

* **Frequency-division multiplexing (FDM)** and **time-division multiplexing (TDM)** are used to share a link between multiple connections.
* **FDM:** Each connection gets a dedicated frequency band.
* **TDM:** Time is divided into frames, and each frame is further divided into slots. Each connection gets a dedicated slot within each frame.

#### Packet Switching vs. Circuit Switching

* **Packet switching:**
    * **Advantages:** Better sharing of transmission capacity, simpler and more efficient implementation, and lower cost.
    * **Disadvantage:** Not suitable for real-time services.
* **Circuit switching:**
    * **Advantages:**  Guaranteed constant rate.
    * **Disadvantages:**  Pre-allocates resources, wasting unused time, and is more complex.

#### A Network of Networks

* The Internet has evolved into a **complex network of networks**.
* This evolution is driven by **economics** and **national policy**.
* **Network Structures:**
    * **Structure 1:** Single global transit ISP connecting all access ISPs (expensive).
    * **Structure 2:** Two-tier hierarchy, with multiple global transit ISPs competing for access ISPs.
    * **Structure 3:** Multi-tier hierarchy, with regional ISPs connecting access ISPs within a region.
    * **Structure 4:**  Adds **Points of Presence (PoPs)**, **multi-homing**, and **peering** to the hierarchy.
    * **Structure 5:** Builds on Structure 4 and includes **content-provider networks**.

#### Delay, Loss, and Throughput

* **Delay:**
    * **Processing delay:**  Microseconds or less.
    * **Queuing delay:** Microseconds to milliseconds, depending on the number of packets waiting.
    * **Transmission delay:** L/R (packet length divided by transmission rate).
    * **Propagation delay:** d/s (distance divided by propagation speed).
    * **Nodal delay:** The sum of all delay components at a node.
* **Loss:**
    * Packets can be dropped if the buffer is full.
    * **Packet loss** is dependent on **traffic intensity** and the **nature of the arriving traffic**.
* **Throughput:**
    * The amount of data transferred per second.
    * **Bottleneck links** limit throughput.
    * In the core of the Internet, throughput is limited by **access networks**.

#### Protocol Layers

* Network protocols are organized into **layers**.
* Layers provide services by performing certain actions and utilizing services from lower layers.
* **Layers:**
    * **Application Layer:**  Where network applications and their protocols reside.
    * **Transport Layer:** Transports application messages between endpoints.
        * **UDP:**  Connectionless service.
        * **TCP:** Connection-oriented service with guaranteed delivery, flow control, and congestion control.
    * **Network Layer:** Moves network packets (datagrams) between hosts.
        * Contains **routing protocols**.
    * **Link Layer:** Delivers datagrams to the next node along the route.
        * Uses different link-layer protocols for different links.
    * **Physical Layer:** Moves individual bits within a frame between nodes.
        * Dependent on the transmission medium.

#### Encapsulation

* Layers encapsulate information from higher layers.
* **Application Layer:** Messages are encapsulated into **transport-layer segments**.
* **Transport Layer:** Segments are encapsulated into **network-layer datagrams**.
* **Network Layer:** Datagrams are encapsulated into **link-layer frames**.

* This layered architecture is used by hosts, routers, and link-layer switches, with each having its own specific layers.

#### Summary

* This lecture covered the fundamentals of computer networks, including the Internet's structure, how data is transmitted, and the different types of delays and throughput.
* The lecture also introduced the concept of protocol layering and how it helps organize network protocols.
* The key takeaways are:
    * The Internet is a network of networks.
    * Packet switching is more efficient than circuit switching but not suitable for real-time services.
    * Network performance is affected by delays, loss, and throughput.
    * Protocol layers provide a structured approach to designing and implementing network protocols.