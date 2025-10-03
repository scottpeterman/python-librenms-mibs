# SNMP MIB module (SLEV2-PPPoE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLEV2-PPPoE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:12 2025
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

(sleV2Mgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleV2Mgmt")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleV2PPPoE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16)
)


# Types definitions



class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleV2PPPoEBase_ObjectIdentity = ObjectIdentity
sleV2PPPoEBase = _SleV2PPPoEBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1)
)
_SleV2PPPoEInfo_ObjectIdentity = ObjectIdentity
sleV2PPPoEInfo = _SleV2PPPoEInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 1)
)


class _SleV2PPPoESnoopingActivity_Type(Integer32):
    """Custom type sleV2PPPoESnoopingActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2PPPoESnoopingActivity_Type.__name__ = "Integer32"
_SleV2PPPoESnoopingActivity_Object = MibScalar
sleV2PPPoESnoopingActivity = _SleV2PPPoESnoopingActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 1, 1),
    _SleV2PPPoESnoopingActivity_Type()
)
sleV2PPPoESnoopingActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoESnoopingActivity.setStatus("current")
_SleV2PPPoEControl_ObjectIdentity = ObjectIdentity
sleV2PPPoEControl = _SleV2PPPoEControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 2)
)


class _SleV2PPPoEControlRequest_Type(Integer32):
    """Custom type sleV2PPPoEControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setPPPoESnoopingActivity", 1)
    )


_SleV2PPPoEControlRequest_Type.__name__ = "Integer32"
_SleV2PPPoEControlRequest_Object = MibScalar
sleV2PPPoEControlRequest = _SleV2PPPoEControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 2, 1),
    _SleV2PPPoEControlRequest_Type()
)
sleV2PPPoEControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEControlRequest.setStatus("current")
_SleV2PPPoEControlStatus_Type = SleControlStatusType
_SleV2PPPoEControlStatus_Object = MibScalar
sleV2PPPoEControlStatus = _SleV2PPPoEControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 2, 2),
    _SleV2PPPoEControlStatus_Type()
)
sleV2PPPoEControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoEControlStatus.setStatus("current")
_SleV2PPPoEControlTimer_Type = Gauge32
_SleV2PPPoEControlTimer_Object = MibScalar
sleV2PPPoEControlTimer = _SleV2PPPoEControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 2, 3),
    _SleV2PPPoEControlTimer_Type()
)
sleV2PPPoEControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEControlTimer.setStatus("current")
_SleV2PPPoEControlTimeStamp_Type = TimeTicks
_SleV2PPPoEControlTimeStamp_Object = MibScalar
sleV2PPPoEControlTimeStamp = _SleV2PPPoEControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 2, 4),
    _SleV2PPPoEControlTimeStamp_Type()
)
sleV2PPPoEControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEControlTimeStamp.setStatus("current")
_SleV2PPPoEControlReqResult_Type = SleControlRequestResultType
_SleV2PPPoEControlReqResult_Object = MibScalar
sleV2PPPoEControlReqResult = _SleV2PPPoEControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 2, 5),
    _SleV2PPPoEControlReqResult_Type()
)
sleV2PPPoEControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoEControlReqResult.setStatus("current")


class _SleV2PPPoEControlSnoopingActivity_Type(Integer32):
    """Custom type sleV2PPPoEControlSnoopingActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleV2PPPoEControlSnoopingActivity_Type.__name__ = "Integer32"
_SleV2PPPoEControlSnoopingActivity_Object = MibScalar
sleV2PPPoEControlSnoopingActivity = _SleV2PPPoEControlSnoopingActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 2, 6),
    _SleV2PPPoEControlSnoopingActivity_Type()
)
sleV2PPPoEControlSnoopingActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEControlSnoopingActivity.setStatus("current")
_SleV2PPPoENotification_ObjectIdentity = ObjectIdentity
sleV2PPPoENotification = _SleV2PPPoENotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 3)
)
_SleV2PPPoEFilter_ObjectIdentity = ObjectIdentity
sleV2PPPoEFilter = _SleV2PPPoEFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2)
)
_SleV2PPPoEFilterTable_Object = MibTable
sleV2PPPoEFilterTable = _SleV2PPPoEFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2PPPoEFilterTable.setStatus("current")
_SleV2PPPoEFilterEntry_Object = MibTableRow
sleV2PPPoEFilterEntry = _SleV2PPPoEFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 1, 1)
)
sleV2PPPoEFilterEntry.setIndexNames(
    (0, "SLEV2-PPPoE-MIB", "sleV2PPPoEFilterId"),
    (0, "SLEV2-PPPoE-MIB", "sleV2PPPoEFilterPortIndex"),
    (0, "SLEV2-PPPoE-MIB", "sleV2PPPoEFilterVlanId"),
)
if mibBuilder.loadTexts:
    sleV2PPPoEFilterEntry.setStatus("current")


class _SleV2PPPoEFilterId_Type(Integer32):
    """Custom type sleV2PPPoEFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleV2PPPoEFilterId_Type.__name__ = "Integer32"
_SleV2PPPoEFilterId_Object = MibTableColumn
sleV2PPPoEFilterId = _SleV2PPPoEFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 1, 1, 1),
    _SleV2PPPoEFilterId_Type()
)
sleV2PPPoEFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterId.setStatus("current")


class _SleV2PPPoEFilterPortIndex_Type(Integer32):
    """Custom type sleV2PPPoEFilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2PPPoEFilterPortIndex_Type.__name__ = "Integer32"
_SleV2PPPoEFilterPortIndex_Object = MibTableColumn
sleV2PPPoEFilterPortIndex = _SleV2PPPoEFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 1, 1, 2),
    _SleV2PPPoEFilterPortIndex_Type()
)
sleV2PPPoEFilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterPortIndex.setStatus("current")


class _SleV2PPPoEFilterVlanId_Type(Integer32):
    """Custom type sleV2PPPoEFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2PPPoEFilterVlanId_Type.__name__ = "Integer32"
_SleV2PPPoEFilterVlanId_Object = MibTableColumn
sleV2PPPoEFilterVlanId = _SleV2PPPoEFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 1, 1, 3),
    _SleV2PPPoEFilterVlanId_Type()
)
sleV2PPPoEFilterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterVlanId.setStatus("current")


class _SleV2PPPoEFilterAction_Type(Integer32):
    """Custom type sleV2PPPoEFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("permit", 2))
    )


_SleV2PPPoEFilterAction_Type.__name__ = "Integer32"
_SleV2PPPoEFilterAction_Object = MibTableColumn
sleV2PPPoEFilterAction = _SleV2PPPoEFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 1, 1, 4),
    _SleV2PPPoEFilterAction_Type()
)
sleV2PPPoEFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterAction.setStatus("current")
_SleV2PPPoEFilterControl_ObjectIdentity = ObjectIdentity
sleV2PPPoEFilterControl = _SleV2PPPoEFilterControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 2)
)


class _SleV2PPPoEFilterControlRequest_Type(Integer32):
    """Custom type sleV2PPPoEFilterControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createPPPoEFilter", 1),
          ("destroyPPPoEFilter", 2),
          ("modifyPPPoEFilter", 3))
    )


_SleV2PPPoEFilterControlRequest_Type.__name__ = "Integer32"
_SleV2PPPoEFilterControlRequest_Object = MibScalar
sleV2PPPoEFilterControlRequest = _SleV2PPPoEFilterControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 2, 1),
    _SleV2PPPoEFilterControlRequest_Type()
)
sleV2PPPoEFilterControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterControlRequest.setStatus("current")
_SleV2PPPoEFilterControlStatus_Type = SleControlStatusType
_SleV2PPPoEFilterControlStatus_Object = MibScalar
sleV2PPPoEFilterControlStatus = _SleV2PPPoEFilterControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 2, 2),
    _SleV2PPPoEFilterControlStatus_Type()
)
sleV2PPPoEFilterControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterControlStatus.setStatus("current")
_SleV2PPPoEFilterControlTimer_Type = Gauge32
_SleV2PPPoEFilterControlTimer_Object = MibScalar
sleV2PPPoEFilterControlTimer = _SleV2PPPoEFilterControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 2, 3),
    _SleV2PPPoEFilterControlTimer_Type()
)
sleV2PPPoEFilterControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterControlTimer.setStatus("current")
_SleV2PPPoEFilterControlTimeStamp_Type = TimeTicks
_SleV2PPPoEFilterControlTimeStamp_Object = MibScalar
sleV2PPPoEFilterControlTimeStamp = _SleV2PPPoEFilterControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 2, 4),
    _SleV2PPPoEFilterControlTimeStamp_Type()
)
sleV2PPPoEFilterControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterControlTimeStamp.setStatus("current")
_SleV2PPPoEFilterControlReqResult_Type = SleControlRequestResultType
_SleV2PPPoEFilterControlReqResult_Object = MibScalar
sleV2PPPoEFilterControlReqResult = _SleV2PPPoEFilterControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 2, 5),
    _SleV2PPPoEFilterControlReqResult_Type()
)
sleV2PPPoEFilterControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterControlReqResult.setStatus("current")


class _SleV2PPPoEFilterControlId_Type(Integer32):
    """Custom type sleV2PPPoEFilterControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleV2PPPoEFilterControlId_Type.__name__ = "Integer32"
_SleV2PPPoEFilterControlId_Object = MibScalar
sleV2PPPoEFilterControlId = _SleV2PPPoEFilterControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 2, 6),
    _SleV2PPPoEFilterControlId_Type()
)
sleV2PPPoEFilterControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterControlId.setStatus("current")


class _SleV2PPPoEFilterControlPortIndex_Type(Integer32):
    """Custom type sleV2PPPoEFilterControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_SleV2PPPoEFilterControlPortIndex_Type.__name__ = "Integer32"
_SleV2PPPoEFilterControlPortIndex_Object = MibScalar
sleV2PPPoEFilterControlPortIndex = _SleV2PPPoEFilterControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 2, 7),
    _SleV2PPPoEFilterControlPortIndex_Type()
)
sleV2PPPoEFilterControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterControlPortIndex.setStatus("current")


class _SleV2PPPoEFilterControlVlanId_Type(Integer32):
    """Custom type sleV2PPPoEFilterControlVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_SleV2PPPoEFilterControlVlanId_Type.__name__ = "Integer32"
_SleV2PPPoEFilterControlVlanId_Object = MibScalar
sleV2PPPoEFilterControlVlanId = _SleV2PPPoEFilterControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 2, 8),
    _SleV2PPPoEFilterControlVlanId_Type()
)
sleV2PPPoEFilterControlVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterControlVlanId.setStatus("current")


class _SleV2PPPoEFilterControlAction_Type(Integer32):
    """Custom type sleV2PPPoEFilterControlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("permit", 2))
    )


_SleV2PPPoEFilterControlAction_Type.__name__ = "Integer32"
_SleV2PPPoEFilterControlAction_Object = MibScalar
sleV2PPPoEFilterControlAction = _SleV2PPPoEFilterControlAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 2, 9),
    _SleV2PPPoEFilterControlAction_Type()
)
sleV2PPPoEFilterControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoEFilterControlAction.setStatus("current")
_SleV2PPPoEFilterNotification_ObjectIdentity = ObjectIdentity
sleV2PPPoEFilterNotification = _SleV2PPPoEFilterNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 4)
)
_SleV2PPPoETag_ObjectIdentity = ObjectIdentity
sleV2PPPoETag = _SleV2PPPoETag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3)
)
_SleV2PPPoETagOper_ObjectIdentity = ObjectIdentity
sleV2PPPoETagOper = _SleV2PPPoETagOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1)
)
_SleV2PPPoETagOperTable_Object = MibTable
sleV2PPPoETagOperTable = _SleV2PPPoETagOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2PPPoETagOperTable.setStatus("current")
_SleV2PPPoETagOperEntry_Object = MibTableRow
sleV2PPPoETagOperEntry = _SleV2PPPoETagOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 1, 1)
)
sleV2PPPoETagOperEntry.setIndexNames(
    (0, "SLEV2-PPPoE-MIB", "sleV2PPPoETagOperId"),
    (0, "SLEV2-PPPoE-MIB", "sleV2PPPoETagOperVlanId"),
    (0, "SLEV2-PPPoE-MIB", "sleV2PPPoETagOperPortIndex"),
)
if mibBuilder.loadTexts:
    sleV2PPPoETagOperEntry.setStatus("current")


class _SleV2PPPoETagOperId_Type(Integer32):
    """Custom type sleV2PPPoETagOperId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleV2PPPoETagOperId_Type.__name__ = "Integer32"
_SleV2PPPoETagOperId_Object = MibTableColumn
sleV2PPPoETagOperId = _SleV2PPPoETagOperId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 1, 1, 1),
    _SleV2PPPoETagOperId_Type()
)
sleV2PPPoETagOperId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperId.setStatus("current")
_SleV2PPPoETagOperType_Type = OctetString
_SleV2PPPoETagOperType_Object = MibTableColumn
sleV2PPPoETagOperType = _SleV2PPPoETagOperType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 1, 1, 2),
    _SleV2PPPoETagOperType_Type()
)
sleV2PPPoETagOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperType.setStatus("current")


class _SleV2PPPoETagOperPortIndex_Type(Integer32):
    """Custom type sleV2PPPoETagOperPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleV2PPPoETagOperPortIndex_Type.__name__ = "Integer32"
_SleV2PPPoETagOperPortIndex_Object = MibTableColumn
sleV2PPPoETagOperPortIndex = _SleV2PPPoETagOperPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 1, 1, 3),
    _SleV2PPPoETagOperPortIndex_Type()
)
sleV2PPPoETagOperPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperPortIndex.setStatus("current")


class _SleV2PPPoETagOperVlanId_Type(Integer32):
    """Custom type sleV2PPPoETagOperVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleV2PPPoETagOperVlanId_Type.__name__ = "Integer32"
_SleV2PPPoETagOperVlanId_Object = MibTableColumn
sleV2PPPoETagOperVlanId = _SleV2PPPoETagOperVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 1, 1, 4),
    _SleV2PPPoETagOperVlanId_Type()
)
sleV2PPPoETagOperVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperVlanId.setStatus("current")


class _SleV2PPPoETagOperAction_Type(Integer32):
    """Custom type sleV2PPPoETagOperAction based on Integer32"""
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
        *(("add", 1),
          ("keep", 2),
          ("remove", 3),
          ("replace", 4),
          ("update", 5))
    )


_SleV2PPPoETagOperAction_Type.__name__ = "Integer32"
_SleV2PPPoETagOperAction_Object = MibTableColumn
sleV2PPPoETagOperAction = _SleV2PPPoETagOperAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 1, 1, 5),
    _SleV2PPPoETagOperAction_Type()
)
sleV2PPPoETagOperAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperAction.setStatus("current")
_SleV2PPPoETagOperTagFmt_Type = OctetString
_SleV2PPPoETagOperTagFmt_Object = MibTableColumn
sleV2PPPoETagOperTagFmt = _SleV2PPPoETagOperTagFmt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 1, 1, 6),
    _SleV2PPPoETagOperTagFmt_Type()
)
sleV2PPPoETagOperTagFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperTagFmt.setStatus("current")
_SleV2PPPoETagOperControl_ObjectIdentity = ObjectIdentity
sleV2PPPoETagOperControl = _SleV2PPPoETagOperControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2)
)


class _SleV2PPPoETagOperControlRequest_Type(Integer32):
    """Custom type sleV2PPPoETagOperControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createPPPoETagOper", 1),
          ("modifyPPPoETagOper", 2),
          ("destroyPPPoETagOper", 3))
    )


_SleV2PPPoETagOperControlRequest_Type.__name__ = "Integer32"
_SleV2PPPoETagOperControlRequest_Object = MibScalar
sleV2PPPoETagOperControlRequest = _SleV2PPPoETagOperControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 1),
    _SleV2PPPoETagOperControlRequest_Type()
)
sleV2PPPoETagOperControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlRequest.setStatus("current")
_SleV2PPPoETagOperControlStatus_Type = SleControlStatusType
_SleV2PPPoETagOperControlStatus_Object = MibScalar
sleV2PPPoETagOperControlStatus = _SleV2PPPoETagOperControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 2),
    _SleV2PPPoETagOperControlStatus_Type()
)
sleV2PPPoETagOperControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlStatus.setStatus("current")
_SleV2PPPoETagOperControlTimer_Type = Gauge32
_SleV2PPPoETagOperControlTimer_Object = MibScalar
sleV2PPPoETagOperControlTimer = _SleV2PPPoETagOperControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 3),
    _SleV2PPPoETagOperControlTimer_Type()
)
sleV2PPPoETagOperControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlTimer.setStatus("current")
_SleV2PPPoETagOperControlTimeStamp_Type = TimeTicks
_SleV2PPPoETagOperControlTimeStamp_Object = MibScalar
sleV2PPPoETagOperControlTimeStamp = _SleV2PPPoETagOperControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 4),
    _SleV2PPPoETagOperControlTimeStamp_Type()
)
sleV2PPPoETagOperControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlTimeStamp.setStatus("current")
_SleV2PPPoETagOperControlReqResult_Type = SleControlRequestResultType
_SleV2PPPoETagOperControlReqResult_Object = MibScalar
sleV2PPPoETagOperControlReqResult = _SleV2PPPoETagOperControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 5),
    _SleV2PPPoETagOperControlReqResult_Type()
)
sleV2PPPoETagOperControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlReqResult.setStatus("current")


class _SleV2PPPoETagOperControlId_Type(Integer32):
    """Custom type sleV2PPPoETagOperControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleV2PPPoETagOperControlId_Type.__name__ = "Integer32"
_SleV2PPPoETagOperControlId_Object = MibScalar
sleV2PPPoETagOperControlId = _SleV2PPPoETagOperControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 6),
    _SleV2PPPoETagOperControlId_Type()
)
sleV2PPPoETagOperControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlId.setStatus("current")
_SleV2PPPoETagOperControlType_Type = OctetString
_SleV2PPPoETagOperControlType_Object = MibScalar
sleV2PPPoETagOperControlType = _SleV2PPPoETagOperControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 7),
    _SleV2PPPoETagOperControlType_Type()
)
sleV2PPPoETagOperControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlType.setStatus("current")


class _SleV2PPPoETagOperControlPortIndex_Type(Integer32):
    """Custom type sleV2PPPoETagOperControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleV2PPPoETagOperControlPortIndex_Type.__name__ = "Integer32"
_SleV2PPPoETagOperControlPortIndex_Object = MibScalar
sleV2PPPoETagOperControlPortIndex = _SleV2PPPoETagOperControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 8),
    _SleV2PPPoETagOperControlPortIndex_Type()
)
sleV2PPPoETagOperControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlPortIndex.setStatus("current")


class _SleV2PPPoETagOperControlVlanId_Type(Integer32):
    """Custom type sleV2PPPoETagOperControlVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SleV2PPPoETagOperControlVlanId_Type.__name__ = "Integer32"
_SleV2PPPoETagOperControlVlanId_Object = MibScalar
sleV2PPPoETagOperControlVlanId = _SleV2PPPoETagOperControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 9),
    _SleV2PPPoETagOperControlVlanId_Type()
)
sleV2PPPoETagOperControlVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlVlanId.setStatus("current")


class _SleV2PPPoETagOperControlAction_Type(Integer32):
    """Custom type sleV2PPPoETagOperControlAction based on Integer32"""
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
        *(("add", 1),
          ("keep", 2),
          ("remove", 3),
          ("replace", 4),
          ("update", 5))
    )


_SleV2PPPoETagOperControlAction_Type.__name__ = "Integer32"
_SleV2PPPoETagOperControlAction_Object = MibScalar
sleV2PPPoETagOperControlAction = _SleV2PPPoETagOperControlAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 10),
    _SleV2PPPoETagOperControlAction_Type()
)
sleV2PPPoETagOperControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlAction.setStatus("current")
_SleV2PPPoETagOperControlTagFmt_Type = OctetString
_SleV2PPPoETagOperControlTagFmt_Object = MibScalar
sleV2PPPoETagOperControlTagFmt = _SleV2PPPoETagOperControlTagFmt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 2, 11),
    _SleV2PPPoETagOperControlTagFmt_Type()
)
sleV2PPPoETagOperControlTagFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagOperControlTagFmt.setStatus("current")
_SleV2PPPoETagOperNotification_ObjectIdentity = ObjectIdentity
sleV2PPPoETagOperNotification = _SleV2PPPoETagOperNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 3)
)
_SleV2PPPoETagFormat_ObjectIdentity = ObjectIdentity
sleV2PPPoETagFormat = _SleV2PPPoETagFormat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2)
)
_SleV2PPPoETagFormatBase_ObjectIdentity = ObjectIdentity
sleV2PPPoETagFormatBase = _SleV2PPPoETagFormatBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1)
)
_SleV2PPPoETagFormatTable_Object = MibTable
sleV2PPPoETagFormatTable = _SleV2PPPoETagFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatTable.setStatus("current")
_SleV2PPPoETagFormatEntry_Object = MibTableRow
sleV2PPPoETagFormatEntry = _SleV2PPPoETagFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 1, 1)
)
sleV2PPPoETagFormatEntry.setIndexNames(
    (0, "SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatName"),
)
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatEntry.setStatus("current")


class _SleV2PPPoETagFormatName_Type(OctetString):
    """Custom type sleV2PPPoETagFormatName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2PPPoETagFormatName_Type.__name__ = "OctetString"
_SleV2PPPoETagFormatName_Object = MibTableColumn
sleV2PPPoETagFormatName = _SleV2PPPoETagFormatName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 1, 1, 1),
    _SleV2PPPoETagFormatName_Type()
)
sleV2PPPoETagFormatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatName.setStatus("current")
_SleV2PPPoETagFormatControl_ObjectIdentity = ObjectIdentity
sleV2PPPoETagFormatControl = _SleV2PPPoETagFormatControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 2)
)


class _SleV2PPPoETagFormatControlRequest_Type(Integer32):
    """Custom type sleV2PPPoETagFormatControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createTagFormat", 1),
          ("destroyTagFormat", 2))
    )


_SleV2PPPoETagFormatControlRequest_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatControlRequest_Object = MibScalar
sleV2PPPoETagFormatControlRequest = _SleV2PPPoETagFormatControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 2, 1),
    _SleV2PPPoETagFormatControlRequest_Type()
)
sleV2PPPoETagFormatControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatControlRequest.setStatus("current")
_SleV2PPPoETagFormatControlStatus_Type = SleControlStatusType
_SleV2PPPoETagFormatControlStatus_Object = MibScalar
sleV2PPPoETagFormatControlStatus = _SleV2PPPoETagFormatControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 2, 2),
    _SleV2PPPoETagFormatControlStatus_Type()
)
sleV2PPPoETagFormatControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatControlStatus.setStatus("current")
_SleV2PPPoETagFormatControlTimer_Type = Gauge32
_SleV2PPPoETagFormatControlTimer_Object = MibScalar
sleV2PPPoETagFormatControlTimer = _SleV2PPPoETagFormatControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 2, 3),
    _SleV2PPPoETagFormatControlTimer_Type()
)
sleV2PPPoETagFormatControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatControlTimer.setStatus("current")
_SleV2PPPoETagFormatControlTimeStamp_Type = TimeTicks
_SleV2PPPoETagFormatControlTimeStamp_Object = MibScalar
sleV2PPPoETagFormatControlTimeStamp = _SleV2PPPoETagFormatControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 2, 4),
    _SleV2PPPoETagFormatControlTimeStamp_Type()
)
sleV2PPPoETagFormatControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatControlTimeStamp.setStatus("current")
_SleV2PPPoETagFormatControlReqResult_Type = SleControlRequestResultType
_SleV2PPPoETagFormatControlReqResult_Object = MibScalar
sleV2PPPoETagFormatControlReqResult = _SleV2PPPoETagFormatControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 2, 5),
    _SleV2PPPoETagFormatControlReqResult_Type()
)
sleV2PPPoETagFormatControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatControlReqResult.setStatus("current")


class _SleV2PPPoETagFormatControlName_Type(OctetString):
    """Custom type sleV2PPPoETagFormatControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2PPPoETagFormatControlName_Type.__name__ = "OctetString"
_SleV2PPPoETagFormatControlName_Object = MibScalar
sleV2PPPoETagFormatControlName = _SleV2PPPoETagFormatControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 2, 6),
    _SleV2PPPoETagFormatControlName_Type()
)
sleV2PPPoETagFormatControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatControlName.setStatus("current")
_SleV2PPPoETagFormatNotification_ObjectIdentity = ObjectIdentity
sleV2PPPoETagFormatNotification = _SleV2PPPoETagFormatNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 3)
)
_SleV2PPPoETagFormatAttribute_ObjectIdentity = ObjectIdentity
sleV2PPPoETagFormatAttribute = _SleV2PPPoETagFormatAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2)
)
_SleV2PPPoETagFormatAttrTable_Object = MibTable
sleV2PPPoETagFormatAttrTable = _SleV2PPPoETagFormatAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrTable.setStatus("current")
_SleV2PPPoETagFormatAttrEntry_Object = MibTableRow
sleV2PPPoETagFormatAttrEntry = _SleV2PPPoETagFormatAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 1, 1)
)
sleV2PPPoETagFormatAttrEntry.setIndexNames(
    (0, "SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatName"),
    (0, "SLEV2-PPPoE-MIB", "sleV2PPPoETagFormattAttrID"),
)
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrEntry.setStatus("current")


class _SleV2PPPoETagFormattAttrID_Type(Integer32):
    """Custom type sleV2PPPoETagFormattAttrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleV2PPPoETagFormattAttrID_Type.__name__ = "Integer32"
_SleV2PPPoETagFormattAttrID_Object = MibTableColumn
sleV2PPPoETagFormattAttrID = _SleV2PPPoETagFormattAttrID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 1, 1, 1),
    _SleV2PPPoETagFormattAttrID_Type()
)
sleV2PPPoETagFormattAttrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormattAttrID.setStatus("current")


class _SleV2PPPoETagFormatAttrLength_Type(Integer32):
    """Custom type sleV2PPPoETagFormatAttrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 128),
    )


_SleV2PPPoETagFormatAttrLength_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatAttrLength_Object = MibTableColumn
sleV2PPPoETagFormatAttrLength = _SleV2PPPoETagFormatAttrLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 1, 1, 2),
    _SleV2PPPoETagFormatAttrLength_Type()
)
sleV2PPPoETagFormatAttrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrLength.setStatus("current")


class _SleV2PPPoETagFormatAttrHiddenLength_Type(Integer32):
    """Custom type sleV2PPPoETagFormatAttrHiddenLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 128),
    )


_SleV2PPPoETagFormatAttrHiddenLength_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatAttrHiddenLength_Object = MibTableColumn
sleV2PPPoETagFormatAttrHiddenLength = _SleV2PPPoETagFormatAttrHiddenLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 1, 1, 3),
    _SleV2PPPoETagFormatAttrHiddenLength_Type()
)
sleV2PPPoETagFormatAttrHiddenLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrHiddenLength.setStatus("current")


class _SleV2PPPoETagFormatAttrType_Type(Integer32):
    """Custom type sleV2PPPoETagFormatAttrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SleV2PPPoETagFormatAttrType_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatAttrType_Object = MibTableColumn
sleV2PPPoETagFormatAttrType = _SleV2PPPoETagFormatAttrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 1, 1, 4),
    _SleV2PPPoETagFormatAttrType_Type()
)
sleV2PPPoETagFormatAttrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrType.setStatus("current")


class _SleV2PPPoETagFormatAttrVarType_Type(Integer32):
    """Custom type sleV2PPPoETagFormatAttrVarType based on Integer32"""
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
        *(("hex", 1),
          ("index", 2),
          ("ip", 3),
          ("string", 4),
          ("tagFmt", 5))
    )


_SleV2PPPoETagFormatAttrVarType_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatAttrVarType_Object = MibTableColumn
sleV2PPPoETagFormatAttrVarType = _SleV2PPPoETagFormatAttrVarType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 1, 1, 5),
    _SleV2PPPoETagFormatAttrVarType_Type()
)
sleV2PPPoETagFormatAttrVarType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrVarType.setStatus("current")


class _SleV2PPPoETagFormatAttrVarValue_Type(OctetString):
    """Custom type sleV2PPPoETagFormatAttrVarValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleV2PPPoETagFormatAttrVarValue_Type.__name__ = "OctetString"
_SleV2PPPoETagFormatAttrVarValue_Object = MibTableColumn
sleV2PPPoETagFormatAttrVarValue = _SleV2PPPoETagFormatAttrVarValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 1, 1, 6),
    _SleV2PPPoETagFormatAttrVarValue_Type()
)
sleV2PPPoETagFormatAttrVarValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrVarValue.setStatus("current")
_SleV2PPPoETagFormatAttrControl_ObjectIdentity = ObjectIdentity
sleV2PPPoETagFormatAttrControl = _SleV2PPPoETagFormatAttrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2)
)


class _SleV2PPPoETagFormatAttrControlRequest_Type(Integer32):
    """Custom type sleV2PPPoETagFormatAttrControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addTagFormatAttr", 1),
          ("deleteTagFormatAttr", 2),
          ("modifyTagFormatAttr", 3))
    )


_SleV2PPPoETagFormatAttrControlRequest_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatAttrControlRequest_Object = MibScalar
sleV2PPPoETagFormatAttrControlRequest = _SleV2PPPoETagFormatAttrControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 1),
    _SleV2PPPoETagFormatAttrControlRequest_Type()
)
sleV2PPPoETagFormatAttrControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlRequest.setStatus("current")
_SleV2PPPoETagFormatAttrControlStatus_Type = SleControlStatusType
_SleV2PPPoETagFormatAttrControlStatus_Object = MibScalar
sleV2PPPoETagFormatAttrControlStatus = _SleV2PPPoETagFormatAttrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 2),
    _SleV2PPPoETagFormatAttrControlStatus_Type()
)
sleV2PPPoETagFormatAttrControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlStatus.setStatus("current")
_SleV2PPPoETagFormatAttrControlTimer_Type = Gauge32
_SleV2PPPoETagFormatAttrControlTimer_Object = MibScalar
sleV2PPPoETagFormatAttrControlTimer = _SleV2PPPoETagFormatAttrControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 3),
    _SleV2PPPoETagFormatAttrControlTimer_Type()
)
sleV2PPPoETagFormatAttrControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlTimer.setStatus("current")
_SleV2PPPoETagFormatAttrControlTimeStamp_Type = TimeTicks
_SleV2PPPoETagFormatAttrControlTimeStamp_Object = MibScalar
sleV2PPPoETagFormatAttrControlTimeStamp = _SleV2PPPoETagFormatAttrControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 4),
    _SleV2PPPoETagFormatAttrControlTimeStamp_Type()
)
sleV2PPPoETagFormatAttrControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlTimeStamp.setStatus("current")
_SleV2PPPoETagFormatAttrControlReqResult_Type = SleControlRequestResultType
_SleV2PPPoETagFormatAttrControlReqResult_Object = MibScalar
sleV2PPPoETagFormatAttrControlReqResult = _SleV2PPPoETagFormatAttrControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 5),
    _SleV2PPPoETagFormatAttrControlReqResult_Type()
)
sleV2PPPoETagFormatAttrControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlReqResult.setStatus("current")


class _SleV2PPPoETagFormatAttrControlName_Type(OctetString):
    """Custom type sleV2PPPoETagFormatAttrControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleV2PPPoETagFormatAttrControlName_Type.__name__ = "OctetString"
_SleV2PPPoETagFormatAttrControlName_Object = MibScalar
sleV2PPPoETagFormatAttrControlName = _SleV2PPPoETagFormatAttrControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 6),
    _SleV2PPPoETagFormatAttrControlName_Type()
)
sleV2PPPoETagFormatAttrControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlName.setStatus("current")


class _SleV2PPPoETagFormatAttrControlID_Type(Integer32):
    """Custom type sleV2PPPoETagFormatAttrControlID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleV2PPPoETagFormatAttrControlID_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatAttrControlID_Object = MibScalar
sleV2PPPoETagFormatAttrControlID = _SleV2PPPoETagFormatAttrControlID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 7),
    _SleV2PPPoETagFormatAttrControlID_Type()
)
sleV2PPPoETagFormatAttrControlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlID.setStatus("current")


class _SleV2PPPoETagFormatAttrControlLength_Type(Integer32):
    """Custom type sleV2PPPoETagFormatAttrControlLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 128),
    )


_SleV2PPPoETagFormatAttrControlLength_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatAttrControlLength_Object = MibScalar
sleV2PPPoETagFormatAttrControlLength = _SleV2PPPoETagFormatAttrControlLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 8),
    _SleV2PPPoETagFormatAttrControlLength_Type()
)
sleV2PPPoETagFormatAttrControlLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlLength.setStatus("current")


class _SleV2PPPoETagFormatAttrControlHiddenLength_Type(Integer32):
    """Custom type sleV2PPPoETagFormatAttrControlHiddenLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 128),
    )


_SleV2PPPoETagFormatAttrControlHiddenLength_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatAttrControlHiddenLength_Object = MibScalar
sleV2PPPoETagFormatAttrControlHiddenLength = _SleV2PPPoETagFormatAttrControlHiddenLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 9),
    _SleV2PPPoETagFormatAttrControlHiddenLength_Type()
)
sleV2PPPoETagFormatAttrControlHiddenLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlHiddenLength.setStatus("current")


class _SleV2PPPoETagFormatAttrControlType_Type(Integer32):
    """Custom type sleV2PPPoETagFormatAttrControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_SleV2PPPoETagFormatAttrControlType_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatAttrControlType_Object = MibScalar
sleV2PPPoETagFormatAttrControlType = _SleV2PPPoETagFormatAttrControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 10),
    _SleV2PPPoETagFormatAttrControlType_Type()
)
sleV2PPPoETagFormatAttrControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlType.setStatus("current")


class _SleV2PPPoETagFormatAttrControlVarType_Type(Integer32):
    """Custom type sleV2PPPoETagFormatAttrControlVarType based on Integer32"""
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
        *(("hex", 1),
          ("index", 2),
          ("ip", 3),
          ("string", 4),
          ("tagFmt", 5))
    )


_SleV2PPPoETagFormatAttrControlVarType_Type.__name__ = "Integer32"
_SleV2PPPoETagFormatAttrControlVarType_Object = MibScalar
sleV2PPPoETagFormatAttrControlVarType = _SleV2PPPoETagFormatAttrControlVarType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 11),
    _SleV2PPPoETagFormatAttrControlVarType_Type()
)
sleV2PPPoETagFormatAttrControlVarType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlVarType.setStatus("current")


class _SleV2PPPoETagFormatAttrControlVarValue_Type(OctetString):
    """Custom type sleV2PPPoETagFormatAttrControlVarValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleV2PPPoETagFormatAttrControlVarValue_Type.__name__ = "OctetString"
_SleV2PPPoETagFormatAttrControlVarValue_Object = MibScalar
sleV2PPPoETagFormatAttrControlVarValue = _SleV2PPPoETagFormatAttrControlVarValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 2, 12),
    _SleV2PPPoETagFormatAttrControlVarValue_Type()
)
sleV2PPPoETagFormatAttrControlVarValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrControlVarValue.setStatus("current")
_SleV2PPPoETagFormatAttrNotification_ObjectIdentity = ObjectIdentity
sleV2PPPoETagFormatAttrNotification = _SleV2PPPoETagFormatAttrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 3)
)

# Managed Objects groups

sleV2PPPoEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 5)
)
sleV2PPPoEGroup.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoEControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEControlStatus"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEControlTimer"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoESnoopingActivity"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEControlSnoopingActivity"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlTimer"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatName"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlStatus"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlName"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlVarType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlHiddenLength"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlLength"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlName"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlID"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlTimer"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlStatus"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrVarValue"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrVarType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrHiddenLength"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrLength"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormattAttrID"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlVarValue"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlAction"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlVlanId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlPortIndex"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlTimer"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlStatus"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperAction"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperVlanId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperPortIndex"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlAction"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlVlanId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlPortIndex"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlTimer"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlStatus"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterVlanId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterPortIndex"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlTagFmt"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperTagFmt"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterAction"))
)
if mibBuilder.loadTexts:
    sleV2PPPoEGroup.setStatus("current")


# Notification objects

sleV2PPPoESnoopingActivityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 1, 3, 1)
)
sleV2PPPoESnoopingActivityChanged.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoEControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEControlSnoopingActivity"))
)
if mibBuilder.loadTexts:
    sleV2PPPoESnoopingActivityChanged.setStatus(
        "current"
    )

sleV2PPPoEFilterCreatedChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 4, 1)
)
sleV2PPPoEFilterCreatedChanged.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlPortIndex"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlVlanId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlAction"))
)
if mibBuilder.loadTexts:
    sleV2PPPoEFilterCreatedChanged.setStatus(
        "current"
    )

sleV2PPPoEFilterModifyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 4, 2)
)
sleV2PPPoEFilterModifyChanged.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlPortIndex"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlVlanId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlAction"))
)
if mibBuilder.loadTexts:
    sleV2PPPoEFilterModifyChanged.setStatus(
        "current"
    )

sleV2PPPoEFilterDestroyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 2, 4, 3)
)
sleV2PPPoEFilterDestroyChanged.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterControlId"))
)
if mibBuilder.loadTexts:
    sleV2PPPoEFilterDestroyChanged.setStatus(
        "current"
    )

sleV2PPPoETagOperCreateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 3, 1)
)
sleV2PPPoETagOperCreateChanged.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlPortIndex"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlVlanId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlAction"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlTagFmt"))
)
if mibBuilder.loadTexts:
    sleV2PPPoETagOperCreateChanged.setStatus(
        "current"
    )

sleV2PPPoETagOperDestroyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 3, 2)
)
sleV2PPPoETagOperDestroyChanged.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlId"))
)
if mibBuilder.loadTexts:
    sleV2PPPoETagOperDestroyChanged.setStatus(
        "current"
    )

sleV2PPPoETagOperModifyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 1, 3, 3)
)
sleV2PPPoETagOperModifyChanged.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlPortIndex"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlVlanId"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlAction"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperControlTagFmt"))
)
if mibBuilder.loadTexts:
    sleV2PPPoETagOperModifyChanged.setStatus(
        "current"
    )

sleV2PPPoETagFormatCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 3, 1)
)
sleV2PPPoETagFormatCreated.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlName"))
)
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatCreated.setStatus(
        "current"
    )

sleV2PPPoETagFormatDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 1, 3, 2)
)
sleV2PPPoETagFormatDestroyed.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatControlName"))
)
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatDestroyed.setStatus(
        "current"
    )

sleV2PPPoETagFormatAttrAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 3, 1)
)
sleV2PPPoETagFormatAttrAdded.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlName"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlID"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlLength"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlHiddenLength"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlVarType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlVarValue"))
)
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrAdded.setStatus(
        "current"
    )

sleV2PPPoETagFormatAttrDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 3, 2)
)
sleV2PPPoETagFormatAttrDeleted.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlName"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlID"))
)
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrDeleted.setStatus(
        "current"
    )

sleV2PPPoETagFormatAttrModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 3, 2, 2, 3, 3)
)
sleV2PPPoETagFormatAttrModified.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlRequest"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlTimeStamp"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlReqResult"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlName"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlID"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlLength"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlHiddenLength"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlVarType"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrControlVarValue"))
)
if mibBuilder.loadTexts:
    sleV2PPPoETagFormatAttrModified.setStatus(
        "current"
    )


# Notifications groups

sleV2PPPoENotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 16, 6)
)
sleV2PPPoENotificationGroup.setObjects(
      *(("SLEV2-PPPoE-MIB", "sleV2PPPoESnoopingActivityChanged"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatDestroyed"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatCreated"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrModified"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrDeleted"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagFormatAttrAdded"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperDestroyChanged"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperCreateChanged"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoETagOperModifyChanged"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterDestroyChanged"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterModifyChanged"),
        ("SLEV2-PPPoE-MIB", "sleV2PPPoEFilterCreatedChanged"))
)
if mibBuilder.loadTexts:
    sleV2PPPoENotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLEV2-PPPoE-MIB",
    **{"Boolean": Boolean,
       "sleV2PPPoE": sleV2PPPoE,
       "sleV2PPPoEBase": sleV2PPPoEBase,
       "sleV2PPPoEInfo": sleV2PPPoEInfo,
       "sleV2PPPoESnoopingActivity": sleV2PPPoESnoopingActivity,
       "sleV2PPPoEControl": sleV2PPPoEControl,
       "sleV2PPPoEControlRequest": sleV2PPPoEControlRequest,
       "sleV2PPPoEControlStatus": sleV2PPPoEControlStatus,
       "sleV2PPPoEControlTimer": sleV2PPPoEControlTimer,
       "sleV2PPPoEControlTimeStamp": sleV2PPPoEControlTimeStamp,
       "sleV2PPPoEControlReqResult": sleV2PPPoEControlReqResult,
       "sleV2PPPoEControlSnoopingActivity": sleV2PPPoEControlSnoopingActivity,
       "sleV2PPPoENotification": sleV2PPPoENotification,
       "sleV2PPPoESnoopingActivityChanged": sleV2PPPoESnoopingActivityChanged,
       "sleV2PPPoEFilter": sleV2PPPoEFilter,
       "sleV2PPPoEFilterTable": sleV2PPPoEFilterTable,
       "sleV2PPPoEFilterEntry": sleV2PPPoEFilterEntry,
       "sleV2PPPoEFilterId": sleV2PPPoEFilterId,
       "sleV2PPPoEFilterPortIndex": sleV2PPPoEFilterPortIndex,
       "sleV2PPPoEFilterVlanId": sleV2PPPoEFilterVlanId,
       "sleV2PPPoEFilterAction": sleV2PPPoEFilterAction,
       "sleV2PPPoEFilterControl": sleV2PPPoEFilterControl,
       "sleV2PPPoEFilterControlRequest": sleV2PPPoEFilterControlRequest,
       "sleV2PPPoEFilterControlStatus": sleV2PPPoEFilterControlStatus,
       "sleV2PPPoEFilterControlTimer": sleV2PPPoEFilterControlTimer,
       "sleV2PPPoEFilterControlTimeStamp": sleV2PPPoEFilterControlTimeStamp,
       "sleV2PPPoEFilterControlReqResult": sleV2PPPoEFilterControlReqResult,
       "sleV2PPPoEFilterControlId": sleV2PPPoEFilterControlId,
       "sleV2PPPoEFilterControlPortIndex": sleV2PPPoEFilterControlPortIndex,
       "sleV2PPPoEFilterControlVlanId": sleV2PPPoEFilterControlVlanId,
       "sleV2PPPoEFilterControlAction": sleV2PPPoEFilterControlAction,
       "sleV2PPPoEFilterNotification": sleV2PPPoEFilterNotification,
       "sleV2PPPoEFilterCreatedChanged": sleV2PPPoEFilterCreatedChanged,
       "sleV2PPPoEFilterModifyChanged": sleV2PPPoEFilterModifyChanged,
       "sleV2PPPoEFilterDestroyChanged": sleV2PPPoEFilterDestroyChanged,
       "sleV2PPPoETag": sleV2PPPoETag,
       "sleV2PPPoETagOper": sleV2PPPoETagOper,
       "sleV2PPPoETagOperTable": sleV2PPPoETagOperTable,
       "sleV2PPPoETagOperEntry": sleV2PPPoETagOperEntry,
       "sleV2PPPoETagOperId": sleV2PPPoETagOperId,
       "sleV2PPPoETagOperType": sleV2PPPoETagOperType,
       "sleV2PPPoETagOperPortIndex": sleV2PPPoETagOperPortIndex,
       "sleV2PPPoETagOperVlanId": sleV2PPPoETagOperVlanId,
       "sleV2PPPoETagOperAction": sleV2PPPoETagOperAction,
       "sleV2PPPoETagOperTagFmt": sleV2PPPoETagOperTagFmt,
       "sleV2PPPoETagOperControl": sleV2PPPoETagOperControl,
       "sleV2PPPoETagOperControlRequest": sleV2PPPoETagOperControlRequest,
       "sleV2PPPoETagOperControlStatus": sleV2PPPoETagOperControlStatus,
       "sleV2PPPoETagOperControlTimer": sleV2PPPoETagOperControlTimer,
       "sleV2PPPoETagOperControlTimeStamp": sleV2PPPoETagOperControlTimeStamp,
       "sleV2PPPoETagOperControlReqResult": sleV2PPPoETagOperControlReqResult,
       "sleV2PPPoETagOperControlId": sleV2PPPoETagOperControlId,
       "sleV2PPPoETagOperControlType": sleV2PPPoETagOperControlType,
       "sleV2PPPoETagOperControlPortIndex": sleV2PPPoETagOperControlPortIndex,
       "sleV2PPPoETagOperControlVlanId": sleV2PPPoETagOperControlVlanId,
       "sleV2PPPoETagOperControlAction": sleV2PPPoETagOperControlAction,
       "sleV2PPPoETagOperControlTagFmt": sleV2PPPoETagOperControlTagFmt,
       "sleV2PPPoETagOperNotification": sleV2PPPoETagOperNotification,
       "sleV2PPPoETagOperCreateChanged": sleV2PPPoETagOperCreateChanged,
       "sleV2PPPoETagOperDestroyChanged": sleV2PPPoETagOperDestroyChanged,
       "sleV2PPPoETagOperModifyChanged": sleV2PPPoETagOperModifyChanged,
       "sleV2PPPoETagFormat": sleV2PPPoETagFormat,
       "sleV2PPPoETagFormatBase": sleV2PPPoETagFormatBase,
       "sleV2PPPoETagFormatTable": sleV2PPPoETagFormatTable,
       "sleV2PPPoETagFormatEntry": sleV2PPPoETagFormatEntry,
       "sleV2PPPoETagFormatName": sleV2PPPoETagFormatName,
       "sleV2PPPoETagFormatControl": sleV2PPPoETagFormatControl,
       "sleV2PPPoETagFormatControlRequest": sleV2PPPoETagFormatControlRequest,
       "sleV2PPPoETagFormatControlStatus": sleV2PPPoETagFormatControlStatus,
       "sleV2PPPoETagFormatControlTimer": sleV2PPPoETagFormatControlTimer,
       "sleV2PPPoETagFormatControlTimeStamp": sleV2PPPoETagFormatControlTimeStamp,
       "sleV2PPPoETagFormatControlReqResult": sleV2PPPoETagFormatControlReqResult,
       "sleV2PPPoETagFormatControlName": sleV2PPPoETagFormatControlName,
       "sleV2PPPoETagFormatNotification": sleV2PPPoETagFormatNotification,
       "sleV2PPPoETagFormatCreated": sleV2PPPoETagFormatCreated,
       "sleV2PPPoETagFormatDestroyed": sleV2PPPoETagFormatDestroyed,
       "sleV2PPPoETagFormatAttribute": sleV2PPPoETagFormatAttribute,
       "sleV2PPPoETagFormatAttrTable": sleV2PPPoETagFormatAttrTable,
       "sleV2PPPoETagFormatAttrEntry": sleV2PPPoETagFormatAttrEntry,
       "sleV2PPPoETagFormattAttrID": sleV2PPPoETagFormattAttrID,
       "sleV2PPPoETagFormatAttrLength": sleV2PPPoETagFormatAttrLength,
       "sleV2PPPoETagFormatAttrHiddenLength": sleV2PPPoETagFormatAttrHiddenLength,
       "sleV2PPPoETagFormatAttrType": sleV2PPPoETagFormatAttrType,
       "sleV2PPPoETagFormatAttrVarType": sleV2PPPoETagFormatAttrVarType,
       "sleV2PPPoETagFormatAttrVarValue": sleV2PPPoETagFormatAttrVarValue,
       "sleV2PPPoETagFormatAttrControl": sleV2PPPoETagFormatAttrControl,
       "sleV2PPPoETagFormatAttrControlRequest": sleV2PPPoETagFormatAttrControlRequest,
       "sleV2PPPoETagFormatAttrControlStatus": sleV2PPPoETagFormatAttrControlStatus,
       "sleV2PPPoETagFormatAttrControlTimer": sleV2PPPoETagFormatAttrControlTimer,
       "sleV2PPPoETagFormatAttrControlTimeStamp": sleV2PPPoETagFormatAttrControlTimeStamp,
       "sleV2PPPoETagFormatAttrControlReqResult": sleV2PPPoETagFormatAttrControlReqResult,
       "sleV2PPPoETagFormatAttrControlName": sleV2PPPoETagFormatAttrControlName,
       "sleV2PPPoETagFormatAttrControlID": sleV2PPPoETagFormatAttrControlID,
       "sleV2PPPoETagFormatAttrControlLength": sleV2PPPoETagFormatAttrControlLength,
       "sleV2PPPoETagFormatAttrControlHiddenLength": sleV2PPPoETagFormatAttrControlHiddenLength,
       "sleV2PPPoETagFormatAttrControlType": sleV2PPPoETagFormatAttrControlType,
       "sleV2PPPoETagFormatAttrControlVarType": sleV2PPPoETagFormatAttrControlVarType,
       "sleV2PPPoETagFormatAttrControlVarValue": sleV2PPPoETagFormatAttrControlVarValue,
       "sleV2PPPoETagFormatAttrNotification": sleV2PPPoETagFormatAttrNotification,
       "sleV2PPPoETagFormatAttrAdded": sleV2PPPoETagFormatAttrAdded,
       "sleV2PPPoETagFormatAttrDeleted": sleV2PPPoETagFormatAttrDeleted,
       "sleV2PPPoETagFormatAttrModified": sleV2PPPoETagFormatAttrModified,
       "sleV2PPPoEGroup": sleV2PPPoEGroup,
       "sleV2PPPoENotificationGroup": sleV2PPPoENotificationGroup}
)
