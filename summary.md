# Computer Networks - Lecture 01: Introduction

## Course Details

- **Instructor:** Prof. Dr. Sahar M. Ghanem
- **Department:** Computer and Systems Engineering Department
- **University:** Faculty of Engineering, Alexandria University
- **Textbook:** Computer Networking: A Top-Down Approach, 8th ed., Kurose & Ross
- **Grading:**
    - Attendance & Participation: 5-7%
    - Assignments & Quizzes: 40%
    - Midterm: 15%
    - Final: 40%
- **Join Code:** 142tcab
- **Course Materials & Discussions:** MS Teams
- **Teaching Assistant:** Eng. Mohamed Essam

## Lecture Outline

- What is the Internet?
- The Network Edge
- The Network Core
- Delay, Loss, and Throughput in Packet-Switched Networks
- Protocol Layers and Their Service Models

## What is the Internet?

- The Internet is a network of networks that interconnects billions of computing devices around the world.
- These devices are called **hosts** or **end systems**.
- The number of devices connected to the Internet is estimated to reach 28.5 billion by 2022.
- End systems are connected by a network of communication links and **packet switches**.
    - **Packet switches** take a packet arriving on one of their incoming links and forward it to one of their outgoing links.
- The two most prominent types of packet switches in the Internet are **routers** and **link-layer switches**.
- The sequence of communication links and packet switches a packet travels through is known as a **route** or **path**.
- End systems access the Internet through **Internet Service Providers (ISPs)**.
    - Each ISP is itself a network of packet switches and communication links.
- End systems, packet switches, and other parts of the Internet run **protocols**.
    - The **Transmission Control Protocol (TCP)** and **Internet Protocol (IP)** are two of the most important protocols in the Internet.
    - **TCP/IP** refers collectively to the Internet's primary protocols.
- **Internet standards** are developed by the **Internet Engineering Task Force (IETF)**.
    - IETF standards documents are called **requests for comments (RFCs)**.
    - There are currently nearly 9000 RFCs.
- Other bodies also specify standards for network components, such as the **IEEE 802 LAN Standards Committee**.

## The Network Edge

- The Internet's **end systems** include desktop computers, servers, and mobile devices, as well as increasingly non-traditional "things".
- End systems are also known as **hosts** because they host application programs.
- Hosts can be categorized as **clients** or **servers**.
- Most servers reside in large **data centers**.
    - Google, for example, has 19 data centers on four continents, collectively containing several million servers.

### Access Networks

- **Home Access:**
    - **DSL (Digital Subscriber Line):** Uses existing telephone lines to exchange data with a **DSLAM (Digital Subscriber Line Access Multiplexer)** located in the telco's central office (CO).
        - Carries data and traditional telephone signals simultaneously, encoded at different frequencies:
            - High-speed downstream channel: 50 kHz to 1 MHz
            - Medium-speed upstream channel: 4 kHz to 50 kHz
            - Ordinary two-way telephone channel: 0 to 4 kHz
        - A **splitter** separates the data and telephone signals on the customer side.
        - On the telco side, the **DSLAM** separates the data and phone signals and sends the data to the Internet.
        - Supports downstream rates of 24 Mbps and 52 Mbps, and upstream rates of 3.5 Mbps and 16 Mbps.
        - Newest standards offer aggregate upstream + downstream rates of 1 Gbps.
        - Designed for short distances between the home and CO (5 to 10 miles).
    - **Cable Internet:** Uses existing cable television infrastructure.
        - Often referred to as **HFC (Hybrid Fiber Coax)**.
        - Shared broadcast medium.
        - Offers downstream rates of 40 Mbps and 1.2 Gbps, and upstream rates of 30 Mbps and 100 Mbps.
    - **FTTH (Fiber to the Home):** Provides even higher speeds, potentially reaching gigabits per second.
    - **5G Fixed Wireless:** Promises high-speed residential access without the need for cabling.

- **Enterprise/Home Access:**
    - **Ethernet:** Uses twisted-pair copper wire to connect devices to an **Ethernet switch**.
        - Users typically have 100 Mbps to tens of Gbps access.
        - Servers may have 1 Gbps to 10 Gbps access.
    - **WiFi:** Uses IEEE 802.11 technology.
        - Requires users to be within a few tens of meters of the **access point**.
        - Shared transmission rate of up to 100 Mbps.
        - Common in homes, consisting of:
            - Roaming laptop, appliances, and wired PC.
            - **WiFi Access Point:** Communicates with wireless devices.
            - **Home Router:** Connects the access point and other devices to the Internet.

- **Wide-Area Wireless Access:**
    - **3G/LTE 4G/5G:** Uses the same wireless infrastructure as **cellular telephony** to send/receive packets through a **base station**.
        - Users must be within a few tens of kilometers of the base station.
        - 4G offers download speeds up to 60 Mbps.
        - 5G promises even higher speeds.

### Physical Media

- A bit travels from source to destination through transmitter-receiver pairs by propagating electromagnetic waves or optical pulses across a **physical medium**.
- **Physical media** fall into two categories:
    - **Guided Media:** Waves are guided along a solid medium, such as fiber-optic cable, twisted-pair copper wire, or coaxial cable.
    - **Unguided Media:** Waves propagate in the atmosphere or outer space, such as in wireless LANs or digital satellite channels.

## The Network Core

- The **Network Core** consists of the packet switches and communication links that connect the ISPs.
- **Packet Switching:**
    - End systems exchange **messages** with each other.
    - Messages are broken into smaller chunks called **packets**.
    - Packets travel through communication links and **packet switches**, including routers and link-layer switches.
    - Most packet switches use **store-and-forward transmission**, where the entire packet is received before any part is transmitted.
    - Each packet consists of **L bits**.
    - Transmission rate is **R bits/sec**.
    - **End-to-End Delay** for sending one packet over **N links** is **NL/R** (ignoring propagation delay).
    - Each packet switch has an **output buffer/queue** to store packets before sending them to the next link.
    - Packet switches also experience **queuing delays** depending on network congestion.
    - Due to finite buffer space, **packet loss** occurs when a packet arrives and the buffer is full.
    - Routers use **forwarding tables** to determine which link to forward a packet to.
        - Each end system has an **IP address** with a hierarchical structure.
        - The **destination's IP address** is included in the packet header.
        - **Routing protocols** are used to automatically set forwarding tables.

- **Circuit Switching:**
    - Traditional telephone networks use circuit switching.
    - Resources along a path (buffers, transmission rate) are **reserved** for the duration of a communication session.
    - A dedicated **end-to-end connection** is established between two hosts.
    - The sender can transfer data at a **guaranteed** constant rate.
    - The Internet uses a **best-effort** approach, not providing guarantees.
    - **Multiplexing** in circuit-switched networks can be implemented with:
        - **FDM (Frequency-Division Multiplexing):** Each circuit gets a continuous portion of the bandwidth.
        - **TDM (Time-Division Multiplexing):** Each circuit gets all the bandwidth periodically during brief intervals.
    - Circuit switching is wasteful because dedicated circuits are idle during silent periods.
    - Establishing end-to-end circuits is complex and requires **signaling software**.

## A Network of Networks

- The Internet's complex structure has evolved due to economics and national policy.
- **Naive Approach:** Each access ISP directly connects to every other access ISP.
- **Network Structure 1:** Interconnects all access ISPs with a single **global transit ISP**.
- **Network Structure 2 (Two-Tier Hierarchy):** Hundreds of thousands of access ISPs and multiple global transit ISPs, competing based on pricing and services.
- **Network Structure 3 (Multi-Tier Hierarchy):**
    - Regional ISPs connect access ISPs within a region.
    - Regional ISPs connect to **tier-1 ISPs** with a broader presence.
    - Access ISPs pay regional ISPs, who pay tier-1 ISPs.
    - Larger regional ISPs can connect smaller regional ISPs.
- **Network Structure 4:**
    - Includes **points of presence (PoPs):** Groups of routers where customer ISPs can connect to the provider ISP.
    - Allows for **multi-homing:** Connecting to multiple provider ISPs.
    - Enables **peering:** Nearby ISPs at the same level of hierarchy connect directly.
    - Utilizes **Internet exchange points (IXPs):** Third-party companies create meeting points for peering.
- **Network Structure 5:**
    - Builds on top of Structure 4 by adding **content-provider networks**.
    - Example: Google data centers are interconnected via a private TCP/IP network spanning the globe, separate from the public Internet.

## Delay, Loss, and Throughput

- **Delay:**
    - The physical laws introduce **delay** and **loss** and constrain **throughput**.
    - **Throughput** is the amount of data transferred per second.
    - Packets experience several types of delay at each node:
        - **Processing Delay:** Microseconds or less.
        - **Queuing Delay:** Microseconds to milliseconds, depending on the number of packets in the queue.
        - **Transmission Delay:** L/R (packet length L bits, transmission rate R bps).
        - **Propagation Delay:** d/s (distance between routers, propagation speed).
    - **Nodal Delay** is the sum of these components: dnodal = dproc + dqueue + dtrans + dprop.
    - The contribution of each delay component can vary significantly.
        - Example: Propagation delay is negligible in LANs but significant in satellite networks.
        - Processing delay is often negligible but influences a router's maximum throughput.

- **Queuing Delay and Packet Loss:**
    - Queuing delay depends on:
        - The rate at which traffic arrives (a packets/sec).
        - The transmission rate of the link (R bps).
        - The nature of the arriving traffic (periodic or bursty).
    - **Traffic Intensity:** La/R.
        - If La/R > 1, the queue will increase unboundedly, and queuing delay approaches infinity.
        - If La/R < 1, the nature of arriving traffic impacts queuing delay.
            - Periodic traffic results in no queuing delay.
            - Bursty traffic can cause significant queuing delays.
    - Small percentage increases in traffic intensity can lead to large percentage increases in delay.
    - Network performance is measured in terms of delay and the probability of packet loss.

- **End-to-End Delay:**
    - Assuming N-1 routers and no queuing delay, the end-to-end delay is dend-to-end = N(dproc + dtrans + dprop).
    - **Traceroute** is a program that helps determine the route and delays between a source and destination.
        - It sends special packets to the destination and receives messages back from each router, reconstructing the route and round-trip delays.

- **Throughput:**
    - The **throughput** of a file transfer with F bits and T seconds is F/T bits/sec.
    - Bits can be thought of as fluid, and links as pipes.
    - The **bottleneck link** determines the throughput.
    - In a simple two-link network, throughput is min{Rc, Rs}.
    - In a multi-link network with N links, throughput is min{R1, R2, ..., RN}.
    - When there is no other traffic, throughput is approximated as the minimum transmission rate along the path.
    - Links in the core of the network have very high transmission rates.
    - **Access networks** often constrain throughput.

## Protocol Layers

- Network designers organize protocols into **layers**.
- Each layer can be implemented in software, hardware, or a combination.
    - Application-layer and transport-layer protocols are usually software-based.
    - Physical layer and data link layer protocols are typically hardware-based.
    - Network layer is often a combination of both.
- **Drawbacks of Layering:**
    - One layer might duplicate functionality from another layer.
    - One layer might require information present only in another layer.

### Protocol Layering Model

- **Application Layer:** Handles network applications and their protocols.
    - Allows applications in different end systems to exchange messages.
    - Examples: HTTP, SMTP, FTP, DNS.

- **Transport Layer:** Transports application-layer messages between application endpoints.
    - Packets are called **segments** at this layer.
    - **UDP (User Datagram Protocol):** Provides a connectionless service.
    - **TCP (Transmission Control Protocol):** Provides a connection-oriented service, guaranteeing delivery, flow control, and congestion control.

- **Network Layer (IP Layer):** Moves network-layer packets called **datagrams** between hosts.
    - IP defines the datagram format and how routers handle it.
    - Includes **routing protocols** for determining datagram routes.

- **Link Layer:** Delivers datagrams to the next node along the route.
    - Handles communication over a specific link, typically implemented in a network interface card.
    - Datagrams might be handled by different link-layer protocols along the way.
    - Packets at this layer are called **frames**.
    - Examples: Ethernet, WiFi.

- **Physical Layer:** Moves individual bits within a frame from one node to the next.
    - Depends on the transmission medium used.
    - Examples: Different protocols for twisted-pair copper wire, coaxial cable, fiber, etc.

### Encapsulation

- The transport layer encapsulates the application-layer message, adding transport-layer information.
- The network layer encapsulates the transport-layer segment, adding network-layer header information (source and destination addresses).
- The link layer encapsulates the network-layer datagram, adding link-layer header information.

- Each layer adds its own information, resulting in a layered packet structure.

## Summary

- The Internet is a complex network of interconnected networks.
- Access networks provide connections to the Internet for end systems.
- Packet switching is the primary method used in the Internet, offering efficiency and flexibility.
- Protocol layers organize network protocols, simplifying development and maintenance.
- Encapsulation allows layers to build upon each other, creating a layered packet structure.