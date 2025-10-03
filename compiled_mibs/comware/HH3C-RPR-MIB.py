# SNMP MIB module (HH3C-RPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-RPR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:46 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(rprTopoImageEntry,
 rprTopoImageInetAddress,
 rprTopoImageMacAddress) = mibBuilder.importSymbols(
    "IEEE-802DOT17-RPR-MIB",
    "rprTopoImageEntry",
    "rprTopoImageInetAddress",
    "rprTopoImageMacAddress")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cRpr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60)
)
if mibBuilder.loadTexts:
    hh3cRpr.setRevisions(
        ("2005-03-16 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cRprRingletID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringlet0", 1),
          ("ringlet1", 2))
    )



class Hh3cRprServiceClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("classC", 1),
          ("classB", 2),
          ("classA1", 3),
          ("classA0", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cRprObjects_ObjectIdentity = ObjectIdentity
hh3cRprObjects = _Hh3cRprObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1)
)
_Hh3cRprMaxmumDefine_ObjectIdentity = ObjectIdentity
hh3cRprMaxmumDefine = _Hh3cRprMaxmumDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 1)
)
_Hh3cRprMaxmumDefineTable_Object = MibTable
hh3cRprMaxmumDefineTable = _Hh3cRprMaxmumDefineTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cRprMaxmumDefineTable.setStatus("current")
_Hh3cRprMaxmumDefineEntry_Object = MibTableRow
hh3cRprMaxmumDefineEntry = _Hh3cRprMaxmumDefineEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 1, 1, 1)
)
hh3cRprMaxmumDefineEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprMaxMumIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cRprMaxmumDefineEntry.setStatus("current")
_Hh3cRprMaxMumIfIndex_Type = InterfaceIndex
_Hh3cRprMaxMumIfIndex_Object = MibTableColumn
hh3cRprMaxMumIfIndex = _Hh3cRprMaxMumIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 1, 1, 1, 1),
    _Hh3cRprMaxMumIfIndex_Type()
)
hh3cRprMaxMumIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprMaxMumIfIndex.setStatus("current")
_Hh3cRprMaxStationNumDefine_Type = Integer32
_Hh3cRprMaxStationNumDefine_Object = MibTableColumn
hh3cRprMaxStationNumDefine = _Hh3cRprMaxStationNumDefine_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 1, 1, 1, 2),
    _Hh3cRprMaxStationNumDefine_Type()
)
hh3cRprMaxStationNumDefine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprMaxStationNumDefine.setStatus("current")
_Hh3cRprMaxReservedRateDefine_Type = Gauge32
_Hh3cRprMaxReservedRateDefine_Object = MibTableColumn
hh3cRprMaxReservedRateDefine = _Hh3cRprMaxReservedRateDefine_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 1, 1, 1, 3),
    _Hh3cRprMaxReservedRateDefine_Type()
)
hh3cRprMaxReservedRateDefine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprMaxReservedRateDefine.setStatus("current")
_Hh3cRprTopoImage_ObjectIdentity = ObjectIdentity
hh3cRprTopoImage = _Hh3cRprTopoImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 2)
)
_Hh3cRprTopoImageXTable_Object = MibTable
hh3cRprTopoImageXTable = _Hh3cRprTopoImageXTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cRprTopoImageXTable.setStatus("current")
_Hh3cRprTopoImageXEntry_Object = MibTableRow
hh3cRprTopoImageXEntry = _Hh3cRprTopoImageXEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cRprTopoImageXEntry.setStatus("current")
_Hh3cRprTopoImageXWestEdgeStatus_Type = TruthValue
_Hh3cRprTopoImageXWestEdgeStatus_Object = MibTableColumn
hh3cRprTopoImageXWestEdgeStatus = _Hh3cRprTopoImageXWestEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 2, 1, 1, 3),
    _Hh3cRprTopoImageXWestEdgeStatus_Type()
)
hh3cRprTopoImageXWestEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprTopoImageXWestEdgeStatus.setStatus("current")
_Hh3cRprTopoImageXEastEdgeStatus_Type = TruthValue
_Hh3cRprTopoImageXEastEdgeStatus_Object = MibTableColumn
hh3cRprTopoImageXEastEdgeStatus = _Hh3cRprTopoImageXEastEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 2, 1, 1, 4),
    _Hh3cRprTopoImageXEastEdgeStatus_Type()
)
hh3cRprTopoImageXEastEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprTopoImageXEastEdgeStatus.setStatus("current")
_Hh3cRprTopoImageXStationName_Type = SnmpAdminString
_Hh3cRprTopoImageXStationName_Object = MibTableColumn
hh3cRprTopoImageXStationName = _Hh3cRprTopoImageXStationName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 2, 1, 1, 5),
    _Hh3cRprTopoImageXStationName_Type()
)
hh3cRprTopoImageXStationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRprTopoImageXStationName.setStatus("current")
_Hh3cRprSpanCounters_ObjectIdentity = ObjectIdentity
hh3cRprSpanCounters = _Hh3cRprSpanCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3)
)
_Hh3cRprSrcMacCountTable_Object = MibTable
hh3cRprSrcMacCountTable = _Hh3cRprSrcMacCountTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cRprSrcMacCountTable.setStatus("current")
_Hh3cRprSrcMacCountEntry_Object = MibTableRow
hh3cRprSrcMacCountEntry = _Hh3cRprSrcMacCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 1, 1)
)
hh3cRprSrcMacCountEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprSrcMacCountIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprSrcMacCountBySrcAddress"),
)
if mibBuilder.loadTexts:
    hh3cRprSrcMacCountEntry.setStatus("current")
_Hh3cRprSrcMacCountIfIndex_Type = InterfaceIndex
_Hh3cRprSrcMacCountIfIndex_Object = MibTableColumn
hh3cRprSrcMacCountIfIndex = _Hh3cRprSrcMacCountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 1, 1, 1),
    _Hh3cRprSrcMacCountIfIndex_Type()
)
hh3cRprSrcMacCountIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprSrcMacCountIfIndex.setStatus("current")
_Hh3cRprSrcMacCountBySrcAddress_Type = MacAddress
_Hh3cRprSrcMacCountBySrcAddress_Object = MibTableColumn
hh3cRprSrcMacCountBySrcAddress = _Hh3cRprSrcMacCountBySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 1, 1, 2),
    _Hh3cRprSrcMacCountBySrcAddress_Type()
)
hh3cRprSrcMacCountBySrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprSrcMacCountBySrcAddress.setStatus("current")
_Hh3cRprSrcMacCountReceivedFrames_Type = Counter64
_Hh3cRprSrcMacCountReceivedFrames_Object = MibTableColumn
hh3cRprSrcMacCountReceivedFrames = _Hh3cRprSrcMacCountReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 1, 1, 3),
    _Hh3cRprSrcMacCountReceivedFrames_Type()
)
hh3cRprSrcMacCountReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprSrcMacCountReceivedFrames.setStatus("current")
_Hh3cRprSrcMacCountReceivedOctets_Type = Counter64
_Hh3cRprSrcMacCountReceivedOctets_Object = MibTableColumn
hh3cRprSrcMacCountReceivedOctets = _Hh3cRprSrcMacCountReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 1, 1, 4),
    _Hh3cRprSrcMacCountReceivedOctets_Type()
)
hh3cRprSrcMacCountReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprSrcMacCountReceivedOctets.setStatus("current")
_Hh3cRprDestMacCountTable_Object = MibTable
hh3cRprDestMacCountTable = _Hh3cRprDestMacCountTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cRprDestMacCountTable.setStatus("current")
_Hh3cRprDestMacCountEntry_Object = MibTableRow
hh3cRprDestMacCountEntry = _Hh3cRprDestMacCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 2, 1)
)
hh3cRprDestMacCountEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprDestMacCountIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprDestMacCountByDestAddress"),
)
if mibBuilder.loadTexts:
    hh3cRprDestMacCountEntry.setStatus("current")
_Hh3cRprDestMacCountIfIndex_Type = InterfaceIndex
_Hh3cRprDestMacCountIfIndex_Object = MibTableColumn
hh3cRprDestMacCountIfIndex = _Hh3cRprDestMacCountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 2, 1, 1),
    _Hh3cRprDestMacCountIfIndex_Type()
)
hh3cRprDestMacCountIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprDestMacCountIfIndex.setStatus("current")
_Hh3cRprDestMacCountByDestAddress_Type = MacAddress
_Hh3cRprDestMacCountByDestAddress_Object = MibTableColumn
hh3cRprDestMacCountByDestAddress = _Hh3cRprDestMacCountByDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 2, 1, 2),
    _Hh3cRprDestMacCountByDestAddress_Type()
)
hh3cRprDestMacCountByDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprDestMacCountByDestAddress.setStatus("current")
_Hh3cRprDestMacCountReceivedFrames_Type = Counter64
_Hh3cRprDestMacCountReceivedFrames_Object = MibTableColumn
hh3cRprDestMacCountReceivedFrames = _Hh3cRprDestMacCountReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 2, 1, 3),
    _Hh3cRprDestMacCountReceivedFrames_Type()
)
hh3cRprDestMacCountReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprDestMacCountReceivedFrames.setStatus("current")
_Hh3cRprDestMacCountReceivedOctets_Type = Counter64
_Hh3cRprDestMacCountReceivedOctets_Object = MibTableColumn
hh3cRprDestMacCountReceivedOctets = _Hh3cRprDestMacCountReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 2, 1, 4),
    _Hh3cRprDestMacCountReceivedOctets_Type()
)
hh3cRprDestMacCountReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprDestMacCountReceivedOctets.setStatus("current")
_Hh3cRprPktDropCountTable_Object = MibTable
hh3cRprPktDropCountTable = _Hh3cRprPktDropCountTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cRprPktDropCountTable.setStatus("current")
_Hh3cRprPktDropCountEntry_Object = MibTableRow
hh3cRprPktDropCountEntry = _Hh3cRprPktDropCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 3, 1)
)
hh3cRprPktDropCountEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprPktDropCntIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprPktDropCntRingletID"),
)
if mibBuilder.loadTexts:
    hh3cRprPktDropCountEntry.setStatus("current")
_Hh3cRprPktDropCntIfIndex_Type = InterfaceIndex
_Hh3cRprPktDropCntIfIndex_Object = MibTableColumn
hh3cRprPktDropCntIfIndex = _Hh3cRprPktDropCntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 3, 1, 1),
    _Hh3cRprPktDropCntIfIndex_Type()
)
hh3cRprPktDropCntIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprPktDropCntIfIndex.setStatus("current")
_Hh3cRprPktDropCntRingletID_Type = Hh3cRprRingletID
_Hh3cRprPktDropCntRingletID_Object = MibTableColumn
hh3cRprPktDropCntRingletID = _Hh3cRprPktDropCntRingletID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 3, 1, 2),
    _Hh3cRprPktDropCntRingletID_Type()
)
hh3cRprPktDropCntRingletID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprPktDropCntRingletID.setStatus("current")
_Hh3cRprDownFlowClassAPktDrops_Type = Counter64
_Hh3cRprDownFlowClassAPktDrops_Object = MibTableColumn
hh3cRprDownFlowClassAPktDrops = _Hh3cRprDownFlowClassAPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 3, 1, 3),
    _Hh3cRprDownFlowClassAPktDrops_Type()
)
hh3cRprDownFlowClassAPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprDownFlowClassAPktDrops.setStatus("current")
_Hh3cRprUpFlowClassAPktDrops_Type = Counter64
_Hh3cRprUpFlowClassAPktDrops_Object = MibTableColumn
hh3cRprUpFlowClassAPktDrops = _Hh3cRprUpFlowClassAPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 3, 1, 4),
    _Hh3cRprUpFlowClassAPktDrops_Type()
)
hh3cRprUpFlowClassAPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprUpFlowClassAPktDrops.setStatus("current")
_Hh3cRprDownFlowClassBPktDrops_Type = Counter64
_Hh3cRprDownFlowClassBPktDrops_Object = MibTableColumn
hh3cRprDownFlowClassBPktDrops = _Hh3cRprDownFlowClassBPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 3, 1, 5),
    _Hh3cRprDownFlowClassBPktDrops_Type()
)
hh3cRprDownFlowClassBPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprDownFlowClassBPktDrops.setStatus("current")
_Hh3cRprUpFlowClassBPktDrops_Type = Counter64
_Hh3cRprUpFlowClassBPktDrops_Object = MibTableColumn
hh3cRprUpFlowClassBPktDrops = _Hh3cRprUpFlowClassBPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 3, 1, 6),
    _Hh3cRprUpFlowClassBPktDrops_Type()
)
hh3cRprUpFlowClassBPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprUpFlowClassBPktDrops.setStatus("current")
_Hh3cRprDownFlowClassCPktDrops_Type = Counter64
_Hh3cRprDownFlowClassCPktDrops_Object = MibTableColumn
hh3cRprDownFlowClassCPktDrops = _Hh3cRprDownFlowClassCPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 3, 1, 7),
    _Hh3cRprDownFlowClassCPktDrops_Type()
)
hh3cRprDownFlowClassCPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprDownFlowClassCPktDrops.setStatus("current")
_Hh3cRprUpFlowClassCPktDrops_Type = Counter64
_Hh3cRprUpFlowClassCPktDrops_Object = MibTableColumn
hh3cRprUpFlowClassCPktDrops = _Hh3cRprUpFlowClassCPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 3, 3, 1, 8),
    _Hh3cRprUpFlowClassCPktDrops_Type()
)
hh3cRprUpFlowClassCPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprUpFlowClassCPktDrops.setStatus("current")
_Hh3cRprRS_ObjectIdentity = ObjectIdentity
hh3cRprRS = _Hh3cRprRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4)
)
_Hh3cRprStaticRSTable_Object = MibTable
hh3cRprStaticRSTable = _Hh3cRprStaticRSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cRprStaticRSTable.setStatus("current")
_Hh3cRprStaticRSEntry_Object = MibTableRow
hh3cRprStaticRSEntry = _Hh3cRprStaticRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 1, 1)
)
hh3cRprStaticRSEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprStaticRSIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprStaticRSMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cRprStaticRSEntry.setStatus("current")
_Hh3cRprStaticRSIfIndex_Type = InterfaceIndex
_Hh3cRprStaticRSIfIndex_Object = MibTableColumn
hh3cRprStaticRSIfIndex = _Hh3cRprStaticRSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 1, 1, 1),
    _Hh3cRprStaticRSIfIndex_Type()
)
hh3cRprStaticRSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprStaticRSIfIndex.setStatus("current")
_Hh3cRprStaticRSMacAddress_Type = MacAddress
_Hh3cRprStaticRSMacAddress_Object = MibTableColumn
hh3cRprStaticRSMacAddress = _Hh3cRprStaticRSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 1, 1, 2),
    _Hh3cRprStaticRSMacAddress_Type()
)
hh3cRprStaticRSMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprStaticRSMacAddress.setStatus("current")
_Hh3cRprStaticRSRingletID_Type = Hh3cRprRingletID
_Hh3cRprStaticRSRingletID_Object = MibTableColumn
hh3cRprStaticRSRingletID = _Hh3cRprStaticRSRingletID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 1, 1, 3),
    _Hh3cRprStaticRSRingletID_Type()
)
hh3cRprStaticRSRingletID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRprStaticRSRingletID.setStatus("current")
_Hh3cRprStaticRSTtl_Type = Integer32
_Hh3cRprStaticRSTtl_Object = MibTableColumn
hh3cRprStaticRSTtl = _Hh3cRprStaticRSTtl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 1, 1, 4),
    _Hh3cRprStaticRSTtl_Type()
)
hh3cRprStaticRSTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprStaticRSTtl.setStatus("current")
_Hh3cRprStaticRSValid_Type = TruthValue
_Hh3cRprStaticRSValid_Object = MibTableColumn
hh3cRprStaticRSValid = _Hh3cRprStaticRSValid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 1, 1, 5),
    _Hh3cRprStaticRSValid_Type()
)
hh3cRprStaticRSValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprStaticRSValid.setStatus("current")
_Hh3cRprStaticRSRowStatus_Type = RowStatus
_Hh3cRprStaticRSRowStatus_Object = MibTableColumn
hh3cRprStaticRSRowStatus = _Hh3cRprStaticRSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 1, 1, 6),
    _Hh3cRprStaticRSRowStatus_Type()
)
hh3cRprStaticRSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRprStaticRSRowStatus.setStatus("current")
_Hh3cRprIpv4DynamicRSTable_Object = MibTable
hh3cRprIpv4DynamicRSTable = _Hh3cRprIpv4DynamicRSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cRprIpv4DynamicRSTable.setStatus("current")
_Hh3cRprIpv4DynamicRSEntry_Object = MibTableRow
hh3cRprIpv4DynamicRSEntry = _Hh3cRprIpv4DynamicRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 2, 1)
)
hh3cRprIpv4DynamicRSEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprIpv4DynamicRSIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprIpv4DynamicRSMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cRprIpv4DynamicRSEntry.setStatus("current")
_Hh3cRprIpv4DynamicRSIfIndex_Type = InterfaceIndex
_Hh3cRprIpv4DynamicRSIfIndex_Object = MibTableColumn
hh3cRprIpv4DynamicRSIfIndex = _Hh3cRprIpv4DynamicRSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 2, 1, 1),
    _Hh3cRprIpv4DynamicRSIfIndex_Type()
)
hh3cRprIpv4DynamicRSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprIpv4DynamicRSIfIndex.setStatus("current")
_Hh3cRprIpv4DynamicRSMacAddress_Type = MacAddress
_Hh3cRprIpv4DynamicRSMacAddress_Object = MibTableColumn
hh3cRprIpv4DynamicRSMacAddress = _Hh3cRprIpv4DynamicRSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 2, 1, 2),
    _Hh3cRprIpv4DynamicRSMacAddress_Type()
)
hh3cRprIpv4DynamicRSMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprIpv4DynamicRSMacAddress.setStatus("current")
_Hh3cRprIpv4DynamicRSRingletID_Type = Hh3cRprRingletID
_Hh3cRprIpv4DynamicRSRingletID_Object = MibTableColumn
hh3cRprIpv4DynamicRSRingletID = _Hh3cRprIpv4DynamicRSRingletID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 2, 1, 3),
    _Hh3cRprIpv4DynamicRSRingletID_Type()
)
hh3cRprIpv4DynamicRSRingletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprIpv4DynamicRSRingletID.setStatus("current")
_Hh3cRprIpv4DynamicRSTtl_Type = Integer32
_Hh3cRprIpv4DynamicRSTtl_Object = MibTableColumn
hh3cRprIpv4DynamicRSTtl = _Hh3cRprIpv4DynamicRSTtl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 2, 1, 4),
    _Hh3cRprIpv4DynamicRSTtl_Type()
)
hh3cRprIpv4DynamicRSTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprIpv4DynamicRSTtl.setStatus("current")
_Hh3cRprIpv6DynamicRSTable_Object = MibTable
hh3cRprIpv6DynamicRSTable = _Hh3cRprIpv6DynamicRSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hh3cRprIpv6DynamicRSTable.setStatus("current")
_Hh3cRprIpv6DynamicRSEntry_Object = MibTableRow
hh3cRprIpv6DynamicRSEntry = _Hh3cRprIpv6DynamicRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 3, 1)
)
hh3cRprIpv6DynamicRSEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprIpv6DynamicRSIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprIpv6DynamicRSMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cRprIpv6DynamicRSEntry.setStatus("current")
_Hh3cRprIpv6DynamicRSIfIndex_Type = InterfaceIndex
_Hh3cRprIpv6DynamicRSIfIndex_Object = MibTableColumn
hh3cRprIpv6DynamicRSIfIndex = _Hh3cRprIpv6DynamicRSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 3, 1, 1),
    _Hh3cRprIpv6DynamicRSIfIndex_Type()
)
hh3cRprIpv6DynamicRSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprIpv6DynamicRSIfIndex.setStatus("current")
_Hh3cRprIpv6DynamicRSMacAddress_Type = MacAddress
_Hh3cRprIpv6DynamicRSMacAddress_Object = MibTableColumn
hh3cRprIpv6DynamicRSMacAddress = _Hh3cRprIpv6DynamicRSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 3, 1, 2),
    _Hh3cRprIpv6DynamicRSMacAddress_Type()
)
hh3cRprIpv6DynamicRSMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprIpv6DynamicRSMacAddress.setStatus("current")
_Hh3cRprIpv6DynamicRSRingletID_Type = Hh3cRprRingletID
_Hh3cRprIpv6DynamicRSRingletID_Object = MibTableColumn
hh3cRprIpv6DynamicRSRingletID = _Hh3cRprIpv6DynamicRSRingletID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 3, 1, 3),
    _Hh3cRprIpv6DynamicRSRingletID_Type()
)
hh3cRprIpv6DynamicRSRingletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprIpv6DynamicRSRingletID.setStatus("current")
_Hh3cRprIpv6DynamicRSTtl_Type = Integer32
_Hh3cRprIpv6DynamicRSTtl_Object = MibTableColumn
hh3cRprIpv6DynamicRSTtl = _Hh3cRprIpv6DynamicRSTtl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 3, 1, 4),
    _Hh3cRprIpv6DynamicRSTtl_Type()
)
hh3cRprIpv6DynamicRSTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprIpv6DynamicRSTtl.setStatus("current")
_Hh3cRprIpv4OverallRSTable_Object = MibTable
hh3cRprIpv4OverallRSTable = _Hh3cRprIpv4OverallRSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 4)
)
if mibBuilder.loadTexts:
    hh3cRprIpv4OverallRSTable.setStatus("current")
_Hh3cRprIpv4OverallRSEntry_Object = MibTableRow
hh3cRprIpv4OverallRSEntry = _Hh3cRprIpv4OverallRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 4, 1)
)
hh3cRprIpv4OverallRSEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprIpv4OverallRSIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprIpv4OverallRSMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cRprIpv4OverallRSEntry.setStatus("current")
_Hh3cRprIpv4OverallRSIfIndex_Type = InterfaceIndex
_Hh3cRprIpv4OverallRSIfIndex_Object = MibTableColumn
hh3cRprIpv4OverallRSIfIndex = _Hh3cRprIpv4OverallRSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 4, 1, 1),
    _Hh3cRprIpv4OverallRSIfIndex_Type()
)
hh3cRprIpv4OverallRSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprIpv4OverallRSIfIndex.setStatus("current")
_Hh3cRprIpv4OverallRSMacAddress_Type = MacAddress
_Hh3cRprIpv4OverallRSMacAddress_Object = MibTableColumn
hh3cRprIpv4OverallRSMacAddress = _Hh3cRprIpv4OverallRSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 4, 1, 2),
    _Hh3cRprIpv4OverallRSMacAddress_Type()
)
hh3cRprIpv4OverallRSMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprIpv4OverallRSMacAddress.setStatus("current")


class _Hh3cRprIpv4OverallRSType_Type(Integer32):
    """Custom type hh3cRprIpv4OverallRSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_Hh3cRprIpv4OverallRSType_Type.__name__ = "Integer32"
_Hh3cRprIpv4OverallRSType_Object = MibTableColumn
hh3cRprIpv4OverallRSType = _Hh3cRprIpv4OverallRSType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 4, 1, 3),
    _Hh3cRprIpv4OverallRSType_Type()
)
hh3cRprIpv4OverallRSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprIpv4OverallRSType.setStatus("current")
_Hh3cRprIpv4OverallRSRingletID_Type = Hh3cRprRingletID
_Hh3cRprIpv4OverallRSRingletID_Object = MibTableColumn
hh3cRprIpv4OverallRSRingletID = _Hh3cRprIpv4OverallRSRingletID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 4, 1, 4),
    _Hh3cRprIpv4OverallRSRingletID_Type()
)
hh3cRprIpv4OverallRSRingletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprIpv4OverallRSRingletID.setStatus("current")
_Hh3cRprIpv4OverallRSTtl_Type = Integer32
_Hh3cRprIpv4OverallRSTtl_Object = MibTableColumn
hh3cRprIpv4OverallRSTtl = _Hh3cRprIpv4OverallRSTtl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 4, 1, 5),
    _Hh3cRprIpv4OverallRSTtl_Type()
)
hh3cRprIpv4OverallRSTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprIpv4OverallRSTtl.setStatus("current")
_Hh3cRprVrrpRSTable_Object = MibTable
hh3cRprVrrpRSTable = _Hh3cRprVrrpRSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 5)
)
if mibBuilder.loadTexts:
    hh3cRprVrrpRSTable.setStatus("current")
_Hh3cRprVrrpRSEntry_Object = MibTableRow
hh3cRprVrrpRSEntry = _Hh3cRprVrrpRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 5, 1)
)
hh3cRprVrrpRSEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprVrrpRSIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprVrrpRSVirtualMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cRprVrrpRSEntry.setStatus("current")
_Hh3cRprVrrpRSIfIndex_Type = InterfaceIndex
_Hh3cRprVrrpRSIfIndex_Object = MibTableColumn
hh3cRprVrrpRSIfIndex = _Hh3cRprVrrpRSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 5, 1, 1),
    _Hh3cRprVrrpRSIfIndex_Type()
)
hh3cRprVrrpRSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprVrrpRSIfIndex.setStatus("current")
_Hh3cRprVrrpRSVirtualMacAddress_Type = MacAddress
_Hh3cRprVrrpRSVirtualMacAddress_Object = MibTableColumn
hh3cRprVrrpRSVirtualMacAddress = _Hh3cRprVrrpRSVirtualMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 5, 1, 2),
    _Hh3cRprVrrpRSVirtualMacAddress_Type()
)
hh3cRprVrrpRSVirtualMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprVrrpRSVirtualMacAddress.setStatus("current")
_Hh3cRprVrrpRSMacAddress_Type = MacAddress
_Hh3cRprVrrpRSMacAddress_Object = MibTableColumn
hh3cRprVrrpRSMacAddress = _Hh3cRprVrrpRSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 5, 1, 3),
    _Hh3cRprVrrpRSMacAddress_Type()
)
hh3cRprVrrpRSMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprVrrpRSMacAddress.setStatus("current")
_Hh3cRprVrrpRSRingletID_Type = Hh3cRprRingletID
_Hh3cRprVrrpRSRingletID_Object = MibTableColumn
hh3cRprVrrpRSRingletID = _Hh3cRprVrrpRSRingletID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 5, 1, 4),
    _Hh3cRprVrrpRSRingletID_Type()
)
hh3cRprVrrpRSRingletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprVrrpRSRingletID.setStatus("current")
_Hh3cRprVrrpRSTtl_Type = Integer32
_Hh3cRprVrrpRSTtl_Object = MibTableColumn
hh3cRprVrrpRSTtl = _Hh3cRprVrrpRSTtl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 5, 1, 5),
    _Hh3cRprVrrpRSTtl_Type()
)
hh3cRprVrrpRSTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprVrrpRSTtl.setStatus("current")
_Hh3cRprDefaultRingIDTable_Object = MibTable
hh3cRprDefaultRingIDTable = _Hh3cRprDefaultRingIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 6)
)
if mibBuilder.loadTexts:
    hh3cRprDefaultRingIDTable.setStatus("current")
_Hh3cRprDefaultRingIDEntry_Object = MibTableRow
hh3cRprDefaultRingIDEntry = _Hh3cRprDefaultRingIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 6, 1)
)
hh3cRprDefaultRingIDEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprDefaultRingIDIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cRprDefaultRingIDEntry.setStatus("current")
_Hh3cRprDefaultRingIDIfIndex_Type = InterfaceIndex
_Hh3cRprDefaultRingIDIfIndex_Object = MibTableColumn
hh3cRprDefaultRingIDIfIndex = _Hh3cRprDefaultRingIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 6, 1, 1),
    _Hh3cRprDefaultRingIDIfIndex_Type()
)
hh3cRprDefaultRingIDIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprDefaultRingIDIfIndex.setStatus("current")
_Hh3cRprDefaultConfigRingletID_Type = Hh3cRprRingletID
_Hh3cRprDefaultConfigRingletID_Object = MibTableColumn
hh3cRprDefaultConfigRingletID = _Hh3cRprDefaultConfigRingletID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 6, 1, 2),
    _Hh3cRprDefaultConfigRingletID_Type()
)
hh3cRprDefaultConfigRingletID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRprDefaultConfigRingletID.setStatus("current")
_Hh3cRprDefaultActiveRingID_Type = Hh3cRprRingletID
_Hh3cRprDefaultActiveRingID_Object = MibTableColumn
hh3cRprDefaultActiveRingID = _Hh3cRprDefaultActiveRingID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 4, 6, 1, 3),
    _Hh3cRprDefaultActiveRingID_Type()
)
hh3cRprDefaultActiveRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprDefaultActiveRingID.setStatus("current")
_Hh3cRprDefect_ObjectIdentity = ObjectIdentity
hh3cRprDefect = _Hh3cRprDefect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 5)
)
_Hh3cRprDefectReportTable_Object = MibTable
hh3cRprDefectReportTable = _Hh3cRprDefectReportTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cRprDefectReportTable.setStatus("current")
_Hh3cRprDefectReportEntry_Object = MibTableRow
hh3cRprDefectReportEntry = _Hh3cRprDefectReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 5, 1, 1)
)
hh3cRprDefectReportEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprDefectIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cRprDefectReportEntry.setStatus("current")
_Hh3cRprDefectIfIndex_Type = InterfaceIndex
_Hh3cRprDefectIfIndex_Object = MibTableColumn
hh3cRprDefectIfIndex = _Hh3cRprDefectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 5, 1, 1, 1),
    _Hh3cRprDefectIfIndex_Type()
)
hh3cRprDefectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprDefectIfIndex.setStatus("current")


class _Hh3cRprDefectCurrentStatus_Type(Bits):
    """Custom type hh3cRprDefectCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("topologyOpenRing", 0),
          ("topoInstability", 1),
          ("topoInconsistent", 2),
          ("dulpMacAddress", 3),
          ("dulpIPAddress", 4),
          ("lrttDefect", 5),
          ("protCfgDefect", 6),
          ("jumboCfgDefect", 7),
          ("excessReservedRateDefect", 8),
          ("excessMaxStationNum", 9),
          ("miscabling", 10),
          ("backPressure", 11))
    )

_Hh3cRprDefectCurrentStatus_Type.__name__ = "Bits"
_Hh3cRprDefectCurrentStatus_Object = MibTableColumn
hh3cRprDefectCurrentStatus = _Hh3cRprDefectCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 5, 1, 1, 2),
    _Hh3cRprDefectCurrentStatus_Type()
)
hh3cRprDefectCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprDefectCurrentStatus.setStatus("current")
_Hh3cRprPriorityMap_ObjectIdentity = ObjectIdentity
hh3cRprPriorityMap = _Hh3cRprPriorityMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 6)
)
_Hh3cRprPriority2ClassMapTable_Object = MibTable
hh3cRprPriority2ClassMapTable = _Hh3cRprPriority2ClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cRprPriority2ClassMapTable.setStatus("current")
_Hh3cRprPriority2ClassMapEntry_Object = MibTableRow
hh3cRprPriority2ClassMapEntry = _Hh3cRprPriority2ClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 6, 1, 1)
)
hh3cRprPriority2ClassMapEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprPriority2ClassMapIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprPriority2ClassMapType"),
    (0, "HH3C-RPR-MIB", "hh3cRprPriorityValue"),
)
if mibBuilder.loadTexts:
    hh3cRprPriority2ClassMapEntry.setStatus("current")
_Hh3cRprPriority2ClassMapIfIndex_Type = InterfaceIndex
_Hh3cRprPriority2ClassMapIfIndex_Object = MibTableColumn
hh3cRprPriority2ClassMapIfIndex = _Hh3cRprPriority2ClassMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 6, 1, 1, 1),
    _Hh3cRprPriority2ClassMapIfIndex_Type()
)
hh3cRprPriority2ClassMapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprPriority2ClassMapIfIndex.setStatus("current")


class _Hh3cRprPriority2ClassMapType_Type(Integer32):
    """Custom type hh3cRprPriority2ClassMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("mpls", 2),
          ("ip", 3))
    )


_Hh3cRprPriority2ClassMapType_Type.__name__ = "Integer32"
_Hh3cRprPriority2ClassMapType_Object = MibTableColumn
hh3cRprPriority2ClassMapType = _Hh3cRprPriority2ClassMapType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 6, 1, 1, 2),
    _Hh3cRprPriority2ClassMapType_Type()
)
hh3cRprPriority2ClassMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprPriority2ClassMapType.setStatus("current")


class _Hh3cRprPriorityValue_Type(Integer32):
    """Custom type hh3cRprPriorityValue based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("pri0", 1),
          ("pri1", 2),
          ("pri2", 3),
          ("pri3", 4),
          ("pri4", 5),
          ("pri5", 6),
          ("pri6", 7),
          ("pri7", 8))
    )


_Hh3cRprPriorityValue_Type.__name__ = "Integer32"
_Hh3cRprPriorityValue_Object = MibTableColumn
hh3cRprPriorityValue = _Hh3cRprPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 6, 1, 1, 3),
    _Hh3cRprPriorityValue_Type()
)
hh3cRprPriorityValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprPriorityValue.setStatus("current")
_Hh3cRprPriority2ClassMap_Type = Hh3cRprServiceClass
_Hh3cRprPriority2ClassMap_Object = MibTableColumn
hh3cRprPriority2ClassMap = _Hh3cRprPriority2ClassMap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 6, 1, 1, 4),
    _Hh3cRprPriority2ClassMap_Type()
)
hh3cRprPriority2ClassMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRprPriority2ClassMap.setStatus("current")
_Hh3cRprRateLimitConfig_ObjectIdentity = ObjectIdentity
hh3cRprRateLimitConfig = _Hh3cRprRateLimitConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 7)
)
_Hh3cRprRateLimitConfigTable_Object = MibTable
hh3cRprRateLimitConfigTable = _Hh3cRprRateLimitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hh3cRprRateLimitConfigTable.setStatus("current")
_Hh3cRprRateLimitConfigEntry_Object = MibTableRow
hh3cRprRateLimitConfigEntry = _Hh3cRprRateLimitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 7, 1, 1)
)
hh3cRprRateLimitConfigEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprRateLimitConfigIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprRateLimitConfigRingletId"),
    (0, "HH3C-RPR-MIB", "hh3cRprRateLimitConfigServiceClass"),
)
if mibBuilder.loadTexts:
    hh3cRprRateLimitConfigEntry.setStatus("current")
_Hh3cRprRateLimitConfigIfIndex_Type = InterfaceIndex
_Hh3cRprRateLimitConfigIfIndex_Object = MibTableColumn
hh3cRprRateLimitConfigIfIndex = _Hh3cRprRateLimitConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 7, 1, 1, 1),
    _Hh3cRprRateLimitConfigIfIndex_Type()
)
hh3cRprRateLimitConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprRateLimitConfigIfIndex.setStatus("current")
_Hh3cRprRateLimitConfigRingletId_Type = Hh3cRprRingletID
_Hh3cRprRateLimitConfigRingletId_Object = MibTableColumn
hh3cRprRateLimitConfigRingletId = _Hh3cRprRateLimitConfigRingletId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 7, 1, 1, 2),
    _Hh3cRprRateLimitConfigRingletId_Type()
)
hh3cRprRateLimitConfigRingletId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprRateLimitConfigRingletId.setStatus("current")
_Hh3cRprRateLimitConfigServiceClass_Type = Hh3cRprServiceClass
_Hh3cRprRateLimitConfigServiceClass_Object = MibTableColumn
hh3cRprRateLimitConfigServiceClass = _Hh3cRprRateLimitConfigServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 7, 1, 1, 3),
    _Hh3cRprRateLimitConfigServiceClass_Type()
)
hh3cRprRateLimitConfigServiceClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprRateLimitConfigServiceClass.setStatus("current")
_Hh3cRprRateLimitConfigValue_Type = Integer32
_Hh3cRprRateLimitConfigValue_Object = MibTableColumn
hh3cRprRateLimitConfigValue = _Hh3cRprRateLimitConfigValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 7, 1, 1, 4),
    _Hh3cRprRateLimitConfigValue_Type()
)
hh3cRprRateLimitConfigValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRprRateLimitConfigValue.setStatus("current")
_Hh3cRprMacAddrLearn_ObjectIdentity = ObjectIdentity
hh3cRprMacAddrLearn = _Hh3cRprMacAddrLearn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8)
)
_Hh3cRprMacLearnCfgTable_Object = MibTable
hh3cRprMacLearnCfgTable = _Hh3cRprMacLearnCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cRprMacLearnCfgTable.setStatus("current")
_Hh3cRprMacLearnCfgEntry_Object = MibTableRow
hh3cRprMacLearnCfgEntry = _Hh3cRprMacLearnCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1, 1)
)
hh3cRprMacLearnCfgEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprMacLearnIfIndex"),
    (0, "HH3C-RPR-MIB", "hh3cRprMacLearnRprMac"),
)
if mibBuilder.loadTexts:
    hh3cRprMacLearnCfgEntry.setStatus("current")
_Hh3cRprMacLearnIfIndex_Type = InterfaceIndex
_Hh3cRprMacLearnIfIndex_Object = MibTableColumn
hh3cRprMacLearnIfIndex = _Hh3cRprMacLearnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1, 1, 1),
    _Hh3cRprMacLearnIfIndex_Type()
)
hh3cRprMacLearnIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprMacLearnIfIndex.setStatus("current")
_Hh3cRprMacLearnRprMac_Type = MacAddress
_Hh3cRprMacLearnRprMac_Object = MibTableColumn
hh3cRprMacLearnRprMac = _Hh3cRprMacLearnRprMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1, 1, 2),
    _Hh3cRprMacLearnRprMac_Type()
)
hh3cRprMacLearnRprMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRprMacLearnRprMac.setStatus("current")
_Hh3cRprMacLearnType_Type = Integer32
_Hh3cRprMacLearnType_Object = MibTableColumn
hh3cRprMacLearnType = _Hh3cRprMacLearnType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1, 1, 3),
    _Hh3cRprMacLearnType_Type()
)
hh3cRprMacLearnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRprMacLearnType.setStatus("current")
_Hh3cRprMacLearnDestMac_Type = MacAddress
_Hh3cRprMacLearnDestMac_Object = MibTableColumn
hh3cRprMacLearnDestMac = _Hh3cRprMacLearnDestMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1, 1, 4),
    _Hh3cRprMacLearnDestMac_Type()
)
hh3cRprMacLearnDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRprMacLearnDestMac.setStatus("current")


class _Hh3cRprMacLearnVlanId_Type(Integer32):
    """Custom type hh3cRprMacLearnVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cRprMacLearnVlanId_Type.__name__ = "Integer32"
_Hh3cRprMacLearnVlanId_Object = MibTableColumn
hh3cRprMacLearnVlanId = _Hh3cRprMacLearnVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1, 1, 5),
    _Hh3cRprMacLearnVlanId_Type()
)
hh3cRprMacLearnVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRprMacLearnVlanId.setStatus("current")
_Hh3cRprMacLearnRinglet_Type = Hh3cRprRingletID
_Hh3cRprMacLearnRinglet_Object = MibTableColumn
hh3cRprMacLearnRinglet = _Hh3cRprMacLearnRinglet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1, 1, 6),
    _Hh3cRprMacLearnRinglet_Type()
)
hh3cRprMacLearnRinglet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRprMacLearnRinglet.setStatus("current")
_Hh3cRprMacLearnTtl_Type = Integer32
_Hh3cRprMacLearnTtl_Object = MibTableColumn
hh3cRprMacLearnTtl = _Hh3cRprMacLearnTtl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1, 1, 7),
    _Hh3cRprMacLearnTtl_Type()
)
hh3cRprMacLearnTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprMacLearnTtl.setStatus("current")
_Hh3cRprMacLearnIsValid_Type = TruthValue
_Hh3cRprMacLearnIsValid_Object = MibTableColumn
hh3cRprMacLearnIsValid = _Hh3cRprMacLearnIsValid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1, 1, 8),
    _Hh3cRprMacLearnIsValid_Type()
)
hh3cRprMacLearnIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRprMacLearnIsValid.setStatus("current")
_Hh3cRprMacLearnRowStatus_Type = RowStatus
_Hh3cRprMacLearnRowStatus_Object = MibTableColumn
hh3cRprMacLearnRowStatus = _Hh3cRprMacLearnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 8, 1, 1, 9),
    _Hh3cRprMacLearnRowStatus_Type()
)
hh3cRprMacLearnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRprMacLearnRowStatus.setStatus("current")
_Hh3cRprTrapVar_ObjectIdentity = ObjectIdentity
hh3cRprTrapVar = _Hh3cRprTrapVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 9)
)
_Hh3cRprTrapVarTable_Object = MibTable
hh3cRprTrapVarTable = _Hh3cRprTrapVarTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hh3cRprTrapVarTable.setStatus("current")
_Hh3cRprTrapVarEntry_Object = MibTableRow
hh3cRprTrapVarEntry = _Hh3cRprTrapVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 9, 1, 1)
)
hh3cRprTrapVarEntry.setIndexNames(
    (0, "HH3C-RPR-MIB", "hh3cRprTrapIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cRprTrapVarEntry.setStatus("current")
_Hh3cRprTrapIfIndex_Type = InterfaceIndex
_Hh3cRprTrapIfIndex_Object = MibTableColumn
hh3cRprTrapIfIndex = _Hh3cRprTrapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 9, 1, 1, 1),
    _Hh3cRprTrapIfIndex_Type()
)
hh3cRprTrapIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRprTrapIfIndex.setStatus("current")
_Hh3cRprTrapRinglet_Type = Hh3cRprRingletID
_Hh3cRprTrapRinglet_Object = MibTableColumn
hh3cRprTrapRinglet = _Hh3cRprTrapRinglet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 9, 1, 1, 2),
    _Hh3cRprTrapRinglet_Type()
)
hh3cRprTrapRinglet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRprTrapRinglet.setStatus("current")
_Hh3cRprTrapTopoMacAddress_Type = MacAddress
_Hh3cRprTrapTopoMacAddress_Object = MibTableColumn
hh3cRprTrapTopoMacAddress = _Hh3cRprTrapTopoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 9, 1, 1, 3),
    _Hh3cRprTrapTopoMacAddress_Type()
)
hh3cRprTrapTopoMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRprTrapTopoMacAddress.setStatus("current")
_Hh3cRprTrapIpAddress_Type = InetAddress
_Hh3cRprTrapIpAddress_Object = MibTableColumn
hh3cRprTrapIpAddress = _Hh3cRprTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 9, 1, 1, 4),
    _Hh3cRprTrapIpAddress_Type()
)
hh3cRprTrapIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRprTrapIpAddress.setStatus("current")
_Hh3cRprTrap_ObjectIdentity = ObjectIdentity
hh3cRprTrap = _Hh3cRprTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10)
)
rprTopoImageEntry.registerAugmentions(
    ("HH3C-RPR-MIB",
     "hh3cRprTopoImageXEntry")
)
hh3cRprTopoImageXEntry.setIndexNames(*rprTopoImageEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hh3cRprTopologyOpenRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 1)
)
hh3cRprTopologyOpenRing.setObjects(
      *(("HH3C-RPR-MIB", "hh3cRprTrapIfIndex"),
        ("HH3C-RPR-MIB", "hh3cRprTrapRinglet"))
)
if mibBuilder.loadTexts:
    hh3cRprTopologyOpenRing.setStatus(
        "current"
    )

hh3cRprTopologyCloseRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 2)
)
hh3cRprTopologyCloseRing.setObjects(
      *(("HH3C-RPR-MIB", "hh3cRprTrapIfIndex"),
        ("HH3C-RPR-MIB", "hh3cRprTrapRinglet"))
)
if mibBuilder.loadTexts:
    hh3cRprTopologyCloseRing.setStatus(
        "current"
    )

hh3cRprTopologyInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 3)
)
hh3cRprTopologyInconsistent.setObjects(
    ("HH3C-RPR-MIB", "hh3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    hh3cRprTopologyInconsistent.setStatus(
        "current"
    )

hh3cRprTopologyInstability = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 4)
)
hh3cRprTopologyInstability.setObjects(
    ("HH3C-RPR-MIB", "hh3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    hh3cRprTopologyInstability.setStatus(
        "current"
    )

hh3cRprDuplicateMacAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 5)
)
hh3cRprDuplicateMacAddress.setObjects(
      *(("HH3C-RPR-MIB", "hh3cRprTrapIfIndex"),
        ("HH3C-RPR-MIB", "hh3cRprTrapTopoMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cRprDuplicateMacAddress.setStatus(
        "current"
    )

hh3cRprDulplicateIPAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 6)
)
hh3cRprDulplicateIPAddress.setObjects(
      *(("HH3C-RPR-MIB", "hh3cRprTrapIfIndex"),
        ("HH3C-RPR-MIB", "hh3cRprTrapIpAddress"))
)
if mibBuilder.loadTexts:
    hh3cRprDulplicateIPAddress.setStatus(
        "current"
    )

hh3cRprIncompleteLRTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 7)
)
hh3cRprIncompleteLRTT.setObjects(
    ("HH3C-RPR-MIB", "hh3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    hh3cRprIncompleteLRTT.setStatus(
        "current"
    )

hh3cRprProtecConfigInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 8)
)
hh3cRprProtecConfigInconsistent.setObjects(
    ("HH3C-RPR-MIB", "hh3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    hh3cRprProtecConfigInconsistent.setStatus(
        "current"
    )

hh3cRprJumboConfigInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 9)
)
hh3cRprJumboConfigInconsistent.setObjects(
    ("HH3C-RPR-MIB", "hh3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    hh3cRprJumboConfigInconsistent.setStatus(
        "current"
    )

hh3cRprExceedMaxReservRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 10)
)
hh3cRprExceedMaxReservRate.setObjects(
      *(("HH3C-RPR-MIB", "hh3cRprTrapIfIndex"),
        ("HH3C-RPR-MIB", "hh3cRprTrapRinglet"))
)
if mibBuilder.loadTexts:
    hh3cRprExceedMaxReservRate.setStatus(
        "current"
    )

hh3cRprExceedMaxStationNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 11)
)
hh3cRprExceedMaxStationNum.setObjects(
    ("HH3C-RPR-MIB", "hh3cRprTrapIfIndex")
)
if mibBuilder.loadTexts:
    hh3cRprExceedMaxStationNum.setStatus(
        "current"
    )

hh3cRprMiscabling = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 12)
)
hh3cRprMiscabling.setObjects(
      *(("HH3C-RPR-MIB", "hh3cRprTrapIfIndex"),
        ("HH3C-RPR-MIB", "hh3cRprTrapRinglet"))
)
if mibBuilder.loadTexts:
    hh3cRprMiscabling.setStatus(
        "current"
    )

hh3cRprBackPressure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 13)
)
hh3cRprBackPressure.setObjects(
      *(("HH3C-RPR-MIB", "hh3cRprTrapIfIndex"),
        ("HH3C-RPR-MIB", "hh3cRprTrapRinglet"),
        ("HH3C-RPR-MIB", "hh3cRprPriority2ClassMap"))
)
if mibBuilder.loadTexts:
    hh3cRprBackPressure.setStatus(
        "current"
    )

hh3cRprBackPressureOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60, 1, 10, 14)
)
hh3cRprBackPressureOver.setObjects(
      *(("HH3C-RPR-MIB", "hh3cRprTrapIfIndex"),
        ("HH3C-RPR-MIB", "hh3cRprTrapRinglet"),
        ("HH3C-RPR-MIB", "hh3cRprPriority2ClassMap"))
)
if mibBuilder.loadTexts:
    hh3cRprBackPressureOver.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RPR-MIB",
    **{"Hh3cRprRingletID": Hh3cRprRingletID,
       "Hh3cRprServiceClass": Hh3cRprServiceClass,
       "hh3cRpr": hh3cRpr,
       "hh3cRprObjects": hh3cRprObjects,
       "hh3cRprMaxmumDefine": hh3cRprMaxmumDefine,
       "hh3cRprMaxmumDefineTable": hh3cRprMaxmumDefineTable,
       "hh3cRprMaxmumDefineEntry": hh3cRprMaxmumDefineEntry,
       "hh3cRprMaxMumIfIndex": hh3cRprMaxMumIfIndex,
       "hh3cRprMaxStationNumDefine": hh3cRprMaxStationNumDefine,
       "hh3cRprMaxReservedRateDefine": hh3cRprMaxReservedRateDefine,
       "hh3cRprTopoImage": hh3cRprTopoImage,
       "hh3cRprTopoImageXTable": hh3cRprTopoImageXTable,
       "hh3cRprTopoImageXEntry": hh3cRprTopoImageXEntry,
       "hh3cRprTopoImageXWestEdgeStatus": hh3cRprTopoImageXWestEdgeStatus,
       "hh3cRprTopoImageXEastEdgeStatus": hh3cRprTopoImageXEastEdgeStatus,
       "hh3cRprTopoImageXStationName": hh3cRprTopoImageXStationName,
       "hh3cRprSpanCounters": hh3cRprSpanCounters,
       "hh3cRprSrcMacCountTable": hh3cRprSrcMacCountTable,
       "hh3cRprSrcMacCountEntry": hh3cRprSrcMacCountEntry,
       "hh3cRprSrcMacCountIfIndex": hh3cRprSrcMacCountIfIndex,
       "hh3cRprSrcMacCountBySrcAddress": hh3cRprSrcMacCountBySrcAddress,
       "hh3cRprSrcMacCountReceivedFrames": hh3cRprSrcMacCountReceivedFrames,
       "hh3cRprSrcMacCountReceivedOctets": hh3cRprSrcMacCountReceivedOctets,
       "hh3cRprDestMacCountTable": hh3cRprDestMacCountTable,
       "hh3cRprDestMacCountEntry": hh3cRprDestMacCountEntry,
       "hh3cRprDestMacCountIfIndex": hh3cRprDestMacCountIfIndex,
       "hh3cRprDestMacCountByDestAddress": hh3cRprDestMacCountByDestAddress,
       "hh3cRprDestMacCountReceivedFrames": hh3cRprDestMacCountReceivedFrames,
       "hh3cRprDestMacCountReceivedOctets": hh3cRprDestMacCountReceivedOctets,
       "hh3cRprPktDropCountTable": hh3cRprPktDropCountTable,
       "hh3cRprPktDropCountEntry": hh3cRprPktDropCountEntry,
       "hh3cRprPktDropCntIfIndex": hh3cRprPktDropCntIfIndex,
       "hh3cRprPktDropCntRingletID": hh3cRprPktDropCntRingletID,
       "hh3cRprDownFlowClassAPktDrops": hh3cRprDownFlowClassAPktDrops,
       "hh3cRprUpFlowClassAPktDrops": hh3cRprUpFlowClassAPktDrops,
       "hh3cRprDownFlowClassBPktDrops": hh3cRprDownFlowClassBPktDrops,
       "hh3cRprUpFlowClassBPktDrops": hh3cRprUpFlowClassBPktDrops,
       "hh3cRprDownFlowClassCPktDrops": hh3cRprDownFlowClassCPktDrops,
       "hh3cRprUpFlowClassCPktDrops": hh3cRprUpFlowClassCPktDrops,
       "hh3cRprRS": hh3cRprRS,
       "hh3cRprStaticRSTable": hh3cRprStaticRSTable,
       "hh3cRprStaticRSEntry": hh3cRprStaticRSEntry,
       "hh3cRprStaticRSIfIndex": hh3cRprStaticRSIfIndex,
       "hh3cRprStaticRSMacAddress": hh3cRprStaticRSMacAddress,
       "hh3cRprStaticRSRingletID": hh3cRprStaticRSRingletID,
       "hh3cRprStaticRSTtl": hh3cRprStaticRSTtl,
       "hh3cRprStaticRSValid": hh3cRprStaticRSValid,
       "hh3cRprStaticRSRowStatus": hh3cRprStaticRSRowStatus,
       "hh3cRprIpv4DynamicRSTable": hh3cRprIpv4DynamicRSTable,
       "hh3cRprIpv4DynamicRSEntry": hh3cRprIpv4DynamicRSEntry,
       "hh3cRprIpv4DynamicRSIfIndex": hh3cRprIpv4DynamicRSIfIndex,
       "hh3cRprIpv4DynamicRSMacAddress": hh3cRprIpv4DynamicRSMacAddress,
       "hh3cRprIpv4DynamicRSRingletID": hh3cRprIpv4DynamicRSRingletID,
       "hh3cRprIpv4DynamicRSTtl": hh3cRprIpv4DynamicRSTtl,
       "hh3cRprIpv6DynamicRSTable": hh3cRprIpv6DynamicRSTable,
       "hh3cRprIpv6DynamicRSEntry": hh3cRprIpv6DynamicRSEntry,
       "hh3cRprIpv6DynamicRSIfIndex": hh3cRprIpv6DynamicRSIfIndex,
       "hh3cRprIpv6DynamicRSMacAddress": hh3cRprIpv6DynamicRSMacAddress,
       "hh3cRprIpv6DynamicRSRingletID": hh3cRprIpv6DynamicRSRingletID,
       "hh3cRprIpv6DynamicRSTtl": hh3cRprIpv6DynamicRSTtl,
       "hh3cRprIpv4OverallRSTable": hh3cRprIpv4OverallRSTable,
       "hh3cRprIpv4OverallRSEntry": hh3cRprIpv4OverallRSEntry,
       "hh3cRprIpv4OverallRSIfIndex": hh3cRprIpv4OverallRSIfIndex,
       "hh3cRprIpv4OverallRSMacAddress": hh3cRprIpv4OverallRSMacAddress,
       "hh3cRprIpv4OverallRSType": hh3cRprIpv4OverallRSType,
       "hh3cRprIpv4OverallRSRingletID": hh3cRprIpv4OverallRSRingletID,
       "hh3cRprIpv4OverallRSTtl": hh3cRprIpv4OverallRSTtl,
       "hh3cRprVrrpRSTable": hh3cRprVrrpRSTable,
       "hh3cRprVrrpRSEntry": hh3cRprVrrpRSEntry,
       "hh3cRprVrrpRSIfIndex": hh3cRprVrrpRSIfIndex,
       "hh3cRprVrrpRSVirtualMacAddress": hh3cRprVrrpRSVirtualMacAddress,
       "hh3cRprVrrpRSMacAddress": hh3cRprVrrpRSMacAddress,
       "hh3cRprVrrpRSRingletID": hh3cRprVrrpRSRingletID,
       "hh3cRprVrrpRSTtl": hh3cRprVrrpRSTtl,
       "hh3cRprDefaultRingIDTable": hh3cRprDefaultRingIDTable,
       "hh3cRprDefaultRingIDEntry": hh3cRprDefaultRingIDEntry,
       "hh3cRprDefaultRingIDIfIndex": hh3cRprDefaultRingIDIfIndex,
       "hh3cRprDefaultConfigRingletID": hh3cRprDefaultConfigRingletID,
       "hh3cRprDefaultActiveRingID": hh3cRprDefaultActiveRingID,
       "hh3cRprDefect": hh3cRprDefect,
       "hh3cRprDefectReportTable": hh3cRprDefectReportTable,
       "hh3cRprDefectReportEntry": hh3cRprDefectReportEntry,
       "hh3cRprDefectIfIndex": hh3cRprDefectIfIndex,
       "hh3cRprDefectCurrentStatus": hh3cRprDefectCurrentStatus,
       "hh3cRprPriorityMap": hh3cRprPriorityMap,
       "hh3cRprPriority2ClassMapTable": hh3cRprPriority2ClassMapTable,
       "hh3cRprPriority2ClassMapEntry": hh3cRprPriority2ClassMapEntry,
       "hh3cRprPriority2ClassMapIfIndex": hh3cRprPriority2ClassMapIfIndex,
       "hh3cRprPriority2ClassMapType": hh3cRprPriority2ClassMapType,
       "hh3cRprPriorityValue": hh3cRprPriorityValue,
       "hh3cRprPriority2ClassMap": hh3cRprPriority2ClassMap,
       "hh3cRprRateLimitConfig": hh3cRprRateLimitConfig,
       "hh3cRprRateLimitConfigTable": hh3cRprRateLimitConfigTable,
       "hh3cRprRateLimitConfigEntry": hh3cRprRateLimitConfigEntry,
       "hh3cRprRateLimitConfigIfIndex": hh3cRprRateLimitConfigIfIndex,
       "hh3cRprRateLimitConfigRingletId": hh3cRprRateLimitConfigRingletId,
       "hh3cRprRateLimitConfigServiceClass": hh3cRprRateLimitConfigServiceClass,
       "hh3cRprRateLimitConfigValue": hh3cRprRateLimitConfigValue,
       "hh3cRprMacAddrLearn": hh3cRprMacAddrLearn,
       "hh3cRprMacLearnCfgTable": hh3cRprMacLearnCfgTable,
       "hh3cRprMacLearnCfgEntry": hh3cRprMacLearnCfgEntry,
       "hh3cRprMacLearnIfIndex": hh3cRprMacLearnIfIndex,
       "hh3cRprMacLearnRprMac": hh3cRprMacLearnRprMac,
       "hh3cRprMacLearnType": hh3cRprMacLearnType,
       "hh3cRprMacLearnDestMac": hh3cRprMacLearnDestMac,
       "hh3cRprMacLearnVlanId": hh3cRprMacLearnVlanId,
       "hh3cRprMacLearnRinglet": hh3cRprMacLearnRinglet,
       "hh3cRprMacLearnTtl": hh3cRprMacLearnTtl,
       "hh3cRprMacLearnIsValid": hh3cRprMacLearnIsValid,
       "hh3cRprMacLearnRowStatus": hh3cRprMacLearnRowStatus,
       "hh3cRprTrapVar": hh3cRprTrapVar,
       "hh3cRprTrapVarTable": hh3cRprTrapVarTable,
       "hh3cRprTrapVarEntry": hh3cRprTrapVarEntry,
       "hh3cRprTrapIfIndex": hh3cRprTrapIfIndex,
       "hh3cRprTrapRinglet": hh3cRprTrapRinglet,
       "hh3cRprTrapTopoMacAddress": hh3cRprTrapTopoMacAddress,
       "hh3cRprTrapIpAddress": hh3cRprTrapIpAddress,
       "hh3cRprTrap": hh3cRprTrap,
       "hh3cRprTopologyOpenRing": hh3cRprTopologyOpenRing,
       "hh3cRprTopologyCloseRing": hh3cRprTopologyCloseRing,
       "hh3cRprTopologyInconsistent": hh3cRprTopologyInconsistent,
       "hh3cRprTopologyInstability": hh3cRprTopologyInstability,
       "hh3cRprDuplicateMacAddress": hh3cRprDuplicateMacAddress,
       "hh3cRprDulplicateIPAddress": hh3cRprDulplicateIPAddress,
       "hh3cRprIncompleteLRTT": hh3cRprIncompleteLRTT,
       "hh3cRprProtecConfigInconsistent": hh3cRprProtecConfigInconsistent,
       "hh3cRprJumboConfigInconsistent": hh3cRprJumboConfigInconsistent,
       "hh3cRprExceedMaxReservRate": hh3cRprExceedMaxReservRate,
       "hh3cRprExceedMaxStationNum": hh3cRprExceedMaxStationNum,
       "hh3cRprMiscabling": hh3cRprMiscabling,
       "hh3cRprBackPressure": hh3cRprBackPressure,
       "hh3cRprBackPressureOver": hh3cRprBackPressureOver}
)
