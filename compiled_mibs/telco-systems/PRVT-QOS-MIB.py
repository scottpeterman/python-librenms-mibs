# SNMP MIB module (PRVT-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-QOS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:50 2025
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

(prvt_products,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "prvt-products")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

prvtQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1)
)
if mibBuilder.loadTexts:
    prvtQosMIB.setRevisions(
        ("2010-03-23 00:00",
         "2009-04-24 00:00",
         "2008-10-01 00:00",
         "2007-11-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TNamedItem(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )



class TNamedItemOrEmpty(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 6),
    )



class TQEncapVal(TextualConvention, Unsigned32):
    status = "current"


class TLspExpValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class Dot1PPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class TFCName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )



class TFCNameOrEmpty(TextualConvention, Integer32):
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
        *(("be", 1),
          ("l2", 2),
          ("af", 3),
          ("l1", 4),
          ("h2", 5),
          ("ef", 6),
          ("h1", 7),
          ("nc", 8))
    )



class TDSCPValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class TItemDescription(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



class TQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TIngressQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TEgressQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TSapIngressPolicyId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class TSapIngressPolicyIdOrNone(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



class TSapEgressPolicyId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class TSapEgressPolicyIdOrNone(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



class TNetworkPolicyId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )



class TNetworkPolicyIdOrNone(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )



class TItemMatch(TextualConvention, Integer32):
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
        *(("off", 1),
          ("false", 2),
          ("true", 3))
    )



class TPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )



class TPriorityOrDefault(TextualConvention, Integer32):
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
        *(("low", 1),
          ("high", 2),
          ("default", 3))
    )



class TProfile(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )



class TCIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )



class TPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000000),
    )



class TRateValue(TextualConvention, Integer32):
    status = "current"


class TLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TTreshold(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 100),
    )



class TConformanceLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )



class TShaperId(TextualConvention, Integer32):
    status = "current"


class TTailDropId(TextualConvention, Integer32):
    status = "current"


class TSredId(TextualConvention, Integer32):
    status = "current"


class TSSchedulingProfile(TextualConvention, Integer32):
    status = "current"


class TSlopePolicy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



# MIB Managed Objects in the order of their OIDs

_ServiceAccessSwitch_ObjectIdentity = ObjectIdentity
serviceAccessSwitch = _ServiceAccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7)
)
_TFCObjects_ObjectIdentity = ObjectIdentity
tFCObjects = _TFCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 1)
)
_TFCNameTable_Object = MibTable
tFCNameTable = _TFCNameTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tFCNameTable.setStatus("current")
_TFCNameEntry_Object = MibTableRow
tFCNameEntry = _TFCNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 1, 1, 1)
)
tFCNameEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "tFCValue"),
)
if mibBuilder.loadTexts:
    tFCNameEntry.setStatus("current")


class _TFCValue_Type(Integer32):
    """Custom type tFCValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TFCValue_Type.__name__ = "Integer32"
_TFCValue_Object = MibTableColumn
tFCValue = _TFCValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 1, 1, 1, 1),
    _TFCValue_Type()
)
tFCValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFCValue.setStatus("current")
_TFCRowStatus_Type = RowStatus
_TFCRowStatus_Object = MibTableColumn
tFCRowStatus = _TFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 1, 1, 1, 2),
    _TFCRowStatus_Type()
)
tFCRowStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFCRowStatus.setStatus("current")


class _TFCStorageType_Type(StorageType):
    """Custom type tFCStorageType based on StorageType"""
    defaultValue = 3


_TFCStorageType_Type.__name__ = "StorageType"
_TFCStorageType_Object = MibTableColumn
tFCStorageType = _TFCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 1, 1, 1, 3),
    _TFCStorageType_Type()
)
tFCStorageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFCStorageType.setStatus("current")
_TFCName_Type = TFCName
_TFCName_Object = MibTableColumn
tFCName = _TFCName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 1, 1, 1, 4),
    _TFCName_Type()
)
tFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFCName.setStatus("current")
_TFCNameLastChanged_Type = TimeStamp
_TFCNameLastChanged_Object = MibTableColumn
tFCNameLastChanged = _TFCNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 1, 1, 1, 5),
    _TFCNameLastChanged_Type()
)
tFCNameLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFCNameLastChanged.setStatus("current")
_HqosSapIngressObjects_ObjectIdentity = ObjectIdentity
hqosSapIngressObjects = _HqosSapIngressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2)
)
_HqosSapIngressTable_Object = MibTable
hqosSapIngressTable = _HqosSapIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hqosSapIngressTable.setStatus("current")
_HqosSapIngressEntry_Object = MibTableRow
hqosSapIngressEntry = _HqosSapIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 1, 1)
)
hqosSapIngressEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosSapIngressIndex"),
)
if mibBuilder.loadTexts:
    hqosSapIngressEntry.setStatus("current")
_HqosSapIngressIndex_Type = TSapIngressPolicyId
_HqosSapIngressIndex_Object = MibTableColumn
hqosSapIngressIndex = _HqosSapIngressIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 1, 1, 1),
    _HqosSapIngressIndex_Type()
)
hqosSapIngressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressIndex.setStatus("current")
_HqosSapIngressRowStatus_Type = RowStatus
_HqosSapIngressRowStatus_Object = MibTableColumn
hqosSapIngressRowStatus = _HqosSapIngressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 1, 1, 2),
    _HqosSapIngressRowStatus_Type()
)
hqosSapIngressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosSapIngressRowStatus.setStatus("current")


class _HqosSapIngressDescription_Type(TItemDescription):
    """Custom type hqosSapIngressDescription based on TItemDescription"""
    defaultHexValue = ""


_HqosSapIngressDescription_Type.__name__ = "TItemDescription"
_HqosSapIngressDescription_Object = MibTableColumn
hqosSapIngressDescription = _HqosSapIngressDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 1, 1, 3),
    _HqosSapIngressDescription_Type()
)
hqosSapIngressDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressDescription.setStatus("current")


class _HqosSapIngressDefaultDscpFC_Type(Integer32):
    """Custom type hqosSapIngressDefaultDscpFC based on Integer32"""
    defaultValue = 4


_HqosSapIngressDefaultDscpFC_Type.__name__ = "Integer32"
_HqosSapIngressDefaultDscpFC_Object = MibTableColumn
hqosSapIngressDefaultDscpFC = _HqosSapIngressDefaultDscpFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 1, 1, 4),
    _HqosSapIngressDefaultDscpFC_Type()
)
hqosSapIngressDefaultDscpFC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressDefaultDscpFC.setStatus("current")


class _HqosSapIngressDefaultVptFC_Type(Integer32):
    """Custom type hqosSapIngressDefaultVptFC based on Integer32"""
    defaultValue = 0


_HqosSapIngressDefaultVptFC_Type.__name__ = "Integer32"
_HqosSapIngressDefaultVptFC_Object = MibTableColumn
hqosSapIngressDefaultVptFC = _HqosSapIngressDefaultVptFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 1, 1, 5),
    _HqosSapIngressDefaultVptFC_Type()
)
hqosSapIngressDefaultVptFC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressDefaultVptFC.setStatus("current")
_HqosSapIngressLastChanged_Type = TimeStamp
_HqosSapIngressLastChanged_Object = MibTableColumn
hqosSapIngressLastChanged = _HqosSapIngressLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 1, 1, 6),
    _HqosSapIngressLastChanged_Type()
)
hqosSapIngressLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressLastChanged.setStatus("current")
_HqosSapIngressQueueTable_Object = MibTable
hqosSapIngressQueueTable = _HqosSapIngressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hqosSapIngressQueueTable.setStatus("current")
_HqosSapIngressQueueEntry_Object = MibTableRow
hqosSapIngressQueueEntry = _HqosSapIngressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2, 1)
)
hqosSapIngressQueueEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosSapIngressIndex"),
    (0, "PRVT-QOS-MIB", "hqosSapIngressQueue"),
    (0, "PRVT-QOS-MIB", "hqosSapIngressQueueParent"),
)
if mibBuilder.loadTexts:
    hqosSapIngressQueueEntry.setStatus("current")


class _HqosSapIngressQueue_Type(TIngressQueueId):
    """Custom type hqosSapIngressQueue based on TIngressQueueId"""
    subtypeSpec = TIngressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HqosSapIngressQueue_Type.__name__ = "TIngressQueueId"
_HqosSapIngressQueue_Object = MibTableColumn
hqosSapIngressQueue = _HqosSapIngressQueue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2, 1, 1),
    _HqosSapIngressQueue_Type()
)
hqosSapIngressQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressQueue.setStatus("current")
_HqosSapIngressQueueParent_Type = TNamedItemOrEmpty
_HqosSapIngressQueueParent_Object = MibTableColumn
hqosSapIngressQueueParent = _HqosSapIngressQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2, 1, 2),
    _HqosSapIngressQueueParent_Type()
)
hqosSapIngressQueueParent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressQueueParent.setStatus("current")
_HqosSapIngressQueueRowStatus_Type = RowStatus
_HqosSapIngressQueueRowStatus_Object = MibTableColumn
hqosSapIngressQueueRowStatus = _HqosSapIngressQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2, 1, 3),
    _HqosSapIngressQueueRowStatus_Type()
)
hqosSapIngressQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosSapIngressQueueRowStatus.setStatus("current")


class _HqosSapIngressQueueLevel_Type(TLevel):
    """Custom type hqosSapIngressQueueLevel based on TLevel"""
    defaultValue = 1


_HqosSapIngressQueueLevel_Type.__name__ = "TLevel"
_HqosSapIngressQueueLevel_Object = MibTableColumn
hqosSapIngressQueueLevel = _HqosSapIngressQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2, 1, 4),
    _HqosSapIngressQueueLevel_Type()
)
hqosSapIngressQueueLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressQueueLevel.setStatus("current")


class _HqosSapIngressQueueServWfq_Type(Integer32):
    """Custom type hqosSapIngressQueueServWfq based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 61),
    )


_HqosSapIngressQueueServWfq_Type.__name__ = "Integer32"
_HqosSapIngressQueueServWfq_Object = MibTableColumn
hqosSapIngressQueueServWfq = _HqosSapIngressQueueServWfq_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2, 1, 5),
    _HqosSapIngressQueueServWfq_Type()
)
hqosSapIngressQueueServWfq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressQueueServWfq.setStatus("current")


class _HqosSapIngressQueueType_Type(Integer32):
    """Custom type hqosSapIngressQueueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3))
    )


_HqosSapIngressQueueType_Type.__name__ = "Integer32"
_HqosSapIngressQueueType_Object = MibTableColumn
hqosSapIngressQueueType = _HqosSapIngressQueueType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2, 1, 6),
    _HqosSapIngressQueueType_Type()
)
hqosSapIngressQueueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressQueueType.setStatus("current")


class _HqosSapIngressQueueHiPriority_Type(TruthValue):
    """Custom type hqosSapIngressQueueHiPriority based on TruthValue"""
    defaultValue = 2


_HqosSapIngressQueueHiPriority_Type.__name__ = "TruthValue"
_HqosSapIngressQueueHiPriority_Object = MibTableColumn
hqosSapIngressQueueHiPriority = _HqosSapIngressQueueHiPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2, 1, 7),
    _HqosSapIngressQueueHiPriority_Type()
)
hqosSapIngressQueueHiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressQueueHiPriority.setStatus("current")


class _HqosSapIngressQueueWred_Type(TSlopePolicy):
    """Custom type hqosSapIngressQueueWred based on TSlopePolicy"""
    subtypeSpec = TSlopePolicy.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HqosSapIngressQueueWred_Type.__name__ = "TSlopePolicy"
_HqosSapIngressQueueWred_Object = MibTableColumn
hqosSapIngressQueueWred = _HqosSapIngressQueueWred_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2, 1, 8),
    _HqosSapIngressQueueWred_Type()
)
hqosSapIngressQueueWred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressQueueWred.setStatus("current")
_HqosSapIngressQueueLastChanged_Type = TimeStamp
_HqosSapIngressQueueLastChanged_Object = MibTableColumn
hqosSapIngressQueueLastChanged = _HqosSapIngressQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 2, 1, 9),
    _HqosSapIngressQueueLastChanged_Type()
)
hqosSapIngressQueueLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressQueueLastChanged.setStatus("current")
_HqosSapIngressDSCPTable_Object = MibTable
hqosSapIngressDSCPTable = _HqosSapIngressDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hqosSapIngressDSCPTable.setStatus("current")
_HqosSapIngressDSCPEntry_Object = MibTableRow
hqosSapIngressDSCPEntry = _HqosSapIngressDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 3, 1)
)
hqosSapIngressDSCPEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosSapIngressIndex"),
    (0, "PRVT-QOS-MIB", "hqosSapIngressDSCP"),
)
if mibBuilder.loadTexts:
    hqosSapIngressDSCPEntry.setStatus("current")
_HqosSapIngressDSCP_Type = TDSCPValue
_HqosSapIngressDSCP_Object = MibTableColumn
hqosSapIngressDSCP = _HqosSapIngressDSCP_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 3, 1, 1),
    _HqosSapIngressDSCP_Type()
)
hqosSapIngressDSCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressDSCP.setStatus("current")
_HqosSapIngressDSCPRowStatus_Type = RowStatus
_HqosSapIngressDSCPRowStatus_Object = MibTableColumn
hqosSapIngressDSCPRowStatus = _HqosSapIngressDSCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 3, 1, 2),
    _HqosSapIngressDSCPRowStatus_Type()
)
hqosSapIngressDSCPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosSapIngressDSCPRowStatus.setStatus("current")
_HqosSapIngressDSCPFC_Type = TFCNameOrEmpty
_HqosSapIngressDSCPFC_Object = MibTableColumn
hqosSapIngressDSCPFC = _HqosSapIngressDSCPFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 3, 1, 3),
    _HqosSapIngressDSCPFC_Type()
)
hqosSapIngressDSCPFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressDSCPFC.setStatus("current")
_HqosSapIngressDSCPConformance_Type = TConformanceLevel
_HqosSapIngressDSCPConformance_Object = MibTableColumn
hqosSapIngressDSCPConformance = _HqosSapIngressDSCPConformance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 3, 1, 4),
    _HqosSapIngressDSCPConformance_Type()
)
hqosSapIngressDSCPConformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressDSCPConformance.setStatus("current")
_HqosSapIngressDSCPLastChanged_Type = TimeStamp
_HqosSapIngressDSCPLastChanged_Object = MibTableColumn
hqosSapIngressDSCPLastChanged = _HqosSapIngressDSCPLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 3, 1, 5),
    _HqosSapIngressDSCPLastChanged_Type()
)
hqosSapIngressDSCPLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressDSCPLastChanged.setStatus("current")
_HqosSapIngressDot1pTable_Object = MibTable
hqosSapIngressDot1pTable = _HqosSapIngressDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hqosSapIngressDot1pTable.setStatus("current")
_HqosSapIngressDot1pEntry_Object = MibTableRow
hqosSapIngressDot1pEntry = _HqosSapIngressDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 4, 1)
)
hqosSapIngressDot1pEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosSapIngressIndex"),
    (0, "PRVT-QOS-MIB", "hqosSapIngressDot1pValue"),
)
if mibBuilder.loadTexts:
    hqosSapIngressDot1pEntry.setStatus("current")
_HqosSapIngressDot1pValue_Type = Dot1PPriority
_HqosSapIngressDot1pValue_Object = MibTableColumn
hqosSapIngressDot1pValue = _HqosSapIngressDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 4, 1, 1),
    _HqosSapIngressDot1pValue_Type()
)
hqosSapIngressDot1pValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressDot1pValue.setStatus("current")
_HqosSapIngressDot1pRowStatus_Type = RowStatus
_HqosSapIngressDot1pRowStatus_Object = MibTableColumn
hqosSapIngressDot1pRowStatus = _HqosSapIngressDot1pRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 4, 1, 2),
    _HqosSapIngressDot1pRowStatus_Type()
)
hqosSapIngressDot1pRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosSapIngressDot1pRowStatus.setStatus("current")
_HqosSapIngressDot1pFC_Type = TFCNameOrEmpty
_HqosSapIngressDot1pFC_Object = MibTableColumn
hqosSapIngressDot1pFC = _HqosSapIngressDot1pFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 4, 1, 3),
    _HqosSapIngressDot1pFC_Type()
)
hqosSapIngressDot1pFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressDot1pFC.setStatus("current")
_HqosSapIngressDot1pConformance_Type = TConformanceLevel
_HqosSapIngressDot1pConformance_Object = MibTableColumn
hqosSapIngressDot1pConformance = _HqosSapIngressDot1pConformance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 4, 1, 4),
    _HqosSapIngressDot1pConformance_Type()
)
hqosSapIngressDot1pConformance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosSapIngressDot1pConformance.setStatus("current")
_HqosSapIngressDot1pLastChanged_Type = TimeStamp
_HqosSapIngressDot1pLastChanged_Object = MibTableColumn
hqosSapIngressDot1pLastChanged = _HqosSapIngressDot1pLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 4, 1, 5),
    _HqosSapIngressDot1pLastChanged_Type()
)
hqosSapIngressDot1pLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressDot1pLastChanged.setStatus("current")
_HqosSapIngressFCTable_Object = MibTable
hqosSapIngressFCTable = _HqosSapIngressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hqosSapIngressFCTable.setStatus("current")
_HqosSapIngressFCEntry_Object = MibTableRow
hqosSapIngressFCEntry = _HqosSapIngressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 5, 1)
)
hqosSapIngressFCEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosSapIngressIndex"),
    (0, "PRVT-QOS-MIB", "hqosSapIngressFCNumber"),
    (0, "PRVT-QOS-MIB", "hqosSapIngressFCQueueType"),
)
if mibBuilder.loadTexts:
    hqosSapIngressFCEntry.setStatus("current")
_HqosSapIngressFCNumber_Type = TFCNameOrEmpty
_HqosSapIngressFCNumber_Object = MibTableColumn
hqosSapIngressFCNumber = _HqosSapIngressFCNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 5, 1, 1),
    _HqosSapIngressFCNumber_Type()
)
hqosSapIngressFCNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressFCNumber.setStatus("current")


class _HqosSapIngressFCQueueType_Type(Integer32):
    """Custom type hqosSapIngressFCQueueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3))
    )


_HqosSapIngressFCQueueType_Type.__name__ = "Integer32"
_HqosSapIngressFCQueueType_Object = MibTableColumn
hqosSapIngressFCQueueType = _HqosSapIngressFCQueueType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 5, 1, 2),
    _HqosSapIngressFCQueueType_Type()
)
hqosSapIngressFCQueueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapIngressFCQueueType.setStatus("current")
_HqosSapIngressFCRowStatus_Type = RowStatus
_HqosSapIngressFCRowStatus_Object = MibTableColumn
hqosSapIngressFCRowStatus = _HqosSapIngressFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 5, 1, 3),
    _HqosSapIngressFCRowStatus_Type()
)
hqosSapIngressFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosSapIngressFCRowStatus.setStatus("current")
_HqosSapIngressFCQueue_Type = TIngressQueueId
_HqosSapIngressFCQueue_Object = MibTableColumn
hqosSapIngressFCQueue = _HqosSapIngressFCQueue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 5, 1, 4),
    _HqosSapIngressFCQueue_Type()
)
hqosSapIngressFCQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressFCQueue.setStatus("current")
_HqosSapIngressFCQueueParent_Type = TNamedItemOrEmpty
_HqosSapIngressFCQueueParent_Object = MibTableColumn
hqosSapIngressFCQueueParent = _HqosSapIngressFCQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 5, 1, 5),
    _HqosSapIngressFCQueueParent_Type()
)
hqosSapIngressFCQueueParent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapIngressFCQueueParent.setStatus("current")
_HqosSapIngressFCLastChanged_Type = TimeStamp
_HqosSapIngressFCLastChanged_Object = MibTableColumn
hqosSapIngressFCLastChanged = _HqosSapIngressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 2, 5, 1, 6),
    _HqosSapIngressFCLastChanged_Type()
)
hqosSapIngressFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosSapIngressFCLastChanged.setStatus("current")
_HqosSapEgressObjects_ObjectIdentity = ObjectIdentity
hqosSapEgressObjects = _HqosSapEgressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3)
)
_HqosSapEgressTable_Object = MibTable
hqosSapEgressTable = _HqosSapEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hqosSapEgressTable.setStatus("current")
_HqosSapEgressEntry_Object = MibTableRow
hqosSapEgressEntry = _HqosSapEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 1, 1)
)
hqosSapEgressEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosSapEgressIndex"),
)
if mibBuilder.loadTexts:
    hqosSapEgressEntry.setStatus("current")
_HqosSapEgressIndex_Type = TSapEgressPolicyId
_HqosSapEgressIndex_Object = MibTableColumn
hqosSapEgressIndex = _HqosSapEgressIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 1, 1, 1),
    _HqosSapEgressIndex_Type()
)
hqosSapEgressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapEgressIndex.setStatus("current")
_HqosSapEgressRowStatus_Type = RowStatus
_HqosSapEgressRowStatus_Object = MibTableColumn
hqosSapEgressRowStatus = _HqosSapEgressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 1, 1, 2),
    _HqosSapEgressRowStatus_Type()
)
hqosSapEgressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosSapEgressRowStatus.setStatus("current")


class _HqosSapEgressDescription_Type(TItemDescription):
    """Custom type hqosSapEgressDescription based on TItemDescription"""
    defaultHexValue = ""


_HqosSapEgressDescription_Type.__name__ = "TItemDescription"
_HqosSapEgressDescription_Object = MibTableColumn
hqosSapEgressDescription = _HqosSapEgressDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 1, 1, 5),
    _HqosSapEgressDescription_Type()
)
hqosSapEgressDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapEgressDescription.setStatus("current")
_HqosSapEgressLastChanged_Type = TimeStamp
_HqosSapEgressLastChanged_Object = MibTableColumn
hqosSapEgressLastChanged = _HqosSapEgressLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 1, 1, 6),
    _HqosSapEgressLastChanged_Type()
)
hqosSapEgressLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapEgressLastChanged.setStatus("current")
_HqosSapEgressQueueTable_Object = MibTable
hqosSapEgressQueueTable = _HqosSapEgressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hqosSapEgressQueueTable.setStatus("current")
_HqosSapEgressQueueEntry_Object = MibTableRow
hqosSapEgressQueueEntry = _HqosSapEgressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2, 1)
)
hqosSapEgressQueueEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosSapEgressIndex"),
    (0, "PRVT-QOS-MIB", "hqosSapEgressQueueIndex"),
    (0, "PRVT-QOS-MIB", "hqosSapEgressQueueParent"),
)
if mibBuilder.loadTexts:
    hqosSapEgressQueueEntry.setStatus("current")
_HqosSapEgressQueueIndex_Type = TEgressQueueId
_HqosSapEgressQueueIndex_Object = MibTableColumn
hqosSapEgressQueueIndex = _HqosSapEgressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2, 1, 1),
    _HqosSapEgressQueueIndex_Type()
)
hqosSapEgressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapEgressQueueIndex.setStatus("current")
_HqosSapEgressQueueParent_Type = TNamedItemOrEmpty
_HqosSapEgressQueueParent_Object = MibTableColumn
hqosSapEgressQueueParent = _HqosSapEgressQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2, 1, 2),
    _HqosSapEgressQueueParent_Type()
)
hqosSapEgressQueueParent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapEgressQueueParent.setStatus("current")
_HqosSapEgressQueueRowStatus_Type = RowStatus
_HqosSapEgressQueueRowStatus_Object = MibTableColumn
hqosSapEgressQueueRowStatus = _HqosSapEgressQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2, 1, 3),
    _HqosSapEgressQueueRowStatus_Type()
)
hqosSapEgressQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosSapEgressQueueRowStatus.setStatus("current")


class _HqosSapEgressQueueLevel_Type(TLevel):
    """Custom type hqosSapEgressQueueLevel based on TLevel"""
    defaultValue = 1


_HqosSapEgressQueueLevel_Type.__name__ = "TLevel"
_HqosSapEgressQueueLevel_Object = MibTableColumn
hqosSapEgressQueueLevel = _HqosSapEgressQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2, 1, 4),
    _HqosSapEgressQueueLevel_Type()
)
hqosSapEgressQueueLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapEgressQueueLevel.setStatus("current")


class _HqosSapEgressQueueServWfq_Type(Integer32):
    """Custom type hqosSapEgressQueueServWfq based on Integer32"""
    defaultValue = 1


_HqosSapEgressQueueServWfq_Type.__name__ = "Integer32"
_HqosSapEgressQueueServWfq_Object = MibTableColumn
hqosSapEgressQueueServWfq = _HqosSapEgressQueueServWfq_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2, 1, 5),
    _HqosSapEgressQueueServWfq_Type()
)
hqosSapEgressQueueServWfq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapEgressQueueServWfq.setStatus("current")


class _HqosSapEgressQueueType_Type(Integer32):
    """Custom type hqosSapEgressQueueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3))
    )


_HqosSapEgressQueueType_Type.__name__ = "Integer32"
_HqosSapEgressQueueType_Object = MibTableColumn
hqosSapEgressQueueType = _HqosSapEgressQueueType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2, 1, 6),
    _HqosSapEgressQueueType_Type()
)
hqosSapEgressQueueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapEgressQueueType.setStatus("current")


class _HqosSapEgressQueueHiPriority_Type(TruthValue):
    """Custom type hqosSapEgressQueueHiPriority based on TruthValue"""
    defaultValue = 2


_HqosSapEgressQueueHiPriority_Type.__name__ = "TruthValue"
_HqosSapEgressQueueHiPriority_Object = MibTableColumn
hqosSapEgressQueueHiPriority = _HqosSapEgressQueueHiPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2, 1, 7),
    _HqosSapEgressQueueHiPriority_Type()
)
hqosSapEgressQueueHiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapEgressQueueHiPriority.setStatus("current")
_HqosSapEgressQueueWred_Type = TSlopePolicy
_HqosSapEgressQueueWred_Object = MibTableColumn
hqosSapEgressQueueWred = _HqosSapEgressQueueWred_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2, 1, 8),
    _HqosSapEgressQueueWred_Type()
)
hqosSapEgressQueueWred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapEgressQueueWred.setStatus("current")
_HqosSapEgressQueueLastChanged_Type = TimeStamp
_HqosSapEgressQueueLastChanged_Object = MibTableColumn
hqosSapEgressQueueLastChanged = _HqosSapEgressQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 2, 1, 9),
    _HqosSapEgressQueueLastChanged_Type()
)
hqosSapEgressQueueLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapEgressQueueLastChanged.setStatus("current")
_HqosSapEgressFCTable_Object = MibTable
hqosSapEgressFCTable = _HqosSapEgressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hqosSapEgressFCTable.setStatus("current")
_HqosSapEgressFCEntry_Object = MibTableRow
hqosSapEgressFCEntry = _HqosSapEgressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 3, 1)
)
hqosSapEgressFCEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosSapEgressIndex"),
    (0, "PRVT-QOS-MIB", "hqosSapEgressFCNumber"),
    (0, "PRVT-QOS-MIB", "hqosSapEgressFCEntryType"),
)
if mibBuilder.loadTexts:
    hqosSapEgressFCEntry.setStatus("current")
_HqosSapEgressFCNumber_Type = TFCNameOrEmpty
_HqosSapEgressFCNumber_Object = MibTableColumn
hqosSapEgressFCNumber = _HqosSapEgressFCNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 3, 1, 1),
    _HqosSapEgressFCNumber_Type()
)
hqosSapEgressFCNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapEgressFCNumber.setStatus("current")


class _HqosSapEgressFCEntryType_Type(Integer32):
    """Custom type hqosSapEgressFCEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3),
          ("dscp", 4),
          ("dot1p", 5))
    )


_HqosSapEgressFCEntryType_Type.__name__ = "Integer32"
_HqosSapEgressFCEntryType_Object = MibTableColumn
hqosSapEgressFCEntryType = _HqosSapEgressFCEntryType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 3, 1, 2),
    _HqosSapEgressFCEntryType_Type()
)
hqosSapEgressFCEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapEgressFCEntryType.setStatus("current")
_HqosSapEgressFCRowStatus_Type = RowStatus
_HqosSapEgressFCRowStatus_Object = MibTableColumn
hqosSapEgressFCRowStatus = _HqosSapEgressFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 3, 1, 3),
    _HqosSapEgressFCRowStatus_Type()
)
hqosSapEgressFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosSapEgressFCRowStatus.setStatus("current")
_HqosSapEgressFCQueue_Type = TEgressQueueId
_HqosSapEgressFCQueue_Object = MibTableColumn
hqosSapEgressFCQueue = _HqosSapEgressFCQueue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 3, 1, 4),
    _HqosSapEgressFCQueue_Type()
)
hqosSapEgressFCQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapEgressFCQueue.setStatus("current")
_HqosSapEgressFCQueueParent_Type = TNamedItemOrEmpty
_HqosSapEgressFCQueueParent_Object = MibTableColumn
hqosSapEgressFCQueueParent = _HqosSapEgressFCQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 3, 1, 5),
    _HqosSapEgressFCQueueParent_Type()
)
hqosSapEgressFCQueueParent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapEgressFCQueueParent.setStatus("current")


class _HqosSapEgressFCDot1PValue_Type(Dot1PPriority):
    """Custom type hqosSapEgressFCDot1PValue based on Dot1PPriority"""
    defaultValue = -1


_HqosSapEgressFCDot1PValue_Type.__name__ = "Dot1PPriority"
_HqosSapEgressFCDot1PValue_Object = MibTableColumn
hqosSapEgressFCDot1PValue = _HqosSapEgressFCDot1PValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 3, 1, 6),
    _HqosSapEgressFCDot1PValue_Type()
)
hqosSapEgressFCDot1PValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapEgressFCDot1PValue.setStatus("current")
_HqosSapEgressFCDSCPValue_Type = TDSCPValue
_HqosSapEgressFCDSCPValue_Object = MibTableColumn
hqosSapEgressFCDSCPValue = _HqosSapEgressFCDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 3, 1, 7),
    _HqosSapEgressFCDSCPValue_Type()
)
hqosSapEgressFCDSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSapEgressFCDSCPValue.setStatus("current")
_HqosSapEgressFCLastChanged_Type = TimeStamp
_HqosSapEgressFCLastChanged_Object = MibTableColumn
hqosSapEgressFCLastChanged = _HqosSapEgressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 3, 3, 1, 8),
    _HqosSapEgressFCLastChanged_Type()
)
hqosSapEgressFCLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSapEgressFCLastChanged.setStatus("current")
_HqosNetworkObjects_ObjectIdentity = ObjectIdentity
hqosNetworkObjects = _HqosNetworkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4)
)
_HqosNetworkPolicyTable_Object = MibTable
hqosNetworkPolicyTable = _HqosNetworkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hqosNetworkPolicyTable.setStatus("current")
_HqosNetworkPolicyEntry_Object = MibTableRow
hqosNetworkPolicyEntry = _HqosNetworkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 1, 1)
)
hqosNetworkPolicyEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosNetworkPolicyIndex"),
)
if mibBuilder.loadTexts:
    hqosNetworkPolicyEntry.setStatus("current")
_HqosNetworkPolicyIndex_Type = TNetworkPolicyId
_HqosNetworkPolicyIndex_Object = MibTableColumn
hqosNetworkPolicyIndex = _HqosNetworkPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 1, 1, 1),
    _HqosNetworkPolicyIndex_Type()
)
hqosNetworkPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkPolicyIndex.setStatus("current")
_HqosNetworkPolicyRowStatus_Type = RowStatus
_HqosNetworkPolicyRowStatus_Object = MibTableColumn
hqosNetworkPolicyRowStatus = _HqosNetworkPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 1, 1, 2),
    _HqosNetworkPolicyRowStatus_Type()
)
hqosNetworkPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosNetworkPolicyRowStatus.setStatus("current")


class _HqosNetworkPolicyDescription_Type(TItemDescription):
    """Custom type hqosNetworkPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_HqosNetworkPolicyDescription_Type.__name__ = "TItemDescription"
_HqosNetworkPolicyDescription_Object = MibTableColumn
hqosNetworkPolicyDescription = _HqosNetworkPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 1, 1, 3),
    _HqosNetworkPolicyDescription_Type()
)
hqosNetworkPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkPolicyDescription.setStatus("current")
_HqosNetworkPolicyIngressDefaultActionFC_Type = TFCNameOrEmpty
_HqosNetworkPolicyIngressDefaultActionFC_Object = MibTableColumn
hqosNetworkPolicyIngressDefaultActionFC = _HqosNetworkPolicyIngressDefaultActionFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 1, 1, 4),
    _HqosNetworkPolicyIngressDefaultActionFC_Type()
)
hqosNetworkPolicyIngressDefaultActionFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkPolicyIngressDefaultActionFC.setStatus("current")
_HqosNetworkPolicyIngressConformance_Type = TConformanceLevel
_HqosNetworkPolicyIngressConformance_Object = MibTableColumn
hqosNetworkPolicyIngressConformance = _HqosNetworkPolicyIngressConformance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 1, 1, 5),
    _HqosNetworkPolicyIngressConformance_Type()
)
hqosNetworkPolicyIngressConformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkPolicyIngressConformance.setStatus("current")


class _HqosNetworkPolicyEgressRemark_Type(TruthValue):
    """Custom type hqosNetworkPolicyEgressRemark based on TruthValue"""
    defaultValue = 2


_HqosNetworkPolicyEgressRemark_Type.__name__ = "TruthValue"
_HqosNetworkPolicyEgressRemark_Object = MibTableColumn
hqosNetworkPolicyEgressRemark = _HqosNetworkPolicyEgressRemark_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 1, 1, 6),
    _HqosNetworkPolicyEgressRemark_Type()
)
hqosNetworkPolicyEgressRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosNetworkPolicyEgressRemark.setStatus("current")
_HqosNetworkPolicyLastChanged_Type = TimeStamp
_HqosNetworkPolicyLastChanged_Object = MibTableColumn
hqosNetworkPolicyLastChanged = _HqosNetworkPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 1, 1, 7),
    _HqosNetworkPolicyLastChanged_Type()
)
hqosNetworkPolicyLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkPolicyLastChanged.setStatus("current")
_HqosNetworkIngressLSPEXPTable_Object = MibTable
hqosNetworkIngressLSPEXPTable = _HqosNetworkIngressLSPEXPTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hqosNetworkIngressLSPEXPTable.setStatus("current")
_HqosNetworkIngressLSPEXPEntry_Object = MibTableRow
hqosNetworkIngressLSPEXPEntry = _HqosNetworkIngressLSPEXPEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 2, 1)
)
hqosNetworkIngressLSPEXPEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosNetworkPolicyIndex"),
    (0, "PRVT-QOS-MIB", "hqosNetworkIngressLSPEXP"),
)
if mibBuilder.loadTexts:
    hqosNetworkIngressLSPEXPEntry.setStatus("current")


class _HqosNetworkIngressLSPEXP_Type(TLspExpValue):
    """Custom type hqosNetworkIngressLSPEXP based on TLspExpValue"""
    subtypeSpec = TLspExpValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HqosNetworkIngressLSPEXP_Type.__name__ = "TLspExpValue"
_HqosNetworkIngressLSPEXP_Object = MibTableColumn
hqosNetworkIngressLSPEXP = _HqosNetworkIngressLSPEXP_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 2, 1, 1),
    _HqosNetworkIngressLSPEXP_Type()
)
hqosNetworkIngressLSPEXP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkIngressLSPEXP.setStatus("current")
_HqosNetworkIngressLSPEXPRowStatus_Type = RowStatus
_HqosNetworkIngressLSPEXPRowStatus_Object = MibTableColumn
hqosNetworkIngressLSPEXPRowStatus = _HqosNetworkIngressLSPEXPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 2, 1, 2),
    _HqosNetworkIngressLSPEXPRowStatus_Type()
)
hqosNetworkIngressLSPEXPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosNetworkIngressLSPEXPRowStatus.setStatus("current")
_HqosNetworkIngressLSPEXPFC_Type = TFCNameOrEmpty
_HqosNetworkIngressLSPEXPFC_Object = MibTableColumn
hqosNetworkIngressLSPEXPFC = _HqosNetworkIngressLSPEXPFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 2, 1, 3),
    _HqosNetworkIngressLSPEXPFC_Type()
)
hqosNetworkIngressLSPEXPFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkIngressLSPEXPFC.setStatus("current")
_HqosNetworkIngressLSPEXPConformance_Type = TConformanceLevel
_HqosNetworkIngressLSPEXPConformance_Object = MibTableColumn
hqosNetworkIngressLSPEXPConformance = _HqosNetworkIngressLSPEXPConformance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 2, 1, 4),
    _HqosNetworkIngressLSPEXPConformance_Type()
)
hqosNetworkIngressLSPEXPConformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkIngressLSPEXPConformance.setStatus("current")
_HqosNetworkIngressLSPEXPLastChanged_Type = TimeStamp
_HqosNetworkIngressLSPEXPLastChanged_Object = MibTableColumn
hqosNetworkIngressLSPEXPLastChanged = _HqosNetworkIngressLSPEXPLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 2, 1, 5),
    _HqosNetworkIngressLSPEXPLastChanged_Type()
)
hqosNetworkIngressLSPEXPLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkIngressLSPEXPLastChanged.setStatus("current")
_HqosNetworkEgressFCTable_Object = MibTable
hqosNetworkEgressFCTable = _HqosNetworkEgressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hqosNetworkEgressFCTable.setStatus("current")
_HqosNetworkEgressFCEntry_Object = MibTableRow
hqosNetworkEgressFCEntry = _HqosNetworkEgressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 3, 1)
)
hqosNetworkEgressFCEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosNetworkPolicyIndex"),
    (0, "PRVT-QOS-MIB", "hqosNetworkEgressFCNumber"),
    (0, "PRVT-QOS-MIB", "hqosNetworkEgressFCConformance"),
)
if mibBuilder.loadTexts:
    hqosNetworkEgressFCEntry.setStatus("current")
_HqosNetworkEgressFCNumber_Type = TFCNameOrEmpty
_HqosNetworkEgressFCNumber_Object = MibTableColumn
hqosNetworkEgressFCNumber = _HqosNetworkEgressFCNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 3, 1, 1),
    _HqosNetworkEgressFCNumber_Type()
)
hqosNetworkEgressFCNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkEgressFCNumber.setStatus("current")
_HqosNetworkEgressFCRowStatus_Type = RowStatus
_HqosNetworkEgressFCRowStatus_Object = MibTableColumn
hqosNetworkEgressFCRowStatus = _HqosNetworkEgressFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 3, 1, 2),
    _HqosNetworkEgressFCRowStatus_Type()
)
hqosNetworkEgressFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosNetworkEgressFCRowStatus.setStatus("current")


class _HqosNetworkEgressFCLspExpValue_Type(TLspExpValue):
    """Custom type hqosNetworkEgressFCLspExpValue based on TLspExpValue"""
    subtypeSpec = TLspExpValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HqosNetworkEgressFCLspExpValue_Type.__name__ = "TLspExpValue"
_HqosNetworkEgressFCLspExpValue_Object = MibTableColumn
hqosNetworkEgressFCLspExpValue = _HqosNetworkEgressFCLspExpValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 3, 1, 3),
    _HqosNetworkEgressFCLspExpValue_Type()
)
hqosNetworkEgressFCLspExpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkEgressFCLspExpValue.setStatus("current")
_HqosNetworkEgressFCDot1Priority_Type = Dot1PPriority
_HqosNetworkEgressFCDot1Priority_Object = MibTableColumn
hqosNetworkEgressFCDot1Priority = _HqosNetworkEgressFCDot1Priority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 3, 1, 4),
    _HqosNetworkEgressFCDot1Priority_Type()
)
hqosNetworkEgressFCDot1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkEgressFCDot1Priority.setStatus("current")
_HqosNetworkEgressFCLastChanged_Type = TimeStamp
_HqosNetworkEgressFCLastChanged_Object = MibTableColumn
hqosNetworkEgressFCLastChanged = _HqosNetworkEgressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 3, 1, 5),
    _HqosNetworkEgressFCLastChanged_Type()
)
hqosNetworkEgressFCLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkEgressFCLastChanged.setStatus("current")
_HqosNetworkEgressFCConformance_Type = TConformanceLevel
_HqosNetworkEgressFCConformance_Object = MibTableColumn
hqosNetworkEgressFCConformance = _HqosNetworkEgressFCConformance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 4, 3, 1, 6),
    _HqosNetworkEgressFCConformance_Type()
)
hqosNetworkEgressFCConformance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkEgressFCConformance.setStatus("current")
_HqosNetworkQueueObjects_ObjectIdentity = ObjectIdentity
hqosNetworkQueueObjects = _HqosNetworkQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5)
)
_HqosNetworkQueuePolicyTable_Object = MibTable
hqosNetworkQueuePolicyTable = _HqosNetworkQueuePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hqosNetworkQueuePolicyTable.setStatus("current")
_HqosNetworkQueuePolicyEntry_Object = MibTableRow
hqosNetworkQueuePolicyEntry = _HqosNetworkQueuePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 1, 1)
)
hqosNetworkQueuePolicyEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosNetworkQueuePolicy"),
)
if mibBuilder.loadTexts:
    hqosNetworkQueuePolicyEntry.setStatus("current")
_HqosNetworkQueuePolicy_Type = TNamedItem
_HqosNetworkQueuePolicy_Object = MibTableColumn
hqosNetworkQueuePolicy = _HqosNetworkQueuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 1, 1, 1),
    _HqosNetworkQueuePolicy_Type()
)
hqosNetworkQueuePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkQueuePolicy.setStatus("current")
_HqosNetworkQueuePolicyRowStatus_Type = RowStatus
_HqosNetworkQueuePolicyRowStatus_Object = MibTableColumn
hqosNetworkQueuePolicyRowStatus = _HqosNetworkQueuePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 1, 1, 2),
    _HqosNetworkQueuePolicyRowStatus_Type()
)
hqosNetworkQueuePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosNetworkQueuePolicyRowStatus.setStatus("current")


class _HqosNetworkQueuePolicyDescription_Type(TItemDescription):
    """Custom type hqosNetworkQueuePolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_HqosNetworkQueuePolicyDescription_Type.__name__ = "TItemDescription"
_HqosNetworkQueuePolicyDescription_Object = MibTableColumn
hqosNetworkQueuePolicyDescription = _HqosNetworkQueuePolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 1, 1, 3),
    _HqosNetworkQueuePolicyDescription_Type()
)
hqosNetworkQueuePolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkQueuePolicyDescription.setStatus("current")
_HqosNetworkQueuePolicyLastChanged_Type = TimeStamp
_HqosNetworkQueuePolicyLastChanged_Object = MibTableColumn
hqosNetworkQueuePolicyLastChanged = _HqosNetworkQueuePolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 1, 1, 8),
    _HqosNetworkQueuePolicyLastChanged_Type()
)
hqosNetworkQueuePolicyLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkQueuePolicyLastChanged.setStatus("current")
_HqosNetworkQueueTable_Object = MibTable
hqosNetworkQueueTable = _HqosNetworkQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hqosNetworkQueueTable.setStatus("current")
_HqosNetworkQueueEntry_Object = MibTableRow
hqosNetworkQueueEntry = _HqosNetworkQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1)
)
hqosNetworkQueueEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosNetworkQueuePolicy"),
    (0, "PRVT-QOS-MIB", "hqosNetworkQueue"),
)
if mibBuilder.loadTexts:
    hqosNetworkQueueEntry.setStatus("current")


class _HqosNetworkQueue_Type(TQueueId):
    """Custom type hqosNetworkQueue based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_HqosNetworkQueue_Type.__name__ = "TQueueId"
_HqosNetworkQueue_Object = MibTableColumn
hqosNetworkQueue = _HqosNetworkQueue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1, 1),
    _HqosNetworkQueue_Type()
)
hqosNetworkQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkQueue.setStatus("current")
_HqosNetworkQueueRowStatus_Type = RowStatus
_HqosNetworkQueueRowStatus_Object = MibTableColumn
hqosNetworkQueueRowStatus = _HqosNetworkQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1, 2),
    _HqosNetworkQueueRowStatus_Type()
)
hqosNetworkQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosNetworkQueueRowStatus.setStatus("current")


class _HqosNetworkQueueParent_Type(TNamedItemOrEmpty):
    """Custom type hqosNetworkQueueParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_HqosNetworkQueueParent_Type.__name__ = "TNamedItemOrEmpty"
_HqosNetworkQueueParent_Object = MibTableColumn
hqosNetworkQueueParent = _HqosNetworkQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1, 3),
    _HqosNetworkQueueParent_Type()
)
hqosNetworkQueueParent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkQueueParent.setStatus("current")


class _HqosNetworkQueueLevel_Type(TLevel):
    """Custom type hqosNetworkQueueLevel based on TLevel"""
    defaultValue = 1


_HqosNetworkQueueLevel_Type.__name__ = "TLevel"
_HqosNetworkQueueLevel_Object = MibTableColumn
hqosNetworkQueueLevel = _HqosNetworkQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1, 4),
    _HqosNetworkQueueLevel_Type()
)
hqosNetworkQueueLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkQueueLevel.setStatus("current")


class _HqosNetworkQueueWfqProfile_Type(Integer32):
    """Custom type hqosNetworkQueueWfqProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HqosNetworkQueueWfqProfile_Type.__name__ = "Integer32"
_HqosNetworkQueueWfqProfile_Object = MibTableColumn
hqosNetworkQueueWfqProfile = _HqosNetworkQueueWfqProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1, 5),
    _HqosNetworkQueueWfqProfile_Type()
)
hqosNetworkQueueWfqProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkQueueWfqProfile.setStatus("current")


class _HqosNetworkQueueType_Type(Integer32):
    """Custom type hqosNetworkQueueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3))
    )


_HqosNetworkQueueType_Type.__name__ = "Integer32"
_HqosNetworkQueueType_Object = MibTableColumn
hqosNetworkQueueType = _HqosNetworkQueueType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1, 6),
    _HqosNetworkQueueType_Type()
)
hqosNetworkQueueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkQueueType.setStatus("current")
_HqosNetworkQueueHiPriority_Type = TruthValue
_HqosNetworkQueueHiPriority_Object = MibTableColumn
hqosNetworkQueueHiPriority = _HqosNetworkQueueHiPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1, 7),
    _HqosNetworkQueueHiPriority_Type()
)
hqosNetworkQueueHiPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosNetworkQueueHiPriority.setStatus("obsolete")


class _HqosNetworkQueueWred_Type(TSlopePolicy):
    """Custom type hqosNetworkQueueWred based on TSlopePolicy"""
    subtypeSpec = TSlopePolicy.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(57, 64),
    )


_HqosNetworkQueueWred_Type.__name__ = "TSlopePolicy"
_HqosNetworkQueueWred_Object = MibTableColumn
hqosNetworkQueueWred = _HqosNetworkQueueWred_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1, 8),
    _HqosNetworkQueueWred_Type()
)
hqosNetworkQueueWred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkQueueWred.setStatus("current")


class _HqosNetworkQueueShaper_Type(TShaperId):
    """Custom type hqosNetworkQueueShaper based on TShaperId"""
    subtypeSpec = TShaperId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 64),
    )


_HqosNetworkQueueShaper_Type.__name__ = "TShaperId"
_HqosNetworkQueueShaper_Object = MibTableColumn
hqosNetworkQueueShaper = _HqosNetworkQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1, 9),
    _HqosNetworkQueueShaper_Type()
)
hqosNetworkQueueShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkQueueShaper.setStatus("current")
_HqosNetworkQueueLastChanged_Type = TimeStamp
_HqosNetworkQueueLastChanged_Object = MibTableColumn
hqosNetworkQueueLastChanged = _HqosNetworkQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 2, 1, 10),
    _HqosNetworkQueueLastChanged_Type()
)
hqosNetworkQueueLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkQueueLastChanged.setStatus("current")
_HqosNetworkQueueFCTable_Object = MibTable
hqosNetworkQueueFCTable = _HqosNetworkQueueFCTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hqosNetworkQueueFCTable.setStatus("current")
_HqosNetworkQueueFCEntry_Object = MibTableRow
hqosNetworkQueueFCEntry = _HqosNetworkQueueFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 3, 1)
)
hqosNetworkQueueFCEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosNetworkQueuePolicy"),
    (0, "PRVT-QOS-MIB", "hqosNetworkQueueFCNumber"),
    (0, "PRVT-QOS-MIB", "hqosNetworkQueueFCType"),
)
if mibBuilder.loadTexts:
    hqosNetworkQueueFCEntry.setStatus("current")
_HqosNetworkQueueFCNumber_Type = TFCNameOrEmpty
_HqosNetworkQueueFCNumber_Object = MibTableColumn
hqosNetworkQueueFCNumber = _HqosNetworkQueueFCNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 3, 1, 1),
    _HqosNetworkQueueFCNumber_Type()
)
hqosNetworkQueueFCNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkQueueFCNumber.setStatus("current")


class _HqosNetworkQueueFCType_Type(Integer32):
    """Custom type hqosNetworkQueueFCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3))
    )


_HqosNetworkQueueFCType_Type.__name__ = "Integer32"
_HqosNetworkQueueFCType_Object = MibTableColumn
hqosNetworkQueueFCType = _HqosNetworkQueueFCType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 3, 1, 2),
    _HqosNetworkQueueFCType_Type()
)
hqosNetworkQueueFCType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkQueueFCType.setStatus("current")
_HqosNetworkQueueFCRowStatus_Type = RowStatus
_HqosNetworkQueueFCRowStatus_Object = MibTableColumn
hqosNetworkQueueFCRowStatus = _HqosNetworkQueueFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 3, 1, 3),
    _HqosNetworkQueueFCRowStatus_Type()
)
hqosNetworkQueueFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosNetworkQueueFCRowStatus.setStatus("current")


class _HqosNetworkQueueFC_Type(TQueueId):
    """Custom type hqosNetworkQueueFC based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_HqosNetworkQueueFC_Type.__name__ = "TQueueId"
_HqosNetworkQueueFC_Object = MibTableColumn
hqosNetworkQueueFC = _HqosNetworkQueueFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 3, 1, 4),
    _HqosNetworkQueueFC_Type()
)
hqosNetworkQueueFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosNetworkQueueFC.setStatus("current")
_HqosNetworkQueueFCLastChanged_Type = TimeStamp
_HqosNetworkQueueFCLastChanged_Object = MibTableColumn
hqosNetworkQueueFCLastChanged = _HqosNetworkQueueFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 5, 3, 1, 5),
    _HqosNetworkQueueFCLastChanged_Type()
)
hqosNetworkQueueFCLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosNetworkQueueFCLastChanged.setStatus("current")
_HqosSchedulerObjects_ObjectIdentity = ObjectIdentity
hqosSchedulerObjects = _HqosSchedulerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6)
)
_HqosSchedulerPolicyTable_Object = MibTable
hqosSchedulerPolicyTable = _HqosSchedulerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hqosSchedulerPolicyTable.setStatus("current")
_HqosSchedulerPolicyEntry_Object = MibTableRow
hqosSchedulerPolicyEntry = _HqosSchedulerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 1, 1)
)
hqosSchedulerPolicyEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosSchedulerPolicyName"),
    (0, "PRVT-QOS-MIB", "hqosSchedulerPolicyType"),
)
if mibBuilder.loadTexts:
    hqosSchedulerPolicyEntry.setStatus("current")
_HqosSchedulerPolicyName_Type = TNamedItem
_HqosSchedulerPolicyName_Object = MibTableColumn
hqosSchedulerPolicyName = _HqosSchedulerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 1, 1, 1),
    _HqosSchedulerPolicyName_Type()
)
hqosSchedulerPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSchedulerPolicyName.setStatus("current")
_HqosSchedulerPolicyRowStatus_Type = RowStatus
_HqosSchedulerPolicyRowStatus_Object = MibTableColumn
hqosSchedulerPolicyRowStatus = _HqosSchedulerPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 1, 1, 2),
    _HqosSchedulerPolicyRowStatus_Type()
)
hqosSchedulerPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosSchedulerPolicyRowStatus.setStatus("current")


class _HqosSchedulerPolicyType_Type(Integer32):
    """Custom type hqosSchedulerPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ingress", 1),
          ("egress", 2),
          ("network", 3))
    )


_HqosSchedulerPolicyType_Type.__name__ = "Integer32"
_HqosSchedulerPolicyType_Object = MibTableColumn
hqosSchedulerPolicyType = _HqosSchedulerPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 1, 1, 3),
    _HqosSchedulerPolicyType_Type()
)
hqosSchedulerPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSchedulerPolicyType.setStatus("current")


class _HqosSchedulerPolicyDescription_Type(TItemDescription):
    """Custom type hqosSchedulerPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_HqosSchedulerPolicyDescription_Type.__name__ = "TItemDescription"
_HqosSchedulerPolicyDescription_Object = MibTableColumn
hqosSchedulerPolicyDescription = _HqosSchedulerPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 1, 1, 4),
    _HqosSchedulerPolicyDescription_Type()
)
hqosSchedulerPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosSchedulerPolicyDescription.setStatus("current")
_HqosSchedulerPolicyLastChanged_Type = TimeStamp
_HqosSchedulerPolicyLastChanged_Object = MibTableColumn
hqosSchedulerPolicyLastChanged = _HqosSchedulerPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 1, 1, 5),
    _HqosSchedulerPolicyLastChanged_Type()
)
hqosSchedulerPolicyLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosSchedulerPolicyLastChanged.setStatus("current")
_HqosVirtualSchedulerTable_Object = MibTable
hqosVirtualSchedulerTable = _HqosVirtualSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hqosVirtualSchedulerTable.setStatus("current")
_HqosVirtualSchedulerEntry_Object = MibTableRow
hqosVirtualSchedulerEntry = _HqosVirtualSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2, 1)
)
hqosVirtualSchedulerEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "hqosSchedulerPolicyName"),
    (0, "PRVT-QOS-MIB", "hqosSchedulerPolicyType"),
    (0, "PRVT-QOS-MIB", "hqosVirtualSchedulerName"),
    (0, "PRVT-QOS-MIB", "hqosVirtualSchedulerLevel"),
)
if mibBuilder.loadTexts:
    hqosVirtualSchedulerEntry.setStatus("current")
_HqosVirtualSchedulerName_Type = TNamedItem
_HqosVirtualSchedulerName_Object = MibTableColumn
hqosVirtualSchedulerName = _HqosVirtualSchedulerName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2, 1, 1),
    _HqosVirtualSchedulerName_Type()
)
hqosVirtualSchedulerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosVirtualSchedulerName.setStatus("current")
_HqosVirtualSchedulerRowStatus_Type = RowStatus
_HqosVirtualSchedulerRowStatus_Object = MibTableColumn
hqosVirtualSchedulerRowStatus = _HqosVirtualSchedulerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2, 1, 2),
    _HqosVirtualSchedulerRowStatus_Type()
)
hqosVirtualSchedulerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hqosVirtualSchedulerRowStatus.setStatus("current")


class _HqosVirtualSchedulerDescription_Type(TItemDescription):
    """Custom type hqosVirtualSchedulerDescription based on TItemDescription"""
    defaultHexValue = ""


_HqosVirtualSchedulerDescription_Type.__name__ = "TItemDescription"
_HqosVirtualSchedulerDescription_Object = MibTableColumn
hqosVirtualSchedulerDescription = _HqosVirtualSchedulerDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2, 1, 3),
    _HqosVirtualSchedulerDescription_Type()
)
hqosVirtualSchedulerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosVirtualSchedulerDescription.setStatus("current")
_HqosVirtualSchedulerParent_Type = TNamedItemOrEmpty
_HqosVirtualSchedulerParent_Object = MibTableColumn
hqosVirtualSchedulerParent = _HqosVirtualSchedulerParent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2, 1, 4),
    _HqosVirtualSchedulerParent_Type()
)
hqosVirtualSchedulerParent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosVirtualSchedulerParent.setStatus("current")
_HqosVirtualSchedulerLevel_Type = TLevel
_HqosVirtualSchedulerLevel_Object = MibTableColumn
hqosVirtualSchedulerLevel = _HqosVirtualSchedulerLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2, 1, 5),
    _HqosVirtualSchedulerLevel_Type()
)
hqosVirtualSchedulerLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosVirtualSchedulerLevel.setStatus("current")


class _HqosVirtualSchedulerPriority_Type(Integer32):
    """Custom type hqosVirtualSchedulerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_HqosVirtualSchedulerPriority_Type.__name__ = "Integer32"
_HqosVirtualSchedulerPriority_Object = MibTableColumn
hqosVirtualSchedulerPriority = _HqosVirtualSchedulerPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2, 1, 6),
    _HqosVirtualSchedulerPriority_Type()
)
hqosVirtualSchedulerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosVirtualSchedulerPriority.setStatus("current")
_HqosVirtualSchedulerWfqProfile_Type = Integer32
_HqosVirtualSchedulerWfqProfile_Object = MibTableColumn
hqosVirtualSchedulerWfqProfile = _HqosVirtualSchedulerWfqProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2, 1, 7),
    _HqosVirtualSchedulerWfqProfile_Type()
)
hqosVirtualSchedulerWfqProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosVirtualSchedulerWfqProfile.setStatus("current")
_HqosVirtualSchedulerShaper_Type = TShaperId
_HqosVirtualSchedulerShaper_Object = MibTableColumn
hqosVirtualSchedulerShaper = _HqosVirtualSchedulerShaper_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2, 1, 8),
    _HqosVirtualSchedulerShaper_Type()
)
hqosVirtualSchedulerShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hqosVirtualSchedulerShaper.setStatus("current")
_HqosVirtualSchedulerLastChanged_Type = TimeStamp
_HqosVirtualSchedulerLastChanged_Object = MibTableColumn
hqosVirtualSchedulerLastChanged = _HqosVirtualSchedulerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 6, 2, 1, 9),
    _HqosVirtualSchedulerLastChanged_Type()
)
hqosVirtualSchedulerLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hqosVirtualSchedulerLastChanged.setStatus("current")
_TWredObjects_ObjectIdentity = ObjectIdentity
tWredObjects = _TWredObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7)
)
_TWredProfileTable_Object = MibTable
tWredProfileTable = _TWredProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tWredProfileTable.setStatus("current")
_TWredProfileEntry_Object = MibTableRow
tWredProfileEntry = _TWredProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1)
)
tWredProfileEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "tWredProfile"),
)
if mibBuilder.loadTexts:
    tWredProfileEntry.setStatus("current")
_TWredProfile_Type = TSlopePolicy
_TWredProfile_Object = MibTableColumn
tWredProfile = _TWredProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 1),
    _TWredProfile_Type()
)
tWredProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tWredProfile.setStatus("current")
_TWredRowStatus_Type = RowStatus
_TWredRowStatus_Object = MibTableColumn
tWredRowStatus = _TWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 2),
    _TWredRowStatus_Type()
)
tWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tWredRowStatus.setStatus("current")


class _TWredDescription_Type(TItemDescription):
    """Custom type tWredDescription based on TItemDescription"""
    defaultHexValue = ""


_TWredDescription_Type.__name__ = "TItemDescription"
_TWredDescription_Object = MibTableColumn
tWredDescription = _TWredDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 3),
    _TWredDescription_Type()
)
tWredDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWredDescription.setStatus("current")
_TWredGreenStartAverage_Type = Unsigned32
_TWredGreenStartAverage_Object = MibTableColumn
tWredGreenStartAverage = _TWredGreenStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 4),
    _TWredGreenStartAverage_Type()
)
tWredGreenStartAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWredGreenStartAverage.setStatus("current")
_TWredGreenMaxAverage_Type = Unsigned32
_TWredGreenMaxAverage_Object = MibTableColumn
tWredGreenMaxAverage = _TWredGreenMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 5),
    _TWredGreenMaxAverage_Type()
)
tWredGreenMaxAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWredGreenMaxAverage.setStatus("current")
_TWredGreenProbability_Type = Unsigned32
_TWredGreenProbability_Object = MibTableColumn
tWredGreenProbability = _TWredGreenProbability_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 6),
    _TWredGreenProbability_Type()
)
tWredGreenProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWredGreenProbability.setStatus("current")
_TWredYellowStartAverage_Type = Unsigned32
_TWredYellowStartAverage_Object = MibTableColumn
tWredYellowStartAverage = _TWredYellowStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 7),
    _TWredYellowStartAverage_Type()
)
tWredYellowStartAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWredYellowStartAverage.setStatus("current")
_TWredYellowMaxAverage_Type = Unsigned32
_TWredYellowMaxAverage_Object = MibTableColumn
tWredYellowMaxAverage = _TWredYellowMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 8),
    _TWredYellowMaxAverage_Type()
)
tWredYellowMaxAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWredYellowMaxAverage.setStatus("current")
_TWredYellowProbability_Type = Unsigned32
_TWredYellowProbability_Object = MibTableColumn
tWredYellowProbability = _TWredYellowProbability_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 9),
    _TWredYellowProbability_Type()
)
tWredYellowProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWredYellowProbability.setStatus("current")
_TWredRedStartAverage_Type = Unsigned32
_TWredRedStartAverage_Object = MibTableColumn
tWredRedStartAverage = _TWredRedStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 10),
    _TWredRedStartAverage_Type()
)
tWredRedStartAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWredRedStartAverage.setStatus("current")
_TWredRedMaxAverage_Type = Unsigned32
_TWredRedMaxAverage_Object = MibTableColumn
tWredRedMaxAverage = _TWredRedMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 11),
    _TWredRedMaxAverage_Type()
)
tWredRedMaxAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWredRedMaxAverage.setStatus("current")
_TWredRedProbability_Type = Unsigned32
_TWredRedProbability_Object = MibTableColumn
tWredRedProbability = _TWredRedProbability_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 12),
    _TWredRedProbability_Type()
)
tWredRedProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWredRedProbability.setStatus("current")
_TWredLastChanged_Type = TimeStamp
_TWredLastChanged_Object = MibTableColumn
tWredLastChanged = _TWredLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 7, 1, 1, 13),
    _TWredLastChanged_Type()
)
tWredLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tWredLastChanged.setStatus("current")
_TCongestionAvoidanceProfileObjects_ObjectIdentity = ObjectIdentity
tCongestionAvoidanceProfileObjects = _TCongestionAvoidanceProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8)
)
_QosTailDropProfileTable_Object = MibTable
qosTailDropProfileTable = _QosTailDropProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 1)
)
if mibBuilder.loadTexts:
    qosTailDropProfileTable.setStatus("current")
_QosTailDropProfileEntry_Object = MibTableRow
qosTailDropProfileEntry = _QosTailDropProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 1, 1)
)
qosTailDropProfileEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosTailDropProfile"),
)
if mibBuilder.loadTexts:
    qosTailDropProfileEntry.setStatus("current")


class _QosTailDropProfile_Type(TTailDropId):
    """Custom type qosTailDropProfile based on TTailDropId"""
    subtypeSpec = TTailDropId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_QosTailDropProfile_Type.__name__ = "TTailDropId"
_QosTailDropProfile_Object = MibTableColumn
qosTailDropProfile = _QosTailDropProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 1, 1, 1),
    _QosTailDropProfile_Type()
)
qosTailDropProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosTailDropProfile.setStatus("current")
_QosTailDropRowStatus_Type = RowStatus
_QosTailDropRowStatus_Object = MibTableColumn
qosTailDropRowStatus = _QosTailDropRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 1, 1, 2),
    _QosTailDropRowStatus_Type()
)
qosTailDropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTailDropRowStatus.setStatus("current")


class _QosMaxTailDropYellowTreshold_Type(TTreshold):
    """Custom type qosMaxTailDropYellowTreshold based on TTreshold"""
    defaultValue = 100


_QosMaxTailDropYellowTreshold_Type.__name__ = "TTreshold"
_QosMaxTailDropYellowTreshold_Object = MibTableColumn
qosMaxTailDropYellowTreshold = _QosMaxTailDropYellowTreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 1, 1, 3),
    _QosMaxTailDropYellowTreshold_Type()
)
qosMaxTailDropYellowTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMaxTailDropYellowTreshold.setStatus("current")


class _QosMaxTailDropRedTreshold_Type(TTreshold):
    """Custom type qosMaxTailDropRedTreshold based on TTreshold"""
    defaultValue = 100


_QosMaxTailDropRedTreshold_Type.__name__ = "TTreshold"
_QosMaxTailDropRedTreshold_Object = MibTableColumn
qosMaxTailDropRedTreshold = _QosMaxTailDropRedTreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 1, 1, 4),
    _QosMaxTailDropRedTreshold_Type()
)
qosMaxTailDropRedTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMaxTailDropRedTreshold.setStatus("current")
_QosSredProfileTable_Object = MibTable
qosSredProfileTable = _QosSredProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 2)
)
if mibBuilder.loadTexts:
    qosSredProfileTable.setStatus("current")
_QosSredProfileEntry_Object = MibTableRow
qosSredProfileEntry = _QosSredProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 2, 1)
)
qosSredProfileEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosTailDropProfile"),
)
if mibBuilder.loadTexts:
    qosSredProfileEntry.setStatus("current")


class _QosSredProfile_Type(TSredId):
    """Custom type qosSredProfile based on TSredId"""
    subtypeSpec = TSredId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_QosSredProfile_Type.__name__ = "TSredId"
_QosSredProfile_Object = MibTableColumn
qosSredProfile = _QosSredProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 2, 1, 1),
    _QosSredProfile_Type()
)
qosSredProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosSredProfile.setStatus("current")
_QosSredRowStatus_Type = RowStatus
_QosSredRowStatus_Object = MibTableColumn
qosSredRowStatus = _QosSredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 2, 1, 2),
    _QosSredRowStatus_Type()
)
qosSredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosSredRowStatus.setStatus("current")


class _QosMaxSredYellowTreshold_Type(TTreshold):
    """Custom type qosMaxSredYellowTreshold based on TTreshold"""
    defaultValue = 100


_QosMaxSredYellowTreshold_Type.__name__ = "TTreshold"
_QosMaxSredYellowTreshold_Object = MibTableColumn
qosMaxSredYellowTreshold = _QosMaxSredYellowTreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 2, 1, 3),
    _QosMaxSredYellowTreshold_Type()
)
qosMaxSredYellowTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMaxSredYellowTreshold.setStatus("current")


class _QosMaxSredYellowProbaility_Type(TTreshold):
    """Custom type qosMaxSredYellowProbaility based on TTreshold"""
    defaultValue = 100


_QosMaxSredYellowProbaility_Type.__name__ = "TTreshold"
_QosMaxSredYellowProbaility_Object = MibTableColumn
qosMaxSredYellowProbaility = _QosMaxSredYellowProbaility_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 2, 1, 4),
    _QosMaxSredYellowProbaility_Type()
)
qosMaxSredYellowProbaility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMaxSredYellowProbaility.setStatus("current")


class _QosMaxSredRedTreshold_Type(TTreshold):
    """Custom type qosMaxSredRedTreshold based on TTreshold"""
    defaultValue = 100


_QosMaxSredRedTreshold_Type.__name__ = "TTreshold"
_QosMaxSredRedTreshold_Object = MibTableColumn
qosMaxSredRedTreshold = _QosMaxSredRedTreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 2, 1, 5),
    _QosMaxSredRedTreshold_Type()
)
qosMaxSredRedTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMaxSredRedTreshold.setStatus("current")


class _QosMaxSredRedProbability_Type(TTreshold):
    """Custom type qosMaxSredRedProbability based on TTreshold"""
    defaultValue = 100


_QosMaxSredRedProbability_Type.__name__ = "TTreshold"
_QosMaxSredRedProbability_Object = MibTableColumn
qosMaxSredRedProbability = _QosMaxSredRedProbability_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 8, 2, 1, 6),
    _QosMaxSredRedProbability_Type()
)
qosMaxSredRedProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMaxSredRedProbability.setStatus("current")
_TShaperObjects_ObjectIdentity = ObjectIdentity
tShaperObjects = _TShaperObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9)
)
_TShaperProfileTable_Object = MibTable
tShaperProfileTable = _TShaperProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tShaperProfileTable.setStatus("current")
_TShaperProfileEntry_Object = MibTableRow
tShaperProfileEntry = _TShaperProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1)
)
tShaperProfileEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "tShaperProfileType"),
    (0, "PRVT-QOS-MIB", "tShaperProfile"),
    (0, "PRVT-QOS-MIB", "tShaperProfileDirection"),
    (0, "PRVT-QOS-MIB", "tShaperProfileLevel"),
)
if mibBuilder.loadTexts:
    tShaperProfileEntry.setStatus("current")


class _TShaperProfileType_Type(Integer32):
    """Custom type tShaperProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qos", 1),
          ("hqos", 2))
    )


_TShaperProfileType_Type.__name__ = "Integer32"
_TShaperProfileType_Object = MibTableColumn
tShaperProfileType = _TShaperProfileType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 1),
    _TShaperProfileType_Type()
)
tShaperProfileType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tShaperProfileType.setStatus("current")


class _TShaperProfile_Type(TShaperId):
    """Custom type tShaperProfile based on TShaperId"""
    subtypeSpec = TShaperId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 216),
    )


_TShaperProfile_Type.__name__ = "TShaperId"
_TShaperProfile_Object = MibTableColumn
tShaperProfile = _TShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 2),
    _TShaperProfile_Type()
)
tShaperProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tShaperProfile.setStatus("current")


class _TShaperProfileDirection_Type(Integer32):
    """Custom type tShaperProfileDirection based on Integer32"""
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
        *(("serviceIngress", 1),
          ("serviceEgress", 2),
          ("networkEgress", 3),
          ("vlanEgress", 4))
    )


_TShaperProfileDirection_Type.__name__ = "Integer32"
_TShaperProfileDirection_Object = MibTableColumn
tShaperProfileDirection = _TShaperProfileDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 3),
    _TShaperProfileDirection_Type()
)
tShaperProfileDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tShaperProfileDirection.setStatus("current")


class _TShaperProfileLevel_Type(Integer32):
    """Custom type tShaperProfileLevel based on Integer32"""
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
        *(("port", 1),
          ("queue", 2),
          ("l1Scheduler", 3),
          ("l2Scheduler", 4),
          ("qosPolicy", 5))
    )


_TShaperProfileLevel_Type.__name__ = "Integer32"
_TShaperProfileLevel_Object = MibTableColumn
tShaperProfileLevel = _TShaperProfileLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 4),
    _TShaperProfileLevel_Type()
)
tShaperProfileLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tShaperProfileLevel.setStatus("current")
_TShaperRowStatus_Type = RowStatus
_TShaperRowStatus_Object = MibTableColumn
tShaperRowStatus = _TShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 5),
    _TShaperRowStatus_Type()
)
tShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tShaperRowStatus.setStatus("current")


class _TShaperDescription_Type(TItemDescription):
    """Custom type tShaperDescription based on TItemDescription"""
    defaultHexValue = ""


_TShaperDescription_Type.__name__ = "TItemDescription"
_TShaperDescription_Object = MibTableColumn
tShaperDescription = _TShaperDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 6),
    _TShaperDescription_Type()
)
tShaperDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tShaperDescription.setStatus("current")


class _TShaperCIR_Type(TRateValue):
    """Custom type tShaperCIR based on TRateValue"""
    defaultValue = 0


_TShaperCIR_Type.__name__ = "TRateValue"
_TShaperCIR_Object = MibTableColumn
tShaperCIR = _TShaperCIR_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 7),
    _TShaperCIR_Type()
)
tShaperCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tShaperCIR.setStatus("current")


class _TShaperPIR_Type(TRateValue):
    """Custom type tShaperPIR based on TRateValue"""
    defaultValue = 100


_TShaperPIR_Type.__name__ = "TRateValue"
_TShaperPIR_Object = MibTableColumn
tShaperPIR = _TShaperPIR_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 8),
    _TShaperPIR_Type()
)
tShaperPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tShaperPIR.setStatus("current")


class _TShaperCBS_Type(Integer32):
    """Custom type tShaperCBS based on Integer32"""
    defaultValue = 0


_TShaperCBS_Type.__name__ = "Integer32"
_TShaperCBS_Object = MibTableColumn
tShaperCBS = _TShaperCBS_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 9),
    _TShaperCBS_Type()
)
tShaperCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tShaperCBS.setStatus("current")


class _TShaperMBS_Type(Integer32):
    """Custom type tShaperMBS based on Integer32"""
    defaultValue = 6000


_TShaperMBS_Type.__name__ = "Integer32"
_TShaperMBS_Object = MibTableColumn
tShaperMBS = _TShaperMBS_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 10),
    _TShaperMBS_Type()
)
tShaperMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tShaperMBS.setStatus("current")
_TShaperLastChanged_Type = TimeStamp
_TShaperLastChanged_Object = MibTableColumn
tShaperLastChanged = _TShaperLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 9, 1, 1, 11),
    _TShaperLastChanged_Type()
)
tShaperLastChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tShaperLastChanged.setStatus("current")
_TWfqObjects_ObjectIdentity = ObjectIdentity
tWfqObjects = _TWfqObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10)
)
_TWfqServiceProfileTable_Object = MibTable
tWfqServiceProfileTable = _TWfqServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tWfqServiceProfileTable.setStatus("current")
_TWfqServiceProfileEntry_Object = MibTableRow
tWfqServiceProfileEntry = _TWfqServiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 1, 1)
)
tWfqServiceProfileEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "tWfqServiceProfileNumber"),
    (0, "PRVT-QOS-MIB", "tWfqServiceProfileDirection"),
)
if mibBuilder.loadTexts:
    tWfqServiceProfileEntry.setStatus("current")


class _TWfqServiceProfileNumber_Type(Integer32):
    """Custom type tWfqServiceProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61),
    )


_TWfqServiceProfileNumber_Type.__name__ = "Integer32"
_TWfqServiceProfileNumber_Object = MibTableColumn
tWfqServiceProfileNumber = _TWfqServiceProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 1, 1, 1),
    _TWfqServiceProfileNumber_Type()
)
tWfqServiceProfileNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tWfqServiceProfileNumber.setStatus("current")


class _TWfqServiceProfileDirection_Type(Integer32):
    """Custom type tWfqServiceProfileDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ingress", 1),
          ("egress", 2))
    )


_TWfqServiceProfileDirection_Type.__name__ = "Integer32"
_TWfqServiceProfileDirection_Object = MibTableColumn
tWfqServiceProfileDirection = _TWfqServiceProfileDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 1, 1, 2),
    _TWfqServiceProfileDirection_Type()
)
tWfqServiceProfileDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tWfqServiceProfileDirection.setStatus("current")
_TWfqServiceProfileRowStatus_Type = RowStatus
_TWfqServiceProfileRowStatus_Object = MibTableColumn
tWfqServiceProfileRowStatus = _TWfqServiceProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 1, 1, 3),
    _TWfqServiceProfileRowStatus_Type()
)
tWfqServiceProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tWfqServiceProfileRowStatus.setStatus("current")
_TWfqServiceProfileWeight_Type = Integer32
_TWfqServiceProfileWeight_Object = MibTableColumn
tWfqServiceProfileWeight = _TWfqServiceProfileWeight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 1, 1, 4),
    _TWfqServiceProfileWeight_Type()
)
tWfqServiceProfileWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWfqServiceProfileWeight.setStatus("current")
_TWfqNetworkProfileTable_Object = MibTable
tWfqNetworkProfileTable = _TWfqNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 2)
)
if mibBuilder.loadTexts:
    tWfqNetworkProfileTable.setStatus("current")
_TWfqNetworkProfileEntry_Object = MibTableRow
tWfqNetworkProfileEntry = _TWfqNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 2, 1)
)
tWfqNetworkProfileEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "tWfqNetworkProfileNumber"),
)
if mibBuilder.loadTexts:
    tWfqNetworkProfileEntry.setStatus("current")


class _TWfqNetworkProfileNumber_Type(Integer32):
    """Custom type tWfqNetworkProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TWfqNetworkProfileNumber_Type.__name__ = "Integer32"
_TWfqNetworkProfileNumber_Object = MibTableColumn
tWfqNetworkProfileNumber = _TWfqNetworkProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 2, 1, 1),
    _TWfqNetworkProfileNumber_Type()
)
tWfqNetworkProfileNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tWfqNetworkProfileNumber.setStatus("current")
_TWfqNetworkProfileRowStatus_Type = RowStatus
_TWfqNetworkProfileRowStatus_Object = MibTableColumn
tWfqNetworkProfileRowStatus = _TWfqNetworkProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 2, 1, 2),
    _TWfqNetworkProfileRowStatus_Type()
)
tWfqNetworkProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tWfqNetworkProfileRowStatus.setStatus("current")


class _TWfqNetworkProfileWeight_Type(Integer32):
    """Custom type tWfqNetworkProfileWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 220),
    )


_TWfqNetworkProfileWeight_Type.__name__ = "Integer32"
_TWfqNetworkProfileWeight_Object = MibTableColumn
tWfqNetworkProfileWeight = _TWfqNetworkProfileWeight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 2, 1, 3),
    _TWfqNetworkProfileWeight_Type()
)
tWfqNetworkProfileWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWfqNetworkProfileWeight.setStatus("current")


class _TWfqNetworkProfileCIRWeight_Type(Integer32):
    """Custom type tWfqNetworkProfileCIRWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 220),
    )


_TWfqNetworkProfileCIRWeight_Type.__name__ = "Integer32"
_TWfqNetworkProfileCIRWeight_Object = MibTableColumn
tWfqNetworkProfileCIRWeight = _TWfqNetworkProfileCIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 2, 1, 4),
    _TWfqNetworkProfileCIRWeight_Type()
)
tWfqNetworkProfileCIRWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWfqNetworkProfileCIRWeight.setStatus("current")
_TWfqSchedulerProfileTable_Object = MibTable
tWfqSchedulerProfileTable = _TWfqSchedulerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 3)
)
if mibBuilder.loadTexts:
    tWfqSchedulerProfileTable.setStatus("current")
_TWfqSchedulerProfileEntry_Object = MibTableRow
tWfqSchedulerProfileEntry = _TWfqSchedulerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 3, 1)
)
tWfqSchedulerProfileEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "tWfqSchedulerProfileNumber"),
    (0, "PRVT-QOS-MIB", "tWfqSchedulerProfileDirection"),
)
if mibBuilder.loadTexts:
    tWfqSchedulerProfileEntry.setStatus("current")


class _TWfqSchedulerProfileNumber_Type(Integer32):
    """Custom type tWfqSchedulerProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_TWfqSchedulerProfileNumber_Type.__name__ = "Integer32"
_TWfqSchedulerProfileNumber_Object = MibTableColumn
tWfqSchedulerProfileNumber = _TWfqSchedulerProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 3, 1, 1),
    _TWfqSchedulerProfileNumber_Type()
)
tWfqSchedulerProfileNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tWfqSchedulerProfileNumber.setStatus("current")


class _TWfqSchedulerProfileDirection_Type(Integer32):
    """Custom type tWfqSchedulerProfileDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ingress", 1),
          ("egress", 2))
    )


_TWfqSchedulerProfileDirection_Type.__name__ = "Integer32"
_TWfqSchedulerProfileDirection_Object = MibTableColumn
tWfqSchedulerProfileDirection = _TWfqSchedulerProfileDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 3, 1, 2),
    _TWfqSchedulerProfileDirection_Type()
)
tWfqSchedulerProfileDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tWfqSchedulerProfileDirection.setStatus("current")
_TWfqSchedulerProfileRowStatus_Type = RowStatus
_TWfqSchedulerProfileRowStatus_Object = MibTableColumn
tWfqSchedulerProfileRowStatus = _TWfqSchedulerProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 3, 1, 3),
    _TWfqSchedulerProfileRowStatus_Type()
)
tWfqSchedulerProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tWfqSchedulerProfileRowStatus.setStatus("current")


class _TWfqSchedulerProfileWeight_Type(Integer32):
    """Custom type tWfqSchedulerProfileWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 220),
    )


_TWfqSchedulerProfileWeight_Type.__name__ = "Integer32"
_TWfqSchedulerProfileWeight_Object = MibTableColumn
tWfqSchedulerProfileWeight = _TWfqSchedulerProfileWeight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 3, 1, 4),
    _TWfqSchedulerProfileWeight_Type()
)
tWfqSchedulerProfileWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWfqSchedulerProfileWeight.setStatus("current")


class _TWfqSchedulerProfileCIRWeight_Type(Integer32):
    """Custom type tWfqSchedulerProfileCIRWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 220),
    )


_TWfqSchedulerProfileCIRWeight_Type.__name__ = "Integer32"
_TWfqSchedulerProfileCIRWeight_Object = MibTableColumn
tWfqSchedulerProfileCIRWeight = _TWfqSchedulerProfileCIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 10, 3, 1, 5),
    _TWfqSchedulerProfileCIRWeight_Type()
)
tWfqSchedulerProfileCIRWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tWfqSchedulerProfileCIRWeight.setStatus("current")
_QosSchedulingProfileObjects_ObjectIdentity = ObjectIdentity
qosSchedulingProfileObjects = _QosSchedulingProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11)
)
_QosSchedulingProfileTable_Object = MibTable
qosSchedulingProfileTable = _QosSchedulingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1)
)
if mibBuilder.loadTexts:
    qosSchedulingProfileTable.setStatus("current")
_QosSchedulingProfileEntry_Object = MibTableRow
qosSchedulingProfileEntry = _QosSchedulingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1)
)
qosSchedulingProfileEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosSchedulingProfile"),
    (0, "PRVT-QOS-MIB", "qosSchedulingProfileDirection"),
    (0, "PRVT-QOS-MIB", "qosSchedulingType"),
)
if mibBuilder.loadTexts:
    qosSchedulingProfileEntry.setStatus("current")


class _QosSchedulingProfile_Type(Integer32):
    """Custom type qosSchedulingProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_QosSchedulingProfile_Type.__name__ = "Integer32"
_QosSchedulingProfile_Object = MibTableColumn
qosSchedulingProfile = _QosSchedulingProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 1),
    _QosSchedulingProfile_Type()
)
qosSchedulingProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosSchedulingProfile.setStatus("current")


class _QosSchedulingProfileDirection_Type(Integer32):
    """Custom type qosSchedulingProfileDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ingress", 1),
          ("egress", 2))
    )


_QosSchedulingProfileDirection_Type.__name__ = "Integer32"
_QosSchedulingProfileDirection_Object = MibTableColumn
qosSchedulingProfileDirection = _QosSchedulingProfileDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 2),
    _QosSchedulingProfileDirection_Type()
)
qosSchedulingProfileDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosSchedulingProfileDirection.setStatus("current")


class _QosSchedulingType_Type(Integer32):
    """Custom type qosSchedulingType based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("wrr", 2),
          ("hybrid-1", 3),
          ("hybrid-2", 4),
          ("hybrid-3", 5),
          ("hybrid-4", 6),
          ("hybrid-5", 7),
          ("hybrid-6", 8),
          ("drr", 9),
          ("mdrr-1", 10),
          ("mdrr-2", 11),
          ("mdrr-3", 12),
          ("mdrr-4", 13),
          ("mdrr-5", 14),
          ("mdrr-6", 15))
    )


_QosSchedulingType_Type.__name__ = "Integer32"
_QosSchedulingType_Object = MibTableColumn
qosSchedulingType = _QosSchedulingType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 3),
    _QosSchedulingType_Type()
)
qosSchedulingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosSchedulingType.setStatus("current")
_QosSchedulingRowStatus_Type = RowStatus
_QosSchedulingRowStatus_Object = MibTableColumn
qosSchedulingRowStatus = _QosSchedulingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 4),
    _QosSchedulingRowStatus_Type()
)
qosSchedulingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosSchedulingRowStatus.setStatus("current")
_QosSchedulingQ1Weight_Type = Integer32
_QosSchedulingQ1Weight_Object = MibTableColumn
qosSchedulingQ1Weight = _QosSchedulingQ1Weight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 5),
    _QosSchedulingQ1Weight_Type()
)
qosSchedulingQ1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSchedulingQ1Weight.setStatus("current")
_QosSchedulingQ2Weight_Type = Integer32
_QosSchedulingQ2Weight_Object = MibTableColumn
qosSchedulingQ2Weight = _QosSchedulingQ2Weight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 6),
    _QosSchedulingQ2Weight_Type()
)
qosSchedulingQ2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSchedulingQ2Weight.setStatus("current")
_QosSchedulingQ3Weight_Type = Integer32
_QosSchedulingQ3Weight_Object = MibTableColumn
qosSchedulingQ3Weight = _QosSchedulingQ3Weight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 7),
    _QosSchedulingQ3Weight_Type()
)
qosSchedulingQ3Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSchedulingQ3Weight.setStatus("current")
_QosSchedulingQ4Weight_Type = Integer32
_QosSchedulingQ4Weight_Object = MibTableColumn
qosSchedulingQ4Weight = _QosSchedulingQ4Weight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 8),
    _QosSchedulingQ4Weight_Type()
)
qosSchedulingQ4Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSchedulingQ4Weight.setStatus("current")
_QosSchedulingQ5Weight_Type = Integer32
_QosSchedulingQ5Weight_Object = MibTableColumn
qosSchedulingQ5Weight = _QosSchedulingQ5Weight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 9),
    _QosSchedulingQ5Weight_Type()
)
qosSchedulingQ5Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSchedulingQ5Weight.setStatus("current")
_QosSchedulingQ6Weight_Type = Integer32
_QosSchedulingQ6Weight_Object = MibTableColumn
qosSchedulingQ6Weight = _QosSchedulingQ6Weight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 10),
    _QosSchedulingQ6Weight_Type()
)
qosSchedulingQ6Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSchedulingQ6Weight.setStatus("current")
_QosSchedulingQ7Weight_Type = Integer32
_QosSchedulingQ7Weight_Object = MibTableColumn
qosSchedulingQ7Weight = _QosSchedulingQ7Weight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 11),
    _QosSchedulingQ7Weight_Type()
)
qosSchedulingQ7Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSchedulingQ7Weight.setStatus("current")
_QosSchedulingQ8Weight_Type = Integer32
_QosSchedulingQ8Weight_Object = MibTableColumn
qosSchedulingQ8Weight = _QosSchedulingQ8Weight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 11, 1, 1, 12),
    _QosSchedulingQ8Weight_Type()
)
qosSchedulingQ8Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSchedulingQ8Weight.setStatus("current")
_QosServicePolicyObjects_ObjectIdentity = ObjectIdentity
qosServicePolicyObjects = _QosServicePolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12)
)
_QosServicePolicyTable_Object = MibTable
qosServicePolicyTable = _QosServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 1)
)
if mibBuilder.loadTexts:
    qosServicePolicyTable.setStatus("current")
_QosServicePolicyEntry_Object = MibTableRow
qosServicePolicyEntry = _QosServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 1, 1)
)
qosServicePolicyEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosServicePolicy"),
)
if mibBuilder.loadTexts:
    qosServicePolicyEntry.setStatus("current")
_QosServicePolicy_Type = TNamedItem
_QosServicePolicy_Object = MibTableColumn
qosServicePolicy = _QosServicePolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 1, 1, 1),
    _QosServicePolicy_Type()
)
qosServicePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosServicePolicy.setStatus("current")
_QosServicePolicyRowStatus_Type = RowStatus
_QosServicePolicyRowStatus_Object = MibTableColumn
qosServicePolicyRowStatus = _QosServicePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 1, 1, 2),
    _QosServicePolicyRowStatus_Type()
)
qosServicePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosServicePolicyRowStatus.setStatus("current")


class _QosServicePolicyDescription_Type(TItemDescription):
    """Custom type qosServicePolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_QosServicePolicyDescription_Type.__name__ = "TItemDescription"
_QosServicePolicyDescription_Object = MibTableColumn
qosServicePolicyDescription = _QosServicePolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 1, 1, 3),
    _QosServicePolicyDescription_Type()
)
qosServicePolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosServicePolicyDescription.setStatus("current")
_QosServiceIngressPolicyTable_Object = MibTable
qosServiceIngressPolicyTable = _QosServiceIngressPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 2)
)
if mibBuilder.loadTexts:
    qosServiceIngressPolicyTable.setStatus("current")
_QosServiceIngressPolicyEntry_Object = MibTableRow
qosServiceIngressPolicyEntry = _QosServiceIngressPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 2, 1)
)
qosServiceIngressPolicyEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosServicePolicy"),
)
if mibBuilder.loadTexts:
    qosServiceIngressPolicyEntry.setStatus("current")
_QosServPolicyShaperProfile_Type = TShaperId
_QosServPolicyShaperProfile_Object = MibTableColumn
qosServPolicyShaperProfile = _QosServPolicyShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 2, 1, 1),
    _QosServPolicyShaperProfile_Type()
)
qosServPolicyShaperProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosServPolicyShaperProfile.setStatus("current")
_QosServPolicySchedulingProfile_Type = TSSchedulingProfile
_QosServPolicySchedulingProfile_Object = MibTableColumn
qosServPolicySchedulingProfile = _QosServPolicySchedulingProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 2, 1, 2),
    _QosServPolicySchedulingProfile_Type()
)
qosServPolicySchedulingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosServPolicySchedulingProfile.setStatus("current")
_QosServPolicyTailDropProfile_Type = TTailDropId
_QosServPolicyTailDropProfile_Object = MibTableColumn
qosServPolicyTailDropProfile = _QosServPolicyTailDropProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 2, 1, 3),
    _QosServPolicyTailDropProfile_Type()
)
qosServPolicyTailDropProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosServPolicyTailDropProfile.setStatus("current")
_QosServiceIngressQueueTable_Object = MibTable
qosServiceIngressQueueTable = _QosServiceIngressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 3)
)
if mibBuilder.loadTexts:
    qosServiceIngressQueueTable.setStatus("current")
_QosServiceIngressQueueEntry_Object = MibTableRow
qosServiceIngressQueueEntry = _QosServiceIngressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 3, 1)
)
qosServiceIngressQueueEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosServicePolicy"),
)
if mibBuilder.loadTexts:
    qosServiceIngressQueueEntry.setStatus("current")


class _QosServInQueueQueue_Type(TQueueId):
    """Custom type qosServInQueueQueue based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QosServInQueueQueue_Type.__name__ = "TQueueId"
_QosServInQueueQueue_Object = MibTableColumn
qosServInQueueQueue = _QosServInQueueQueue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 3, 1, 1),
    _QosServInQueueQueue_Type()
)
qosServInQueueQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosServInQueueQueue.setStatus("current")
_QosServInQueueRowStatus_Type = RowStatus
_QosServInQueueRowStatus_Object = MibTableColumn
qosServInQueueRowStatus = _QosServInQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 3, 1, 2),
    _QosServInQueueRowStatus_Type()
)
qosServInQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosServInQueueRowStatus.setStatus("current")
_QosServInQueueShaperProfile_Type = TShaperId
_QosServInQueueShaperProfile_Object = MibTableColumn
qosServInQueueShaperProfile = _QosServInQueueShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 3, 1, 3),
    _QosServInQueueShaperProfile_Type()
)
qosServInQueueShaperProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosServInQueueShaperProfile.setStatus("current")
_QosServInQueueTailDropProfile_Type = TTailDropId
_QosServInQueueTailDropProfile_Object = MibTableColumn
qosServInQueueTailDropProfile = _QosServInQueueTailDropProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 12, 3, 1, 4),
    _QosServInQueueTailDropProfile_Type()
)
qosServInQueueTailDropProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosServInQueueTailDropProfile.setStatus("current")
_QosNetworkPolicyObjects_ObjectIdentity = ObjectIdentity
qosNetworkPolicyObjects = _QosNetworkPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13)
)
_QosNetworkPolicyTable_Object = MibTable
qosNetworkPolicyTable = _QosNetworkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 1)
)
if mibBuilder.loadTexts:
    qosNetworkPolicyTable.setStatus("current")
_QosNetworkPolicyEntry_Object = MibTableRow
qosNetworkPolicyEntry = _QosNetworkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 1, 1)
)
qosNetworkPolicyEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosNetworkPolicy"),
)
if mibBuilder.loadTexts:
    qosNetworkPolicyEntry.setStatus("current")
_QosNetworkPolicy_Type = TNamedItem
_QosNetworkPolicy_Object = MibTableColumn
qosNetworkPolicy = _QosNetworkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 1, 1, 1),
    _QosNetworkPolicy_Type()
)
qosNetworkPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosNetworkPolicy.setStatus("current")
_QosNetworkPolicyRowStatus_Type = RowStatus
_QosNetworkPolicyRowStatus_Object = MibTableColumn
qosNetworkPolicyRowStatus = _QosNetworkPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 1, 1, 2),
    _QosNetworkPolicyRowStatus_Type()
)
qosNetworkPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosNetworkPolicyRowStatus.setStatus("current")


class _QosNetworkPolicyDescription_Type(TItemDescription):
    """Custom type qosNetworkPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_QosNetworkPolicyDescription_Type.__name__ = "TItemDescription"
_QosNetworkPolicyDescription_Object = MibTableColumn
qosNetworkPolicyDescription = _QosNetworkPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 1, 1, 3),
    _QosNetworkPolicyDescription_Type()
)
qosNetworkPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNetworkPolicyDescription.setStatus("current")
_QosNetworkIngressTable_Object = MibTable
qosNetworkIngressTable = _QosNetworkIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 2)
)
if mibBuilder.loadTexts:
    qosNetworkIngressTable.setStatus("current")
_QosNetworkIngressEntry_Object = MibTableRow
qosNetworkIngressEntry = _QosNetworkIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 2, 1)
)
qosNetworkIngressEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosNetworkPolicy"),
)
if mibBuilder.loadTexts:
    qosNetworkIngressEntry.setStatus("current")
_QosNetworkIngressFC_Type = TFCNameOrEmpty
_QosNetworkIngressFC_Object = MibTableColumn
qosNetworkIngressFC = _QosNetworkIngressFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 2, 1, 1),
    _QosNetworkIngressFC_Type()
)
qosNetworkIngressFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNetworkIngressFC.setStatus("current")
_QosNetworkIngressConformance_Type = TConformanceLevel
_QosNetworkIngressConformance_Object = MibTableColumn
qosNetworkIngressConformance = _QosNetworkIngressConformance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 2, 1, 2),
    _QosNetworkIngressConformance_Type()
)
qosNetworkIngressConformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNetworkIngressConformance.setStatus("current")
_QosTrustDot1pMode_Type = TruthValue
_QosTrustDot1pMode_Object = MibTableColumn
qosTrustDot1pMode = _QosTrustDot1pMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 2, 1, 3),
    _QosTrustDot1pMode_Type()
)
qosTrustDot1pMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrustDot1pMode.setStatus("current")
_QosTrustDot1pModePreservePriority_Type = TruthValue
_QosTrustDot1pModePreservePriority_Object = MibTableColumn
qosTrustDot1pModePreservePriority = _QosTrustDot1pModePreservePriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 2, 1, 4),
    _QosTrustDot1pModePreservePriority_Type()
)
qosTrustDot1pModePreservePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrustDot1pModePreservePriority.setStatus("current")
_QosTrustDscpMode_Type = TruthValue
_QosTrustDscpMode_Object = MibTableColumn
qosTrustDscpMode = _QosTrustDscpMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 2, 1, 5),
    _QosTrustDscpMode_Type()
)
qosTrustDscpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrustDscpMode.setStatus("current")
_QosNetworkEgressTable_Object = MibTable
qosNetworkEgressTable = _QosNetworkEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 3)
)
if mibBuilder.loadTexts:
    qosNetworkEgressTable.setStatus("current")
_QosNetworkEgressEntry_Object = MibTableRow
qosNetworkEgressEntry = _QosNetworkEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 3, 1)
)
qosNetworkEgressEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosNetworkPolicy"),
)
if mibBuilder.loadTexts:
    qosNetworkEgressEntry.setStatus("current")
_QosNetPolicySchedulingProfile_Type = TSSchedulingProfile
_QosNetPolicySchedulingProfile_Object = MibTableColumn
qosNetPolicySchedulingProfile = _QosNetPolicySchedulingProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 3, 1, 1),
    _QosNetPolicySchedulingProfile_Type()
)
qosNetPolicySchedulingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNetPolicySchedulingProfile.setStatus("current")
_QosNetPolicyShaperProfile_Type = TShaperId
_QosNetPolicyShaperProfile_Object = MibTableColumn
qosNetPolicyShaperProfile = _QosNetPolicyShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 3, 1, 2),
    _QosNetPolicyShaperProfile_Type()
)
qosNetPolicyShaperProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNetPolicyShaperProfile.setStatus("current")
_QosNetPolicyTailDropProfile_Type = TTailDropId
_QosNetPolicyTailDropProfile_Object = MibTableColumn
qosNetPolicyTailDropProfile = _QosNetPolicyTailDropProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 3, 1, 3),
    _QosNetPolicyTailDropProfile_Type()
)
qosNetPolicyTailDropProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNetPolicyTailDropProfile.setStatus("current")
_QosNetPolicySredProfile_Type = TSredId
_QosNetPolicySredProfile_Object = MibTableColumn
qosNetPolicySredProfile = _QosNetPolicySredProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 3, 1, 4),
    _QosNetPolicySredProfile_Type()
)
qosNetPolicySredProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNetPolicySredProfile.setStatus("current")
_QosNetworkEgressQueueTable_Object = MibTable
qosNetworkEgressQueueTable = _QosNetworkEgressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 4)
)
if mibBuilder.loadTexts:
    qosNetworkEgressQueueTable.setStatus("current")
_QosNetworkEgressQueueEntry_Object = MibTableRow
qosNetworkEgressQueueEntry = _QosNetworkEgressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 4, 1)
)
qosNetworkEgressQueueEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosNetworkPolicy"),
    (0, "PRVT-QOS-MIB", "qosNetworkQueue"),
)
if mibBuilder.loadTexts:
    qosNetworkEgressQueueEntry.setStatus("current")


class _QosNetworkQueue_Type(TQueueId):
    """Custom type qosNetworkQueue based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QosNetworkQueue_Type.__name__ = "TQueueId"
_QosNetworkQueue_Object = MibTableColumn
qosNetworkQueue = _QosNetworkQueue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 4, 1, 1),
    _QosNetworkQueue_Type()
)
qosNetworkQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosNetworkQueue.setStatus("current")
_QosNetworkQueueRowStatus_Type = RowStatus
_QosNetworkQueueRowStatus_Object = MibTableColumn
qosNetworkQueueRowStatus = _QosNetworkQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 4, 1, 2),
    _QosNetworkQueueRowStatus_Type()
)
qosNetworkQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosNetworkQueueRowStatus.setStatus("current")
_QosNetworkQueueShaperProfile_Type = TShaperId
_QosNetworkQueueShaperProfile_Object = MibTableColumn
qosNetworkQueueShaperProfile = _QosNetworkQueueShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 4, 1, 3),
    _QosNetworkQueueShaperProfile_Type()
)
qosNetworkQueueShaperProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNetworkQueueShaperProfile.setStatus("current")
_QosNetworkQueueTailDropProfile_Type = TTailDropId
_QosNetworkQueueTailDropProfile_Object = MibTableColumn
qosNetworkQueueTailDropProfile = _QosNetworkQueueTailDropProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 4, 1, 4),
    _QosNetworkQueueTailDropProfile_Type()
)
qosNetworkQueueTailDropProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNetworkQueueTailDropProfile.setStatus("current")
_QosNetworkQueueSredProfile_Type = TSredId
_QosNetworkQueueSredProfile_Object = MibTableColumn
qosNetworkQueueSredProfile = _QosNetworkQueueSredProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 13, 4, 1, 5),
    _QosNetworkQueueSredProfile_Type()
)
qosNetworkQueueSredProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNetworkQueueSredProfile.setStatus("current")
_QosGlobalObjects_ObjectIdentity = ObjectIdentity
qosGlobalObjects = _QosGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14)
)
_QosGlobalIngressMapTable_Object = MibTable
qosGlobalIngressMapTable = _QosGlobalIngressMapTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 1)
)
if mibBuilder.loadTexts:
    qosGlobalIngressMapTable.setStatus("current")
_QosGlobalIngressMapEntry_Object = MibTableRow
qosGlobalIngressMapEntry = _QosGlobalIngressMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 1, 1)
)
qosGlobalIngressMapEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosIngressMapType"),
    (0, "PRVT-QOS-MIB", "qosIngressMapValue"),
)
if mibBuilder.loadTexts:
    qosGlobalIngressMapEntry.setStatus("current")


class _QosIngressMapType_Type(Integer32):
    """Custom type qosIngressMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1p", 1),
          ("dscp", 2))
    )


_QosIngressMapType_Type.__name__ = "Integer32"
_QosIngressMapType_Object = MibTableColumn
qosIngressMapType = _QosIngressMapType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 1, 1, 1),
    _QosIngressMapType_Type()
)
qosIngressMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIngressMapType.setStatus("current")


class _QosIngressMapValue_Type(Integer32):
    """Custom type qosIngressMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_QosIngressMapValue_Type.__name__ = "Integer32"
_QosIngressMapValue_Object = MibTableColumn
qosIngressMapValue = _QosIngressMapValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 1, 1, 2),
    _QosIngressMapValue_Type()
)
qosIngressMapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIngressMapValue.setStatus("current")
_QosIngressRowStatus_Type = RowStatus
_QosIngressRowStatus_Object = MibTableColumn
qosIngressRowStatus = _QosIngressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 1, 1, 3),
    _QosIngressRowStatus_Type()
)
qosIngressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIngressRowStatus.setStatus("current")
_QosIngressFC_Type = TFCNameOrEmpty
_QosIngressFC_Object = MibTableColumn
qosIngressFC = _QosIngressFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 1, 1, 4),
    _QosIngressFC_Type()
)
qosIngressFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosIngressFC.setStatus("current")
_QosIngressFCConformance_Type = TConformanceLevel
_QosIngressFCConformance_Object = MibTableColumn
qosIngressFCConformance = _QosIngressFCConformance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 1, 1, 5),
    _QosIngressFCConformance_Type()
)
qosIngressFCConformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosIngressFCConformance.setStatus("current")
_QosGlobalEgressRemarkTable_Object = MibTable
qosGlobalEgressRemarkTable = _QosGlobalEgressRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 2)
)
if mibBuilder.loadTexts:
    qosGlobalEgressRemarkTable.setStatus("current")
_QosGlobalEgressRemarkEntry_Object = MibTableRow
qosGlobalEgressRemarkEntry = _QosGlobalEgressRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 2, 1)
)
qosGlobalEgressRemarkEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosEgressFC"),
    (0, "PRVT-QOS-MIB", "qosEgressFCConformance"),
)
if mibBuilder.loadTexts:
    qosGlobalEgressRemarkEntry.setStatus("current")
_QosEgressFC_Type = TFCNameOrEmpty
_QosEgressFC_Object = MibTableColumn
qosEgressFC = _QosEgressFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 2, 1, 1),
    _QosEgressFC_Type()
)
qosEgressFC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosEgressFC.setStatus("current")
_QosEgressFCConformance_Type = TConformanceLevel
_QosEgressFCConformance_Object = MibTableColumn
qosEgressFCConformance = _QosEgressFCConformance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 2, 1, 2),
    _QosEgressFCConformance_Type()
)
qosEgressFCConformance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosEgressFCConformance.setStatus("current")
_QosEgressRowStatus_Type = RowStatus
_QosEgressRowStatus_Object = MibTableColumn
qosEgressRowStatus = _QosEgressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 2, 1, 3),
    _QosEgressRowStatus_Type()
)
qosEgressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosEgressRowStatus.setStatus("current")


class _QosEgressRemarkType_Type(Integer32):
    """Custom type qosEgressRemarkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1p", 1),
          ("dscp", 2))
    )


_QosEgressRemarkType_Type.__name__ = "Integer32"
_QosEgressRemarkType_Object = MibTableColumn
qosEgressRemarkType = _QosEgressRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 2, 1, 4),
    _QosEgressRemarkType_Type()
)
qosEgressRemarkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEgressRemarkType.setStatus("current")


class _QosEgressRemarkValue_Type(Integer32):
    """Custom type qosEgressRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_QosEgressRemarkValue_Type.__name__ = "Integer32"
_QosEgressRemarkValue_Object = MibTableColumn
qosEgressRemarkValue = _QosEgressRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 14, 2, 1, 5),
    _QosEgressRemarkValue_Type()
)
qosEgressRemarkValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEgressRemarkValue.setStatus("current")
_QosServiceObjects_ObjectIdentity = ObjectIdentity
qosServiceObjects = _QosServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15)
)
_QosServiceTable_Object = MibTable
qosServiceTable = _QosServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 1)
)
if mibBuilder.loadTexts:
    qosServiceTable.setStatus("current")
_QosServiceEntry_Object = MibTableRow
qosServiceEntry = _QosServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 1, 1)
)
qosServiceEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosServiceIndex"),
)
if mibBuilder.loadTexts:
    qosServiceEntry.setStatus("current")


class _QosServiceIndex_Type(Integer32):
    """Custom type qosServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QosServiceIndex_Type.__name__ = "Integer32"
_QosServiceIndex_Object = MibTableColumn
qosServiceIndex = _QosServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 1, 1, 1),
    _QosServiceIndex_Type()
)
qosServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosServiceIndex.setStatus("current")
_QosServiceRowStatus_Type = RowStatus
_QosServiceRowStatus_Object = MibTableColumn
qosServiceRowStatus = _QosServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 1, 1, 2),
    _QosServiceRowStatus_Type()
)
qosServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosServiceRowStatus.setStatus("current")
_QosServicePolicyOnServ_Type = TNamedItem
_QosServicePolicyOnServ_Object = MibTableColumn
qosServicePolicyOnServ = _QosServicePolicyOnServ_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 1, 1, 3),
    _QosServicePolicyOnServ_Type()
)
qosServicePolicyOnServ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosServicePolicyOnServ.setStatus("current")
_QosServiceSapTable_Object = MibTable
qosServiceSapTable = _QosServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 2)
)
if mibBuilder.loadTexts:
    qosServiceSapTable.setStatus("current")
_QosServiceSapEntry_Object = MibTableRow
qosServiceSapEntry = _QosServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 2, 1)
)
qosServiceSapEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosServiceIndex"),
    (0, "PRVT-QOS-MIB", "qosServiceSapPortId"),
    (0, "PRVT-QOS-MIB", "qosServiceSapEncapValue"),
)
if mibBuilder.loadTexts:
    qosServiceSapEntry.setStatus("current")


class _QosServiceSapPortId_Type(Integer32):
    """Custom type qosServiceSapPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QosServiceSapPortId_Type.__name__ = "Integer32"
_QosServiceSapPortId_Object = MibTableColumn
qosServiceSapPortId = _QosServiceSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 2, 1, 1),
    _QosServiceSapPortId_Type()
)
qosServiceSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosServiceSapPortId.setStatus("current")
_QosServiceSapEncapValue_Type = TQEncapVal
_QosServiceSapEncapValue_Object = MibTableColumn
qosServiceSapEncapValue = _QosServiceSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 2, 1, 2),
    _QosServiceSapEncapValue_Type()
)
qosServiceSapEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosServiceSapEncapValue.setStatus("current")
_QosServiceSapRowStatus_Type = RowStatus
_QosServiceSapRowStatus_Object = MibTableColumn
qosServiceSapRowStatus = _QosServiceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 2, 1, 3),
    _QosServiceSapRowStatus_Type()
)
qosServiceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosServiceSapRowStatus.setStatus("current")
_QosServiceSapPolicyEnable_Type = TruthValue
_QosServiceSapPolicyEnable_Object = MibTableColumn
qosServiceSapPolicyEnable = _QosServiceSapPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 15, 2, 1, 4),
    _QosServiceSapPolicyEnable_Type()
)
qosServiceSapPolicyEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosServiceSapPolicyEnable.setStatus("current")
_QosInterfaceObjects_ObjectIdentity = ObjectIdentity
qosInterfaceObjects = _QosInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 16)
)
_QosInterfaceTable_Object = MibTable
qosInterfaceTable = _QosInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 16, 1)
)
if mibBuilder.loadTexts:
    qosInterfaceTable.setStatus("current")
_QosInterfaceEntry_Object = MibTableRow
qosInterfaceEntry = _QosInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 16, 1, 1)
)
qosInterfaceEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosInterfaceIndex"),
)
if mibBuilder.loadTexts:
    qosInterfaceEntry.setStatus("current")
_QosInterfaceIndex_Type = InterfaceIndexOrZero
_QosInterfaceIndex_Object = MibTableColumn
qosInterfaceIndex = _QosInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 16, 1, 1, 1),
    _QosInterfaceIndex_Type()
)
qosInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosInterfaceIndex.setStatus("current")
_QosInterfaceRowStatus_Type = RowStatus
_QosInterfaceRowStatus_Object = MibTableColumn
qosInterfaceRowStatus = _QosInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 16, 1, 1, 2),
    _QosInterfaceRowStatus_Type()
)
qosInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInterfaceRowStatus.setStatus("current")
_QosInterfacePolicy_Type = TNamedItem
_QosInterfacePolicy_Object = MibTableColumn
qosInterfacePolicy = _QosInterfacePolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 16, 1, 1, 3),
    _QosInterfacePolicy_Type()
)
qosInterfacePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInterfacePolicy.setStatus("current")
_QosStatisticsObjects_ObjectIdentity = ObjectIdentity
qosStatisticsObjects = _QosStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 17)
)
_QosStatisticsTable_Object = MibTable
qosStatisticsTable = _QosStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 17, 1)
)
if mibBuilder.loadTexts:
    qosStatisticsTable.setStatus("current")
_QosStatisticsEntry_Object = MibTableRow
qosStatisticsEntry = _QosStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 17, 1, 1)
)
qosStatisticsEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosStatInterfaceIndex"),
    (0, "PRVT-QOS-MIB", "qosQueueIndex"),
)
if mibBuilder.loadTexts:
    qosStatisticsEntry.setStatus("current")
_QosStatInterfaceIndex_Type = InterfaceIndexOrZero
_QosStatInterfaceIndex_Object = MibTableColumn
qosStatInterfaceIndex = _QosStatInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 17, 1, 1, 1),
    _QosStatInterfaceIndex_Type()
)
qosStatInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosStatInterfaceIndex.setStatus("current")
_QosQueueIndex_Type = TQueueId
_QosQueueIndex_Object = MibTableColumn
qosQueueIndex = _QosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 17, 1, 1, 2),
    _QosQueueIndex_Type()
)
qosQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosQueueIndex.setStatus("current")
_QosReceivedBytes_Type = Counter32
_QosReceivedBytes_Object = MibTableColumn
qosReceivedBytes = _QosReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 17, 1, 1, 3),
    _QosReceivedBytes_Type()
)
qosReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosReceivedBytes.setStatus("current")
_QosDroppedBytes_Type = Counter32
_QosDroppedBytes_Object = MibTableColumn
qosDroppedBytes = _QosDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 17, 1, 1, 4),
    _QosDroppedBytes_Type()
)
qosDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDroppedBytes.setStatus("current")


class _QosClearStatistics_Type(TruthValue):
    """Custom type qosClearStatistics based on TruthValue"""
    defaultValue = 2


_QosClearStatistics_Type.__name__ = "TruthValue"
_QosClearStatistics_Object = MibTableColumn
qosClearStatistics = _QosClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 17, 1, 1, 5),
    _QosClearStatistics_Type()
)
qosClearStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosClearStatistics.setStatus("current")
_QosVlanPolicyObjects_ObjectIdentity = ObjectIdentity
qosVlanPolicyObjects = _QosVlanPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18)
)
_QosVlanPolicyTable_Object = MibTable
qosVlanPolicyTable = _QosVlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 1)
)
if mibBuilder.loadTexts:
    qosVlanPolicyTable.setStatus("current")
_QosVlanPolicyEntry_Object = MibTableRow
qosVlanPolicyEntry = _QosVlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 1, 1)
)
qosVlanPolicyEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosVlanPolicy"),
)
if mibBuilder.loadTexts:
    qosVlanPolicyEntry.setStatus("current")
_QosVlanPolicy_Type = TNamedItem
_QosVlanPolicy_Object = MibTableColumn
qosVlanPolicy = _QosVlanPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 1, 1, 1),
    _QosVlanPolicy_Type()
)
qosVlanPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosVlanPolicy.setStatus("current")


class _QosVlanPolicyDescription_Type(TItemDescription):
    """Custom type qosVlanPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_QosVlanPolicyDescription_Type.__name__ = "TItemDescription"
_QosVlanPolicyDescription_Object = MibTableColumn
qosVlanPolicyDescription = _QosVlanPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 1, 1, 2),
    _QosVlanPolicyDescription_Type()
)
qosVlanPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanPolicyDescription.setStatus("current")
_QosVlanPolicyRowStatus_Type = RowStatus
_QosVlanPolicyRowStatus_Object = MibTableColumn
qosVlanPolicyRowStatus = _QosVlanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 1, 1, 3),
    _QosVlanPolicyRowStatus_Type()
)
qosVlanPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosVlanPolicyRowStatus.setStatus("current")
_QosVlanIngressPolicyTable_Object = MibTable
qosVlanIngressPolicyTable = _QosVlanIngressPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 2)
)
if mibBuilder.loadTexts:
    qosVlanIngressPolicyTable.setStatus("current")
_QosVlanIngressPolicyEntry_Object = MibTableRow
qosVlanIngressPolicyEntry = _QosVlanIngressPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 2, 1)
)
qosVlanIngressPolicyEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosVlanPolicy"),
)
if mibBuilder.loadTexts:
    qosVlanIngressPolicyEntry.setStatus("current")
_QosVlanPolicyShaperProfile_Type = TShaperId
_QosVlanPolicyShaperProfile_Object = MibTableColumn
qosVlanPolicyShaperProfile = _QosVlanPolicyShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 2, 1, 1),
    _QosVlanPolicyShaperProfile_Type()
)
qosVlanPolicyShaperProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanPolicyShaperProfile.setStatus("current")
_QosVlanPolicySchedulingProfile_Type = TSSchedulingProfile
_QosVlanPolicySchedulingProfile_Object = MibTableColumn
qosVlanPolicySchedulingProfile = _QosVlanPolicySchedulingProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 2, 1, 2),
    _QosVlanPolicySchedulingProfile_Type()
)
qosVlanPolicySchedulingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanPolicySchedulingProfile.setStatus("current")
_QosVlanPolicyTailDropProfile_Type = TTailDropId
_QosVlanPolicyTailDropProfile_Object = MibTableColumn
qosVlanPolicyTailDropProfile = _QosVlanPolicyTailDropProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 2, 1, 3),
    _QosVlanPolicyTailDropProfile_Type()
)
qosVlanPolicyTailDropProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanPolicyTailDropProfile.setStatus("current")
_QosVlanIngressQueueTable_Object = MibTable
qosVlanIngressQueueTable = _QosVlanIngressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 3)
)
if mibBuilder.loadTexts:
    qosVlanIngressQueueTable.setStatus("current")
_QosVlanIngressQueueEntry_Object = MibTableRow
qosVlanIngressQueueEntry = _QosVlanIngressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 3, 1)
)
qosVlanIngressQueueEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosVlanPolicy"),
)
if mibBuilder.loadTexts:
    qosVlanIngressQueueEntry.setStatus("current")


class _QosVlanInQueueQueue_Type(TQueueId):
    """Custom type qosVlanInQueueQueue based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QosVlanInQueueQueue_Type.__name__ = "TQueueId"
_QosVlanInQueueQueue_Object = MibTableColumn
qosVlanInQueueQueue = _QosVlanInQueueQueue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 3, 1, 1),
    _QosVlanInQueueQueue_Type()
)
qosVlanInQueueQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosVlanInQueueQueue.setStatus("current")
_QosVlanInQueueShaperProfile_Type = TShaperId
_QosVlanInQueueShaperProfile_Object = MibTableColumn
qosVlanInQueueShaperProfile = _QosVlanInQueueShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 3, 1, 2),
    _QosVlanInQueueShaperProfile_Type()
)
qosVlanInQueueShaperProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanInQueueShaperProfile.setStatus("current")
_QosVlanInQueueTailDropProfile_Type = TTailDropId
_QosVlanInQueueTailDropProfile_Object = MibTableColumn
qosVlanInQueueTailDropProfile = _QosVlanInQueueTailDropProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 3, 1, 3),
    _QosVlanInQueueTailDropProfile_Type()
)
qosVlanInQueueTailDropProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanInQueueTailDropProfile.setStatus("current")
_QosVlanInQueueRowStatus_Type = RowStatus
_QosVlanInQueueRowStatus_Object = MibTableColumn
qosVlanInQueueRowStatus = _QosVlanInQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 18, 3, 1, 4),
    _QosVlanInQueueRowStatus_Type()
)
qosVlanInQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosVlanInQueueRowStatus.setStatus("current")
_QosVlanObjects_ObjectIdentity = ObjectIdentity
qosVlanObjects = _QosVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19)
)
_QosVlanTable_Object = MibTable
qosVlanTable = _QosVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19, 1)
)
if mibBuilder.loadTexts:
    qosVlanTable.setStatus("current")
_QosVlanEntry_Object = MibTableRow
qosVlanEntry = _QosVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19, 1, 1)
)
qosVlanEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosVlanIndex"),
)
if mibBuilder.loadTexts:
    qosVlanEntry.setStatus("current")


class _QosVlanIndex_Type(Integer32):
    """Custom type qosVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QosVlanIndex_Type.__name__ = "Integer32"
_QosVlanIndex_Object = MibTableColumn
qosVlanIndex = _QosVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19, 1, 1, 1),
    _QosVlanIndex_Type()
)
qosVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosVlanIndex.setStatus("current")
_QosVlanPolicyOnVlan_Type = TNamedItem
_QosVlanPolicyOnVlan_Object = MibTableColumn
qosVlanPolicyOnVlan = _QosVlanPolicyOnVlan_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19, 1, 1, 2),
    _QosVlanPolicyOnVlan_Type()
)
qosVlanPolicyOnVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosVlanPolicyOnVlan.setStatus("current")
_QosVlanRowStatus_Type = RowStatus
_QosVlanRowStatus_Object = MibTableColumn
qosVlanRowStatus = _QosVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19, 1, 1, 3),
    _QosVlanRowStatus_Type()
)
qosVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosVlanRowStatus.setStatus("current")
_QosVlanIngressPortTable_Object = MibTable
qosVlanIngressPortTable = _QosVlanIngressPortTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19, 2)
)
if mibBuilder.loadTexts:
    qosVlanIngressPortTable.setStatus("current")
_QosVlanIngressPortEntry_Object = MibTableRow
qosVlanIngressPortEntry = _QosVlanIngressPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19, 2, 1)
)
qosVlanIngressPortEntry.setIndexNames(
    (0, "PRVT-QOS-MIB", "qosVlanIndex"),
    (0, "PRVT-QOS-MIB", "qosVlanIngressPortId"),
)
if mibBuilder.loadTexts:
    qosVlanIngressPortEntry.setStatus("current")


class _QosVlanIngressPortId_Type(Integer32):
    """Custom type qosVlanIngressPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QosVlanIngressPortId_Type.__name__ = "Integer32"
_QosVlanIngressPortId_Object = MibTableColumn
qosVlanIngressPortId = _QosVlanIngressPortId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19, 2, 1, 1),
    _QosVlanIngressPortId_Type()
)
qosVlanIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosVlanIngressPortId.setStatus("current")
_QosVlanPortPolicyEnable_Type = TruthValue
_QosVlanPortPolicyEnable_Object = MibTableColumn
qosVlanPortPolicyEnable = _QosVlanPortPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19, 2, 1, 2),
    _QosVlanPortPolicyEnable_Type()
)
qosVlanPortPolicyEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosVlanPortPolicyEnable.setStatus("current")
_QosVlanPortRowStatus_Type = RowStatus
_QosVlanPortRowStatus_Object = MibTableColumn
qosVlanPortRowStatus = _QosVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 1, 19, 2, 1, 3),
    _QosVlanPortRowStatus_Type()
)
qosVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosVlanPortRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-QOS-MIB",
    **{"TNamedItem": TNamedItem,
       "TNamedItemOrEmpty": TNamedItemOrEmpty,
       "TQEncapVal": TQEncapVal,
       "TLspExpValue": TLspExpValue,
       "Dot1PPriority": Dot1PPriority,
       "TFCName": TFCName,
       "TFCNameOrEmpty": TFCNameOrEmpty,
       "TDSCPValue": TDSCPValue,
       "TItemDescription": TItemDescription,
       "TQueueId": TQueueId,
       "TIngressQueueId": TIngressQueueId,
       "TEgressQueueId": TEgressQueueId,
       "TSapIngressPolicyId": TSapIngressPolicyId,
       "TSapIngressPolicyIdOrNone": TSapIngressPolicyIdOrNone,
       "TSapEgressPolicyId": TSapEgressPolicyId,
       "TSapEgressPolicyIdOrNone": TSapEgressPolicyIdOrNone,
       "TNetworkPolicyId": TNetworkPolicyId,
       "TNetworkPolicyIdOrNone": TNetworkPolicyIdOrNone,
       "TItemMatch": TItemMatch,
       "TPriority": TPriority,
       "TPriorityOrDefault": TPriorityOrDefault,
       "TProfile": TProfile,
       "TCIRRate": TCIRRate,
       "TPIRRate": TPIRRate,
       "TRateValue": TRateValue,
       "TLevel": TLevel,
       "TWeight": TWeight,
       "TTreshold": TTreshold,
       "TConformanceLevel": TConformanceLevel,
       "TShaperId": TShaperId,
       "TTailDropId": TTailDropId,
       "TSredId": TSredId,
       "TSSchedulingProfile": TSSchedulingProfile,
       "TSlopePolicy": TSlopePolicy,
       "serviceAccessSwitch": serviceAccessSwitch,
       "prvtQosMIB": prvtQosMIB,
       "tFCObjects": tFCObjects,
       "tFCNameTable": tFCNameTable,
       "tFCNameEntry": tFCNameEntry,
       "tFCValue": tFCValue,
       "tFCRowStatus": tFCRowStatus,
       "tFCStorageType": tFCStorageType,
       "tFCName": tFCName,
       "tFCNameLastChanged": tFCNameLastChanged,
       "hqosSapIngressObjects": hqosSapIngressObjects,
       "hqosSapIngressTable": hqosSapIngressTable,
       "hqosSapIngressEntry": hqosSapIngressEntry,
       "hqosSapIngressIndex": hqosSapIngressIndex,
       "hqosSapIngressRowStatus": hqosSapIngressRowStatus,
       "hqosSapIngressDescription": hqosSapIngressDescription,
       "hqosSapIngressDefaultDscpFC": hqosSapIngressDefaultDscpFC,
       "hqosSapIngressDefaultVptFC": hqosSapIngressDefaultVptFC,
       "hqosSapIngressLastChanged": hqosSapIngressLastChanged,
       "hqosSapIngressQueueTable": hqosSapIngressQueueTable,
       "hqosSapIngressQueueEntry": hqosSapIngressQueueEntry,
       "hqosSapIngressQueue": hqosSapIngressQueue,
       "hqosSapIngressQueueParent": hqosSapIngressQueueParent,
       "hqosSapIngressQueueRowStatus": hqosSapIngressQueueRowStatus,
       "hqosSapIngressQueueLevel": hqosSapIngressQueueLevel,
       "hqosSapIngressQueueServWfq": hqosSapIngressQueueServWfq,
       "hqosSapIngressQueueType": hqosSapIngressQueueType,
       "hqosSapIngressQueueHiPriority": hqosSapIngressQueueHiPriority,
       "hqosSapIngressQueueWred": hqosSapIngressQueueWred,
       "hqosSapIngressQueueLastChanged": hqosSapIngressQueueLastChanged,
       "hqosSapIngressDSCPTable": hqosSapIngressDSCPTable,
       "hqosSapIngressDSCPEntry": hqosSapIngressDSCPEntry,
       "hqosSapIngressDSCP": hqosSapIngressDSCP,
       "hqosSapIngressDSCPRowStatus": hqosSapIngressDSCPRowStatus,
       "hqosSapIngressDSCPFC": hqosSapIngressDSCPFC,
       "hqosSapIngressDSCPConformance": hqosSapIngressDSCPConformance,
       "hqosSapIngressDSCPLastChanged": hqosSapIngressDSCPLastChanged,
       "hqosSapIngressDot1pTable": hqosSapIngressDot1pTable,
       "hqosSapIngressDot1pEntry": hqosSapIngressDot1pEntry,
       "hqosSapIngressDot1pValue": hqosSapIngressDot1pValue,
       "hqosSapIngressDot1pRowStatus": hqosSapIngressDot1pRowStatus,
       "hqosSapIngressDot1pFC": hqosSapIngressDot1pFC,
       "hqosSapIngressDot1pConformance": hqosSapIngressDot1pConformance,
       "hqosSapIngressDot1pLastChanged": hqosSapIngressDot1pLastChanged,
       "hqosSapIngressFCTable": hqosSapIngressFCTable,
       "hqosSapIngressFCEntry": hqosSapIngressFCEntry,
       "hqosSapIngressFCNumber": hqosSapIngressFCNumber,
       "hqosSapIngressFCQueueType": hqosSapIngressFCQueueType,
       "hqosSapIngressFCRowStatus": hqosSapIngressFCRowStatus,
       "hqosSapIngressFCQueue": hqosSapIngressFCQueue,
       "hqosSapIngressFCQueueParent": hqosSapIngressFCQueueParent,
       "hqosSapIngressFCLastChanged": hqosSapIngressFCLastChanged,
       "hqosSapEgressObjects": hqosSapEgressObjects,
       "hqosSapEgressTable": hqosSapEgressTable,
       "hqosSapEgressEntry": hqosSapEgressEntry,
       "hqosSapEgressIndex": hqosSapEgressIndex,
       "hqosSapEgressRowStatus": hqosSapEgressRowStatus,
       "hqosSapEgressDescription": hqosSapEgressDescription,
       "hqosSapEgressLastChanged": hqosSapEgressLastChanged,
       "hqosSapEgressQueueTable": hqosSapEgressQueueTable,
       "hqosSapEgressQueueEntry": hqosSapEgressQueueEntry,
       "hqosSapEgressQueueIndex": hqosSapEgressQueueIndex,
       "hqosSapEgressQueueParent": hqosSapEgressQueueParent,
       "hqosSapEgressQueueRowStatus": hqosSapEgressQueueRowStatus,
       "hqosSapEgressQueueLevel": hqosSapEgressQueueLevel,
       "hqosSapEgressQueueServWfq": hqosSapEgressQueueServWfq,
       "hqosSapEgressQueueType": hqosSapEgressQueueType,
       "hqosSapEgressQueueHiPriority": hqosSapEgressQueueHiPriority,
       "hqosSapEgressQueueWred": hqosSapEgressQueueWred,
       "hqosSapEgressQueueLastChanged": hqosSapEgressQueueLastChanged,
       "hqosSapEgressFCTable": hqosSapEgressFCTable,
       "hqosSapEgressFCEntry": hqosSapEgressFCEntry,
       "hqosSapEgressFCNumber": hqosSapEgressFCNumber,
       "hqosSapEgressFCEntryType": hqosSapEgressFCEntryType,
       "hqosSapEgressFCRowStatus": hqosSapEgressFCRowStatus,
       "hqosSapEgressFCQueue": hqosSapEgressFCQueue,
       "hqosSapEgressFCQueueParent": hqosSapEgressFCQueueParent,
       "hqosSapEgressFCDot1PValue": hqosSapEgressFCDot1PValue,
       "hqosSapEgressFCDSCPValue": hqosSapEgressFCDSCPValue,
       "hqosSapEgressFCLastChanged": hqosSapEgressFCLastChanged,
       "hqosNetworkObjects": hqosNetworkObjects,
       "hqosNetworkPolicyTable": hqosNetworkPolicyTable,
       "hqosNetworkPolicyEntry": hqosNetworkPolicyEntry,
       "hqosNetworkPolicyIndex": hqosNetworkPolicyIndex,
       "hqosNetworkPolicyRowStatus": hqosNetworkPolicyRowStatus,
       "hqosNetworkPolicyDescription": hqosNetworkPolicyDescription,
       "hqosNetworkPolicyIngressDefaultActionFC": hqosNetworkPolicyIngressDefaultActionFC,
       "hqosNetworkPolicyIngressConformance": hqosNetworkPolicyIngressConformance,
       "hqosNetworkPolicyEgressRemark": hqosNetworkPolicyEgressRemark,
       "hqosNetworkPolicyLastChanged": hqosNetworkPolicyLastChanged,
       "hqosNetworkIngressLSPEXPTable": hqosNetworkIngressLSPEXPTable,
       "hqosNetworkIngressLSPEXPEntry": hqosNetworkIngressLSPEXPEntry,
       "hqosNetworkIngressLSPEXP": hqosNetworkIngressLSPEXP,
       "hqosNetworkIngressLSPEXPRowStatus": hqosNetworkIngressLSPEXPRowStatus,
       "hqosNetworkIngressLSPEXPFC": hqosNetworkIngressLSPEXPFC,
       "hqosNetworkIngressLSPEXPConformance": hqosNetworkIngressLSPEXPConformance,
       "hqosNetworkIngressLSPEXPLastChanged": hqosNetworkIngressLSPEXPLastChanged,
       "hqosNetworkEgressFCTable": hqosNetworkEgressFCTable,
       "hqosNetworkEgressFCEntry": hqosNetworkEgressFCEntry,
       "hqosNetworkEgressFCNumber": hqosNetworkEgressFCNumber,
       "hqosNetworkEgressFCRowStatus": hqosNetworkEgressFCRowStatus,
       "hqosNetworkEgressFCLspExpValue": hqosNetworkEgressFCLspExpValue,
       "hqosNetworkEgressFCDot1Priority": hqosNetworkEgressFCDot1Priority,
       "hqosNetworkEgressFCLastChanged": hqosNetworkEgressFCLastChanged,
       "hqosNetworkEgressFCConformance": hqosNetworkEgressFCConformance,
       "hqosNetworkQueueObjects": hqosNetworkQueueObjects,
       "hqosNetworkQueuePolicyTable": hqosNetworkQueuePolicyTable,
       "hqosNetworkQueuePolicyEntry": hqosNetworkQueuePolicyEntry,
       "hqosNetworkQueuePolicy": hqosNetworkQueuePolicy,
       "hqosNetworkQueuePolicyRowStatus": hqosNetworkQueuePolicyRowStatus,
       "hqosNetworkQueuePolicyDescription": hqosNetworkQueuePolicyDescription,
       "hqosNetworkQueuePolicyLastChanged": hqosNetworkQueuePolicyLastChanged,
       "hqosNetworkQueueTable": hqosNetworkQueueTable,
       "hqosNetworkQueueEntry": hqosNetworkQueueEntry,
       "hqosNetworkQueue": hqosNetworkQueue,
       "hqosNetworkQueueRowStatus": hqosNetworkQueueRowStatus,
       "hqosNetworkQueueParent": hqosNetworkQueueParent,
       "hqosNetworkQueueLevel": hqosNetworkQueueLevel,
       "hqosNetworkQueueWfqProfile": hqosNetworkQueueWfqProfile,
       "hqosNetworkQueueType": hqosNetworkQueueType,
       "hqosNetworkQueueHiPriority": hqosNetworkQueueHiPriority,
       "hqosNetworkQueueWred": hqosNetworkQueueWred,
       "hqosNetworkQueueShaper": hqosNetworkQueueShaper,
       "hqosNetworkQueueLastChanged": hqosNetworkQueueLastChanged,
       "hqosNetworkQueueFCTable": hqosNetworkQueueFCTable,
       "hqosNetworkQueueFCEntry": hqosNetworkQueueFCEntry,
       "hqosNetworkQueueFCNumber": hqosNetworkQueueFCNumber,
       "hqosNetworkQueueFCType": hqosNetworkQueueFCType,
       "hqosNetworkQueueFCRowStatus": hqosNetworkQueueFCRowStatus,
       "hqosNetworkQueueFC": hqosNetworkQueueFC,
       "hqosNetworkQueueFCLastChanged": hqosNetworkQueueFCLastChanged,
       "hqosSchedulerObjects": hqosSchedulerObjects,
       "hqosSchedulerPolicyTable": hqosSchedulerPolicyTable,
       "hqosSchedulerPolicyEntry": hqosSchedulerPolicyEntry,
       "hqosSchedulerPolicyName": hqosSchedulerPolicyName,
       "hqosSchedulerPolicyRowStatus": hqosSchedulerPolicyRowStatus,
       "hqosSchedulerPolicyType": hqosSchedulerPolicyType,
       "hqosSchedulerPolicyDescription": hqosSchedulerPolicyDescription,
       "hqosSchedulerPolicyLastChanged": hqosSchedulerPolicyLastChanged,
       "hqosVirtualSchedulerTable": hqosVirtualSchedulerTable,
       "hqosVirtualSchedulerEntry": hqosVirtualSchedulerEntry,
       "hqosVirtualSchedulerName": hqosVirtualSchedulerName,
       "hqosVirtualSchedulerRowStatus": hqosVirtualSchedulerRowStatus,
       "hqosVirtualSchedulerDescription": hqosVirtualSchedulerDescription,
       "hqosVirtualSchedulerParent": hqosVirtualSchedulerParent,
       "hqosVirtualSchedulerLevel": hqosVirtualSchedulerLevel,
       "hqosVirtualSchedulerPriority": hqosVirtualSchedulerPriority,
       "hqosVirtualSchedulerWfqProfile": hqosVirtualSchedulerWfqProfile,
       "hqosVirtualSchedulerShaper": hqosVirtualSchedulerShaper,
       "hqosVirtualSchedulerLastChanged": hqosVirtualSchedulerLastChanged,
       "tWredObjects": tWredObjects,
       "tWredProfileTable": tWredProfileTable,
       "tWredProfileEntry": tWredProfileEntry,
       "tWredProfile": tWredProfile,
       "tWredRowStatus": tWredRowStatus,
       "tWredDescription": tWredDescription,
       "tWredGreenStartAverage": tWredGreenStartAverage,
       "tWredGreenMaxAverage": tWredGreenMaxAverage,
       "tWredGreenProbability": tWredGreenProbability,
       "tWredYellowStartAverage": tWredYellowStartAverage,
       "tWredYellowMaxAverage": tWredYellowMaxAverage,
       "tWredYellowProbability": tWredYellowProbability,
       "tWredRedStartAverage": tWredRedStartAverage,
       "tWredRedMaxAverage": tWredRedMaxAverage,
       "tWredRedProbability": tWredRedProbability,
       "tWredLastChanged": tWredLastChanged,
       "tCongestionAvoidanceProfileObjects": tCongestionAvoidanceProfileObjects,
       "qosTailDropProfileTable": qosTailDropProfileTable,
       "qosTailDropProfileEntry": qosTailDropProfileEntry,
       "qosTailDropProfile": qosTailDropProfile,
       "qosTailDropRowStatus": qosTailDropRowStatus,
       "qosMaxTailDropYellowTreshold": qosMaxTailDropYellowTreshold,
       "qosMaxTailDropRedTreshold": qosMaxTailDropRedTreshold,
       "qosSredProfileTable": qosSredProfileTable,
       "qosSredProfileEntry": qosSredProfileEntry,
       "qosSredProfile": qosSredProfile,
       "qosSredRowStatus": qosSredRowStatus,
       "qosMaxSredYellowTreshold": qosMaxSredYellowTreshold,
       "qosMaxSredYellowProbaility": qosMaxSredYellowProbaility,
       "qosMaxSredRedTreshold": qosMaxSredRedTreshold,
       "qosMaxSredRedProbability": qosMaxSredRedProbability,
       "tShaperObjects": tShaperObjects,
       "tShaperProfileTable": tShaperProfileTable,
       "tShaperProfileEntry": tShaperProfileEntry,
       "tShaperProfileType": tShaperProfileType,
       "tShaperProfile": tShaperProfile,
       "tShaperProfileDirection": tShaperProfileDirection,
       "tShaperProfileLevel": tShaperProfileLevel,
       "tShaperRowStatus": tShaperRowStatus,
       "tShaperDescription": tShaperDescription,
       "tShaperCIR": tShaperCIR,
       "tShaperPIR": tShaperPIR,
       "tShaperCBS": tShaperCBS,
       "tShaperMBS": tShaperMBS,
       "tShaperLastChanged": tShaperLastChanged,
       "tWfqObjects": tWfqObjects,
       "tWfqServiceProfileTable": tWfqServiceProfileTable,
       "tWfqServiceProfileEntry": tWfqServiceProfileEntry,
       "tWfqServiceProfileNumber": tWfqServiceProfileNumber,
       "tWfqServiceProfileDirection": tWfqServiceProfileDirection,
       "tWfqServiceProfileRowStatus": tWfqServiceProfileRowStatus,
       "tWfqServiceProfileWeight": tWfqServiceProfileWeight,
       "tWfqNetworkProfileTable": tWfqNetworkProfileTable,
       "tWfqNetworkProfileEntry": tWfqNetworkProfileEntry,
       "tWfqNetworkProfileNumber": tWfqNetworkProfileNumber,
       "tWfqNetworkProfileRowStatus": tWfqNetworkProfileRowStatus,
       "tWfqNetworkProfileWeight": tWfqNetworkProfileWeight,
       "tWfqNetworkProfileCIRWeight": tWfqNetworkProfileCIRWeight,
       "tWfqSchedulerProfileTable": tWfqSchedulerProfileTable,
       "tWfqSchedulerProfileEntry": tWfqSchedulerProfileEntry,
       "tWfqSchedulerProfileNumber": tWfqSchedulerProfileNumber,
       "tWfqSchedulerProfileDirection": tWfqSchedulerProfileDirection,
       "tWfqSchedulerProfileRowStatus": tWfqSchedulerProfileRowStatus,
       "tWfqSchedulerProfileWeight": tWfqSchedulerProfileWeight,
       "tWfqSchedulerProfileCIRWeight": tWfqSchedulerProfileCIRWeight,
       "qosSchedulingProfileObjects": qosSchedulingProfileObjects,
       "qosSchedulingProfileTable": qosSchedulingProfileTable,
       "qosSchedulingProfileEntry": qosSchedulingProfileEntry,
       "qosSchedulingProfile": qosSchedulingProfile,
       "qosSchedulingProfileDirection": qosSchedulingProfileDirection,
       "qosSchedulingType": qosSchedulingType,
       "qosSchedulingRowStatus": qosSchedulingRowStatus,
       "qosSchedulingQ1Weight": qosSchedulingQ1Weight,
       "qosSchedulingQ2Weight": qosSchedulingQ2Weight,
       "qosSchedulingQ3Weight": qosSchedulingQ3Weight,
       "qosSchedulingQ4Weight": qosSchedulingQ4Weight,
       "qosSchedulingQ5Weight": qosSchedulingQ5Weight,
       "qosSchedulingQ6Weight": qosSchedulingQ6Weight,
       "qosSchedulingQ7Weight": qosSchedulingQ7Weight,
       "qosSchedulingQ8Weight": qosSchedulingQ8Weight,
       "qosServicePolicyObjects": qosServicePolicyObjects,
       "qosServicePolicyTable": qosServicePolicyTable,
       "qosServicePolicyEntry": qosServicePolicyEntry,
       "qosServicePolicy": qosServicePolicy,
       "qosServicePolicyRowStatus": qosServicePolicyRowStatus,
       "qosServicePolicyDescription": qosServicePolicyDescription,
       "qosServiceIngressPolicyTable": qosServiceIngressPolicyTable,
       "qosServiceIngressPolicyEntry": qosServiceIngressPolicyEntry,
       "qosServPolicyShaperProfile": qosServPolicyShaperProfile,
       "qosServPolicySchedulingProfile": qosServPolicySchedulingProfile,
       "qosServPolicyTailDropProfile": qosServPolicyTailDropProfile,
       "qosServiceIngressQueueTable": qosServiceIngressQueueTable,
       "qosServiceIngressQueueEntry": qosServiceIngressQueueEntry,
       "qosServInQueueQueue": qosServInQueueQueue,
       "qosServInQueueRowStatus": qosServInQueueRowStatus,
       "qosServInQueueShaperProfile": qosServInQueueShaperProfile,
       "qosServInQueueTailDropProfile": qosServInQueueTailDropProfile,
       "qosNetworkPolicyObjects": qosNetworkPolicyObjects,
       "qosNetworkPolicyTable": qosNetworkPolicyTable,
       "qosNetworkPolicyEntry": qosNetworkPolicyEntry,
       "qosNetworkPolicy": qosNetworkPolicy,
       "qosNetworkPolicyRowStatus": qosNetworkPolicyRowStatus,
       "qosNetworkPolicyDescription": qosNetworkPolicyDescription,
       "qosNetworkIngressTable": qosNetworkIngressTable,
       "qosNetworkIngressEntry": qosNetworkIngressEntry,
       "qosNetworkIngressFC": qosNetworkIngressFC,
       "qosNetworkIngressConformance": qosNetworkIngressConformance,
       "qosTrustDot1pMode": qosTrustDot1pMode,
       "qosTrustDot1pModePreservePriority": qosTrustDot1pModePreservePriority,
       "qosTrustDscpMode": qosTrustDscpMode,
       "qosNetworkEgressTable": qosNetworkEgressTable,
       "qosNetworkEgressEntry": qosNetworkEgressEntry,
       "qosNetPolicySchedulingProfile": qosNetPolicySchedulingProfile,
       "qosNetPolicyShaperProfile": qosNetPolicyShaperProfile,
       "qosNetPolicyTailDropProfile": qosNetPolicyTailDropProfile,
       "qosNetPolicySredProfile": qosNetPolicySredProfile,
       "qosNetworkEgressQueueTable": qosNetworkEgressQueueTable,
       "qosNetworkEgressQueueEntry": qosNetworkEgressQueueEntry,
       "qosNetworkQueue": qosNetworkQueue,
       "qosNetworkQueueRowStatus": qosNetworkQueueRowStatus,
       "qosNetworkQueueShaperProfile": qosNetworkQueueShaperProfile,
       "qosNetworkQueueTailDropProfile": qosNetworkQueueTailDropProfile,
       "qosNetworkQueueSredProfile": qosNetworkQueueSredProfile,
       "qosGlobalObjects": qosGlobalObjects,
       "qosGlobalIngressMapTable": qosGlobalIngressMapTable,
       "qosGlobalIngressMapEntry": qosGlobalIngressMapEntry,
       "qosIngressMapType": qosIngressMapType,
       "qosIngressMapValue": qosIngressMapValue,
       "qosIngressRowStatus": qosIngressRowStatus,
       "qosIngressFC": qosIngressFC,
       "qosIngressFCConformance": qosIngressFCConformance,
       "qosGlobalEgressRemarkTable": qosGlobalEgressRemarkTable,
       "qosGlobalEgressRemarkEntry": qosGlobalEgressRemarkEntry,
       "qosEgressFC": qosEgressFC,
       "qosEgressFCConformance": qosEgressFCConformance,
       "qosEgressRowStatus": qosEgressRowStatus,
       "qosEgressRemarkType": qosEgressRemarkType,
       "qosEgressRemarkValue": qosEgressRemarkValue,
       "qosServiceObjects": qosServiceObjects,
       "qosServiceTable": qosServiceTable,
       "qosServiceEntry": qosServiceEntry,
       "qosServiceIndex": qosServiceIndex,
       "qosServiceRowStatus": qosServiceRowStatus,
       "qosServicePolicyOnServ": qosServicePolicyOnServ,
       "qosServiceSapTable": qosServiceSapTable,
       "qosServiceSapEntry": qosServiceSapEntry,
       "qosServiceSapPortId": qosServiceSapPortId,
       "qosServiceSapEncapValue": qosServiceSapEncapValue,
       "qosServiceSapRowStatus": qosServiceSapRowStatus,
       "qosServiceSapPolicyEnable": qosServiceSapPolicyEnable,
       "qosInterfaceObjects": qosInterfaceObjects,
       "qosInterfaceTable": qosInterfaceTable,
       "qosInterfaceEntry": qosInterfaceEntry,
       "qosInterfaceIndex": qosInterfaceIndex,
       "qosInterfaceRowStatus": qosInterfaceRowStatus,
       "qosInterfacePolicy": qosInterfacePolicy,
       "qosStatisticsObjects": qosStatisticsObjects,
       "qosStatisticsTable": qosStatisticsTable,
       "qosStatisticsEntry": qosStatisticsEntry,
       "qosStatInterfaceIndex": qosStatInterfaceIndex,
       "qosQueueIndex": qosQueueIndex,
       "qosReceivedBytes": qosReceivedBytes,
       "qosDroppedBytes": qosDroppedBytes,
       "qosClearStatistics": qosClearStatistics,
       "qosVlanPolicyObjects": qosVlanPolicyObjects,
       "qosVlanPolicyTable": qosVlanPolicyTable,
       "qosVlanPolicyEntry": qosVlanPolicyEntry,
       "qosVlanPolicy": qosVlanPolicy,
       "qosVlanPolicyDescription": qosVlanPolicyDescription,
       "qosVlanPolicyRowStatus": qosVlanPolicyRowStatus,
       "qosVlanIngressPolicyTable": qosVlanIngressPolicyTable,
       "qosVlanIngressPolicyEntry": qosVlanIngressPolicyEntry,
       "qosVlanPolicyShaperProfile": qosVlanPolicyShaperProfile,
       "qosVlanPolicySchedulingProfile": qosVlanPolicySchedulingProfile,
       "qosVlanPolicyTailDropProfile": qosVlanPolicyTailDropProfile,
       "qosVlanIngressQueueTable": qosVlanIngressQueueTable,
       "qosVlanIngressQueueEntry": qosVlanIngressQueueEntry,
       "qosVlanInQueueQueue": qosVlanInQueueQueue,
       "qosVlanInQueueShaperProfile": qosVlanInQueueShaperProfile,
       "qosVlanInQueueTailDropProfile": qosVlanInQueueTailDropProfile,
       "qosVlanInQueueRowStatus": qosVlanInQueueRowStatus,
       "qosVlanObjects": qosVlanObjects,
       "qosVlanTable": qosVlanTable,
       "qosVlanEntry": qosVlanEntry,
       "qosVlanIndex": qosVlanIndex,
       "qosVlanPolicyOnVlan": qosVlanPolicyOnVlan,
       "qosVlanRowStatus": qosVlanRowStatus,
       "qosVlanIngressPortTable": qosVlanIngressPortTable,
       "qosVlanIngressPortEntry": qosVlanIngressPortEntry,
       "qosVlanIngressPortId": qosVlanIngressPortId,
       "qosVlanPortPolicyEnable": qosVlanPortPolicyEnable,
       "qosVlanPortRowStatus": qosVlanPortRowStatus}
)
