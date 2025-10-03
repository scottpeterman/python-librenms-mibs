# SNMP MIB module (RAJANT-CORPORATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\rajant\RAJANT-CORPORATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:10 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rajantCorporation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34861)
)
if mibBuilder.loadTexts:
    rajantCorporation.setRevisions(
        ("2024-02-21 00:00",
         "2022-02-25 00:00",
         "2013-08-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34861, 1)
)
if mibBuilder.loadTexts:
    system.setStatus("current")
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 34861, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_SystemTemperature_Type = Integer32
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34861, 1, 2),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")
_FreeMemory_Type = Gauge32
_FreeMemory_Object = MibScalar
freeMemory = _FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 34861, 1, 3),
    _FreeMemory_Type()
)
freeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMemory.setStatus("current")
_Idle_Type = TimeTicks
_Idle_Object = MibScalar
idle = _Idle_Object(
    (1, 3, 6, 1, 4, 1, 34861, 1, 4),
    _Idle_Type()
)
idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idle.setStatus("current")
_Uptime_Type = TimeTicks
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 1, 5),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("current")
_Instamesh_ObjectIdentity = ObjectIdentity
instamesh = _Instamesh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34861, 2)
)
if mibBuilder.loadTexts:
    instamesh.setStatus("current")
_InstameshArpDropped_Type = Counter64
_InstameshArpDropped_Object = MibScalar
instameshArpDropped = _InstameshArpDropped_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 1),
    _InstameshArpDropped_Type()
)
instameshArpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshArpDropped.setStatus("current")
_InstameshArpRequests_Type = Counter64
_InstameshArpRequests_Object = MibScalar
instameshArpRequests = _InstameshArpRequests_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 2),
    _InstameshArpRequests_Type()
)
instameshArpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshArpRequests.setStatus("current")
_InstameshArpRequestsAnswered_Type = Counter64
_InstameshArpRequestsAnswered_Object = MibScalar
instameshArpRequestsAnswered = _InstameshArpRequestsAnswered_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 3),
    _InstameshArpRequestsAnswered_Type()
)
instameshArpRequestsAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshArpRequestsAnswered.setStatus("current")
_InstameshArpRequestsUnicasted_Type = Counter64
_InstameshArpRequestsUnicasted_Object = MibScalar
instameshArpRequestsUnicasted = _InstameshArpRequestsUnicasted_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 4),
    _InstameshArpRequestsUnicasted_Type()
)
instameshArpRequestsUnicasted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshArpRequestsUnicasted.setStatus("current")
_InstameshArpTotal_Type = Counter64
_InstameshArpTotal_Object = MibScalar
instameshArpTotal = _InstameshArpTotal_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 5),
    _InstameshArpTotal_Type()
)
instameshArpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshArpTotal.setStatus("current")
_InstameshFloodsDropped_Type = Counter64
_InstameshFloodsDropped_Object = MibScalar
instameshFloodsDropped = _InstameshFloodsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 6),
    _InstameshFloodsDropped_Type()
)
instameshFloodsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshFloodsDropped.setStatus("current")
_InstameshPacketsDropped_Type = Counter64
_InstameshPacketsDropped_Object = MibScalar
instameshPacketsDropped = _InstameshPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 7),
    _InstameshPacketsDropped_Type()
)
instameshPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshPacketsDropped.setStatus("current")
_InstameshPacketsMulticast_Type = Counter64
_InstameshPacketsMulticast_Object = MibScalar
instameshPacketsMulticast = _InstameshPacketsMulticast_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 8),
    _InstameshPacketsMulticast_Type()
)
instameshPacketsMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshPacketsMulticast.setStatus("current")
_InstameshPacketsReceived_Type = Counter64
_InstameshPacketsReceived_Object = MibScalar
instameshPacketsReceived = _InstameshPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 9),
    _InstameshPacketsReceived_Type()
)
instameshPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshPacketsReceived.setStatus("current")
_InstameshPacketsSent_Type = Counter64
_InstameshPacketsSent_Object = MibScalar
instameshPacketsSent = _InstameshPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 10),
    _InstameshPacketsSent_Type()
)
instameshPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshPacketsSent.setStatus("current")
_InstameshSourceFloodsDropped_Type = Counter64
_InstameshSourceFloodsDropped_Object = MibScalar
instameshSourceFloodsDropped = _InstameshSourceFloodsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 11),
    _InstameshSourceFloodsDropped_Type()
)
instameshSourceFloodsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshSourceFloodsDropped.setStatus("current")
_InstameshTimeWaited_Type = Counter64
_InstameshTimeWaited_Object = MibScalar
instameshTimeWaited = _InstameshTimeWaited_Object(
    (1, 3, 6, 1, 4, 1, 34861, 2, 12),
    _InstameshTimeWaited_Type()
)
instameshTimeWaited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instameshTimeWaited.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34861, 3)
)
if mibBuilder.loadTexts:
    wireless.setStatus("current")
_Wlan0_ObjectIdentity = ObjectIdentity
wlan0 = _Wlan0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34861, 3, 1)
)
if mibBuilder.loadTexts:
    wlan0.setStatus("current")
_Wlan0name_Type = OctetString
_Wlan0name_Object = MibScalar
wlan0name = _Wlan0name_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 1, 1),
    _Wlan0name_Type()
)
wlan0name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0name.setStatus("current")
_Wlan0frequency_Type = Integer32
_Wlan0frequency_Object = MibScalar
wlan0frequency = _Wlan0frequency_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 1, 2),
    _Wlan0frequency_Type()
)
wlan0frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0frequency.setStatus("current")
_Wlan0noise_Type = Integer32
_Wlan0noise_Object = MibScalar
wlan0noise = _Wlan0noise_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 1, 3),
    _Wlan0noise_Type()
)
wlan0noise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0noise.setStatus("current")
_Wlan0channelActiveTime_Type = TimeTicks
_Wlan0channelActiveTime_Object = MibScalar
wlan0channelActiveTime = _Wlan0channelActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 1, 4),
    _Wlan0channelActiveTime_Type()
)
wlan0channelActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0channelActiveTime.setStatus("current")
_Wlan0channelBusyTime_Type = TimeTicks
_Wlan0channelBusyTime_Object = MibScalar
wlan0channelBusyTime = _Wlan0channelBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 1, 5),
    _Wlan0channelBusyTime_Type()
)
wlan0channelBusyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0channelBusyTime.setStatus("current")
_Wlan0channelReceiveTime_Type = TimeTicks
_Wlan0channelReceiveTime_Object = MibScalar
wlan0channelReceiveTime = _Wlan0channelReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 1, 6),
    _Wlan0channelReceiveTime_Type()
)
wlan0channelReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0channelReceiveTime.setStatus("current")
_Wlan0channelTransmitTime_Type = TimeTicks
_Wlan0channelTransmitTime_Object = MibScalar
wlan0channelTransmitTime = _Wlan0channelTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 1, 7),
    _Wlan0channelTransmitTime_Type()
)
wlan0channelTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0channelTransmitTime.setStatus("current")
_Wlan1_ObjectIdentity = ObjectIdentity
wlan1 = _Wlan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34861, 3, 2)
)
if mibBuilder.loadTexts:
    wlan1.setStatus("current")
_Wlan1name_Type = OctetString
_Wlan1name_Object = MibScalar
wlan1name = _Wlan1name_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 2, 1),
    _Wlan1name_Type()
)
wlan1name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1name.setStatus("current")
_Wlan1frequency_Type = Integer32
_Wlan1frequency_Object = MibScalar
wlan1frequency = _Wlan1frequency_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 2, 2),
    _Wlan1frequency_Type()
)
wlan1frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1frequency.setStatus("current")
_Wlan1noise_Type = Integer32
_Wlan1noise_Object = MibScalar
wlan1noise = _Wlan1noise_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 2, 3),
    _Wlan1noise_Type()
)
wlan1noise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1noise.setStatus("current")
_Wlan1channelActiveTime_Type = TimeTicks
_Wlan1channelActiveTime_Object = MibScalar
wlan1channelActiveTime = _Wlan1channelActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 2, 4),
    _Wlan1channelActiveTime_Type()
)
wlan1channelActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1channelActiveTime.setStatus("current")
_Wlan1channelBusyTime_Type = TimeTicks
_Wlan1channelBusyTime_Object = MibScalar
wlan1channelBusyTime = _Wlan1channelBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 2, 5),
    _Wlan1channelBusyTime_Type()
)
wlan1channelBusyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1channelBusyTime.setStatus("current")
_Wlan1channelReceiveTime_Type = TimeTicks
_Wlan1channelReceiveTime_Object = MibScalar
wlan1channelReceiveTime = _Wlan1channelReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 2, 6),
    _Wlan1channelReceiveTime_Type()
)
wlan1channelReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1channelReceiveTime.setStatus("current")
_Wlan1channelTransmitTime_Type = TimeTicks
_Wlan1channelTransmitTime_Object = MibScalar
wlan1channelTransmitTime = _Wlan1channelTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 2, 7),
    _Wlan1channelTransmitTime_Type()
)
wlan1channelTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1channelTransmitTime.setStatus("current")
_Wlan2_ObjectIdentity = ObjectIdentity
wlan2 = _Wlan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34861, 3, 3)
)
if mibBuilder.loadTexts:
    wlan2.setStatus("current")
_Wlan2name_Type = OctetString
_Wlan2name_Object = MibScalar
wlan2name = _Wlan2name_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 3, 1),
    _Wlan2name_Type()
)
wlan2name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2name.setStatus("current")
_Wlan2frequency_Type = Integer32
_Wlan2frequency_Object = MibScalar
wlan2frequency = _Wlan2frequency_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 3, 2),
    _Wlan2frequency_Type()
)
wlan2frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2frequency.setStatus("current")
_Wlan2noise_Type = Integer32
_Wlan2noise_Object = MibScalar
wlan2noise = _Wlan2noise_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 3, 3),
    _Wlan2noise_Type()
)
wlan2noise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2noise.setStatus("current")
_Wlan2channelActiveTime_Type = TimeTicks
_Wlan2channelActiveTime_Object = MibScalar
wlan2channelActiveTime = _Wlan2channelActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 3, 4),
    _Wlan2channelActiveTime_Type()
)
wlan2channelActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2channelActiveTime.setStatus("current")
_Wlan2channelBusyTime_Type = TimeTicks
_Wlan2channelBusyTime_Object = MibScalar
wlan2channelBusyTime = _Wlan2channelBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 3, 5),
    _Wlan2channelBusyTime_Type()
)
wlan2channelBusyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2channelBusyTime.setStatus("current")
_Wlan2channelReceiveTime_Type = TimeTicks
_Wlan2channelReceiveTime_Object = MibScalar
wlan2channelReceiveTime = _Wlan2channelReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 3, 6),
    _Wlan2channelReceiveTime_Type()
)
wlan2channelReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2channelReceiveTime.setStatus("current")
_Wlan2channelTransmitTime_Type = TimeTicks
_Wlan2channelTransmitTime_Object = MibScalar
wlan2channelTransmitTime = _Wlan2channelTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 3, 7),
    _Wlan2channelTransmitTime_Type()
)
wlan2channelTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2channelTransmitTime.setStatus("current")
_Wlan3_ObjectIdentity = ObjectIdentity
wlan3 = _Wlan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34861, 3, 4)
)
if mibBuilder.loadTexts:
    wlan3.setStatus("current")
_Wlan3name_Type = OctetString
_Wlan3name_Object = MibScalar
wlan3name = _Wlan3name_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 4, 1),
    _Wlan3name_Type()
)
wlan3name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3name.setStatus("current")
_Wlan3frequency_Type = Integer32
_Wlan3frequency_Object = MibScalar
wlan3frequency = _Wlan3frequency_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 4, 2),
    _Wlan3frequency_Type()
)
wlan3frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3frequency.setStatus("current")
_Wlan3noise_Type = Integer32
_Wlan3noise_Object = MibScalar
wlan3noise = _Wlan3noise_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 4, 3),
    _Wlan3noise_Type()
)
wlan3noise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3noise.setStatus("current")
_Wlan3channelActiveTime_Type = TimeTicks
_Wlan3channelActiveTime_Object = MibScalar
wlan3channelActiveTime = _Wlan3channelActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 4, 4),
    _Wlan3channelActiveTime_Type()
)
wlan3channelActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3channelActiveTime.setStatus("current")
_Wlan3channelBusyTime_Type = TimeTicks
_Wlan3channelBusyTime_Object = MibScalar
wlan3channelBusyTime = _Wlan3channelBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 4, 5),
    _Wlan3channelBusyTime_Type()
)
wlan3channelBusyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3channelBusyTime.setStatus("current")
_Wlan3channelReceiveTime_Type = TimeTicks
_Wlan3channelReceiveTime_Object = MibScalar
wlan3channelReceiveTime = _Wlan3channelReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 4, 6),
    _Wlan3channelReceiveTime_Type()
)
wlan3channelReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3channelReceiveTime.setStatus("current")
_Wlan3channelTransmitTime_Type = TimeTicks
_Wlan3channelTransmitTime_Object = MibScalar
wlan3channelTransmitTime = _Wlan3channelTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 3, 4, 7),
    _Wlan3channelTransmitTime_Type()
)
wlan3channelTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3channelTransmitTime.setStatus("current")
_Gps_ObjectIdentity = ObjectIdentity
gps = _Gps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34861, 4)
)
if mibBuilder.loadTexts:
    gps.setStatus("current")
_GpsDate_Type = OctetString
_GpsDate_Object = MibScalar
gpsDate = _GpsDate_Object(
    (1, 3, 6, 1, 4, 1, 34861, 4, 1),
    _GpsDate_Type()
)
gpsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsDate.setStatus("current")
_GpsTime_Type = OctetString
_GpsTime_Object = MibScalar
gpsTime = _GpsTime_Object(
    (1, 3, 6, 1, 4, 1, 34861, 4, 2),
    _GpsTime_Type()
)
gpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTime.setStatus("current")
_GpsLongitude_Type = OctetString
_GpsLongitude_Object = MibScalar
gpsLongitude = _GpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 34861, 4, 3),
    _GpsLongitude_Type()
)
gpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLongitude.setStatus("current")
_GpsLatitude_Type = OctetString
_GpsLatitude_Object = MibScalar
gpsLatitude = _GpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 34861, 4, 4),
    _GpsLatitude_Type()
)
gpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLatitude.setStatus("current")
_GpsAltitude_Type = OctetString
_GpsAltitude_Object = MibScalar
gpsAltitude = _GpsAltitude_Object(
    (1, 3, 6, 1, 4, 1, 34861, 4, 5),
    _GpsAltitude_Type()
)
gpsAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAltitude.setStatus("current")
_GpsSpeedKnots_Type = OctetString
_GpsSpeedKnots_Object = MibScalar
gpsSpeedKnots = _GpsSpeedKnots_Object(
    (1, 3, 6, 1, 4, 1, 34861, 4, 6),
    _GpsSpeedKnots_Type()
)
gpsSpeedKnots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSpeedKnots.setStatus("current")
_GpsSatellites_Type = Integer32
_GpsSatellites_Object = MibScalar
gpsSatellites = _GpsSatellites_Object(
    (1, 3, 6, 1, 4, 1, 34861, 4, 7),
    _GpsSatellites_Type()
)
gpsSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatellites.setStatus("current")
_GpsValid_Type = Integer32
_GpsValid_Object = MibScalar
gpsValid = _GpsValid_Object(
    (1, 3, 6, 1, 4, 1, 34861, 4, 8),
    _GpsValid_Type()
)
gpsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsValid.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAJANT-CORPORATION-MIB",
    **{"rajantCorporation": rajantCorporation,
       "system": system,
       "serialNumber": serialNumber,
       "systemTemperature": systemTemperature,
       "freeMemory": freeMemory,
       "idle": idle,
       "uptime": uptime,
       "instamesh": instamesh,
       "instameshArpDropped": instameshArpDropped,
       "instameshArpRequests": instameshArpRequests,
       "instameshArpRequestsAnswered": instameshArpRequestsAnswered,
       "instameshArpRequestsUnicasted": instameshArpRequestsUnicasted,
       "instameshArpTotal": instameshArpTotal,
       "instameshFloodsDropped": instameshFloodsDropped,
       "instameshPacketsDropped": instameshPacketsDropped,
       "instameshPacketsMulticast": instameshPacketsMulticast,
       "instameshPacketsReceived": instameshPacketsReceived,
       "instameshPacketsSent": instameshPacketsSent,
       "instameshSourceFloodsDropped": instameshSourceFloodsDropped,
       "instameshTimeWaited": instameshTimeWaited,
       "wireless": wireless,
       "wlan0": wlan0,
       "wlan0name": wlan0name,
       "wlan0frequency": wlan0frequency,
       "wlan0noise": wlan0noise,
       "wlan0channelActiveTime": wlan0channelActiveTime,
       "wlan0channelBusyTime": wlan0channelBusyTime,
       "wlan0channelReceiveTime": wlan0channelReceiveTime,
       "wlan0channelTransmitTime": wlan0channelTransmitTime,
       "wlan1": wlan1,
       "wlan1name": wlan1name,
       "wlan1frequency": wlan1frequency,
       "wlan1noise": wlan1noise,
       "wlan1channelActiveTime": wlan1channelActiveTime,
       "wlan1channelBusyTime": wlan1channelBusyTime,
       "wlan1channelReceiveTime": wlan1channelReceiveTime,
       "wlan1channelTransmitTime": wlan1channelTransmitTime,
       "wlan2": wlan2,
       "wlan2name": wlan2name,
       "wlan2frequency": wlan2frequency,
       "wlan2noise": wlan2noise,
       "wlan2channelActiveTime": wlan2channelActiveTime,
       "wlan2channelBusyTime": wlan2channelBusyTime,
       "wlan2channelReceiveTime": wlan2channelReceiveTime,
       "wlan2channelTransmitTime": wlan2channelTransmitTime,
       "wlan3": wlan3,
       "wlan3name": wlan3name,
       "wlan3frequency": wlan3frequency,
       "wlan3noise": wlan3noise,
       "wlan3channelActiveTime": wlan3channelActiveTime,
       "wlan3channelBusyTime": wlan3channelBusyTime,
       "wlan3channelReceiveTime": wlan3channelReceiveTime,
       "wlan3channelTransmitTime": wlan3channelTransmitTime,
       "gps": gps,
       "gpsDate": gpsDate,
       "gpsTime": gpsTime,
       "gpsLongitude": gpsLongitude,
       "gpsLatitude": gpsLatitude,
       "gpsAltitude": gpsAltitude,
       "gpsSpeedKnots": gpsSpeedKnots,
       "gpsSatellites": gpsSatellites,
       "gpsValid": gpsValid}
)
