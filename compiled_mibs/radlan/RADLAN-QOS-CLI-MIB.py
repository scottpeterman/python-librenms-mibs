# SNMP MIB module (RADLAN-QOS-CLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\radlan\RADLAN-QOS-CLI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:28 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(Percents,
 rnd) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "Percents",
    "rnd")

(RowPointer,
 RowStatus,
 TruthValue) = mibBuilder.importSymbols(
    "RADLAN-SNMPv2",
    "RowPointer",
    "RowStatus",
    "TruthValue")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rlQosCliMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 88)
)
if mibBuilder.loadTexts:
    rlQosCliMib.setRevisions(
        ("2005-03-14 00:00",
         "2005-02-07 00:00",
         "2005-01-27 00:00",
         "2004-11-15 00:00",
         "2003-09-29 00:00",
         "2003-09-21 00:00",
         "2005-04-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClassOffsetType(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("packetStart", 1),
          ("layer2-start", 2),
          ("mpls-start", 3),
          ("layer3-start", 4),
          ("layer4-start", 5),
          ("layer5-start", 6),
          ("vlan", 7),
          ("in-port", 8),
          ("out-port", 9),
          ("vpt", 10),
          ("ethertype", 11))
    )



class ClassTupleType(TextualConvention, Integer32):
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("protocol", 1),
          ("ip-src", 2),
          ("ip-dest", 3),
          ("dscp", 4),
          ("ip-precedence", 5),
          ("udp-port-src", 6),
          ("udp-port-dest", 7),
          ("tcp-port-src", 8),
          ("tcp-port-dest", 9),
          ("mac-src", 10),
          ("mac-dest", 11),
          ("vlan", 12),
          ("in-port", 13),
          ("out-port", 14),
          ("general", 15),
          ("vpt", 16),
          ("ether-type", 17),
          ("tcp-flags", 18),
          ("icmp-type", 19),
          ("icmp-code", 20),
          ("igmp-type", 21))
    )



class AceActionType(TextualConvention, Integer32):
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
        *(("permit", 1),
          ("deny", 2),
          ("deny-DisablePort", 3))
    )



class AceObjectType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ip-TCP", 2),
          ("ip-UDP", 3),
          ("ip-Offset", 4),
          ("mac", 5),
          ("mac-Offset", 6),
          ("ip-ICMP", 7),
          ("ip-IGMP", 8))
    )



class AclObjectType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ip", 2))
    )



class ClassMapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchAll", 1),
          ("matchAny", 2))
    )



class ClassMapAction(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("setIP-Precedence", 2),
          ("setDSCP", 3),
          ("setQueue", 4),
          ("setCos", 5),
          ("trustCos", 6),
          ("trustDSCP", 7),
          ("trustTCP-UDPport", 8),
          ("trustCosDscp", 9))
    )



class PolicerType(TextualConvention, Integer32):
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
        *(("single", 1),
          ("aggregate", 2),
          ("cascade", 3))
    )



class PolicerAction(TextualConvention, Integer32):
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
        *(("none", 1),
          ("drop", 2),
          ("remark", 3),
          ("explicit-remark", 4),
          ("cascadePointer", 5))
    )



class QosObjectMode(TextualConvention, Integer32):
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
        *(("disable", 1),
          ("basic", 2),
          ("advance", 3),
          ("service", 4))
    )



class QosObjectBasicMode(TextualConvention, Integer32):
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
        *(("none", 1),
          ("vpt", 2),
          ("dscp", 3),
          ("dscp-mutation", 4),
          ("tcp-udp", 5))
    )



class BinaryStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )



class QueueType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ef", 1),
          ("wrr", 2))
    )



class AclDefaultAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny-all", 1),
          ("forward-all", 2))
    )



class InterfaceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("port", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlQosCliQosMode_Type = QosObjectMode
_RlQosCliQosMode_Object = MibScalar
rlQosCliQosMode = _RlQosCliQosMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 1),
    _RlQosCliQosMode_Type()
)
rlQosCliQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosCliQosMode.setStatus("current")
_RlQosCliBasicModeCfg_Type = QosObjectBasicMode
_RlQosCliBasicModeCfg_Object = MibScalar
rlQosCliBasicModeCfg = _RlQosCliBasicModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 2),
    _RlQosCliBasicModeCfg_Type()
)
rlQosCliBasicModeCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosCliBasicModeCfg.setStatus("current")
_RlQosMaxNumOfAce_Type = Integer32
_RlQosMaxNumOfAce_Object = MibScalar
rlQosMaxNumOfAce = _RlQosMaxNumOfAce_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 3),
    _RlQosMaxNumOfAce_Type()
)
rlQosMaxNumOfAce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosMaxNumOfAce.setStatus("current")
_RlQosOffsetTable_Object = MibTable
rlQosOffsetTable = _RlQosOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 4)
)
if mibBuilder.loadTexts:
    rlQosOffsetTable.setStatus("current")
_RlQosOffsetEntry_Object = MibTableRow
rlQosOffsetEntry = _RlQosOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 4, 1)
)
rlQosOffsetEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosOffsetIndex"),
)
if mibBuilder.loadTexts:
    rlQosOffsetEntry.setStatus("current")
_RlQosOffsetIndex_Type = Integer32
_RlQosOffsetIndex_Object = MibTableColumn
rlQosOffsetIndex = _RlQosOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 4, 1, 1),
    _RlQosOffsetIndex_Type()
)
rlQosOffsetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosOffsetIndex.setStatus("current")
_RlQosOffsetType_Type = ClassOffsetType
_RlQosOffsetType_Object = MibTableColumn
rlQosOffsetType = _RlQosOffsetType_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 4, 1, 2),
    _RlQosOffsetType_Type()
)
rlQosOffsetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetType.setStatus("current")
_RlQosOffsetValue_Type = Integer32
_RlQosOffsetValue_Object = MibTableColumn
rlQosOffsetValue = _RlQosOffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 4, 1, 3),
    _RlQosOffsetValue_Type()
)
rlQosOffsetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetValue.setStatus("current")


class _RlQosOffsetMask_Type(Integer32):
    """Custom type rlQosOffsetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlQosOffsetMask_Type.__name__ = "Integer32"
_RlQosOffsetMask_Object = MibTableColumn
rlQosOffsetMask = _RlQosOffsetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 4, 1, 4),
    _RlQosOffsetMask_Type()
)
rlQosOffsetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetMask.setStatus("current")


class _RlQosOffsetPattern_Type(Integer32):
    """Custom type rlQosOffsetPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlQosOffsetPattern_Type.__name__ = "Integer32"
_RlQosOffsetPattern_Object = MibTableColumn
rlQosOffsetPattern = _RlQosOffsetPattern_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 4, 1, 5),
    _RlQosOffsetPattern_Type()
)
rlQosOffsetPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetPattern.setStatus("current")
_RlQosOffsetTuplePointer_Type = Integer32
_RlQosOffsetTuplePointer_Object = MibTableColumn
rlQosOffsetTuplePointer = _RlQosOffsetTuplePointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 4, 1, 6),
    _RlQosOffsetTuplePointer_Type()
)
rlQosOffsetTuplePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetTuplePointer.setStatus("current")
_RlQosOffsetStatus_Type = RowStatus
_RlQosOffsetStatus_Object = MibTableColumn
rlQosOffsetStatus = _RlQosOffsetStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 4, 1, 7),
    _RlQosOffsetStatus_Type()
)
rlQosOffsetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetStatus.setStatus("current")
_RlQosTupleTable_Object = MibTable
rlQosTupleTable = _RlQosTupleTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 5)
)
if mibBuilder.loadTexts:
    rlQosTupleTable.setStatus("current")
_RlQosTupleEntry_Object = MibTableRow
rlQosTupleEntry = _RlQosTupleEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 5, 1)
)
rlQosTupleEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosTupleIndex"),
)
if mibBuilder.loadTexts:
    rlQosTupleEntry.setStatus("current")
_RlQosTupleIndex_Type = Integer32
_RlQosTupleIndex_Object = MibTableColumn
rlQosTupleIndex = _RlQosTupleIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 5, 1, 1),
    _RlQosTupleIndex_Type()
)
rlQosTupleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosTupleIndex.setStatus("current")
_RlQosTupleType_Type = ClassTupleType
_RlQosTupleType_Object = MibTableColumn
rlQosTupleType = _RlQosTupleType_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 5, 1, 2),
    _RlQosTupleType_Type()
)
rlQosTupleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTupleType.setStatus("current")
_RlQosTupleValue1_Type = Integer32
_RlQosTupleValue1_Object = MibTableColumn
rlQosTupleValue1 = _RlQosTupleValue1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 5, 1, 3),
    _RlQosTupleValue1_Type()
)
rlQosTupleValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTupleValue1.setStatus("current")


class _RlQosTupleValue2_Type(OctetString):
    """Custom type rlQosTupleValue2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RlQosTupleValue2_Type.__name__ = "OctetString"
_RlQosTupleValue2_Object = MibTableColumn
rlQosTupleValue2 = _RlQosTupleValue2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 5, 1, 4),
    _RlQosTupleValue2_Type()
)
rlQosTupleValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTupleValue2.setStatus("current")
_RlQosTupleStatus_Type = RowStatus
_RlQosTupleStatus_Object = MibTableColumn
rlQosTupleStatus = _RlQosTupleStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 5, 1, 5),
    _RlQosTupleStatus_Type()
)
rlQosTupleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTupleStatus.setStatus("current")
_RlQosAceTable_Object = MibTable
rlQosAceTable = _RlQosAceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6)
)
if mibBuilder.loadTexts:
    rlQosAceTable.setStatus("current")
_RlQosAceEntry_Object = MibTableRow
rlQosAceEntry = _RlQosAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1)
)
rlQosAceEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosAceIndex"),
)
if mibBuilder.loadTexts:
    rlQosAceEntry.setStatus("current")
_RlQosAceIndex_Type = Integer32
_RlQosAceIndex_Object = MibTableColumn
rlQosAceIndex = _RlQosAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 1),
    _RlQosAceIndex_Type()
)
rlQosAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosAceIndex.setStatus("current")
_RlQosAceAction_Type = AceActionType
_RlQosAceAction_Object = MibTableColumn
rlQosAceAction = _RlQosAceAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 2),
    _RlQosAceAction_Type()
)
rlQosAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceAction.setStatus("current")
_RlQosAceType_Type = AceObjectType
_RlQosAceType_Object = MibTableColumn
rlQosAceType = _RlQosAceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 3),
    _RlQosAceType_Type()
)
rlQosAceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceType.setStatus("current")
_RlQosAceTuple1_Type = Integer32
_RlQosAceTuple1_Object = MibTableColumn
rlQosAceTuple1 = _RlQosAceTuple1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 4),
    _RlQosAceTuple1_Type()
)
rlQosAceTuple1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple1.setStatus("current")
_RlQosAceTuple2_Type = Integer32
_RlQosAceTuple2_Object = MibTableColumn
rlQosAceTuple2 = _RlQosAceTuple2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 5),
    _RlQosAceTuple2_Type()
)
rlQosAceTuple2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple2.setStatus("current")
_RlQosAceTuple3_Type = Integer32
_RlQosAceTuple3_Object = MibTableColumn
rlQosAceTuple3 = _RlQosAceTuple3_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 6),
    _RlQosAceTuple3_Type()
)
rlQosAceTuple3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple3.setStatus("current")
_RlQosAceTuple4_Type = Integer32
_RlQosAceTuple4_Object = MibTableColumn
rlQosAceTuple4 = _RlQosAceTuple4_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 7),
    _RlQosAceTuple4_Type()
)
rlQosAceTuple4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple4.setStatus("current")
_RlQosAceTuple5_Type = Integer32
_RlQosAceTuple5_Object = MibTableColumn
rlQosAceTuple5 = _RlQosAceTuple5_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 8),
    _RlQosAceTuple5_Type()
)
rlQosAceTuple5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple5.setStatus("current")
_RlQosAceTuple6_Type = Integer32
_RlQosAceTuple6_Object = MibTableColumn
rlQosAceTuple6 = _RlQosAceTuple6_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 9),
    _RlQosAceTuple6_Type()
)
rlQosAceTuple6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple6.setStatus("current")
_RlQosAceTuple7_Type = Integer32
_RlQosAceTuple7_Object = MibTableColumn
rlQosAceTuple7 = _RlQosAceTuple7_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 10),
    _RlQosAceTuple7_Type()
)
rlQosAceTuple7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple7.setStatus("current")
_RlQosAceTuple8_Type = Integer32
_RlQosAceTuple8_Object = MibTableColumn
rlQosAceTuple8 = _RlQosAceTuple8_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 11),
    _RlQosAceTuple8_Type()
)
rlQosAceTuple8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple8.setStatus("current")
_RlQosAceAccount_Type = BinaryStatus
_RlQosAceAccount_Object = MibTableColumn
rlQosAceAccount = _RlQosAceAccount_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 12),
    _RlQosAceAccount_Type()
)
rlQosAceAccount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceAccount.setStatus("current")
_RlQosAceStatus_Type = RowStatus
_RlQosAceStatus_Object = MibTableColumn
rlQosAceStatus = _RlQosAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 6, 1, 13),
    _RlQosAceStatus_Type()
)
rlQosAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceStatus.setStatus("current")
_RlQosAclTable_Object = MibTable
rlQosAclTable = _RlQosAclTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 7)
)
if mibBuilder.loadTexts:
    rlQosAclTable.setStatus("current")
_RlQosAclEntry_Object = MibTableRow
rlQosAclEntry = _RlQosAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 7, 1)
)
rlQosAclEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosAclIndex"),
)
if mibBuilder.loadTexts:
    rlQosAclEntry.setStatus("current")
_RlQosAclIndex_Type = Integer32
_RlQosAclIndex_Object = MibTableColumn
rlQosAclIndex = _RlQosAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 7, 1, 1),
    _RlQosAclIndex_Type()
)
rlQosAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosAclIndex.setStatus("current")


class _RlQosAclName_Type(DisplayString):
    """Custom type rlQosAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosAclName_Type.__name__ = "DisplayString"
_RlQosAclName_Object = MibTableColumn
rlQosAclName = _RlQosAclName_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 7, 1, 2),
    _RlQosAclName_Type()
)
rlQosAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclName.setStatus("current")
_RlQosAclType_Type = AclObjectType
_RlQosAclType_Object = MibTableColumn
rlQosAclType = _RlQosAclType_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 7, 1, 3),
    _RlQosAclType_Type()
)
rlQosAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclType.setStatus("current")
_RlQosAclStatus_Type = RowStatus
_RlQosAclStatus_Object = MibTableColumn
rlQosAclStatus = _RlQosAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 7, 1, 4),
    _RlQosAclStatus_Type()
)
rlQosAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclStatus.setStatus("current")
_RlQosAclAceRefTable_Object = MibTable
rlQosAclAceRefTable = _RlQosAclAceRefTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 8)
)
if mibBuilder.loadTexts:
    rlQosAclAceRefTable.setStatus("current")
_RlQosAclAceRefEntry_Object = MibTableRow
rlQosAclAceRefEntry = _RlQosAclAceRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 8, 1)
)
rlQosAclAceRefEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosAclAceRefAcePointer"),
)
if mibBuilder.loadTexts:
    rlQosAclAceRefEntry.setStatus("current")
_RlQosAclAceRefAcePointer_Type = Integer32
_RlQosAclAceRefAcePointer_Object = MibTableColumn
rlQosAclAceRefAcePointer = _RlQosAclAceRefAcePointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 8, 1, 1),
    _RlQosAclAceRefAcePointer_Type()
)
rlQosAclAceRefAcePointer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosAclAceRefAcePointer.setStatus("current")
_RlQosAclAceRefAclPointer_Type = Integer32
_RlQosAclAceRefAclPointer_Object = MibTableColumn
rlQosAclAceRefAclPointer = _RlQosAclAceRefAclPointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 8, 1, 2),
    _RlQosAclAceRefAclPointer_Type()
)
rlQosAclAceRefAclPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclAceRefAclPointer.setStatus("current")
_RlQosAclAceRefStatus_Type = RowStatus
_RlQosAclAceRefStatus_Object = MibTableColumn
rlQosAclAceRefStatus = _RlQosAclAceRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 8, 1, 3),
    _RlQosAclAceRefStatus_Type()
)
rlQosAclAceRefStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclAceRefStatus.setStatus("current")
_RlQosClassMapTable_Object = MibTable
rlQosClassMapTable = _RlQosClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9)
)
if mibBuilder.loadTexts:
    rlQosClassMapTable.setStatus("current")
_RlQosClassMapEntry_Object = MibTableRow
rlQosClassMapEntry = _RlQosClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1)
)
rlQosClassMapEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosClassMapIndex"),
)
if mibBuilder.loadTexts:
    rlQosClassMapEntry.setStatus("current")
_RlQosClassMapIndex_Type = Integer32
_RlQosClassMapIndex_Object = MibTableColumn
rlQosClassMapIndex = _RlQosClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 1),
    _RlQosClassMapIndex_Type()
)
rlQosClassMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosClassMapIndex.setStatus("current")


class _RlQosClassMapName_Type(DisplayString):
    """Custom type rlQosClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosClassMapName_Type.__name__ = "DisplayString"
_RlQosClassMapName_Object = MibTableColumn
rlQosClassMapName = _RlQosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 2),
    _RlQosClassMapName_Type()
)
rlQosClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapName.setStatus("current")
_RlQosClassMapType_Type = ClassMapType
_RlQosClassMapType_Object = MibTableColumn
rlQosClassMapType = _RlQosClassMapType_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 3),
    _RlQosClassMapType_Type()
)
rlQosClassMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapType.setStatus("current")
_RlQosClassMapAction_Type = ClassMapAction
_RlQosClassMapAction_Object = MibTableColumn
rlQosClassMapAction = _RlQosClassMapAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 4),
    _RlQosClassMapAction_Type()
)
rlQosClassMapAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapAction.setStatus("current")
_RlQosClassMapMarkValue_Type = Integer32
_RlQosClassMapMarkValue_Object = MibTableColumn
rlQosClassMapMarkValue = _RlQosClassMapMarkValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 5),
    _RlQosClassMapMarkValue_Type()
)
rlQosClassMapMarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapMarkValue.setStatus("current")
_RlQosClassMapPolicer_Type = Integer32
_RlQosClassMapPolicer_Object = MibTableColumn
rlQosClassMapPolicer = _RlQosClassMapPolicer_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 6),
    _RlQosClassMapPolicer_Type()
)
rlQosClassMapPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapPolicer.setStatus("current")
_RlQosClassMapMatch1_Type = Integer32
_RlQosClassMapMatch1_Object = MibTableColumn
rlQosClassMapMatch1 = _RlQosClassMapMatch1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 7),
    _RlQosClassMapMatch1_Type()
)
rlQosClassMapMatch1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapMatch1.setStatus("current")
_RlQosClassMapMatch2_Type = Integer32
_RlQosClassMapMatch2_Object = MibTableColumn
rlQosClassMapMatch2 = _RlQosClassMapMatch2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 8),
    _RlQosClassMapMatch2_Type()
)
rlQosClassMapMatch2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapMatch2.setStatus("current")
_RlQosClassMapMarkVlan_Type = BinaryStatus
_RlQosClassMapMarkVlan_Object = MibTableColumn
rlQosClassMapMarkVlan = _RlQosClassMapMarkVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 9),
    _RlQosClassMapMarkVlan_Type()
)
rlQosClassMapMarkVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapMarkVlan.setStatus("current")


class _RlQosClassMapNewVlan_Type(Integer32):
    """Custom type rlQosClassMapNewVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlQosClassMapNewVlan_Type.__name__ = "Integer32"
_RlQosClassMapNewVlan_Object = MibTableColumn
rlQosClassMapNewVlan = _RlQosClassMapNewVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 10),
    _RlQosClassMapNewVlan_Type()
)
rlQosClassMapNewVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapNewVlan.setStatus("current")
_RlQosClassMapNewPort_Type = Integer32
_RlQosClassMapNewPort_Object = MibTableColumn
rlQosClassMapNewPort = _RlQosClassMapNewPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 11),
    _RlQosClassMapNewPort_Type()
)
rlQosClassMapNewPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapNewPort.setStatus("current")
_RlQosClassMapCopyPort_Type = Integer32
_RlQosClassMapCopyPort_Object = MibTableColumn
rlQosClassMapCopyPort = _RlQosClassMapCopyPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 12),
    _RlQosClassMapCopyPort_Type()
)
rlQosClassMapCopyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapCopyPort.setStatus("current")
_RlQosClassMapStatus_Type = RowStatus
_RlQosClassMapStatus_Object = MibTableColumn
rlQosClassMapStatus = _RlQosClassMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 9, 1, 13),
    _RlQosClassMapStatus_Type()
)
rlQosClassMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapStatus.setStatus("current")
_RlQosPolicerTable_Object = MibTable
rlQosPolicerTable = _RlQosPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 10)
)
if mibBuilder.loadTexts:
    rlQosPolicerTable.setStatus("current")
_RlQosPolicerEntry_Object = MibTableRow
rlQosPolicerEntry = _RlQosPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 10, 1)
)
rlQosPolicerEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosPolicerIndex"),
)
if mibBuilder.loadTexts:
    rlQosPolicerEntry.setStatus("current")
_RlQosPolicerIndex_Type = Integer32
_RlQosPolicerIndex_Object = MibTableColumn
rlQosPolicerIndex = _RlQosPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 10, 1, 1),
    _RlQosPolicerIndex_Type()
)
rlQosPolicerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPolicerIndex.setStatus("current")


class _RlQosPolicerName_Type(DisplayString):
    """Custom type rlQosPolicerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosPolicerName_Type.__name__ = "DisplayString"
_RlQosPolicerName_Object = MibTableColumn
rlQosPolicerName = _RlQosPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 10, 1, 2),
    _RlQosPolicerName_Type()
)
rlQosPolicerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerName.setStatus("current")
_RlQosPolicerType_Type = PolicerType
_RlQosPolicerType_Object = MibTableColumn
rlQosPolicerType = _RlQosPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 10, 1, 3),
    _RlQosPolicerType_Type()
)
rlQosPolicerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerType.setStatus("current")
_RlQosPolicerCir_Type = Unsigned32
_RlQosPolicerCir_Object = MibTableColumn
rlQosPolicerCir = _RlQosPolicerCir_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 10, 1, 4),
    _RlQosPolicerCir_Type()
)
rlQosPolicerCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerCir.setStatus("current")
if mibBuilder.loadTexts:
    rlQosPolicerCir.setUnits("kbps")
_RlQosPolicerCbs_Type = Unsigned32
_RlQosPolicerCbs_Object = MibTableColumn
rlQosPolicerCbs = _RlQosPolicerCbs_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 10, 1, 5),
    _RlQosPolicerCbs_Type()
)
rlQosPolicerCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerCbs.setStatus("current")
if mibBuilder.loadTexts:
    rlQosPolicerCbs.setUnits("bytes")
_RlQosPolicerAction_Type = PolicerAction
_RlQosPolicerAction_Object = MibTableColumn
rlQosPolicerAction = _RlQosPolicerAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 10, 1, 6),
    _RlQosPolicerAction_Type()
)
rlQosPolicerAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerAction.setStatus("current")
_RlQosPolicerCasPointerRemVal_Type = Integer32
_RlQosPolicerCasPointerRemVal_Object = MibTableColumn
rlQosPolicerCasPointerRemVal = _RlQosPolicerCasPointerRemVal_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 10, 1, 7),
    _RlQosPolicerCasPointerRemVal_Type()
)
rlQosPolicerCasPointerRemVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerCasPointerRemVal.setStatus("current")
_RlQosPolicerStatus_Type = RowStatus
_RlQosPolicerStatus_Object = MibTableColumn
rlQosPolicerStatus = _RlQosPolicerStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 10, 1, 8),
    _RlQosPolicerStatus_Type()
)
rlQosPolicerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerStatus.setStatus("current")
_RlQosPolicyMapTable_Object = MibTable
rlQosPolicyMapTable = _RlQosPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 11)
)
if mibBuilder.loadTexts:
    rlQosPolicyMapTable.setStatus("current")
_RlQosPolicyMapEntry_Object = MibTableRow
rlQosPolicyMapEntry = _RlQosPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 11, 1)
)
rlQosPolicyMapEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    rlQosPolicyMapEntry.setStatus("current")
_RlQosPolicyMapIndex_Type = Integer32
_RlQosPolicyMapIndex_Object = MibTableColumn
rlQosPolicyMapIndex = _RlQosPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 11, 1, 1),
    _RlQosPolicyMapIndex_Type()
)
rlQosPolicyMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPolicyMapIndex.setStatus("current")


class _RlQosPolicyMapName_Type(DisplayString):
    """Custom type rlQosPolicyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosPolicyMapName_Type.__name__ = "DisplayString"
_RlQosPolicyMapName_Object = MibTableColumn
rlQosPolicyMapName = _RlQosPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 11, 1, 2),
    _RlQosPolicyMapName_Type()
)
rlQosPolicyMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyMapName.setStatus("current")
_RlQosPolicyMapStatus_Type = RowStatus
_RlQosPolicyMapStatus_Object = MibTableColumn
rlQosPolicyMapStatus = _RlQosPolicyMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 11, 1, 3),
    _RlQosPolicyMapStatus_Type()
)
rlQosPolicyMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyMapStatus.setStatus("current")
_RlQosPolicyClassRefTable_Object = MibTable
rlQosPolicyClassRefTable = _RlQosPolicyClassRefTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 12)
)
if mibBuilder.loadTexts:
    rlQosPolicyClassRefTable.setStatus("current")
_RlQosPolicyClassRefEntry_Object = MibTableRow
rlQosPolicyClassRefEntry = _RlQosPolicyClassRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 12, 1)
)
rlQosPolicyClassRefEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosPolicyClassRefClassPointer"),
)
if mibBuilder.loadTexts:
    rlQosPolicyClassRefEntry.setStatus("current")
_RlQosPolicyClassRefClassPointer_Type = Integer32
_RlQosPolicyClassRefClassPointer_Object = MibTableColumn
rlQosPolicyClassRefClassPointer = _RlQosPolicyClassRefClassPointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 12, 1, 1),
    _RlQosPolicyClassRefClassPointer_Type()
)
rlQosPolicyClassRefClassPointer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPolicyClassRefClassPointer.setStatus("current")
_RlQosPolicyClassRefPolicyPointer_Type = Integer32
_RlQosPolicyClassRefPolicyPointer_Object = MibTableColumn
rlQosPolicyClassRefPolicyPointer = _RlQosPolicyClassRefPolicyPointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 12, 1, 2),
    _RlQosPolicyClassRefPolicyPointer_Type()
)
rlQosPolicyClassRefPolicyPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyClassRefPolicyPointer.setStatus("current")
_RlQosPolicyClassRefStatus_Type = RowStatus
_RlQosPolicyClassRefStatus_Object = MibTableColumn
rlQosPolicyClassRefStatus = _RlQosPolicyClassRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 12, 1, 3),
    _RlQosPolicyClassRefStatus_Type()
)
rlQosPolicyClassRefStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyClassRefStatus.setStatus("current")
_RlQosIfPolicyTable_Object = MibTable
rlQosIfPolicyTable = _RlQosIfPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13)
)
if mibBuilder.loadTexts:
    rlQosIfPolicyTable.setStatus("current")
_RlQosIfPolicyEntry_Object = MibTableRow
rlQosIfPolicyEntry = _RlQosIfPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1)
)
rlQosIfPolicyEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlIfIndex"),
    (0, "RADLAN-QOS-CLI-MIB", "rlIfType"),
)
if mibBuilder.loadTexts:
    rlQosIfPolicyEntry.setStatus("current")
_RlIfIndex_Type = InterfaceIndex
_RlIfIndex_Object = MibTableColumn
rlIfIndex = _RlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 1),
    _RlIfIndex_Type()
)
rlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIfIndex.setStatus("current")
_RlIfType_Type = InterfaceType
_RlIfType_Object = MibTableColumn
rlIfType = _RlIfType_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 2),
    _RlIfType_Type()
)
rlIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIfType.setStatus("current")
_RlQosIfPolicyMapPointerIn_Type = Integer32
_RlQosIfPolicyMapPointerIn_Object = MibTableColumn
rlQosIfPolicyMapPointerIn = _RlQosIfPolicyMapPointerIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 3),
    _RlQosIfPolicyMapPointerIn_Type()
)
rlQosIfPolicyMapPointerIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfPolicyMapPointerIn.setStatus("current")
_RlQosIfPolicyMapPointerOut_Type = Integer32
_RlQosIfPolicyMapPointerOut_Object = MibTableColumn
rlQosIfPolicyMapPointerOut = _RlQosIfPolicyMapPointerOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 4),
    _RlQosIfPolicyMapPointerOut_Type()
)
rlQosIfPolicyMapPointerOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfPolicyMapPointerOut.setStatus("current")
_RlQosIfTrustActive_Type = BinaryStatus
_RlQosIfTrustActive_Object = MibTableColumn
rlQosIfTrustActive = _RlQosIfTrustActive_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 5),
    _RlQosIfTrustActive_Type()
)
rlQosIfTrustActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfTrustActive.setStatus("current")
_RlQosPortShaperStatus_Type = BinaryStatus
_RlQosPortShaperStatus_Object = MibTableColumn
rlQosPortShaperStatus = _RlQosPortShaperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 6),
    _RlQosPortShaperStatus_Type()
)
rlQosPortShaperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPortShaperStatus.setStatus("current")
_RlQosCirPortShaper_Type = Integer32
_RlQosCirPortShaper_Object = MibTableColumn
rlQosCirPortShaper = _RlQosCirPortShaper_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 7),
    _RlQosCirPortShaper_Type()
)
rlQosCirPortShaper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirPortShaper.setStatus("current")
if mibBuilder.loadTexts:
    rlQosCirPortShaper.setUnits("bps")
_RlQosCbsPortShaper_Type = Integer32
_RlQosCbsPortShaper_Object = MibTableColumn
rlQosCbsPortShaper = _RlQosCbsPortShaper_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 8),
    _RlQosCbsPortShaper_Type()
)
rlQosCbsPortShaper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsPortShaper.setStatus("current")
if mibBuilder.loadTexts:
    rlQosCbsPortShaper.setUnits("bytes")


class _RlQosIfProfilePointer_Type(DisplayString):
    """Custom type rlQosIfProfilePointer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosIfProfilePointer_Type.__name__ = "DisplayString"
_RlQosIfProfilePointer_Object = MibTableColumn
rlQosIfProfilePointer = _RlQosIfProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 9),
    _RlQosIfProfilePointer_Type()
)
rlQosIfProfilePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfProfilePointer.setStatus("current")


class _RlQosQueueProfilePointer_Type(DisplayString):
    """Custom type rlQosQueueProfilePointer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosQueueProfilePointer_Type.__name__ = "DisplayString"
_RlQosQueueProfilePointer_Object = MibTableColumn
rlQosQueueProfilePointer = _RlQosQueueProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 10),
    _RlQosQueueProfilePointer_Type()
)
rlQosQueueProfilePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosQueueProfilePointer.setStatus("current")
_RlQosQueueShapeProfilePointer_Type = Integer32
_RlQosQueueShapeProfilePointer_Object = MibTableColumn
rlQosQueueShapeProfilePointer = _RlQosQueueShapeProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 11),
    _RlQosQueueShapeProfilePointer_Type()
)
rlQosQueueShapeProfilePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosQueueShapeProfilePointer.setStatus("current")
_RlQosAclDefaultAction_Type = AclDefaultAction
_RlQosAclDefaultAction_Object = MibTableColumn
rlQosAclDefaultAction = _RlQosAclDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 12),
    _RlQosAclDefaultAction_Type()
)
rlQosAclDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclDefaultAction.setStatus("current")
_RlQosIfPolicyMapStatus_Type = RowStatus
_RlQosIfPolicyMapStatus_Object = MibTableColumn
rlQosIfPolicyMapStatus = _RlQosIfPolicyMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 13),
    _RlQosIfPolicyMapStatus_Type()
)
rlQosIfPolicyMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfPolicyMapStatus.setStatus("current")


class _RlQosIfAclIn_Type(Integer32):
    """Custom type rlQosIfAclIn based on Integer32"""
    defaultValue = 0


_RlQosIfAclIn_Type.__name__ = "Integer32"
_RlQosIfAclIn_Object = MibTableColumn
rlQosIfAclIn = _RlQosIfAclIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 14),
    _RlQosIfAclIn_Type()
)
rlQosIfAclIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfAclIn.setStatus("current")


class _RlQosIfAclOut_Type(Integer32):
    """Custom type rlQosIfAclOut based on Integer32"""
    defaultValue = 0


_RlQosIfAclOut_Type.__name__ = "Integer32"
_RlQosIfAclOut_Object = MibTableColumn
rlQosIfAclOut = _RlQosIfAclOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 15),
    _RlQosIfAclOut_Type()
)
rlQosIfAclOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfAclOut.setStatus("current")


class _RlQosIfPolicerIn_Type(Integer32):
    """Custom type rlQosIfPolicerIn based on Integer32"""
    defaultValue = 0


_RlQosIfPolicerIn_Type.__name__ = "Integer32"
_RlQosIfPolicerIn_Object = MibTableColumn
rlQosIfPolicerIn = _RlQosIfPolicerIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 16),
    _RlQosIfPolicerIn_Type()
)
rlQosIfPolicerIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfPolicerIn.setStatus("current")


class _RlQosPortRateLimitStatus_Type(BinaryStatus):
    """Custom type rlQosPortRateLimitStatus based on BinaryStatus"""
    defaultValue = 1


_RlQosPortRateLimitStatus_Type.__name__ = "BinaryStatus"
_RlQosPortRateLimitStatus_Object = MibTableColumn
rlQosPortRateLimitStatus = _RlQosPortRateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 17),
    _RlQosPortRateLimitStatus_Type()
)
rlQosPortRateLimitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPortRateLimitStatus.setStatus("current")


class _RlQosCirPortRateLimit_Type(Integer32):
    """Custom type rlQosCirPortRateLimit based on Integer32"""
    defaultValue = 0


_RlQosCirPortRateLimit_Type.__name__ = "Integer32"
_RlQosCirPortRateLimit_Object = MibTableColumn
rlQosCirPortRateLimit = _RlQosCirPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 18),
    _RlQosCirPortRateLimit_Type()
)
rlQosCirPortRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirPortRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    rlQosCirPortRateLimit.setUnits("bps")


class _RlQosCbsPortRateLimit_Type(Integer32):
    """Custom type rlQosCbsPortRateLimit based on Integer32"""
    defaultValue = 0


_RlQosCbsPortRateLimit_Type.__name__ = "Integer32"
_RlQosCbsPortRateLimit_Object = MibTableColumn
rlQosCbsPortRateLimit = _RlQosCbsPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 13, 1, 19),
    _RlQosCbsPortRateLimit_Type()
)
rlQosCbsPortRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsPortRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    rlQosCbsPortRateLimit.setUnits("bytes")
_RlQosIfProfileCfgTable_Object = MibTable
rlQosIfProfileCfgTable = _RlQosIfProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14)
)
if mibBuilder.loadTexts:
    rlQosIfProfileCfgTable.setStatus("current")
_RlQosIfProfileCfgEntry_Object = MibTableRow
rlQosIfProfileCfgEntry = _RlQosIfProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1)
)
rlQosIfProfileCfgEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlIfProfileName"),
    (0, "RADLAN-QOS-CLI-MIB", "rlQosQueueId"),
)
if mibBuilder.loadTexts:
    rlQosIfProfileCfgEntry.setStatus("current")


class _RlIfProfileName_Type(DisplayString):
    """Custom type rlIfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlIfProfileName_Type.__name__ = "DisplayString"
_RlIfProfileName_Object = MibTableColumn
rlIfProfileName = _RlIfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 1),
    _RlIfProfileName_Type()
)
rlIfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIfProfileName.setStatus("current")


class _RlQosQueueId_Type(Integer32):
    """Custom type rlQosQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosQueueId_Type.__name__ = "Integer32"
_RlQosQueueId_Object = MibTableColumn
rlQosQueueId = _RlQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 2),
    _RlQosQueueId_Type()
)
rlQosQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosQueueId.setStatus("current")


class _RlQosTdThersholdDp0_Type(Integer32):
    """Custom type rlQosTdThersholdDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosTdThersholdDp0_Type.__name__ = "Integer32"
_RlQosTdThersholdDp0_Object = MibTableColumn
rlQosTdThersholdDp0 = _RlQosTdThersholdDp0_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 3),
    _RlQosTdThersholdDp0_Type()
)
rlQosTdThersholdDp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp0.setStatus("current")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp0.setUnits("percent")


class _RlQosTdThersholdDp1_Type(Integer32):
    """Custom type rlQosTdThersholdDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosTdThersholdDp1_Type.__name__ = "Integer32"
_RlQosTdThersholdDp1_Object = MibTableColumn
rlQosTdThersholdDp1 = _RlQosTdThersholdDp1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 4),
    _RlQosTdThersholdDp1_Type()
)
rlQosTdThersholdDp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp1.setStatus("current")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp1.setUnits("percent")


class _RlQosTdThersholdDp2_Type(Integer32):
    """Custom type rlQosTdThersholdDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosTdThersholdDp2_Type.__name__ = "Integer32"
_RlQosTdThersholdDp2_Object = MibTableColumn
rlQosTdThersholdDp2 = _RlQosTdThersholdDp2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 5),
    _RlQosTdThersholdDp2_Type()
)
rlQosTdThersholdDp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp2.setStatus("current")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp2.setUnits("percent")


class _RlQosRedMinDp0_Type(Integer32):
    """Custom type rlQosRedMinDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMinDp0_Type.__name__ = "Integer32"
_RlQosRedMinDp0_Object = MibTableColumn
rlQosRedMinDp0 = _RlQosRedMinDp0_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 6),
    _RlQosRedMinDp0_Type()
)
rlQosRedMinDp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMinDp0.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMinDp0.setUnits("percent")


class _RlQosRedMaxDp0_Type(Integer32):
    """Custom type rlQosRedMaxDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMaxDp0_Type.__name__ = "Integer32"
_RlQosRedMaxDp0_Object = MibTableColumn
rlQosRedMaxDp0 = _RlQosRedMaxDp0_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 7),
    _RlQosRedMaxDp0_Type()
)
rlQosRedMaxDp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMaxDp0.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMaxDp0.setUnits("percent")
_RlQosRedProbDp0_Type = Integer32
_RlQosRedProbDp0_Object = MibTableColumn
rlQosRedProbDp0 = _RlQosRedProbDp0_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 8),
    _RlQosRedProbDp0_Type()
)
rlQosRedProbDp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedProbDp0.setStatus("current")


class _RlQosRedMinDp1_Type(Integer32):
    """Custom type rlQosRedMinDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMinDp1_Type.__name__ = "Integer32"
_RlQosRedMinDp1_Object = MibTableColumn
rlQosRedMinDp1 = _RlQosRedMinDp1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 9),
    _RlQosRedMinDp1_Type()
)
rlQosRedMinDp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMinDp1.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMinDp1.setUnits("percent")


class _RlQosRedMaxDp1_Type(Integer32):
    """Custom type rlQosRedMaxDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMaxDp1_Type.__name__ = "Integer32"
_RlQosRedMaxDp1_Object = MibTableColumn
rlQosRedMaxDp1 = _RlQosRedMaxDp1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 10),
    _RlQosRedMaxDp1_Type()
)
rlQosRedMaxDp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMaxDp1.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMaxDp1.setUnits("percent")
_RlQosRedProbDp1_Type = Integer32
_RlQosRedProbDp1_Object = MibTableColumn
rlQosRedProbDp1 = _RlQosRedProbDp1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 11),
    _RlQosRedProbDp1_Type()
)
rlQosRedProbDp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedProbDp1.setStatus("current")


class _RlQosRedMinDp2_Type(Integer32):
    """Custom type rlQosRedMinDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMinDp2_Type.__name__ = "Integer32"
_RlQosRedMinDp2_Object = MibTableColumn
rlQosRedMinDp2 = _RlQosRedMinDp2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 12),
    _RlQosRedMinDp2_Type()
)
rlQosRedMinDp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMinDp2.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMinDp2.setUnits("percent")


class _RlQosRedMaxDp2_Type(Integer32):
    """Custom type rlQosRedMaxDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMaxDp2_Type.__name__ = "Integer32"
_RlQosRedMaxDp2_Object = MibTableColumn
rlQosRedMaxDp2 = _RlQosRedMaxDp2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 13),
    _RlQosRedMaxDp2_Type()
)
rlQosRedMaxDp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMaxDp2.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMaxDp2.setUnits("percent")
_RlQosRedProbDp2_Type = Integer32
_RlQosRedProbDp2_Object = MibTableColumn
rlQosRedProbDp2 = _RlQosRedProbDp2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 14),
    _RlQosRedProbDp2_Type()
)
rlQosRedProbDp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedProbDp2.setStatus("current")
_RlQosRedQweight_Type = Integer32
_RlQosRedQweight_Object = MibTableColumn
rlQosRedQweight = _RlQosRedQweight_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 15),
    _RlQosRedQweight_Type()
)
rlQosRedQweight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedQweight.setStatus("current")
_RlQosIfprofileStatus_Type = RowStatus
_RlQosIfprofileStatus_Object = MibTableColumn
rlQosIfprofileStatus = _RlQosIfprofileStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 14, 1, 16),
    _RlQosIfprofileStatus_Type()
)
rlQosIfprofileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfprofileStatus.setStatus("current")
_RlQosDscpMutationTable_Object = MibTable
rlQosDscpMutationTable = _RlQosDscpMutationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 15)
)
if mibBuilder.loadTexts:
    rlQosDscpMutationTable.setStatus("current")
_RlQosDscpMutationEntry_Object = MibTableRow
rlQosDscpMutationEntry = _RlQosDscpMutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 15, 1)
)
rlQosDscpMutationEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosOldDscp"),
)
if mibBuilder.loadTexts:
    rlQosDscpMutationEntry.setStatus("current")


class _RlQosOldDscp_Type(Integer32):
    """Custom type rlQosOldDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosOldDscp_Type.__name__ = "Integer32"
_RlQosOldDscp_Object = MibTableColumn
rlQosOldDscp = _RlQosOldDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 15, 1, 1),
    _RlQosOldDscp_Type()
)
rlQosOldDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosOldDscp.setStatus("current")


class _RlQosNewDscp_Type(Integer32):
    """Custom type rlQosNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosNewDscp_Type.__name__ = "Integer32"
_RlQosNewDscp_Object = MibTableColumn
rlQosNewDscp = _RlQosNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 15, 1, 2),
    _RlQosNewDscp_Type()
)
rlQosNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosNewDscp.setStatus("current")
_RlQosDscpRemarkTable_Object = MibTable
rlQosDscpRemarkTable = _RlQosDscpRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 16)
)
if mibBuilder.loadTexts:
    rlQosDscpRemarkTable.setStatus("current")
_RlQosDscpRemarkEntry_Object = MibTableRow
rlQosDscpRemarkEntry = _RlQosDscpRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 16, 1)
)
rlQosDscpRemarkEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosRmOldDscp"),
)
if mibBuilder.loadTexts:
    rlQosDscpRemarkEntry.setStatus("current")


class _RlQosRmOldDscp_Type(Integer32):
    """Custom type rlQosRmOldDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosRmOldDscp_Type.__name__ = "Integer32"
_RlQosRmOldDscp_Object = MibTableColumn
rlQosRmOldDscp = _RlQosRmOldDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 16, 1, 1),
    _RlQosRmOldDscp_Type()
)
rlQosRmOldDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosRmOldDscp.setStatus("current")


class _RlQosRmNewDscp_Type(Integer32):
    """Custom type rlQosRmNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosRmNewDscp_Type.__name__ = "Integer32"
_RlQosRmNewDscp_Object = MibTableColumn
rlQosRmNewDscp = _RlQosRmNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 16, 1, 2),
    _RlQosRmNewDscp_Type()
)
rlQosRmNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRmNewDscp.setStatus("current")
_RlQosCosQueueTable_Object = MibTable
rlQosCosQueueTable = _RlQosCosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 17)
)
if mibBuilder.loadTexts:
    rlQosCosQueueTable.setStatus("current")
_RlQosCosQueueEntry_Object = MibTableRow
rlQosCosQueueEntry = _RlQosCosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 17, 1)
)
rlQosCosQueueEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosCosIndex"),
)
if mibBuilder.loadTexts:
    rlQosCosQueueEntry.setStatus("current")


class _RlQosCosIndex_Type(Integer32):
    """Custom type rlQosCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlQosCosIndex_Type.__name__ = "Integer32"
_RlQosCosIndex_Object = MibTableColumn
rlQosCosIndex = _RlQosCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 17, 1, 1),
    _RlQosCosIndex_Type()
)
rlQosCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosCosIndex.setStatus("current")


class _RlQosCosQueueId_Type(Integer32):
    """Custom type rlQosCosQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosCosQueueId_Type.__name__ = "Integer32"
_RlQosCosQueueId_Object = MibTableColumn
rlQosCosQueueId = _RlQosCosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 17, 1, 2),
    _RlQosCosQueueId_Type()
)
rlQosCosQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCosQueueId.setStatus("current")
_RlQosDscpQueueTable_Object = MibTable
rlQosDscpQueueTable = _RlQosDscpQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 18)
)
if mibBuilder.loadTexts:
    rlQosDscpQueueTable.setStatus("current")
_RlQosDscpQueueEntry_Object = MibTableRow
rlQosDscpQueueEntry = _RlQosDscpQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 18, 1)
)
rlQosDscpQueueEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosDscpIndex"),
)
if mibBuilder.loadTexts:
    rlQosDscpQueueEntry.setStatus("current")


class _RlQosDscpIndex_Type(Integer32):
    """Custom type rlQosDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosDscpIndex_Type.__name__ = "Integer32"
_RlQosDscpIndex_Object = MibTableColumn
rlQosDscpIndex = _RlQosDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 18, 1, 1),
    _RlQosDscpIndex_Type()
)
rlQosDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosDscpIndex.setStatus("current")


class _RlQosQueueNum_Type(Integer32):
    """Custom type rlQosQueueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosQueueNum_Type.__name__ = "Integer32"
_RlQosQueueNum_Object = MibTableColumn
rlQosQueueNum = _RlQosQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 18, 1, 2),
    _RlQosQueueNum_Type()
)
rlQosQueueNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosQueueNum.setStatus("current")
_RlQosTcpPortQueueTable_Object = MibTable
rlQosTcpPortQueueTable = _RlQosTcpPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 19)
)
if mibBuilder.loadTexts:
    rlQosTcpPortQueueTable.setStatus("current")
_RlQosTcpPortQueueEntry_Object = MibTableRow
rlQosTcpPortQueueEntry = _RlQosTcpPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 19, 1)
)
rlQosTcpPortQueueEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosTcpPort"),
)
if mibBuilder.loadTexts:
    rlQosTcpPortQueueEntry.setStatus("current")
_RlQosTcpPort_Type = Integer32
_RlQosTcpPort_Object = MibTableColumn
rlQosTcpPort = _RlQosTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 19, 1, 1),
    _RlQosTcpPort_Type()
)
rlQosTcpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosTcpPort.setStatus("current")


class _RlQosTcpQueueValue_Type(Integer32):
    """Custom type rlQosTcpQueueValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosTcpQueueValue_Type.__name__ = "Integer32"
_RlQosTcpQueueValue_Object = MibTableColumn
rlQosTcpQueueValue = _RlQosTcpQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 19, 1, 2),
    _RlQosTcpQueueValue_Type()
)
rlQosTcpQueueValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTcpQueueValue.setStatus("current")
_RlQosTcpPortQueueStatus_Type = RowStatus
_RlQosTcpPortQueueStatus_Object = MibTableColumn
rlQosTcpPortQueueStatus = _RlQosTcpPortQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 19, 1, 3),
    _RlQosTcpPortQueueStatus_Type()
)
rlQosTcpPortQueueStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTcpPortQueueStatus.setStatus("current")
_RlQosUdpPortQueueTable_Object = MibTable
rlQosUdpPortQueueTable = _RlQosUdpPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 20)
)
if mibBuilder.loadTexts:
    rlQosUdpPortQueueTable.setStatus("current")
_RlQosUdpPortQueueEntry_Object = MibTableRow
rlQosUdpPortQueueEntry = _RlQosUdpPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 20, 1)
)
rlQosUdpPortQueueEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosUdpPort"),
)
if mibBuilder.loadTexts:
    rlQosUdpPortQueueEntry.setStatus("current")
_RlQosUdpPort_Type = Integer32
_RlQosUdpPort_Object = MibTableColumn
rlQosUdpPort = _RlQosUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 20, 1, 1),
    _RlQosUdpPort_Type()
)
rlQosUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosUdpPort.setStatus("current")


class _RlQosUdpQueueValue_Type(Integer32):
    """Custom type rlQosUdpQueueValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosUdpQueueValue_Type.__name__ = "Integer32"
_RlQosUdpQueueValue_Object = MibTableColumn
rlQosUdpQueueValue = _RlQosUdpQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 20, 1, 2),
    _RlQosUdpQueueValue_Type()
)
rlQosUdpQueueValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosUdpQueueValue.setStatus("current")
_RlQosUdpPortQueueStatus_Type = RowStatus
_RlQosUdpPortQueueStatus_Object = MibTableColumn
rlQosUdpPortQueueStatus = _RlQosUdpPortQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 20, 1, 3),
    _RlQosUdpPortQueueStatus_Type()
)
rlQosUdpPortQueueStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosUdpPortQueueStatus.setStatus("current")
_RlQosEfManageTable_Object = MibTable
rlQosEfManageTable = _RlQosEfManageTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 21)
)
if mibBuilder.loadTexts:
    rlQosEfManageTable.setStatus("current")
_RlQosEfManageEntry_Object = MibTableRow
rlQosEfManageEntry = _RlQosEfManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 21, 1)
)
rlQosEfManageEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosEfQueueId"),
)
if mibBuilder.loadTexts:
    rlQosEfManageEntry.setStatus("current")


class _RlQosEfQueueId_Type(Integer32):
    """Custom type rlQosEfQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosEfQueueId_Type.__name__ = "Integer32"
_RlQosEfQueueId_Object = MibTableColumn
rlQosEfQueueId = _RlQosEfQueueId_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 21, 1, 1),
    _RlQosEfQueueId_Type()
)
rlQosEfQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosEfQueueId.setStatus("current")
_RlQosEfState_Type = BinaryStatus
_RlQosEfState_Object = MibTableColumn
rlQosEfState = _RlQosEfState_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 21, 1, 2),
    _RlQosEfState_Type()
)
rlQosEfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosEfState.setStatus("current")


class _RlQosEfPriority_Type(Integer32):
    """Custom type rlQosEfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosEfPriority_Type.__name__ = "Integer32"
_RlQosEfPriority_Object = MibTableColumn
rlQosEfPriority = _RlQosEfPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 21, 1, 3),
    _RlQosEfPriority_Type()
)
rlQosEfPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosEfPriority.setStatus("current")
_RlQosQueueProfileTable_Object = MibTable
rlQosQueueProfileTable = _RlQosQueueProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22)
)
if mibBuilder.loadTexts:
    rlQosQueueProfileTable.setStatus("current")
_RlQosQueueProfileEntry_Object = MibTableRow
rlQosQueueProfileEntry = _RlQosQueueProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1)
)
rlQosQueueProfileEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQueueProfileName"),
)
if mibBuilder.loadTexts:
    rlQosQueueProfileEntry.setStatus("current")


class _RlQueueProfileName_Type(DisplayString):
    """Custom type rlQueueProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQueueProfileName_Type.__name__ = "DisplayString"
_RlQueueProfileName_Object = MibTableColumn
rlQueueProfileName = _RlQueueProfileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 1),
    _RlQueueProfileName_Type()
)
rlQueueProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQueueProfileName.setStatus("current")
_RlQosTypeQueue1_Type = QueueType
_RlQosTypeQueue1_Object = MibTableColumn
rlQosTypeQueue1 = _RlQosTypeQueue1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 2),
    _RlQosTypeQueue1_Type()
)
rlQosTypeQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosTypeQueue1.setStatus("current")
_RlQosValueQueue1_Type = Integer32
_RlQosValueQueue1_Object = MibTableColumn
rlQosValueQueue1 = _RlQosValueQueue1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 3),
    _RlQosValueQueue1_Type()
)
rlQosValueQueue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue1.setStatus("current")
_RlQosTypeQueue2_Type = QueueType
_RlQosTypeQueue2_Object = MibTableColumn
rlQosTypeQueue2 = _RlQosTypeQueue2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 4),
    _RlQosTypeQueue2_Type()
)
rlQosTypeQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosTypeQueue2.setStatus("current")
_RlQosValueQueue2_Type = Integer32
_RlQosValueQueue2_Object = MibTableColumn
rlQosValueQueue2 = _RlQosValueQueue2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 5),
    _RlQosValueQueue2_Type()
)
rlQosValueQueue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue2.setStatus("current")
_RlQosTypeQueue3_Type = QueueType
_RlQosTypeQueue3_Object = MibTableColumn
rlQosTypeQueue3 = _RlQosTypeQueue3_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 6),
    _RlQosTypeQueue3_Type()
)
rlQosTypeQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosTypeQueue3.setStatus("current")
_RlQosValueQueue3_Type = Integer32
_RlQosValueQueue3_Object = MibTableColumn
rlQosValueQueue3 = _RlQosValueQueue3_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 7),
    _RlQosValueQueue3_Type()
)
rlQosValueQueue3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue3.setStatus("current")
_RlQosTypeQueue4_Type = QueueType
_RlQosTypeQueue4_Object = MibTableColumn
rlQosTypeQueue4 = _RlQosTypeQueue4_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 8),
    _RlQosTypeQueue4_Type()
)
rlQosTypeQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosTypeQueue4.setStatus("current")
_RlQosValueQueue4_Type = Integer32
_RlQosValueQueue4_Object = MibTableColumn
rlQosValueQueue4 = _RlQosValueQueue4_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 9),
    _RlQosValueQueue4_Type()
)
rlQosValueQueue4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue4.setStatus("current")
_RlQosTypeQueue5_Type = QueueType
_RlQosTypeQueue5_Object = MibTableColumn
rlQosTypeQueue5 = _RlQosTypeQueue5_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 10),
    _RlQosTypeQueue5_Type()
)
rlQosTypeQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosTypeQueue5.setStatus("current")
_RlQosValueQueue5_Type = Integer32
_RlQosValueQueue5_Object = MibTableColumn
rlQosValueQueue5 = _RlQosValueQueue5_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 11),
    _RlQosValueQueue5_Type()
)
rlQosValueQueue5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue5.setStatus("current")
_RlQosTypeQueue6_Type = QueueType
_RlQosTypeQueue6_Object = MibTableColumn
rlQosTypeQueue6 = _RlQosTypeQueue6_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 12),
    _RlQosTypeQueue6_Type()
)
rlQosTypeQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosTypeQueue6.setStatus("current")
_RlQosValueQueue6_Type = Integer32
_RlQosValueQueue6_Object = MibTableColumn
rlQosValueQueue6 = _RlQosValueQueue6_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 13),
    _RlQosValueQueue6_Type()
)
rlQosValueQueue6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue6.setStatus("current")
_RlQosTypeQueue7_Type = QueueType
_RlQosTypeQueue7_Object = MibTableColumn
rlQosTypeQueue7 = _RlQosTypeQueue7_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 14),
    _RlQosTypeQueue7_Type()
)
rlQosTypeQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosTypeQueue7.setStatus("current")
_RlQosValueQueue7_Type = Integer32
_RlQosValueQueue7_Object = MibTableColumn
rlQosValueQueue7 = _RlQosValueQueue7_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 15),
    _RlQosValueQueue7_Type()
)
rlQosValueQueue7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue7.setStatus("current")
_RlQosTypeQueue8_Type = QueueType
_RlQosTypeQueue8_Object = MibTableColumn
rlQosTypeQueue8 = _RlQosTypeQueue8_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 16),
    _RlQosTypeQueue8_Type()
)
rlQosTypeQueue8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosTypeQueue8.setStatus("current")
_RlQosValueQueue8_Type = Integer32
_RlQosValueQueue8_Object = MibTableColumn
rlQosValueQueue8 = _RlQosValueQueue8_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 17),
    _RlQosValueQueue8_Type()
)
rlQosValueQueue8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue8.setStatus("current")
_RlQosQueueProfileStatus_Type = RowStatus
_RlQosQueueProfileStatus_Object = MibTableColumn
rlQosQueueProfileStatus = _RlQosQueueProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 18),
    _RlQosQueueProfileStatus_Type()
)
rlQosQueueProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosQueueProfileStatus.setStatus("current")
_RlQosNumOfIfConnections_Type = Integer32
_RlQosNumOfIfConnections_Object = MibTableColumn
rlQosNumOfIfConnections = _RlQosNumOfIfConnections_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 22, 1, 19),
    _RlQosNumOfIfConnections_Type()
)
rlQosNumOfIfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosNumOfIfConnections.setStatus("current")
_RlQosQueueShapeProfileTable_Object = MibTable
rlQosQueueShapeProfileTable = _RlQosQueueShapeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23)
)
if mibBuilder.loadTexts:
    rlQosQueueShapeProfileTable.setStatus("current")
_RlQosQueueShapeProfileEntry_Object = MibTableRow
rlQosQueueShapeProfileEntry = _RlQosQueueShapeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1)
)
rlQosQueueShapeProfileEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosQueueShapeIndex"),
)
if mibBuilder.loadTexts:
    rlQosQueueShapeProfileEntry.setStatus("current")
_RlQosQueueShapeIndex_Type = Integer32
_RlQosQueueShapeIndex_Object = MibTableColumn
rlQosQueueShapeIndex = _RlQosQueueShapeIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 1),
    _RlQosQueueShapeIndex_Type()
)
rlQosQueueShapeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosQueueShapeIndex.setStatus("current")
_RlQosCirQueue1_Type = Integer32
_RlQosCirQueue1_Object = MibTableColumn
rlQosCirQueue1 = _RlQosCirQueue1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 2),
    _RlQosCirQueue1_Type()
)
rlQosCirQueue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue1.setStatus("current")
_RlQosCbsQueue1_Type = Integer32
_RlQosCbsQueue1_Object = MibTableColumn
rlQosCbsQueue1 = _RlQosCbsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 3),
    _RlQosCbsQueue1_Type()
)
rlQosCbsQueue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue1.setStatus("current")
_RlQosCirQueue2_Type = Integer32
_RlQosCirQueue2_Object = MibTableColumn
rlQosCirQueue2 = _RlQosCirQueue2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 4),
    _RlQosCirQueue2_Type()
)
rlQosCirQueue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue2.setStatus("current")
_RlQosCbsQueue2_Type = Integer32
_RlQosCbsQueue2_Object = MibTableColumn
rlQosCbsQueue2 = _RlQosCbsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 5),
    _RlQosCbsQueue2_Type()
)
rlQosCbsQueue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue2.setStatus("current")
_RlQosCirQueue3_Type = Integer32
_RlQosCirQueue3_Object = MibTableColumn
rlQosCirQueue3 = _RlQosCirQueue3_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 6),
    _RlQosCirQueue3_Type()
)
rlQosCirQueue3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue3.setStatus("current")
_RlQosCbsQueue3_Type = Integer32
_RlQosCbsQueue3_Object = MibTableColumn
rlQosCbsQueue3 = _RlQosCbsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 7),
    _RlQosCbsQueue3_Type()
)
rlQosCbsQueue3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue3.setStatus("current")
_RlQosCirQueue4_Type = Integer32
_RlQosCirQueue4_Object = MibTableColumn
rlQosCirQueue4 = _RlQosCirQueue4_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 8),
    _RlQosCirQueue4_Type()
)
rlQosCirQueue4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue4.setStatus("current")
_RlQosCbsQueue4_Type = Integer32
_RlQosCbsQueue4_Object = MibTableColumn
rlQosCbsQueue4 = _RlQosCbsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 9),
    _RlQosCbsQueue4_Type()
)
rlQosCbsQueue4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue4.setStatus("current")
_RlQosCirQueue5_Type = Integer32
_RlQosCirQueue5_Object = MibTableColumn
rlQosCirQueue5 = _RlQosCirQueue5_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 10),
    _RlQosCirQueue5_Type()
)
rlQosCirQueue5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue5.setStatus("current")
_RlQosCbsQueue5_Type = Integer32
_RlQosCbsQueue5_Object = MibTableColumn
rlQosCbsQueue5 = _RlQosCbsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 11),
    _RlQosCbsQueue5_Type()
)
rlQosCbsQueue5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue5.setStatus("current")
_RlQosCirQueue6_Type = Integer32
_RlQosCirQueue6_Object = MibTableColumn
rlQosCirQueue6 = _RlQosCirQueue6_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 12),
    _RlQosCirQueue6_Type()
)
rlQosCirQueue6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue6.setStatus("current")
_RlQosCbsQueue6_Type = Integer32
_RlQosCbsQueue6_Object = MibTableColumn
rlQosCbsQueue6 = _RlQosCbsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 13),
    _RlQosCbsQueue6_Type()
)
rlQosCbsQueue6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue6.setStatus("current")
_RlQosCirQueue7_Type = Integer32
_RlQosCirQueue7_Object = MibTableColumn
rlQosCirQueue7 = _RlQosCirQueue7_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 14),
    _RlQosCirQueue7_Type()
)
rlQosCirQueue7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue7.setStatus("current")
_RlQosCbsQueue7_Type = Integer32
_RlQosCbsQueue7_Object = MibTableColumn
rlQosCbsQueue7 = _RlQosCbsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 15),
    _RlQosCbsQueue7_Type()
)
rlQosCbsQueue7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue7.setStatus("current")
_RlQosCirQueue8_Type = Integer32
_RlQosCirQueue8_Object = MibTableColumn
rlQosCirQueue8 = _RlQosCirQueue8_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 16),
    _RlQosCirQueue8_Type()
)
rlQosCirQueue8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue8.setStatus("current")
_RlQosCbsQueue8_Type = Integer32
_RlQosCbsQueue8_Object = MibTableColumn
rlQosCbsQueue8 = _RlQosCbsQueue8_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 17),
    _RlQosCbsQueue8_Type()
)
rlQosCbsQueue8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue8.setStatus("current")
_RlQosQueueShapeProfileStatus_Type = RowStatus
_RlQosQueueShapeProfileStatus_Object = MibTableColumn
rlQosQueueShapeProfileStatus = _RlQosQueueShapeProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 23, 1, 18),
    _RlQosQueueShapeProfileStatus_Type()
)
rlQosQueueShapeProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosQueueShapeProfileStatus.setStatus("current")
_RlQosAclCounterTable_Object = MibTable
rlQosAclCounterTable = _RlQosAclCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 24)
)
if mibBuilder.loadTexts:
    rlQosAclCounterTable.setStatus("current")
_RlQosAclCounterEntry_Object = MibTableRow
rlQosAclCounterEntry = _RlQosAclCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 24, 1)
)
rlQosAclCounterEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosAclCounterInterface"),
    (0, "RADLAN-QOS-CLI-MIB", "rlQosAclCounterAclIndex"),
    (0, "RADLAN-QOS-CLI-MIB", "rlQosAclCounterAceIndex"),
)
if mibBuilder.loadTexts:
    rlQosAclCounterEntry.setStatus("current")
_RlQosAclCounterInterface_Type = InterfaceIndex
_RlQosAclCounterInterface_Object = MibTableColumn
rlQosAclCounterInterface = _RlQosAclCounterInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 24, 1, 1),
    _RlQosAclCounterInterface_Type()
)
rlQosAclCounterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAclCounterInterface.setStatus("current")
_RlQosAclCounterAclIndex_Type = Integer32
_RlQosAclCounterAclIndex_Object = MibTableColumn
rlQosAclCounterAclIndex = _RlQosAclCounterAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 24, 1, 2),
    _RlQosAclCounterAclIndex_Type()
)
rlQosAclCounterAclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAclCounterAclIndex.setStatus("current")
_RlQosAclCounterAceIndex_Type = Integer32
_RlQosAclCounterAceIndex_Object = MibTableColumn
rlQosAclCounterAceIndex = _RlQosAclCounterAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 24, 1, 3),
    _RlQosAclCounterAceIndex_Type()
)
rlQosAclCounterAceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAclCounterAceIndex.setStatus("current")
_RlQosAclCounterValue_Type = Counter32
_RlQosAclCounterValue_Object = MibTableColumn
rlQosAclCounterValue = _RlQosAclCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 24, 1, 4),
    _RlQosAclCounterValue_Type()
)
rlQosAclCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAclCounterValue.setStatus("current")
_RlQosFreeIndexesTable_Object = MibTable
rlQosFreeIndexesTable = _RlQosFreeIndexesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 25)
)
if mibBuilder.loadTexts:
    rlQosFreeIndexesTable.setStatus("current")
_RlQosFreeIndexesEntry_Object = MibTableRow
rlQosFreeIndexesEntry = _RlQosFreeIndexesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 25, 1)
)
rlQosFreeIndexesEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosFreeIndexesTableId"),
)
if mibBuilder.loadTexts:
    rlQosFreeIndexesEntry.setStatus("current")


class _RlQosFreeIndexesTableId_Type(Integer32):
    """Custom type rlQosFreeIndexesTableId based on Integer32"""
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
        *(("tuple", 1),
          ("offset", 2),
          ("ace", 3),
          ("acl", 4),
          ("class", 5),
          ("policy", 6),
          ("policer", 7),
          ("shaper", 8))
    )


_RlQosFreeIndexesTableId_Type.__name__ = "Integer32"
_RlQosFreeIndexesTableId_Object = MibTableColumn
rlQosFreeIndexesTableId = _RlQosFreeIndexesTableId_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 25, 1, 1),
    _RlQosFreeIndexesTableId_Type()
)
rlQosFreeIndexesTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosFreeIndexesTableId.setStatus("current")
_RlQosFreeIndexesValue_Type = Integer32
_RlQosFreeIndexesValue_Object = MibTableColumn
rlQosFreeIndexesValue = _RlQosFreeIndexesValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 25, 1, 2),
    _RlQosFreeIndexesValue_Type()
)
rlQosFreeIndexesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosFreeIndexesValue.setStatus("current")
_RlQosNamesToIndexesTable_Object = MibTable
rlQosNamesToIndexesTable = _RlQosNamesToIndexesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 26)
)
if mibBuilder.loadTexts:
    rlQosNamesToIndexesTable.setStatus("current")
_RlQosNamesToIndexesEntry_Object = MibTableRow
rlQosNamesToIndexesEntry = _RlQosNamesToIndexesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 26, 1)
)
rlQosNamesToIndexesEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosNamesToIndexesTableId"),
    (0, "RADLAN-QOS-CLI-MIB", "rlQosNamesToIndexesName"),
)
if mibBuilder.loadTexts:
    rlQosNamesToIndexesEntry.setStatus("current")


class _RlQosNamesToIndexesTableId_Type(Integer32):
    """Custom type rlQosNamesToIndexesTableId based on Integer32"""
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
        *(("acl", 1),
          ("class", 2),
          ("policy", 3),
          ("policer", 4))
    )


_RlQosNamesToIndexesTableId_Type.__name__ = "Integer32"
_RlQosNamesToIndexesTableId_Object = MibTableColumn
rlQosNamesToIndexesTableId = _RlQosNamesToIndexesTableId_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 26, 1, 1),
    _RlQosNamesToIndexesTableId_Type()
)
rlQosNamesToIndexesTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosNamesToIndexesTableId.setStatus("current")


class _RlQosNamesToIndexesName_Type(DisplayString):
    """Custom type rlQosNamesToIndexesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosNamesToIndexesName_Type.__name__ = "DisplayString"
_RlQosNamesToIndexesName_Object = MibTableColumn
rlQosNamesToIndexesName = _RlQosNamesToIndexesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 26, 1, 2),
    _RlQosNamesToIndexesName_Type()
)
rlQosNamesToIndexesName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosNamesToIndexesName.setStatus("current")
_RlQosNamesToIndexesValue_Type = Integer32
_RlQosNamesToIndexesValue_Object = MibTableColumn
rlQosNamesToIndexesValue = _RlQosNamesToIndexesValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 26, 1, 3),
    _RlQosNamesToIndexesValue_Type()
)
rlQosNamesToIndexesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosNamesToIndexesValue.setStatus("current")
_RlQosStackControlQueue_Type = Integer32
_RlQosStackControlQueue_Object = MibScalar
rlQosStackControlQueue = _RlQosStackControlQueue_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 27),
    _RlQosStackControlQueue_Type()
)
rlQosStackControlQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosStackControlQueue.setStatus("current")
_RlQosStackControlCos_Type = Integer32
_RlQosStackControlCos_Object = MibScalar
rlQosStackControlCos = _RlQosStackControlCos_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 28),
    _RlQosStackControlCos_Type()
)
rlQosStackControlCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosStackControlCos.setStatus("current")
_RlQosCosQueueDefaultMapTable_Object = MibTable
rlQosCosQueueDefaultMapTable = _RlQosCosQueueDefaultMapTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 29)
)
if mibBuilder.loadTexts:
    rlQosCosQueueDefaultMapTable.setStatus("current")
_RlQosCosQueueDefaultMapEntry_Object = MibTableRow
rlQosCosQueueDefaultMapEntry = _RlQosCosQueueDefaultMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 29, 1)
)
rlQosCosQueueDefaultMapEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosCosQueueDefaultMapVpt"),
)
if mibBuilder.loadTexts:
    rlQosCosQueueDefaultMapEntry.setStatus("current")


class _RlQosCosQueueDefaultMapVpt_Type(Integer32):
    """Custom type rlQosCosQueueDefaultMapVpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlQosCosQueueDefaultMapVpt_Type.__name__ = "Integer32"
_RlQosCosQueueDefaultMapVpt_Object = MibTableColumn
rlQosCosQueueDefaultMapVpt = _RlQosCosQueueDefaultMapVpt_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 29, 1, 1),
    _RlQosCosQueueDefaultMapVpt_Type()
)
rlQosCosQueueDefaultMapVpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosCosQueueDefaultMapVpt.setStatus("current")


class _RlQosCosQueueDefaultMapQueueId_Type(Integer32):
    """Custom type rlQosCosQueueDefaultMapQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosCosQueueDefaultMapQueueId_Type.__name__ = "Integer32"
_RlQosCosQueueDefaultMapQueueId_Object = MibTableColumn
rlQosCosQueueDefaultMapQueueId = _RlQosCosQueueDefaultMapQueueId_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 29, 1, 2),
    _RlQosCosQueueDefaultMapQueueId_Type()
)
rlQosCosQueueDefaultMapQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosCosQueueDefaultMapQueueId.setStatus("current")
_RlQosPredefBlockAclTable_Object = MibTable
rlQosPredefBlockAclTable = _RlQosPredefBlockAclTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 30)
)
if mibBuilder.loadTexts:
    rlQosPredefBlockAclTable.setStatus("current")
_RlQosPredefBlockAclEntry_Object = MibTableRow
rlQosPredefBlockAclEntry = _RlQosPredefBlockAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 30, 1)
)
rlQosPredefBlockAclEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosPredefBlockAclIfIndex"),
    (0, "RADLAN-QOS-CLI-MIB", "rlQosPredefBlockAclIfType"),
)
if mibBuilder.loadTexts:
    rlQosPredefBlockAclEntry.setStatus("current")
_RlQosPredefBlockAclIfIndex_Type = InterfaceIndex
_RlQosPredefBlockAclIfIndex_Object = MibTableColumn
rlQosPredefBlockAclIfIndex = _RlQosPredefBlockAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 30, 1, 1),
    _RlQosPredefBlockAclIfIndex_Type()
)
rlQosPredefBlockAclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPredefBlockAclIfIndex.setStatus("current")
_RlQosPredefBlockAclIfType_Type = InterfaceType
_RlQosPredefBlockAclIfType_Object = MibTableColumn
rlQosPredefBlockAclIfType = _RlQosPredefBlockAclIfType_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 30, 1, 2),
    _RlQosPredefBlockAclIfType_Type()
)
rlQosPredefBlockAclIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPredefBlockAclIfType.setStatus("current")


class _RlQosPredefBlockAclMask_Type(OctetString):
    """Custom type rlQosPredefBlockAclMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RlQosPredefBlockAclMask_Type.__name__ = "OctetString"
_RlQosPredefBlockAclMask_Object = MibTableColumn
rlQosPredefBlockAclMask = _RlQosPredefBlockAclMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 30, 1, 3),
    _RlQosPredefBlockAclMask_Type()
)
rlQosPredefBlockAclMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPredefBlockAclMask.setStatus("current")
_RlQosPredefBlockAclStatus_Type = RowStatus
_RlQosPredefBlockAclStatus_Object = MibTableColumn
rlQosPredefBlockAclStatus = _RlQosPredefBlockAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 30, 1, 4),
    _RlQosPredefBlockAclStatus_Type()
)
rlQosPredefBlockAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPredefBlockAclStatus.setStatus("current")
_RlQosAceTidxTable_Object = MibTable
rlQosAceTidxTable = _RlQosAceTidxTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31)
)
if mibBuilder.loadTexts:
    rlQosAceTidxTable.setStatus("current")
_RlQosAceTidxEntry_Object = MibTableRow
rlQosAceTidxEntry = _RlQosAceTidxEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1)
)
rlQosAceTidxEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosAceTidxAclIndex"),
    (0, "RADLAN-QOS-CLI-MIB", "rlQosAceTidxIndex"),
)
if mibBuilder.loadTexts:
    rlQosAceTidxEntry.setStatus("current")
_RlQosAceTidxAclIndex_Type = Integer32
_RlQosAceTidxAclIndex_Object = MibTableColumn
rlQosAceTidxAclIndex = _RlQosAceTidxAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 1),
    _RlQosAceTidxAclIndex_Type()
)
rlQosAceTidxAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosAceTidxAclIndex.setStatus("current")
_RlQosAceTidxIndex_Type = Integer32
_RlQosAceTidxIndex_Object = MibTableColumn
rlQosAceTidxIndex = _RlQosAceTidxIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 2),
    _RlQosAceTidxIndex_Type()
)
rlQosAceTidxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosAceTidxIndex.setStatus("current")
_RlQosAceTidxAction_Type = AceActionType
_RlQosAceTidxAction_Object = MibTableColumn
rlQosAceTidxAction = _RlQosAceTidxAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 3),
    _RlQosAceTidxAction_Type()
)
rlQosAceTidxAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxAction.setStatus("current")
_RlQosAceTidxType_Type = AceObjectType
_RlQosAceTidxType_Object = MibTableColumn
rlQosAceTidxType = _RlQosAceTidxType_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 4),
    _RlQosAceTidxType_Type()
)
rlQosAceTidxType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxType.setStatus("current")
_RlQosAceTidxTuple1_Type = Integer32
_RlQosAceTidxTuple1_Object = MibTableColumn
rlQosAceTidxTuple1 = _RlQosAceTidxTuple1_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 5),
    _RlQosAceTidxTuple1_Type()
)
rlQosAceTidxTuple1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple1.setStatus("current")
_RlQosAceTidxTuple2_Type = Integer32
_RlQosAceTidxTuple2_Object = MibTableColumn
rlQosAceTidxTuple2 = _RlQosAceTidxTuple2_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 6),
    _RlQosAceTidxTuple2_Type()
)
rlQosAceTidxTuple2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple2.setStatus("current")
_RlQosAceTidxTuple3_Type = Integer32
_RlQosAceTidxTuple3_Object = MibTableColumn
rlQosAceTidxTuple3 = _RlQosAceTidxTuple3_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 7),
    _RlQosAceTidxTuple3_Type()
)
rlQosAceTidxTuple3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple3.setStatus("current")
_RlQosAceTidxTuple4_Type = Integer32
_RlQosAceTidxTuple4_Object = MibTableColumn
rlQosAceTidxTuple4 = _RlQosAceTidxTuple4_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 8),
    _RlQosAceTidxTuple4_Type()
)
rlQosAceTidxTuple4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple4.setStatus("current")
_RlQosAceTidxTuple5_Type = Integer32
_RlQosAceTidxTuple5_Object = MibTableColumn
rlQosAceTidxTuple5 = _RlQosAceTidxTuple5_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 9),
    _RlQosAceTidxTuple5_Type()
)
rlQosAceTidxTuple5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple5.setStatus("current")
_RlQosAceTidxTuple6_Type = Integer32
_RlQosAceTidxTuple6_Object = MibTableColumn
rlQosAceTidxTuple6 = _RlQosAceTidxTuple6_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 10),
    _RlQosAceTidxTuple6_Type()
)
rlQosAceTidxTuple6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple6.setStatus("current")
_RlQosAceTidxTuple7_Type = Integer32
_RlQosAceTidxTuple7_Object = MibTableColumn
rlQosAceTidxTuple7 = _RlQosAceTidxTuple7_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 11),
    _RlQosAceTidxTuple7_Type()
)
rlQosAceTidxTuple7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple7.setStatus("current")
_RlQosAceTidxTuple8_Type = Integer32
_RlQosAceTidxTuple8_Object = MibTableColumn
rlQosAceTidxTuple8 = _RlQosAceTidxTuple8_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 12),
    _RlQosAceTidxTuple8_Type()
)
rlQosAceTidxTuple8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple8.setStatus("current")
_RlQosAceTidxAccount_Type = BinaryStatus
_RlQosAceTidxAccount_Object = MibTableColumn
rlQosAceTidxAccount = _RlQosAceTidxAccount_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 13),
    _RlQosAceTidxAccount_Type()
)
rlQosAceTidxAccount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxAccount.setStatus("current")
_RlQosAceTidxStatus_Type = RowStatus
_RlQosAceTidxStatus_Object = MibTableColumn
rlQosAceTidxStatus = _RlQosAceTidxStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 31, 1, 14),
    _RlQosAceTidxStatus_Type()
)
rlQosAceTidxStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxStatus.setStatus("current")
_RlQosMibVersion_Type = Integer32
_RlQosMibVersion_Object = MibScalar
rlQosMibVersion = _RlQosMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 32),
    _RlQosMibVersion_Type()
)
rlQosMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosMibVersion.setStatus("current")
_RlQosDscpQueueDefaultMapTable_Object = MibTable
rlQosDscpQueueDefaultMapTable = _RlQosDscpQueueDefaultMapTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 33)
)
if mibBuilder.loadTexts:
    rlQosDscpQueueDefaultMapTable.setStatus("current")
_RlQosDscpQueueDefaultMapEntry_Object = MibTableRow
rlQosDscpQueueDefaultMapEntry = _RlQosDscpQueueDefaultMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 33, 1)
)
rlQosDscpQueueDefaultMapEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosDscpQueueDefaultMapDscp"),
)
if mibBuilder.loadTexts:
    rlQosDscpQueueDefaultMapEntry.setStatus("current")


class _RlQosDscpQueueDefaultMapDscp_Type(Integer32):
    """Custom type rlQosDscpQueueDefaultMapDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosDscpQueueDefaultMapDscp_Type.__name__ = "Integer32"
_RlQosDscpQueueDefaultMapDscp_Object = MibTableColumn
rlQosDscpQueueDefaultMapDscp = _RlQosDscpQueueDefaultMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 33, 1, 1),
    _RlQosDscpQueueDefaultMapDscp_Type()
)
rlQosDscpQueueDefaultMapDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosDscpQueueDefaultMapDscp.setStatus("current")


class _RlQosDscpQueueDefaultMapQueueId_Type(Integer32):
    """Custom type rlQosDscpQueueDefaultMapQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosDscpQueueDefaultMapQueueId_Type.__name__ = "Integer32"
_RlQosDscpQueueDefaultMapQueueId_Object = MibTableColumn
rlQosDscpQueueDefaultMapQueueId = _RlQosDscpQueueDefaultMapQueueId_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 33, 1, 2),
    _RlQosDscpQueueDefaultMapQueueId_Type()
)
rlQosDscpQueueDefaultMapQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosDscpQueueDefaultMapQueueId.setStatus("current")
_RlQosDscpToDpTable_Object = MibTable
rlQosDscpToDpTable = _RlQosDscpToDpTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 34)
)
if mibBuilder.loadTexts:
    rlQosDscpToDpTable.setStatus("current")
_RlQosDscpToDpEntry_Object = MibTableRow
rlQosDscpToDpEntry = _RlQosDscpToDpEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 34, 1)
)
rlQosDscpToDpEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosDscp"),
)
if mibBuilder.loadTexts:
    rlQosDscpToDpEntry.setStatus("current")


class _RlQosDscp_Type(Integer32):
    """Custom type rlQosDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosDscp_Type.__name__ = "Integer32"
_RlQosDscp_Object = MibTableColumn
rlQosDscp = _RlQosDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 34, 1, 1),
    _RlQosDscp_Type()
)
rlQosDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosDscp.setStatus("current")


class _RlQosDp_Type(Integer32):
    """Custom type rlQosDp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RlQosDp_Type.__name__ = "Integer32"
_RlQosDp_Object = MibTableColumn
rlQosDp = _RlQosDp_Object(
    (1, 3, 6, 1, 4, 1, 89, 88, 34, 1, 2),
    _RlQosDp_Type()
)
rlQosDp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosDp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-QOS-CLI-MIB",
    **{"ClassOffsetType": ClassOffsetType,
       "ClassTupleType": ClassTupleType,
       "AceActionType": AceActionType,
       "AceObjectType": AceObjectType,
       "AclObjectType": AclObjectType,
       "ClassMapType": ClassMapType,
       "ClassMapAction": ClassMapAction,
       "PolicerType": PolicerType,
       "PolicerAction": PolicerAction,
       "QosObjectMode": QosObjectMode,
       "QosObjectBasicMode": QosObjectBasicMode,
       "BinaryStatus": BinaryStatus,
       "QueueType": QueueType,
       "AclDefaultAction": AclDefaultAction,
       "InterfaceType": InterfaceType,
       "rlQosCliMib": rlQosCliMib,
       "rlQosCliQosMode": rlQosCliQosMode,
       "rlQosCliBasicModeCfg": rlQosCliBasicModeCfg,
       "rlQosMaxNumOfAce": rlQosMaxNumOfAce,
       "rlQosOffsetTable": rlQosOffsetTable,
       "rlQosOffsetEntry": rlQosOffsetEntry,
       "rlQosOffsetIndex": rlQosOffsetIndex,
       "rlQosOffsetType": rlQosOffsetType,
       "rlQosOffsetValue": rlQosOffsetValue,
       "rlQosOffsetMask": rlQosOffsetMask,
       "rlQosOffsetPattern": rlQosOffsetPattern,
       "rlQosOffsetTuplePointer": rlQosOffsetTuplePointer,
       "rlQosOffsetStatus": rlQosOffsetStatus,
       "rlQosTupleTable": rlQosTupleTable,
       "rlQosTupleEntry": rlQosTupleEntry,
       "rlQosTupleIndex": rlQosTupleIndex,
       "rlQosTupleType": rlQosTupleType,
       "rlQosTupleValue1": rlQosTupleValue1,
       "rlQosTupleValue2": rlQosTupleValue2,
       "rlQosTupleStatus": rlQosTupleStatus,
       "rlQosAceTable": rlQosAceTable,
       "rlQosAceEntry": rlQosAceEntry,
       "rlQosAceIndex": rlQosAceIndex,
       "rlQosAceAction": rlQosAceAction,
       "rlQosAceType": rlQosAceType,
       "rlQosAceTuple1": rlQosAceTuple1,
       "rlQosAceTuple2": rlQosAceTuple2,
       "rlQosAceTuple3": rlQosAceTuple3,
       "rlQosAceTuple4": rlQosAceTuple4,
       "rlQosAceTuple5": rlQosAceTuple5,
       "rlQosAceTuple6": rlQosAceTuple6,
       "rlQosAceTuple7": rlQosAceTuple7,
       "rlQosAceTuple8": rlQosAceTuple8,
       "rlQosAceAccount": rlQosAceAccount,
       "rlQosAceStatus": rlQosAceStatus,
       "rlQosAclTable": rlQosAclTable,
       "rlQosAclEntry": rlQosAclEntry,
       "rlQosAclIndex": rlQosAclIndex,
       "rlQosAclName": rlQosAclName,
       "rlQosAclType": rlQosAclType,
       "rlQosAclStatus": rlQosAclStatus,
       "rlQosAclAceRefTable": rlQosAclAceRefTable,
       "rlQosAclAceRefEntry": rlQosAclAceRefEntry,
       "rlQosAclAceRefAcePointer": rlQosAclAceRefAcePointer,
       "rlQosAclAceRefAclPointer": rlQosAclAceRefAclPointer,
       "rlQosAclAceRefStatus": rlQosAclAceRefStatus,
       "rlQosClassMapTable": rlQosClassMapTable,
       "rlQosClassMapEntry": rlQosClassMapEntry,
       "rlQosClassMapIndex": rlQosClassMapIndex,
       "rlQosClassMapName": rlQosClassMapName,
       "rlQosClassMapType": rlQosClassMapType,
       "rlQosClassMapAction": rlQosClassMapAction,
       "rlQosClassMapMarkValue": rlQosClassMapMarkValue,
       "rlQosClassMapPolicer": rlQosClassMapPolicer,
       "rlQosClassMapMatch1": rlQosClassMapMatch1,
       "rlQosClassMapMatch2": rlQosClassMapMatch2,
       "rlQosClassMapMarkVlan": rlQosClassMapMarkVlan,
       "rlQosClassMapNewVlan": rlQosClassMapNewVlan,
       "rlQosClassMapNewPort": rlQosClassMapNewPort,
       "rlQosClassMapCopyPort": rlQosClassMapCopyPort,
       "rlQosClassMapStatus": rlQosClassMapStatus,
       "rlQosPolicerTable": rlQosPolicerTable,
       "rlQosPolicerEntry": rlQosPolicerEntry,
       "rlQosPolicerIndex": rlQosPolicerIndex,
       "rlQosPolicerName": rlQosPolicerName,
       "rlQosPolicerType": rlQosPolicerType,
       "rlQosPolicerCir": rlQosPolicerCir,
       "rlQosPolicerCbs": rlQosPolicerCbs,
       "rlQosPolicerAction": rlQosPolicerAction,
       "rlQosPolicerCasPointerRemVal": rlQosPolicerCasPointerRemVal,
       "rlQosPolicerStatus": rlQosPolicerStatus,
       "rlQosPolicyMapTable": rlQosPolicyMapTable,
       "rlQosPolicyMapEntry": rlQosPolicyMapEntry,
       "rlQosPolicyMapIndex": rlQosPolicyMapIndex,
       "rlQosPolicyMapName": rlQosPolicyMapName,
       "rlQosPolicyMapStatus": rlQosPolicyMapStatus,
       "rlQosPolicyClassRefTable": rlQosPolicyClassRefTable,
       "rlQosPolicyClassRefEntry": rlQosPolicyClassRefEntry,
       "rlQosPolicyClassRefClassPointer": rlQosPolicyClassRefClassPointer,
       "rlQosPolicyClassRefPolicyPointer": rlQosPolicyClassRefPolicyPointer,
       "rlQosPolicyClassRefStatus": rlQosPolicyClassRefStatus,
       "rlQosIfPolicyTable": rlQosIfPolicyTable,
       "rlQosIfPolicyEntry": rlQosIfPolicyEntry,
       "rlIfIndex": rlIfIndex,
       "rlIfType": rlIfType,
       "rlQosIfPolicyMapPointerIn": rlQosIfPolicyMapPointerIn,
       "rlQosIfPolicyMapPointerOut": rlQosIfPolicyMapPointerOut,
       "rlQosIfTrustActive": rlQosIfTrustActive,
       "rlQosPortShaperStatus": rlQosPortShaperStatus,
       "rlQosCirPortShaper": rlQosCirPortShaper,
       "rlQosCbsPortShaper": rlQosCbsPortShaper,
       "rlQosIfProfilePointer": rlQosIfProfilePointer,
       "rlQosQueueProfilePointer": rlQosQueueProfilePointer,
       "rlQosQueueShapeProfilePointer": rlQosQueueShapeProfilePointer,
       "rlQosAclDefaultAction": rlQosAclDefaultAction,
       "rlQosIfPolicyMapStatus": rlQosIfPolicyMapStatus,
       "rlQosIfAclIn": rlQosIfAclIn,
       "rlQosIfAclOut": rlQosIfAclOut,
       "rlQosIfPolicerIn": rlQosIfPolicerIn,
       "rlQosPortRateLimitStatus": rlQosPortRateLimitStatus,
       "rlQosCirPortRateLimit": rlQosCirPortRateLimit,
       "rlQosCbsPortRateLimit": rlQosCbsPortRateLimit,
       "rlQosIfProfileCfgTable": rlQosIfProfileCfgTable,
       "rlQosIfProfileCfgEntry": rlQosIfProfileCfgEntry,
       "rlIfProfileName": rlIfProfileName,
       "rlQosQueueId": rlQosQueueId,
       "rlQosTdThersholdDp0": rlQosTdThersholdDp0,
       "rlQosTdThersholdDp1": rlQosTdThersholdDp1,
       "rlQosTdThersholdDp2": rlQosTdThersholdDp2,
       "rlQosRedMinDp0": rlQosRedMinDp0,
       "rlQosRedMaxDp0": rlQosRedMaxDp0,
       "rlQosRedProbDp0": rlQosRedProbDp0,
       "rlQosRedMinDp1": rlQosRedMinDp1,
       "rlQosRedMaxDp1": rlQosRedMaxDp1,
       "rlQosRedProbDp1": rlQosRedProbDp1,
       "rlQosRedMinDp2": rlQosRedMinDp2,
       "rlQosRedMaxDp2": rlQosRedMaxDp2,
       "rlQosRedProbDp2": rlQosRedProbDp2,
       "rlQosRedQweight": rlQosRedQweight,
       "rlQosIfprofileStatus": rlQosIfprofileStatus,
       "rlQosDscpMutationTable": rlQosDscpMutationTable,
       "rlQosDscpMutationEntry": rlQosDscpMutationEntry,
       "rlQosOldDscp": rlQosOldDscp,
       "rlQosNewDscp": rlQosNewDscp,
       "rlQosDscpRemarkTable": rlQosDscpRemarkTable,
       "rlQosDscpRemarkEntry": rlQosDscpRemarkEntry,
       "rlQosRmOldDscp": rlQosRmOldDscp,
       "rlQosRmNewDscp": rlQosRmNewDscp,
       "rlQosCosQueueTable": rlQosCosQueueTable,
       "rlQosCosQueueEntry": rlQosCosQueueEntry,
       "rlQosCosIndex": rlQosCosIndex,
       "rlQosCosQueueId": rlQosCosQueueId,
       "rlQosDscpQueueTable": rlQosDscpQueueTable,
       "rlQosDscpQueueEntry": rlQosDscpQueueEntry,
       "rlQosDscpIndex": rlQosDscpIndex,
       "rlQosQueueNum": rlQosQueueNum,
       "rlQosTcpPortQueueTable": rlQosTcpPortQueueTable,
       "rlQosTcpPortQueueEntry": rlQosTcpPortQueueEntry,
       "rlQosTcpPort": rlQosTcpPort,
       "rlQosTcpQueueValue": rlQosTcpQueueValue,
       "rlQosTcpPortQueueStatus": rlQosTcpPortQueueStatus,
       "rlQosUdpPortQueueTable": rlQosUdpPortQueueTable,
       "rlQosUdpPortQueueEntry": rlQosUdpPortQueueEntry,
       "rlQosUdpPort": rlQosUdpPort,
       "rlQosUdpQueueValue": rlQosUdpQueueValue,
       "rlQosUdpPortQueueStatus": rlQosUdpPortQueueStatus,
       "rlQosEfManageTable": rlQosEfManageTable,
       "rlQosEfManageEntry": rlQosEfManageEntry,
       "rlQosEfQueueId": rlQosEfQueueId,
       "rlQosEfState": rlQosEfState,
       "rlQosEfPriority": rlQosEfPriority,
       "rlQosQueueProfileTable": rlQosQueueProfileTable,
       "rlQosQueueProfileEntry": rlQosQueueProfileEntry,
       "rlQueueProfileName": rlQueueProfileName,
       "rlQosTypeQueue1": rlQosTypeQueue1,
       "rlQosValueQueue1": rlQosValueQueue1,
       "rlQosTypeQueue2": rlQosTypeQueue2,
       "rlQosValueQueue2": rlQosValueQueue2,
       "rlQosTypeQueue3": rlQosTypeQueue3,
       "rlQosValueQueue3": rlQosValueQueue3,
       "rlQosTypeQueue4": rlQosTypeQueue4,
       "rlQosValueQueue4": rlQosValueQueue4,
       "rlQosTypeQueue5": rlQosTypeQueue5,
       "rlQosValueQueue5": rlQosValueQueue5,
       "rlQosTypeQueue6": rlQosTypeQueue6,
       "rlQosValueQueue6": rlQosValueQueue6,
       "rlQosTypeQueue7": rlQosTypeQueue7,
       "rlQosValueQueue7": rlQosValueQueue7,
       "rlQosTypeQueue8": rlQosTypeQueue8,
       "rlQosValueQueue8": rlQosValueQueue8,
       "rlQosQueueProfileStatus": rlQosQueueProfileStatus,
       "rlQosNumOfIfConnections": rlQosNumOfIfConnections,
       "rlQosQueueShapeProfileTable": rlQosQueueShapeProfileTable,
       "rlQosQueueShapeProfileEntry": rlQosQueueShapeProfileEntry,
       "rlQosQueueShapeIndex": rlQosQueueShapeIndex,
       "rlQosCirQueue1": rlQosCirQueue1,
       "rlQosCbsQueue1": rlQosCbsQueue1,
       "rlQosCirQueue2": rlQosCirQueue2,
       "rlQosCbsQueue2": rlQosCbsQueue2,
       "rlQosCirQueue3": rlQosCirQueue3,
       "rlQosCbsQueue3": rlQosCbsQueue3,
       "rlQosCirQueue4": rlQosCirQueue4,
       "rlQosCbsQueue4": rlQosCbsQueue4,
       "rlQosCirQueue5": rlQosCirQueue5,
       "rlQosCbsQueue5": rlQosCbsQueue5,
       "rlQosCirQueue6": rlQosCirQueue6,
       "rlQosCbsQueue6": rlQosCbsQueue6,
       "rlQosCirQueue7": rlQosCirQueue7,
       "rlQosCbsQueue7": rlQosCbsQueue7,
       "rlQosCirQueue8": rlQosCirQueue8,
       "rlQosCbsQueue8": rlQosCbsQueue8,
       "rlQosQueueShapeProfileStatus": rlQosQueueShapeProfileStatus,
       "rlQosAclCounterTable": rlQosAclCounterTable,
       "rlQosAclCounterEntry": rlQosAclCounterEntry,
       "rlQosAclCounterInterface": rlQosAclCounterInterface,
       "rlQosAclCounterAclIndex": rlQosAclCounterAclIndex,
       "rlQosAclCounterAceIndex": rlQosAclCounterAceIndex,
       "rlQosAclCounterValue": rlQosAclCounterValue,
       "rlQosFreeIndexesTable": rlQosFreeIndexesTable,
       "rlQosFreeIndexesEntry": rlQosFreeIndexesEntry,
       "rlQosFreeIndexesTableId": rlQosFreeIndexesTableId,
       "rlQosFreeIndexesValue": rlQosFreeIndexesValue,
       "rlQosNamesToIndexesTable": rlQosNamesToIndexesTable,
       "rlQosNamesToIndexesEntry": rlQosNamesToIndexesEntry,
       "rlQosNamesToIndexesTableId": rlQosNamesToIndexesTableId,
       "rlQosNamesToIndexesName": rlQosNamesToIndexesName,
       "rlQosNamesToIndexesValue": rlQosNamesToIndexesValue,
       "rlQosStackControlQueue": rlQosStackControlQueue,
       "rlQosStackControlCos": rlQosStackControlCos,
       "rlQosCosQueueDefaultMapTable": rlQosCosQueueDefaultMapTable,
       "rlQosCosQueueDefaultMapEntry": rlQosCosQueueDefaultMapEntry,
       "rlQosCosQueueDefaultMapVpt": rlQosCosQueueDefaultMapVpt,
       "rlQosCosQueueDefaultMapQueueId": rlQosCosQueueDefaultMapQueueId,
       "rlQosPredefBlockAclTable": rlQosPredefBlockAclTable,
       "rlQosPredefBlockAclEntry": rlQosPredefBlockAclEntry,
       "rlQosPredefBlockAclIfIndex": rlQosPredefBlockAclIfIndex,
       "rlQosPredefBlockAclIfType": rlQosPredefBlockAclIfType,
       "rlQosPredefBlockAclMask": rlQosPredefBlockAclMask,
       "rlQosPredefBlockAclStatus": rlQosPredefBlockAclStatus,
       "rlQosAceTidxTable": rlQosAceTidxTable,
       "rlQosAceTidxEntry": rlQosAceTidxEntry,
       "rlQosAceTidxAclIndex": rlQosAceTidxAclIndex,
       "rlQosAceTidxIndex": rlQosAceTidxIndex,
       "rlQosAceTidxAction": rlQosAceTidxAction,
       "rlQosAceTidxType": rlQosAceTidxType,
       "rlQosAceTidxTuple1": rlQosAceTidxTuple1,
       "rlQosAceTidxTuple2": rlQosAceTidxTuple2,
       "rlQosAceTidxTuple3": rlQosAceTidxTuple3,
       "rlQosAceTidxTuple4": rlQosAceTidxTuple4,
       "rlQosAceTidxTuple5": rlQosAceTidxTuple5,
       "rlQosAceTidxTuple6": rlQosAceTidxTuple6,
       "rlQosAceTidxTuple7": rlQosAceTidxTuple7,
       "rlQosAceTidxTuple8": rlQosAceTidxTuple8,
       "rlQosAceTidxAccount": rlQosAceTidxAccount,
       "rlQosAceTidxStatus": rlQosAceTidxStatus,
       "rlQosMibVersion": rlQosMibVersion,
       "rlQosDscpQueueDefaultMapTable": rlQosDscpQueueDefaultMapTable,
       "rlQosDscpQueueDefaultMapEntry": rlQosDscpQueueDefaultMapEntry,
       "rlQosDscpQueueDefaultMapDscp": rlQosDscpQueueDefaultMapDscp,
       "rlQosDscpQueueDefaultMapQueueId": rlQosDscpQueueDefaultMapQueueId,
       "rlQosDscpToDpTable": rlQosDscpToDpTable,
       "rlQosDscpToDpEntry": rlQosDscpToDpEntry,
       "rlQosDscp": rlQosDscp,
       "rlQosDp": rlQosDp}
)
