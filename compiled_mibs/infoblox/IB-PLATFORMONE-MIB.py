# SNMP MIB module (IB-PLATFORMONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\infoblox\IB-PLATFORMONE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:47 2025
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

(IbFloat,
 IbIpAddr,
 IbString,
 ibPlatformOne) = mibBuilder.importSymbols(
    "IB-SMI-MIB",
    "IbFloat",
    "IbIpAddr",
    "IbString",
    "ibPlatformOne")

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

ibPlatformModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ibPlatformModule.setRevisions(
        ("2016-06-12 00:00",
         "2016-06-07 00:00",
         "2016-05-06 00:00",
         "2015-11-19 00:00",
         "2015-10-29 00:00",
         "2015-10-09 00:00",
         "2015-05-19 00:00",
         "2014-07-30 00:00",
         "2013-10-29 00:00",
         "2013-10-22 00:00",
         "2013-08-02 00:00",
         "2013-05-07 00:00",
         "2012-05-24 00:00",
         "2012-04-13 00:00",
         "2011-12-02 00:00",
         "2011-12-01 00:00",
         "2011-05-05 00:00",
         "2010-11-15 00:00",
         "2010-10-19 00:00",
         "2010-07-28 00:00",
         "2009-06-05 00:00",
         "2008-09-29 00:00",
         "2005-01-10 00:00",
         "2004-05-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IbServiceStates(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("warning", 2),
          ("failed", 3),
          ("inactive", 4),
          ("unknown", 5))
    )



class IbServiceNames(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("dns", 2),
          ("ntp", 3),
          ("tftp", 4),
          ("http-file-dist", 5),
          ("ftp", 6),
          ("bloxtools-move", 7),
          ("bloxtools", 8),
          ("node-status", 9),
          ("disk-usage", 10),
          ("enet-lan", 11),
          ("enet-lan2", 12),
          ("enet-ha", 13),
          ("enet-mgmt", 14),
          ("lcd", 15),
          ("memory", 16),
          ("replication", 17),
          ("db-object", 18),
          ("raid-summary", 19),
          ("raid-disk1", 20),
          ("raid-disk2", 21),
          ("raid-disk3", 22),
          ("raid-disk4", 23),
          ("raid-disk5", 24),
          ("raid-disk6", 25),
          ("raid-disk7", 26),
          ("raid-disk8", 27),
          ("fan1", 28),
          ("fan2", 29),
          ("fan3", 30),
          ("fan4", 31),
          ("fan5", 32),
          ("fan6", 33),
          ("fan7", 34),
          ("fan8", 35),
          ("power-supply1", 36),
          ("power-supply2", 37),
          ("ntp-sync", 38),
          ("cpu1-temp", 39),
          ("cpu2-temp", 40),
          ("sys-temp", 41),
          ("raid-battery", 42),
          ("cpu-usage", 43),
          ("ospf", 44),
          ("bgp", 45),
          ("mgm-service", 46),
          ("subgrid-conn", 47),
          ("network-capacity", 48),
          ("reporting", 49),
          ("dns-cache-acceleration", 50),
          ("ospf6", 51),
          ("swap-usage", 52),
          ("discovery-consolidator", 53),
          ("discovery-collector", 54),
          ("discovery-capacity", 55),
          ("threat-protection", 56),
          ("cloud-api", 57),
          ("threat-analytics", 58),
          ("taxii", 59),
          ("bfd", 60),
          ("outbound", 61))
    )



class IbSnicNames(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan1", 1),
          ("lan2", 2),
          ("ha", 3))
    )



# MIB Managed Objects in the order of their OIDs

_IbClusterReplicationStatusTable_Object = MibTable
ibClusterReplicationStatusTable = _IbClusterReplicationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ibClusterReplicationStatusTable.setStatus("current")
_IbClusterReplicationStatusEntry_Object = MibTableRow
ibClusterReplicationStatusEntry = _IbClusterReplicationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1)
)
ibClusterReplicationStatusEntry.setIndexNames(
    (0, "IB-PLATFORMONE-MIB", "ibNodeIPAddress"),
)
if mibBuilder.loadTexts:
    ibClusterReplicationStatusEntry.setStatus("current")
_IbNodeIPAddress_Type = IbIpAddr
_IbNodeIPAddress_Object = MibTableColumn
ibNodeIPAddress = _IbNodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 1),
    _IbNodeIPAddress_Type()
)
ibNodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeIPAddress.setStatus("current")
_IbNodeReplicationStatus_Type = IbString
_IbNodeReplicationStatus_Object = MibTableColumn
ibNodeReplicationStatus = _IbNodeReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 2),
    _IbNodeReplicationStatus_Type()
)
ibNodeReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeReplicationStatus.setStatus("current")
_IbNodeQueueFromMaster_Type = Integer32
_IbNodeQueueFromMaster_Object = MibTableColumn
ibNodeQueueFromMaster = _IbNodeQueueFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 3),
    _IbNodeQueueFromMaster_Type()
)
ibNodeQueueFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeQueueFromMaster.setStatus("current")
_IbNodeLastRepTimeFromMaster_Type = IbString
_IbNodeLastRepTimeFromMaster_Object = MibTableColumn
ibNodeLastRepTimeFromMaster = _IbNodeLastRepTimeFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 4),
    _IbNodeLastRepTimeFromMaster_Type()
)
ibNodeLastRepTimeFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeLastRepTimeFromMaster.setStatus("current")
_IbNodeQueueToMaster_Type = Integer32
_IbNodeQueueToMaster_Object = MibTableColumn
ibNodeQueueToMaster = _IbNodeQueueToMaster_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 5),
    _IbNodeQueueToMaster_Type()
)
ibNodeQueueToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeQueueToMaster.setStatus("current")
_IbNodeLastRepTimeToMaster_Type = IbString
_IbNodeLastRepTimeToMaster_Object = MibTableColumn
ibNodeLastRepTimeToMaster = _IbNodeLastRepTimeToMaster_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 6),
    _IbNodeLastRepTimeToMaster_Type()
)
ibNodeLastRepTimeToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeLastRepTimeToMaster.setStatus("current")
_IbNetworkMonitor_ObjectIdentity = ObjectIdentity
ibNetworkMonitor = _IbNetworkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3)
)
_IbNetworkMonitorDNS_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNS = _IbNetworkMonitorDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1)
)


class _IbNetworkMonitorDNSActive_Type(Integer32):
    """Custom type ibNetworkMonitorDNSActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonactive", 0),
          ("active", 1))
    )


_IbNetworkMonitorDNSActive_Type.__name__ = "Integer32"
_IbNetworkMonitorDNSActive_Object = MibScalar
ibNetworkMonitorDNSActive = _IbNetworkMonitorDNSActive_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 1),
    _IbNetworkMonitorDNSActive_Type()
)
ibNetworkMonitorDNSActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSActive.setStatus("current")
_IbNetworkMonitorDNSNonAA_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAA = _IbNetworkMonitorDNSNonAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2)
)
_IbNetworkMonitorDNSNonAAT1_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAAT1 = _IbNetworkMonitorDNSNonAAT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 1)
)
_IbNetworkMonitorDNSNonAAT1AvgLatency_Type = Integer32
_IbNetworkMonitorDNSNonAAT1AvgLatency_Object = MibScalar
ibNetworkMonitorDNSNonAAT1AvgLatency = _IbNetworkMonitorDNSNonAAT1AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 1, 1),
    _IbNetworkMonitorDNSNonAAT1AvgLatency_Type()
)
ibNetworkMonitorDNSNonAAT1AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT1AvgLatency.setStatus("current")
_IbNetworkMonitorDNSNonAAT1Count_Type = Integer32
_IbNetworkMonitorDNSNonAAT1Count_Object = MibScalar
ibNetworkMonitorDNSNonAAT1Count = _IbNetworkMonitorDNSNonAAT1Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 1, 2),
    _IbNetworkMonitorDNSNonAAT1Count_Type()
)
ibNetworkMonitorDNSNonAAT1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT1Count.setStatus("current")
_IbNetworkMonitorDNSNonAAT5_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAAT5 = _IbNetworkMonitorDNSNonAAT5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 2)
)
_IbNetworkMonitorDNSNonAAT5AvgLatency_Type = Integer32
_IbNetworkMonitorDNSNonAAT5AvgLatency_Object = MibScalar
ibNetworkMonitorDNSNonAAT5AvgLatency = _IbNetworkMonitorDNSNonAAT5AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 2, 1),
    _IbNetworkMonitorDNSNonAAT5AvgLatency_Type()
)
ibNetworkMonitorDNSNonAAT5AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT5AvgLatency.setStatus("current")
_IbNetworkMonitorDNSNonAAT5Count_Type = Integer32
_IbNetworkMonitorDNSNonAAT5Count_Object = MibScalar
ibNetworkMonitorDNSNonAAT5Count = _IbNetworkMonitorDNSNonAAT5Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 2, 2),
    _IbNetworkMonitorDNSNonAAT5Count_Type()
)
ibNetworkMonitorDNSNonAAT5Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT5Count.setStatus("current")
_IbNetworkMonitorDNSNonAAT15_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAAT15 = _IbNetworkMonitorDNSNonAAT15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 3)
)
_IbNetworkMonitorDNSNonAAT15AvgLatency_Type = Integer32
_IbNetworkMonitorDNSNonAAT15AvgLatency_Object = MibScalar
ibNetworkMonitorDNSNonAAT15AvgLatency = _IbNetworkMonitorDNSNonAAT15AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 3, 1),
    _IbNetworkMonitorDNSNonAAT15AvgLatency_Type()
)
ibNetworkMonitorDNSNonAAT15AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT15AvgLatency.setStatus("current")
_IbNetworkMonitorDNSNonAAT15Count_Type = Integer32
_IbNetworkMonitorDNSNonAAT15Count_Object = MibScalar
ibNetworkMonitorDNSNonAAT15Count = _IbNetworkMonitorDNSNonAAT15Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 3, 2),
    _IbNetworkMonitorDNSNonAAT15Count_Type()
)
ibNetworkMonitorDNSNonAAT15Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT15Count.setStatus("current")
_IbNetworkMonitorDNSNonAAT60_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAAT60 = _IbNetworkMonitorDNSNonAAT60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 4)
)
_IbNetworkMonitorDNSNonAAT60AvgLatency_Type = Integer32
_IbNetworkMonitorDNSNonAAT60AvgLatency_Object = MibScalar
ibNetworkMonitorDNSNonAAT60AvgLatency = _IbNetworkMonitorDNSNonAAT60AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 4, 1),
    _IbNetworkMonitorDNSNonAAT60AvgLatency_Type()
)
ibNetworkMonitorDNSNonAAT60AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT60AvgLatency.setStatus("current")
_IbNetworkMonitorDNSNonAAT60Count_Type = Integer32
_IbNetworkMonitorDNSNonAAT60Count_Object = MibScalar
ibNetworkMonitorDNSNonAAT60Count = _IbNetworkMonitorDNSNonAAT60Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 4, 2),
    _IbNetworkMonitorDNSNonAAT60Count_Type()
)
ibNetworkMonitorDNSNonAAT60Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT60Count.setStatus("current")
_IbNetworkMonitorDNSNonAAT1440_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAAT1440 = _IbNetworkMonitorDNSNonAAT1440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 5)
)
_IbNetworkMonitorDNSNonAAT1440AvgLatency_Type = Integer32
_IbNetworkMonitorDNSNonAAT1440AvgLatency_Object = MibScalar
ibNetworkMonitorDNSNonAAT1440AvgLatency = _IbNetworkMonitorDNSNonAAT1440AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 5, 1),
    _IbNetworkMonitorDNSNonAAT1440AvgLatency_Type()
)
ibNetworkMonitorDNSNonAAT1440AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT1440AvgLatency.setStatus("current")
_IbNetworkMonitorDNSNonAAT1440Count_Type = Integer32
_IbNetworkMonitorDNSNonAAT1440Count_Object = MibScalar
ibNetworkMonitorDNSNonAAT1440Count = _IbNetworkMonitorDNSNonAAT1440Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 5, 2),
    _IbNetworkMonitorDNSNonAAT1440Count_Type()
)
ibNetworkMonitorDNSNonAAT1440Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT1440Count.setStatus("current")
_IbNetworkMonitorDNSAA_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAA = _IbNetworkMonitorDNSAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3)
)
_IbNetworkMonitorDNSAAT1_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAAT1 = _IbNetworkMonitorDNSAAT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 1)
)
_IbNetworkMonitorDNSAAT1AvgLatency_Type = Integer32
_IbNetworkMonitorDNSAAT1AvgLatency_Object = MibScalar
ibNetworkMonitorDNSAAT1AvgLatency = _IbNetworkMonitorDNSAAT1AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 1, 1),
    _IbNetworkMonitorDNSAAT1AvgLatency_Type()
)
ibNetworkMonitorDNSAAT1AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT1AvgLatency.setStatus("current")
_IbNetworkMonitorDNSAAT1Count_Type = Integer32
_IbNetworkMonitorDNSAAT1Count_Object = MibScalar
ibNetworkMonitorDNSAAT1Count = _IbNetworkMonitorDNSAAT1Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 1, 2),
    _IbNetworkMonitorDNSAAT1Count_Type()
)
ibNetworkMonitorDNSAAT1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT1Count.setStatus("current")
_IbNetworkMonitorDNSAAT5_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAAT5 = _IbNetworkMonitorDNSAAT5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 2)
)
_IbNetworkMonitorDNSAAT5AvgLatency_Type = Integer32
_IbNetworkMonitorDNSAAT5AvgLatency_Object = MibScalar
ibNetworkMonitorDNSAAT5AvgLatency = _IbNetworkMonitorDNSAAT5AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 2, 1),
    _IbNetworkMonitorDNSAAT5AvgLatency_Type()
)
ibNetworkMonitorDNSAAT5AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT5AvgLatency.setStatus("current")
_IbNetworkMonitorDNSAAT5Count_Type = Integer32
_IbNetworkMonitorDNSAAT5Count_Object = MibScalar
ibNetworkMonitorDNSAAT5Count = _IbNetworkMonitorDNSAAT5Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 2, 2),
    _IbNetworkMonitorDNSAAT5Count_Type()
)
ibNetworkMonitorDNSAAT5Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT5Count.setStatus("current")
_IbNetworkMonitorDNSAAT15_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAAT15 = _IbNetworkMonitorDNSAAT15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 3)
)
_IbNetworkMonitorDNSAAT15AvgLatency_Type = Integer32
_IbNetworkMonitorDNSAAT15AvgLatency_Object = MibScalar
ibNetworkMonitorDNSAAT15AvgLatency = _IbNetworkMonitorDNSAAT15AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 3, 1),
    _IbNetworkMonitorDNSAAT15AvgLatency_Type()
)
ibNetworkMonitorDNSAAT15AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT15AvgLatency.setStatus("current")
_IbNetworkMonitorDNSAAT15Count_Type = Integer32
_IbNetworkMonitorDNSAAT15Count_Object = MibScalar
ibNetworkMonitorDNSAAT15Count = _IbNetworkMonitorDNSAAT15Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 3, 2),
    _IbNetworkMonitorDNSAAT15Count_Type()
)
ibNetworkMonitorDNSAAT15Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT15Count.setStatus("current")
_IbNetworkMonitorDNSAAT60_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAAT60 = _IbNetworkMonitorDNSAAT60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 4)
)
_IbNetworkMonitorDNSAAT60AvgLatency_Type = Integer32
_IbNetworkMonitorDNSAAT60AvgLatency_Object = MibScalar
ibNetworkMonitorDNSAAT60AvgLatency = _IbNetworkMonitorDNSAAT60AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 4, 1),
    _IbNetworkMonitorDNSAAT60AvgLatency_Type()
)
ibNetworkMonitorDNSAAT60AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT60AvgLatency.setStatus("current")
_IbNetworkMonitorDNSAAT60Count_Type = Integer32
_IbNetworkMonitorDNSAAT60Count_Object = MibScalar
ibNetworkMonitorDNSAAT60Count = _IbNetworkMonitorDNSAAT60Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 4, 2),
    _IbNetworkMonitorDNSAAT60Count_Type()
)
ibNetworkMonitorDNSAAT60Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT60Count.setStatus("current")
_IbNetworkMonitorDNSAAT1440_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAAT1440 = _IbNetworkMonitorDNSAAT1440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 5)
)
_IbNetworkMonitorDNSAAT1440AvgLatency_Type = Integer32
_IbNetworkMonitorDNSAAT1440AvgLatency_Object = MibScalar
ibNetworkMonitorDNSAAT1440AvgLatency = _IbNetworkMonitorDNSAAT1440AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 5, 1),
    _IbNetworkMonitorDNSAAT1440AvgLatency_Type()
)
ibNetworkMonitorDNSAAT1440AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT1440AvgLatency.setStatus("current")
_IbNetworkMonitorDNSAAT1440Count_Type = Integer32
_IbNetworkMonitorDNSAAT1440Count_Object = MibScalar
ibNetworkMonitorDNSAAT1440Count = _IbNetworkMonitorDNSAAT1440Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 5, 2),
    _IbNetworkMonitorDNSAAT1440Count_Type()
)
ibNetworkMonitorDNSAAT1440Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT1440Count.setStatus("current")
_IbNetworkMonitorDNSSecurity_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSSecurity = _IbNetworkMonitorDNSSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4)
)
_IbNetworkMonitorDNSSecurityInvalidPort_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSSecurityInvalidPort = _IbNetworkMonitorDNSSecurityInvalidPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1)
)
_IbNetworkMonitorDNSSecurityInvalidPort1_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidPort1_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPort1 = _IbNetworkMonitorDNSSecurityInvalidPort1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 1),
    _IbNetworkMonitorDNSSecurityInvalidPort1_Type()
)
ibNetworkMonitorDNSSecurityInvalidPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPort1.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPort5_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidPort5_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPort5 = _IbNetworkMonitorDNSSecurityInvalidPort5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 2),
    _IbNetworkMonitorDNSSecurityInvalidPort5_Type()
)
ibNetworkMonitorDNSSecurityInvalidPort5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPort5.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPort15_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidPort15_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPort15 = _IbNetworkMonitorDNSSecurityInvalidPort15_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 3),
    _IbNetworkMonitorDNSSecurityInvalidPort15_Type()
)
ibNetworkMonitorDNSSecurityInvalidPort15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPort15.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPort60_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidPort60_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPort60 = _IbNetworkMonitorDNSSecurityInvalidPort60_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 4),
    _IbNetworkMonitorDNSSecurityInvalidPort60_Type()
)
ibNetworkMonitorDNSSecurityInvalidPort60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPort60.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPort1440_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidPort1440_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPort1440 = _IbNetworkMonitorDNSSecurityInvalidPort1440_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 5),
    _IbNetworkMonitorDNSSecurityInvalidPort1440_Type()
)
ibNetworkMonitorDNSSecurityInvalidPort1440.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPort1440.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPortCount_Type = Counter32
_IbNetworkMonitorDNSSecurityInvalidPortCount_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPortCount = _IbNetworkMonitorDNSSecurityInvalidPortCount_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 6),
    _IbNetworkMonitorDNSSecurityInvalidPortCount_Type()
)
ibNetworkMonitorDNSSecurityInvalidPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPortCount.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxid_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSSecurityInvalidTxid = _IbNetworkMonitorDNSSecurityInvalidTxid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2)
)
_IbNetworkMonitorDNSSecurityInvalidTxid1_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid1_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid1 = _IbNetworkMonitorDNSSecurityInvalidTxid1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 1),
    _IbNetworkMonitorDNSSecurityInvalidTxid1_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxid1.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxid5_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid5_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid5 = _IbNetworkMonitorDNSSecurityInvalidTxid5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 2),
    _IbNetworkMonitorDNSSecurityInvalidTxid5_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxid5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxid5.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxid15_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid15_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid15 = _IbNetworkMonitorDNSSecurityInvalidTxid15_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 3),
    _IbNetworkMonitorDNSSecurityInvalidTxid15_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxid15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxid15.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxid60_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid60_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid60 = _IbNetworkMonitorDNSSecurityInvalidTxid60_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 4),
    _IbNetworkMonitorDNSSecurityInvalidTxid60_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxid60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxid60.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxid1440_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid1440_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid1440 = _IbNetworkMonitorDNSSecurityInvalidTxid1440_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 5),
    _IbNetworkMonitorDNSSecurityInvalidTxid1440_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxid1440.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxid1440.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxidCount_Type = Counter32
_IbNetworkMonitorDNSSecurityInvalidTxidCount_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxidCount = _IbNetworkMonitorDNSSecurityInvalidTxidCount_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 6),
    _IbNetworkMonitorDNSSecurityInvalidTxidCount_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxidCount.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPortOnly_Type = Counter32
_IbNetworkMonitorDNSSecurityInvalidPortOnly_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPortOnly = _IbNetworkMonitorDNSSecurityInvalidPortOnly_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 3),
    _IbNetworkMonitorDNSSecurityInvalidPortOnly_Type()
)
ibNetworkMonitorDNSSecurityInvalidPortOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPortOnly.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxidOnly_Type = Counter32
_IbNetworkMonitorDNSSecurityInvalidTxidOnly_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxidOnly = _IbNetworkMonitorDNSSecurityInvalidTxidOnly_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 4),
    _IbNetworkMonitorDNSSecurityInvalidTxidOnly_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxidOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxidOnly.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Type = Counter32
_IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxidAndPort = _IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 5),
    _IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxidAndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxidAndPort.setStatus("current")
_IbHardwareType_Type = IbString
_IbHardwareType_Object = MibScalar
ibHardwareType = _IbHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 4),
    _IbHardwareType_Type()
)
ibHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibHardwareType.setStatus("current")
_IbHardwareId_Type = IbString
_IbHardwareId_Object = MibScalar
ibHardwareId = _IbHardwareId_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 5),
    _IbHardwareId_Type()
)
ibHardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibHardwareId.setStatus("current")
_IbSerialNumber_Type = IbString
_IbSerialNumber_Object = MibScalar
ibSerialNumber = _IbSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 6),
    _IbSerialNumber_Type()
)
ibSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSerialNumber.setStatus("current")
_IbNiosVersion_Type = IbString
_IbNiosVersion_Object = MibScalar
ibNiosVersion = _IbNiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 7),
    _IbNiosVersion_Type()
)
ibNiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNiosVersion.setStatus("current")
_IbSystemMonitor_ObjectIdentity = ObjectIdentity
ibSystemMonitor = _IbSystemMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8)
)
_IbSystemMonitorCpu_ObjectIdentity = ObjectIdentity
ibSystemMonitorCpu = _IbSystemMonitorCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 1)
)
_IbSystemMonitorCpuUsage_Type = Integer32
_IbSystemMonitorCpuUsage_Object = MibScalar
ibSystemMonitorCpuUsage = _IbSystemMonitorCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 1, 1),
    _IbSystemMonitorCpuUsage_Type()
)
ibSystemMonitorCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSystemMonitorCpuUsage.setStatus("current")
_IbSystemMonitorMem_ObjectIdentity = ObjectIdentity
ibSystemMonitorMem = _IbSystemMonitorMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 2)
)
_IbSystemMonitorMemUsage_Type = Integer32
_IbSystemMonitorMemUsage_Object = MibScalar
ibSystemMonitorMemUsage = _IbSystemMonitorMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 2, 1),
    _IbSystemMonitorMemUsage_Type()
)
ibSystemMonitorMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSystemMonitorMemUsage.setStatus("current")
_IbSystemMonitorSwap_ObjectIdentity = ObjectIdentity
ibSystemMonitorSwap = _IbSystemMonitorSwap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 3)
)
_IbSystemMonitorSwapUsage_Type = Integer32
_IbSystemMonitorSwapUsage_Object = MibScalar
ibSystemMonitorSwapUsage = _IbSystemMonitorSwapUsage_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 3, 1),
    _IbSystemMonitorSwapUsage_Type()
)
ibSystemMonitorSwapUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSystemMonitorSwapUsage.setStatus("current")
_IbSystemMonitorSnic_ObjectIdentity = ObjectIdentity
ibSystemMonitorSnic = _IbSystemMonitorSnic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4)
)
_IbSystemMonitorSnicStatsTable1_Object = MibTable
ibSystemMonitorSnicStatsTable1 = _IbSystemMonitorSnicStatsTable1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    ibSystemMonitorSnicStatsTable1.setStatus("current")
_IbSystemMonitorSnicStatsEntry1_Object = MibTableRow
ibSystemMonitorSnicStatsEntry1 = _IbSystemMonitorSnicStatsEntry1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 1, 1)
)
ibSystemMonitorSnicStatsEntry1.setIndexNames(
    (0, "IB-PLATFORMONE-MIB", "ibSnicName1"),
)
if mibBuilder.loadTexts:
    ibSystemMonitorSnicStatsEntry1.setStatus("current")
_IbSnicName1_Type = IbSnicNames
_IbSnicName1_Object = MibTableColumn
ibSnicName1 = _IbSnicName1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 1, 1, 1),
    _IbSnicName1_Type()
)
ibSnicName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicName1.setStatus("current")
_IbSnicRxBits1_Type = Integer32
_IbSnicRxBits1_Object = MibTableColumn
ibSnicRxBits1 = _IbSnicRxBits1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 1, 1, 2),
    _IbSnicRxBits1_Type()
)
ibSnicRxBits1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicRxBits1.setStatus("current")
_IbSnicRxPackets1_Type = Integer32
_IbSnicRxPackets1_Object = MibTableColumn
ibSnicRxPackets1 = _IbSnicRxPackets1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 1, 1, 3),
    _IbSnicRxPackets1_Type()
)
ibSnicRxPackets1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicRxPackets1.setStatus("current")
_IbSnicTxBits1_Type = Integer32
_IbSnicTxBits1_Object = MibTableColumn
ibSnicTxBits1 = _IbSnicTxBits1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 1, 1, 4),
    _IbSnicTxBits1_Type()
)
ibSnicTxBits1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicTxBits1.setStatus("current")
_IbSnicTxPackets1_Type = Integer32
_IbSnicTxPackets1_Object = MibTableColumn
ibSnicTxPackets1 = _IbSnicTxPackets1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 1, 1, 5),
    _IbSnicTxPackets1_Type()
)
ibSnicTxPackets1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicTxPackets1.setStatus("current")
_IbSnicDropBits1_Type = Integer32
_IbSnicDropBits1_Object = MibTableColumn
ibSnicDropBits1 = _IbSnicDropBits1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 1, 1, 6),
    _IbSnicDropBits1_Type()
)
ibSnicDropBits1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicDropBits1.setStatus("current")
_IbSnicDropPackets1_Type = Integer32
_IbSnicDropPackets1_Object = MibTableColumn
ibSnicDropPackets1 = _IbSnicDropPackets1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 1, 1, 7),
    _IbSnicDropPackets1_Type()
)
ibSnicDropPackets1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicDropPackets1.setStatus("current")
_IbSystemMonitorSnicStatsTable5_Object = MibTable
ibSystemMonitorSnicStatsTable5 = _IbSystemMonitorSnicStatsTable5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 2)
)
if mibBuilder.loadTexts:
    ibSystemMonitorSnicStatsTable5.setStatus("current")
_IbSystemMonitorSnicStatsEntry5_Object = MibTableRow
ibSystemMonitorSnicStatsEntry5 = _IbSystemMonitorSnicStatsEntry5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 2, 1)
)
ibSystemMonitorSnicStatsEntry5.setIndexNames(
    (0, "IB-PLATFORMONE-MIB", "ibSnicName5"),
)
if mibBuilder.loadTexts:
    ibSystemMonitorSnicStatsEntry5.setStatus("current")
_IbSnicName5_Type = IbSnicNames
_IbSnicName5_Object = MibTableColumn
ibSnicName5 = _IbSnicName5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 2, 1, 1),
    _IbSnicName5_Type()
)
ibSnicName5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicName5.setStatus("current")
_IbSnicRxBits5_Type = Integer32
_IbSnicRxBits5_Object = MibTableColumn
ibSnicRxBits5 = _IbSnicRxBits5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 2, 1, 2),
    _IbSnicRxBits5_Type()
)
ibSnicRxBits5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicRxBits5.setStatus("current")
_IbSnicRxPackets5_Type = Integer32
_IbSnicRxPackets5_Object = MibTableColumn
ibSnicRxPackets5 = _IbSnicRxPackets5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 2, 1, 3),
    _IbSnicRxPackets5_Type()
)
ibSnicRxPackets5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicRxPackets5.setStatus("current")
_IbSnicTxBits5_Type = Integer32
_IbSnicTxBits5_Object = MibTableColumn
ibSnicTxBits5 = _IbSnicTxBits5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 2, 1, 4),
    _IbSnicTxBits5_Type()
)
ibSnicTxBits5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicTxBits5.setStatus("current")
_IbSnicTxPackets5_Type = Integer32
_IbSnicTxPackets5_Object = MibTableColumn
ibSnicTxPackets5 = _IbSnicTxPackets5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 2, 1, 5),
    _IbSnicTxPackets5_Type()
)
ibSnicTxPackets5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicTxPackets5.setStatus("current")
_IbSnicDropBits5_Type = Integer32
_IbSnicDropBits5_Object = MibTableColumn
ibSnicDropBits5 = _IbSnicDropBits5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 2, 1, 6),
    _IbSnicDropBits5_Type()
)
ibSnicDropBits5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicDropBits5.setStatus("current")
_IbSnicDropPackets5_Type = Integer32
_IbSnicDropPackets5_Object = MibTableColumn
ibSnicDropPackets5 = _IbSnicDropPackets5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 4, 2, 1, 7),
    _IbSnicDropPackets5_Type()
)
ibSnicDropPackets5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSnicDropPackets5.setStatus("current")
_IbMemberServiceStatusTable_Object = MibTable
ibMemberServiceStatusTable = _IbMemberServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ibMemberServiceStatusTable.setStatus("current")
_IbMemberServiceStatusEntry_Object = MibTableRow
ibMemberServiceStatusEntry = _IbMemberServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1)
)
ibMemberServiceStatusEntry.setIndexNames(
    (0, "IB-PLATFORMONE-MIB", "ibServiceName"),
)
if mibBuilder.loadTexts:
    ibMemberServiceStatusEntry.setStatus("current")
_IbServiceName_Type = IbServiceNames
_IbServiceName_Object = MibTableColumn
ibServiceName = _IbServiceName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1, 1),
    _IbServiceName_Type()
)
ibServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibServiceName.setStatus("current")
_IbServiceStatus_Type = IbServiceStates
_IbServiceStatus_Object = MibTableColumn
ibServiceStatus = _IbServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1, 2),
    _IbServiceStatus_Type()
)
ibServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibServiceStatus.setStatus("current")
_IbServiceDesc_Type = IbString
_IbServiceDesc_Object = MibTableColumn
ibServiceDesc = _IbServiceDesc_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1, 3),
    _IbServiceDesc_Type()
)
ibServiceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibServiceDesc.setStatus("current")
_IbMemberNodeServiceStatusTable_Object = MibTable
ibMemberNodeServiceStatusTable = _IbMemberNodeServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ibMemberNodeServiceStatusTable.setStatus("current")
_IbMemberNodeServiceStatusEntry_Object = MibTableRow
ibMemberNodeServiceStatusEntry = _IbMemberNodeServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1)
)
ibMemberNodeServiceStatusEntry.setIndexNames(
    (0, "IB-PLATFORMONE-MIB", "ibNodeServiceName"),
)
if mibBuilder.loadTexts:
    ibMemberNodeServiceStatusEntry.setStatus("current")
_IbNodeServiceName_Type = IbServiceNames
_IbNodeServiceName_Object = MibTableColumn
ibNodeServiceName = _IbNodeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1, 1),
    _IbNodeServiceName_Type()
)
ibNodeServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeServiceName.setStatus("current")
_IbNodeServiceStatus_Type = IbServiceStates
_IbNodeServiceStatus_Object = MibTableColumn
ibNodeServiceStatus = _IbNodeServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1, 2),
    _IbNodeServiceStatus_Type()
)
ibNodeServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeServiceStatus.setStatus("current")
_IbNodeServiceDesc_Type = IbString
_IbNodeServiceDesc_Object = MibTableColumn
ibNodeServiceDesc = _IbNodeServiceDesc_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1, 3),
    _IbNodeServiceDesc_Type()
)
ibNodeServiceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeServiceDesc.setStatus("current")
_IbMemberPasiveNodeServiceStatusTable_Object = MibTable
ibMemberPasiveNodeServiceStatusTable = _IbMemberPasiveNodeServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ibMemberPasiveNodeServiceStatusTable.setStatus("current")
_IbMemberPasiveNodeServiceStatusEntry_Object = MibTableRow
ibMemberPasiveNodeServiceStatusEntry = _IbMemberPasiveNodeServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1)
)
ibMemberPasiveNodeServiceStatusEntry.setIndexNames(
    (0, "IB-PLATFORMONE-MIB", "ibPasiveNodeServiceName"),
)
if mibBuilder.loadTexts:
    ibMemberPasiveNodeServiceStatusEntry.setStatus("current")
_IbPasiveNodeServiceName_Type = IbServiceNames
_IbPasiveNodeServiceName_Object = MibTableColumn
ibPasiveNodeServiceName = _IbPasiveNodeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1, 1),
    _IbPasiveNodeServiceName_Type()
)
ibPasiveNodeServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPasiveNodeServiceName.setStatus("current")
_IbPasiveNodeServiceStatus_Type = IbServiceStates
_IbPasiveNodeServiceStatus_Object = MibTableColumn
ibPasiveNodeServiceStatus = _IbPasiveNodeServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1, 2),
    _IbPasiveNodeServiceStatus_Type()
)
ibPasiveNodeServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPasiveNodeServiceStatus.setStatus("current")
_IbPasiveNodeServiceDesc_Type = IbString
_IbPasiveNodeServiceDesc_Object = MibTableColumn
ibPasiveNodeServiceDesc = _IbPasiveNodeServiceDesc_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1, 3),
    _IbPasiveNodeServiceDesc_Type()
)
ibPasiveNodeServiceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibPasiveNodeServiceDesc.setStatus("current")
_IbGridStatus_Type = IbString
_IbGridStatus_Object = MibScalar
ibGridStatus = _IbGridStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 12),
    _IbGridStatus_Type()
)
ibGridStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibGridStatus.setStatus("current")
_IbHaStatus_Type = IbString
_IbHaStatus_Object = MibScalar
ibHaStatus = _IbHaStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 13),
    _IbHaStatus_Type()
)
ibHaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibHaStatus.setStatus("current")
_IbGridMasterCandStatus_Type = IbString
_IbGridMasterCandStatus_Object = MibScalar
ibGridMasterCandStatus = _IbGridMasterCandStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 14),
    _IbGridMasterCandStatus_Type()
)
ibGridMasterCandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibGridMasterCandStatus.setStatus("current")
_IbGridMasterVIP_Type = IbString
_IbGridMasterVIP_Object = MibScalar
ibGridMasterVIP = _IbGridMasterVIP_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 15),
    _IbGridMasterVIP_Type()
)
ibGridMasterVIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibGridMasterVIP.setStatus("current")
_IbGridReplicationState_Type = IbString
_IbGridReplicationState_Object = MibScalar
ibGridReplicationState = _IbGridReplicationState_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 16),
    _IbGridReplicationState_Type()
)
ibGridReplicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibGridReplicationState.setStatus("current")
_IbCPU1Temperature_Type = IbFloat
_IbCPU1Temperature_Object = MibScalar
ibCPU1Temperature = _IbCPU1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 17),
    _IbCPU1Temperature_Type()
)
ibCPU1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCPU1Temperature.setStatus("current")
_IbCPU2Temperature_Type = IbFloat
_IbCPU2Temperature_Object = MibScalar
ibCPU2Temperature = _IbCPU2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 18),
    _IbCPU2Temperature_Type()
)
ibCPU2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCPU2Temperature.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IB-PLATFORMONE-MIB",
    **{"IbServiceStates": IbServiceStates,
       "IbServiceNames": IbServiceNames,
       "IbSnicNames": IbSnicNames,
       "ibPlatformModule": ibPlatformModule,
       "ibClusterReplicationStatusTable": ibClusterReplicationStatusTable,
       "ibClusterReplicationStatusEntry": ibClusterReplicationStatusEntry,
       "ibNodeIPAddress": ibNodeIPAddress,
       "ibNodeReplicationStatus": ibNodeReplicationStatus,
       "ibNodeQueueFromMaster": ibNodeQueueFromMaster,
       "ibNodeLastRepTimeFromMaster": ibNodeLastRepTimeFromMaster,
       "ibNodeQueueToMaster": ibNodeQueueToMaster,
       "ibNodeLastRepTimeToMaster": ibNodeLastRepTimeToMaster,
       "ibNetworkMonitor": ibNetworkMonitor,
       "ibNetworkMonitorDNS": ibNetworkMonitorDNS,
       "ibNetworkMonitorDNSActive": ibNetworkMonitorDNSActive,
       "ibNetworkMonitorDNSNonAA": ibNetworkMonitorDNSNonAA,
       "ibNetworkMonitorDNSNonAAT1": ibNetworkMonitorDNSNonAAT1,
       "ibNetworkMonitorDNSNonAAT1AvgLatency": ibNetworkMonitorDNSNonAAT1AvgLatency,
       "ibNetworkMonitorDNSNonAAT1Count": ibNetworkMonitorDNSNonAAT1Count,
       "ibNetworkMonitorDNSNonAAT5": ibNetworkMonitorDNSNonAAT5,
       "ibNetworkMonitorDNSNonAAT5AvgLatency": ibNetworkMonitorDNSNonAAT5AvgLatency,
       "ibNetworkMonitorDNSNonAAT5Count": ibNetworkMonitorDNSNonAAT5Count,
       "ibNetworkMonitorDNSNonAAT15": ibNetworkMonitorDNSNonAAT15,
       "ibNetworkMonitorDNSNonAAT15AvgLatency": ibNetworkMonitorDNSNonAAT15AvgLatency,
       "ibNetworkMonitorDNSNonAAT15Count": ibNetworkMonitorDNSNonAAT15Count,
       "ibNetworkMonitorDNSNonAAT60": ibNetworkMonitorDNSNonAAT60,
       "ibNetworkMonitorDNSNonAAT60AvgLatency": ibNetworkMonitorDNSNonAAT60AvgLatency,
       "ibNetworkMonitorDNSNonAAT60Count": ibNetworkMonitorDNSNonAAT60Count,
       "ibNetworkMonitorDNSNonAAT1440": ibNetworkMonitorDNSNonAAT1440,
       "ibNetworkMonitorDNSNonAAT1440AvgLatency": ibNetworkMonitorDNSNonAAT1440AvgLatency,
       "ibNetworkMonitorDNSNonAAT1440Count": ibNetworkMonitorDNSNonAAT1440Count,
       "ibNetworkMonitorDNSAA": ibNetworkMonitorDNSAA,
       "ibNetworkMonitorDNSAAT1": ibNetworkMonitorDNSAAT1,
       "ibNetworkMonitorDNSAAT1AvgLatency": ibNetworkMonitorDNSAAT1AvgLatency,
       "ibNetworkMonitorDNSAAT1Count": ibNetworkMonitorDNSAAT1Count,
       "ibNetworkMonitorDNSAAT5": ibNetworkMonitorDNSAAT5,
       "ibNetworkMonitorDNSAAT5AvgLatency": ibNetworkMonitorDNSAAT5AvgLatency,
       "ibNetworkMonitorDNSAAT5Count": ibNetworkMonitorDNSAAT5Count,
       "ibNetworkMonitorDNSAAT15": ibNetworkMonitorDNSAAT15,
       "ibNetworkMonitorDNSAAT15AvgLatency": ibNetworkMonitorDNSAAT15AvgLatency,
       "ibNetworkMonitorDNSAAT15Count": ibNetworkMonitorDNSAAT15Count,
       "ibNetworkMonitorDNSAAT60": ibNetworkMonitorDNSAAT60,
       "ibNetworkMonitorDNSAAT60AvgLatency": ibNetworkMonitorDNSAAT60AvgLatency,
       "ibNetworkMonitorDNSAAT60Count": ibNetworkMonitorDNSAAT60Count,
       "ibNetworkMonitorDNSAAT1440": ibNetworkMonitorDNSAAT1440,
       "ibNetworkMonitorDNSAAT1440AvgLatency": ibNetworkMonitorDNSAAT1440AvgLatency,
       "ibNetworkMonitorDNSAAT1440Count": ibNetworkMonitorDNSAAT1440Count,
       "ibNetworkMonitorDNSSecurity": ibNetworkMonitorDNSSecurity,
       "ibNetworkMonitorDNSSecurityInvalidPort": ibNetworkMonitorDNSSecurityInvalidPort,
       "ibNetworkMonitorDNSSecurityInvalidPort1": ibNetworkMonitorDNSSecurityInvalidPort1,
       "ibNetworkMonitorDNSSecurityInvalidPort5": ibNetworkMonitorDNSSecurityInvalidPort5,
       "ibNetworkMonitorDNSSecurityInvalidPort15": ibNetworkMonitorDNSSecurityInvalidPort15,
       "ibNetworkMonitorDNSSecurityInvalidPort60": ibNetworkMonitorDNSSecurityInvalidPort60,
       "ibNetworkMonitorDNSSecurityInvalidPort1440": ibNetworkMonitorDNSSecurityInvalidPort1440,
       "ibNetworkMonitorDNSSecurityInvalidPortCount": ibNetworkMonitorDNSSecurityInvalidPortCount,
       "ibNetworkMonitorDNSSecurityInvalidTxid": ibNetworkMonitorDNSSecurityInvalidTxid,
       "ibNetworkMonitorDNSSecurityInvalidTxid1": ibNetworkMonitorDNSSecurityInvalidTxid1,
       "ibNetworkMonitorDNSSecurityInvalidTxid5": ibNetworkMonitorDNSSecurityInvalidTxid5,
       "ibNetworkMonitorDNSSecurityInvalidTxid15": ibNetworkMonitorDNSSecurityInvalidTxid15,
       "ibNetworkMonitorDNSSecurityInvalidTxid60": ibNetworkMonitorDNSSecurityInvalidTxid60,
       "ibNetworkMonitorDNSSecurityInvalidTxid1440": ibNetworkMonitorDNSSecurityInvalidTxid1440,
       "ibNetworkMonitorDNSSecurityInvalidTxidCount": ibNetworkMonitorDNSSecurityInvalidTxidCount,
       "ibNetworkMonitorDNSSecurityInvalidPortOnly": ibNetworkMonitorDNSSecurityInvalidPortOnly,
       "ibNetworkMonitorDNSSecurityInvalidTxidOnly": ibNetworkMonitorDNSSecurityInvalidTxidOnly,
       "ibNetworkMonitorDNSSecurityInvalidTxidAndPort": ibNetworkMonitorDNSSecurityInvalidTxidAndPort,
       "ibHardwareType": ibHardwareType,
       "ibHardwareId": ibHardwareId,
       "ibSerialNumber": ibSerialNumber,
       "ibNiosVersion": ibNiosVersion,
       "ibSystemMonitor": ibSystemMonitor,
       "ibSystemMonitorCpu": ibSystemMonitorCpu,
       "ibSystemMonitorCpuUsage": ibSystemMonitorCpuUsage,
       "ibSystemMonitorMem": ibSystemMonitorMem,
       "ibSystemMonitorMemUsage": ibSystemMonitorMemUsage,
       "ibSystemMonitorSwap": ibSystemMonitorSwap,
       "ibSystemMonitorSwapUsage": ibSystemMonitorSwapUsage,
       "ibSystemMonitorSnic": ibSystemMonitorSnic,
       "ibSystemMonitorSnicStatsTable1": ibSystemMonitorSnicStatsTable1,
       "ibSystemMonitorSnicStatsEntry1": ibSystemMonitorSnicStatsEntry1,
       "ibSnicName1": ibSnicName1,
       "ibSnicRxBits1": ibSnicRxBits1,
       "ibSnicRxPackets1": ibSnicRxPackets1,
       "ibSnicTxBits1": ibSnicTxBits1,
       "ibSnicTxPackets1": ibSnicTxPackets1,
       "ibSnicDropBits1": ibSnicDropBits1,
       "ibSnicDropPackets1": ibSnicDropPackets1,
       "ibSystemMonitorSnicStatsTable5": ibSystemMonitorSnicStatsTable5,
       "ibSystemMonitorSnicStatsEntry5": ibSystemMonitorSnicStatsEntry5,
       "ibSnicName5": ibSnicName5,
       "ibSnicRxBits5": ibSnicRxBits5,
       "ibSnicRxPackets5": ibSnicRxPackets5,
       "ibSnicTxBits5": ibSnicTxBits5,
       "ibSnicTxPackets5": ibSnicTxPackets5,
       "ibSnicDropBits5": ibSnicDropBits5,
       "ibSnicDropPackets5": ibSnicDropPackets5,
       "ibMemberServiceStatusTable": ibMemberServiceStatusTable,
       "ibMemberServiceStatusEntry": ibMemberServiceStatusEntry,
       "ibServiceName": ibServiceName,
       "ibServiceStatus": ibServiceStatus,
       "ibServiceDesc": ibServiceDesc,
       "ibMemberNodeServiceStatusTable": ibMemberNodeServiceStatusTable,
       "ibMemberNodeServiceStatusEntry": ibMemberNodeServiceStatusEntry,
       "ibNodeServiceName": ibNodeServiceName,
       "ibNodeServiceStatus": ibNodeServiceStatus,
       "ibNodeServiceDesc": ibNodeServiceDesc,
       "ibMemberPasiveNodeServiceStatusTable": ibMemberPasiveNodeServiceStatusTable,
       "ibMemberPasiveNodeServiceStatusEntry": ibMemberPasiveNodeServiceStatusEntry,
       "ibPasiveNodeServiceName": ibPasiveNodeServiceName,
       "ibPasiveNodeServiceStatus": ibPasiveNodeServiceStatus,
       "ibPasiveNodeServiceDesc": ibPasiveNodeServiceDesc,
       "ibGridStatus": ibGridStatus,
       "ibHaStatus": ibHaStatus,
       "ibGridMasterCandStatus": ibGridMasterCandStatus,
       "ibGridMasterVIP": ibGridMasterVIP,
       "ibGridReplicationState": ibGridReplicationState,
       "ibCPU1Temperature": ibCPU1Temperature,
       "ibCPU2Temperature": ibCPU2Temperature}
)
