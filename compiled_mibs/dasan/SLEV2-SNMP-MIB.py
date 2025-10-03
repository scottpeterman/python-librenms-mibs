# SNMP MIB module (SLEV2-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLEV2-SNMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:14 2025
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

sleV2Snmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleV2SnmpBase_ObjectIdentity = ObjectIdentity
sleV2SnmpBase = _SleV2SnmpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1)
)
_SleV2SnmpBaseInfo_ObjectIdentity = ObjectIdentity
sleV2SnmpBaseInfo = _SleV2SnmpBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1)
)
_SleV2SnmpBaseAgentAddrType_Type = InetAddressType
_SleV2SnmpBaseAgentAddrType_Object = MibScalar
sleV2SnmpBaseAgentAddrType = _SleV2SnmpBaseAgentAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 1),
    _SleV2SnmpBaseAgentAddrType_Type()
)
sleV2SnmpBaseAgentAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseAgentAddrType.setStatus("current")
_SleV2SnmpBaseAgentAddrValue_Type = InetAddress
_SleV2SnmpBaseAgentAddrValue_Object = MibScalar
sleV2SnmpBaseAgentAddrValue = _SleV2SnmpBaseAgentAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 2),
    _SleV2SnmpBaseAgentAddrValue_Type()
)
sleV2SnmpBaseAgentAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseAgentAddrValue.setStatus("current")
_SleV2SnmpBaseContacts_Type = OctetString
_SleV2SnmpBaseContacts_Object = MibScalar
sleV2SnmpBaseContacts = _SleV2SnmpBaseContacts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 3),
    _SleV2SnmpBaseContacts_Type()
)
sleV2SnmpBaseContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseContacts.setStatus("current")


class _SleV2SnmpBaseEngineIdType_Type(Integer32):
    """Custom type sleV2SnmpBaseEngineIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("text", 2))
    )


_SleV2SnmpBaseEngineIdType_Type.__name__ = "Integer32"
_SleV2SnmpBaseEngineIdType_Object = MibScalar
sleV2SnmpBaseEngineIdType = _SleV2SnmpBaseEngineIdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 4),
    _SleV2SnmpBaseEngineIdType_Type()
)
sleV2SnmpBaseEngineIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseEngineIdType.setStatus("current")
_SleV2SnmpBaseEngineIdValue_Type = OctetString
_SleV2SnmpBaseEngineIdValue_Object = MibScalar
sleV2SnmpBaseEngineIdValue = _SleV2SnmpBaseEngineIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 5),
    _SleV2SnmpBaseEngineIdValue_Type()
)
sleV2SnmpBaseEngineIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseEngineIdValue.setStatus("current")
_SleV2SnmpBaseLocation_Type = OctetString
_SleV2SnmpBaseLocation_Object = MibScalar
sleV2SnmpBaseLocation = _SleV2SnmpBaseLocation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 6),
    _SleV2SnmpBaseLocation_Type()
)
sleV2SnmpBaseLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseLocation.setStatus("current")


class _SleV2SnmpBaseLogStatus_Type(Integer32):
    """Custom type sleV2SnmpBaseLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("volatile", 0),
          ("nonvolatile", 1))
    )


_SleV2SnmpBaseLogStatus_Type.__name__ = "Integer32"
_SleV2SnmpBaseLogStatus_Object = MibScalar
sleV2SnmpBaseLogStatus = _SleV2SnmpBaseLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 7),
    _SleV2SnmpBaseLogStatus_Type()
)
sleV2SnmpBaseLogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseLogStatus.setStatus("current")


class _SleV2SnmpBaseTrapLogStatus_Type(Integer32):
    """Custom type sleV2SnmpBaseTrapLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("volatile", 0),
          ("nonvolatile", 1))
    )


_SleV2SnmpBaseTrapLogStatus_Type.__name__ = "Integer32"
_SleV2SnmpBaseTrapLogStatus_Object = MibScalar
sleV2SnmpBaseTrapLogStatus = _SleV2SnmpBaseTrapLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 8),
    _SleV2SnmpBaseTrapLogStatus_Type()
)
sleV2SnmpBaseTrapLogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseTrapLogStatus.setStatus("current")
_SleV2SnmpBaseTrapLogThreshold_Type = Integer32
_SleV2SnmpBaseTrapLogThreshold_Object = MibScalar
sleV2SnmpBaseTrapLogThreshold = _SleV2SnmpBaseTrapLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 9),
    _SleV2SnmpBaseTrapLogThreshold_Type()
)
sleV2SnmpBaseTrapLogThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseTrapLogThreshold.setStatus("current")


class _SleV2SnmpBaseTrapMode_Type(Integer32):
    """Custom type sleV2SnmpBaseTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("event", 0),
          ("alarmReport", 1))
    )


_SleV2SnmpBaseTrapMode_Type.__name__ = "Integer32"
_SleV2SnmpBaseTrapMode_Object = MibScalar
sleV2SnmpBaseTrapMode = _SleV2SnmpBaseTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 10),
    _SleV2SnmpBaseTrapMode_Type()
)
sleV2SnmpBaseTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseTrapMode.setStatus("current")
_SleV2SnmpBaseVrfName_Type = OctetString
_SleV2SnmpBaseVrfName_Object = MibScalar
sleV2SnmpBaseVrfName = _SleV2SnmpBaseVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 1, 11),
    _SleV2SnmpBaseVrfName_Type()
)
sleV2SnmpBaseVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseVrfName.setStatus("current")
_SleV2SnmpBaseControl_ObjectIdentity = ObjectIdentity
sleV2SnmpBaseControl = _SleV2SnmpBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2)
)


class _SleV2SnmpBaseControlRequest_Type(Integer32):
    """Custom type sleV2SnmpBaseControlRequest based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("resetSnmp", 1),
          ("clearSnmpAlarmHistory", 2),
          ("clearSnmpAlarmReport", 3),
          ("clearSnmpLog", 4),
          ("clearSnmpTrapLog", 5),
          ("setSnmpAgentAddr", 6),
          ("unsetSnmpAgentAddr", 7),
          ("setSnmpContacts", 8),
          ("unsetSnmpContacts", 9),
          ("setSnmpLocation", 10),
          ("unsetSnmpLocation", 11),
          ("setSnmpTrapLogStatus", 12),
          ("setSnmpTrapMode", 13),
          ("setSnmpEngineId", 14),
          ("unsetSnmpEngineId", 15),
          ("setSnmpLogStatus", 16),
          ("setSnmpVrf", 17),
          ("unsetSnmpVrf", 18))
    )


_SleV2SnmpBaseControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpBaseControlRequest_Object = MibScalar
sleV2SnmpBaseControlRequest = _SleV2SnmpBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 1),
    _SleV2SnmpBaseControlRequest_Type()
)
sleV2SnmpBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlRequest.setStatus("current")
_SleV2SnmpBaseControlStatus_Type = SleControlStatusType
_SleV2SnmpBaseControlStatus_Object = MibScalar
sleV2SnmpBaseControlStatus = _SleV2SnmpBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 2),
    _SleV2SnmpBaseControlStatus_Type()
)
sleV2SnmpBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlStatus.setStatus("current")
_SleV2SnmpBaseControlTimer_Type = Gauge32
_SleV2SnmpBaseControlTimer_Object = MibScalar
sleV2SnmpBaseControlTimer = _SleV2SnmpBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 3),
    _SleV2SnmpBaseControlTimer_Type()
)
sleV2SnmpBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlTimer.setStatus("current")
_SleV2SnmpBaseControlTimeStamp_Type = TimeTicks
_SleV2SnmpBaseControlTimeStamp_Object = MibScalar
sleV2SnmpBaseControlTimeStamp = _SleV2SnmpBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 4),
    _SleV2SnmpBaseControlTimeStamp_Type()
)
sleV2SnmpBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlTimeStamp.setStatus("current")
_SleV2SnmpBaseControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpBaseControlReqResult_Object = MibScalar
sleV2SnmpBaseControlReqResult = _SleV2SnmpBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 5),
    _SleV2SnmpBaseControlReqResult_Type()
)
sleV2SnmpBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlReqResult.setStatus("current")
_SleV2SnmpBaseControlAgentAddrType_Type = InetAddressType
_SleV2SnmpBaseControlAgentAddrType_Object = MibScalar
sleV2SnmpBaseControlAgentAddrType = _SleV2SnmpBaseControlAgentAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 6),
    _SleV2SnmpBaseControlAgentAddrType_Type()
)
sleV2SnmpBaseControlAgentAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlAgentAddrType.setStatus("current")
_SleV2SnmpBaseControlAgentAddrValue_Type = InetAddress
_SleV2SnmpBaseControlAgentAddrValue_Object = MibScalar
sleV2SnmpBaseControlAgentAddrValue = _SleV2SnmpBaseControlAgentAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 7),
    _SleV2SnmpBaseControlAgentAddrValue_Type()
)
sleV2SnmpBaseControlAgentAddrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlAgentAddrValue.setStatus("current")
_SleV2SnmpBaseControlContacts_Type = OctetString
_SleV2SnmpBaseControlContacts_Object = MibScalar
sleV2SnmpBaseControlContacts = _SleV2SnmpBaseControlContacts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 8),
    _SleV2SnmpBaseControlContacts_Type()
)
sleV2SnmpBaseControlContacts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlContacts.setStatus("current")


class _SleV2SnmpBaseControlEngineIdType_Type(Integer32):
    """Custom type sleV2SnmpBaseControlEngineIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("text", 2))
    )


_SleV2SnmpBaseControlEngineIdType_Type.__name__ = "Integer32"
_SleV2SnmpBaseControlEngineIdType_Object = MibScalar
sleV2SnmpBaseControlEngineIdType = _SleV2SnmpBaseControlEngineIdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 9),
    _SleV2SnmpBaseControlEngineIdType_Type()
)
sleV2SnmpBaseControlEngineIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlEngineIdType.setStatus("current")
_SleV2SnmpBaseControlEngineIdValue_Type = OctetString
_SleV2SnmpBaseControlEngineIdValue_Object = MibScalar
sleV2SnmpBaseControlEngineIdValue = _SleV2SnmpBaseControlEngineIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 10),
    _SleV2SnmpBaseControlEngineIdValue_Type()
)
sleV2SnmpBaseControlEngineIdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlEngineIdValue.setStatus("current")
_SleV2SnmpBaseControlLocation_Type = OctetString
_SleV2SnmpBaseControlLocation_Object = MibScalar
sleV2SnmpBaseControlLocation = _SleV2SnmpBaseControlLocation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 11),
    _SleV2SnmpBaseControlLocation_Type()
)
sleV2SnmpBaseControlLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlLocation.setStatus("current")


class _SleV2SnmpBaseControlLogStatus_Type(Integer32):
    """Custom type sleV2SnmpBaseControlLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("volatile", 0),
          ("nonvolatile", 1))
    )


_SleV2SnmpBaseControlLogStatus_Type.__name__ = "Integer32"
_SleV2SnmpBaseControlLogStatus_Object = MibScalar
sleV2SnmpBaseControlLogStatus = _SleV2SnmpBaseControlLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 12),
    _SleV2SnmpBaseControlLogStatus_Type()
)
sleV2SnmpBaseControlLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlLogStatus.setStatus("current")


class _SleV2SnmpBaseControlTrapLogStatus_Type(Integer32):
    """Custom type sleV2SnmpBaseControlTrapLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("volatile", 0),
          ("nonvolatile", 1))
    )


_SleV2SnmpBaseControlTrapLogStatus_Type.__name__ = "Integer32"
_SleV2SnmpBaseControlTrapLogStatus_Object = MibScalar
sleV2SnmpBaseControlTrapLogStatus = _SleV2SnmpBaseControlTrapLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 13),
    _SleV2SnmpBaseControlTrapLogStatus_Type()
)
sleV2SnmpBaseControlTrapLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlTrapLogStatus.setStatus("current")
_SleV2SnmpBaseControlTrapLogThreshold_Type = Integer32
_SleV2SnmpBaseControlTrapLogThreshold_Object = MibScalar
sleV2SnmpBaseControlTrapLogThreshold = _SleV2SnmpBaseControlTrapLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 14),
    _SleV2SnmpBaseControlTrapLogThreshold_Type()
)
sleV2SnmpBaseControlTrapLogThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlTrapLogThreshold.setStatus("current")


class _SleV2SnmpBaseControlTrapMode_Type(Integer32):
    """Custom type sleV2SnmpBaseControlTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("event", 0),
          ("alarmReport", 1))
    )


_SleV2SnmpBaseControlTrapMode_Type.__name__ = "Integer32"
_SleV2SnmpBaseControlTrapMode_Object = MibScalar
sleV2SnmpBaseControlTrapMode = _SleV2SnmpBaseControlTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 15),
    _SleV2SnmpBaseControlTrapMode_Type()
)
sleV2SnmpBaseControlTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlTrapMode.setStatus("current")
_SleV2SnmpBaseControlVrfName_Type = OctetString
_SleV2SnmpBaseControlVrfName_Object = MibScalar
sleV2SnmpBaseControlVrfName = _SleV2SnmpBaseControlVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 2, 16),
    _SleV2SnmpBaseControlVrfName_Type()
)
sleV2SnmpBaseControlVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpBaseControlVrfName.setStatus("current")
_SleV2SnmpBaseNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpBaseNotification = _SleV2SnmpBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3)
)
_SleV2SnmpAccess_ObjectIdentity = ObjectIdentity
sleV2SnmpAccess = _SleV2SnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2)
)
_SleV2SnmpAccessTable_Object = MibTable
sleV2SnmpAccessTable = _SleV2SnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2SnmpAccessTable.setStatus("current")
_SleV2SnmpAccessEntry_Object = MibTableRow
sleV2SnmpAccessEntry = _SleV2SnmpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 1, 1)
)
sleV2SnmpAccessEntry.setIndexNames(
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpAccessGroupName"),
)
if mibBuilder.loadTexts:
    sleV2SnmpAccessEntry.setStatus("current")
_SleV2SnmpAccessGroupName_Type = OctetString
_SleV2SnmpAccessGroupName_Object = MibTableColumn
sleV2SnmpAccessGroupName = _SleV2SnmpAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 1, 1, 1),
    _SleV2SnmpAccessGroupName_Type()
)
sleV2SnmpAccessGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpAccessGroupName.setStatus("current")


class _SleV2SnmpAccessSecurityModel_Type(Integer32):
    """Custom type sleV2SnmpAccessSecurityModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SleV2SnmpAccessSecurityModel_Type.__name__ = "Integer32"
_SleV2SnmpAccessSecurityModel_Object = MibTableColumn
sleV2SnmpAccessSecurityModel = _SleV2SnmpAccessSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 1, 1, 2),
    _SleV2SnmpAccessSecurityModel_Type()
)
sleV2SnmpAccessSecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpAccessSecurityModel.setStatus("current")


class _SleV2SnmpAccessSecurityLevel_Type(Integer32):
    """Custom type sleV2SnmpAccessSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noauth", 1),
          ("auth", 2),
          ("priv", 3))
    )


_SleV2SnmpAccessSecurityLevel_Type.__name__ = "Integer32"
_SleV2SnmpAccessSecurityLevel_Object = MibTableColumn
sleV2SnmpAccessSecurityLevel = _SleV2SnmpAccessSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 1, 1, 3),
    _SleV2SnmpAccessSecurityLevel_Type()
)
sleV2SnmpAccessSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpAccessSecurityLevel.setStatus("current")
_SleV2SnmpAccessReadViewName_Type = OctetString
_SleV2SnmpAccessReadViewName_Object = MibTableColumn
sleV2SnmpAccessReadViewName = _SleV2SnmpAccessReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 1, 1, 4),
    _SleV2SnmpAccessReadViewName_Type()
)
sleV2SnmpAccessReadViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpAccessReadViewName.setStatus("current")
_SleV2SnmpAccessWriteViewName_Type = OctetString
_SleV2SnmpAccessWriteViewName_Object = MibTableColumn
sleV2SnmpAccessWriteViewName = _SleV2SnmpAccessWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 1, 1, 5),
    _SleV2SnmpAccessWriteViewName_Type()
)
sleV2SnmpAccessWriteViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpAccessWriteViewName.setStatus("current")
_SleV2SnmpAccessNotifyViewName_Type = OctetString
_SleV2SnmpAccessNotifyViewName_Object = MibTableColumn
sleV2SnmpAccessNotifyViewName = _SleV2SnmpAccessNotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 1, 1, 6),
    _SleV2SnmpAccessNotifyViewName_Type()
)
sleV2SnmpAccessNotifyViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpAccessNotifyViewName.setStatus("current")
_SleV2SnmpAccessControl_ObjectIdentity = ObjectIdentity
sleV2SnmpAccessControl = _SleV2SnmpAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2)
)


class _SleV2SnmpAccessControlRequest_Type(Integer32):
    """Custom type sleV2SnmpAccessControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createAccess", 1),
          ("deleteAccess", 2),
          ("setAccessProfile", 3))
    )


_SleV2SnmpAccessControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpAccessControlRequest_Object = MibScalar
sleV2SnmpAccessControlRequest = _SleV2SnmpAccessControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 1),
    _SleV2SnmpAccessControlRequest_Type()
)
sleV2SnmpAccessControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlRequest.setStatus("current")
_SleV2SnmpAccessControlStatus_Type = SleControlStatusType
_SleV2SnmpAccessControlStatus_Object = MibScalar
sleV2SnmpAccessControlStatus = _SleV2SnmpAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 2),
    _SleV2SnmpAccessControlStatus_Type()
)
sleV2SnmpAccessControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlStatus.setStatus("current")
_SleV2SnmpAccessControlTimer_Type = Gauge32
_SleV2SnmpAccessControlTimer_Object = MibScalar
sleV2SnmpAccessControlTimer = _SleV2SnmpAccessControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 3),
    _SleV2SnmpAccessControlTimer_Type()
)
sleV2SnmpAccessControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlTimer.setStatus("current")
_SleV2SnmpAccessControlTimeStamp_Type = TimeTicks
_SleV2SnmpAccessControlTimeStamp_Object = MibScalar
sleV2SnmpAccessControlTimeStamp = _SleV2SnmpAccessControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 4),
    _SleV2SnmpAccessControlTimeStamp_Type()
)
sleV2SnmpAccessControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlTimeStamp.setStatus("current")
_SleV2SnmpAccessControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpAccessControlReqResult_Object = MibScalar
sleV2SnmpAccessControlReqResult = _SleV2SnmpAccessControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 5),
    _SleV2SnmpAccessControlReqResult_Type()
)
sleV2SnmpAccessControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlReqResult.setStatus("current")
_SleV2SnmpAccessControlGroupName_Type = OctetString
_SleV2SnmpAccessControlGroupName_Object = MibScalar
sleV2SnmpAccessControlGroupName = _SleV2SnmpAccessControlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 6),
    _SleV2SnmpAccessControlGroupName_Type()
)
sleV2SnmpAccessControlGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlGroupName.setStatus("current")


class _SleV2SnmpAccessControlSecurityModel_Type(Integer32):
    """Custom type sleV2SnmpAccessControlSecurityModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SleV2SnmpAccessControlSecurityModel_Type.__name__ = "Integer32"
_SleV2SnmpAccessControlSecurityModel_Object = MibScalar
sleV2SnmpAccessControlSecurityModel = _SleV2SnmpAccessControlSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 7),
    _SleV2SnmpAccessControlSecurityModel_Type()
)
sleV2SnmpAccessControlSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlSecurityModel.setStatus("current")


class _SleV2SnmpAccessControlSecurityLevel_Type(Integer32):
    """Custom type sleV2SnmpAccessControlSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noauth", 1),
          ("auth", 2),
          ("priv", 3))
    )


_SleV2SnmpAccessControlSecurityLevel_Type.__name__ = "Integer32"
_SleV2SnmpAccessControlSecurityLevel_Object = MibScalar
sleV2SnmpAccessControlSecurityLevel = _SleV2SnmpAccessControlSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 8),
    _SleV2SnmpAccessControlSecurityLevel_Type()
)
sleV2SnmpAccessControlSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlSecurityLevel.setStatus("current")
_SleV2SnmpAccessControlReadViewName_Type = OctetString
_SleV2SnmpAccessControlReadViewName_Object = MibScalar
sleV2SnmpAccessControlReadViewName = _SleV2SnmpAccessControlReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 9),
    _SleV2SnmpAccessControlReadViewName_Type()
)
sleV2SnmpAccessControlReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlReadViewName.setStatus("current")
_SleV2SnmpAccessControlWriteViewName_Type = OctetString
_SleV2SnmpAccessControlWriteViewName_Object = MibScalar
sleV2SnmpAccessControlWriteViewName = _SleV2SnmpAccessControlWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 10),
    _SleV2SnmpAccessControlWriteViewName_Type()
)
sleV2SnmpAccessControlWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlWriteViewName.setStatus("current")
_SleV2SnmpAccessControlNotifyViewName_Type = OctetString
_SleV2SnmpAccessControlNotifyViewName_Object = MibScalar
sleV2SnmpAccessControlNotifyViewName = _SleV2SnmpAccessControlNotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 2, 11),
    _SleV2SnmpAccessControlNotifyViewName_Type()
)
sleV2SnmpAccessControlNotifyViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpAccessControlNotifyViewName.setStatus("current")
_SleV2SnmpAccessNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpAccessNotification = _SleV2SnmpAccessNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 3)
)
_SleV2SnmpCom2sec_ObjectIdentity = ObjectIdentity
sleV2SnmpCom2sec = _SleV2SnmpCom2sec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3)
)
_SleV2SnmpCom2secTable_Object = MibTable
sleV2SnmpCom2secTable = _SleV2SnmpCom2secTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 1)
)
if mibBuilder.loadTexts:
    sleV2SnmpCom2secTable.setStatus("current")
_SleV2SnmpCom2secEntry_Object = MibTableRow
sleV2SnmpCom2secEntry = _SleV2SnmpCom2secEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 1, 1)
)
sleV2SnmpCom2secEntry.setIndexNames(
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpCom2secName"),
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpCom2secAddrType"),
)
if mibBuilder.loadTexts:
    sleV2SnmpCom2secEntry.setStatus("current")
_SleV2SnmpCom2secName_Type = OctetString
_SleV2SnmpCom2secName_Object = MibTableColumn
sleV2SnmpCom2secName = _SleV2SnmpCom2secName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 1, 1, 1),
    _SleV2SnmpCom2secName_Type()
)
sleV2SnmpCom2secName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secName.setStatus("current")
_SleV2SnmpCom2secAddrType_Type = InetAddressType
_SleV2SnmpCom2secAddrType_Object = MibTableColumn
sleV2SnmpCom2secAddrType = _SleV2SnmpCom2secAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 1, 1, 2),
    _SleV2SnmpCom2secAddrType_Type()
)
sleV2SnmpCom2secAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secAddrType.setStatus("current")
_SleV2SnmpCom2secAddrValue_Type = InetAddress
_SleV2SnmpCom2secAddrValue_Object = MibTableColumn
sleV2SnmpCom2secAddrValue = _SleV2SnmpCom2secAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 1, 1, 3),
    _SleV2SnmpCom2secAddrValue_Type()
)
sleV2SnmpCom2secAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secAddrValue.setStatus("current")
_SleV2SnmpCom2secPrefixLen_Type = InetAddressPrefixLength
_SleV2SnmpCom2secPrefixLen_Object = MibTableColumn
sleV2SnmpCom2secPrefixLen = _SleV2SnmpCom2secPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 1, 1, 4),
    _SleV2SnmpCom2secPrefixLen_Type()
)
sleV2SnmpCom2secPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secPrefixLen.setStatus("current")
_SleV2SnmpCom2secCommunity_Type = OctetString
_SleV2SnmpCom2secCommunity_Object = MibTableColumn
sleV2SnmpCom2secCommunity = _SleV2SnmpCom2secCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 1, 1, 5),
    _SleV2SnmpCom2secCommunity_Type()
)
sleV2SnmpCom2secCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secCommunity.setStatus("current")
_SleV2SnmpCom2secControl_ObjectIdentity = ObjectIdentity
sleV2SnmpCom2secControl = _SleV2SnmpCom2secControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2)
)


class _SleV2SnmpCom2secControlRequest_Type(Integer32):
    """Custom type sleV2SnmpCom2secControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createCom2sec", 1),
          ("deleteCom2sec", 2),
          ("changeCom2sec", 3))
    )


_SleV2SnmpCom2secControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpCom2secControlRequest_Object = MibScalar
sleV2SnmpCom2secControlRequest = _SleV2SnmpCom2secControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2, 1),
    _SleV2SnmpCom2secControlRequest_Type()
)
sleV2SnmpCom2secControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secControlRequest.setStatus("current")
_SleV2SnmpCom2secControlStatus_Type = SleControlStatusType
_SleV2SnmpCom2secControlStatus_Object = MibScalar
sleV2SnmpCom2secControlStatus = _SleV2SnmpCom2secControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2, 2),
    _SleV2SnmpCom2secControlStatus_Type()
)
sleV2SnmpCom2secControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secControlStatus.setStatus("current")
_SleV2SnmpCom2secControlTimer_Type = Gauge32
_SleV2SnmpCom2secControlTimer_Object = MibScalar
sleV2SnmpCom2secControlTimer = _SleV2SnmpCom2secControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2, 3),
    _SleV2SnmpCom2secControlTimer_Type()
)
sleV2SnmpCom2secControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secControlTimer.setStatus("current")
_SleV2SnmpCom2secControlTimeStamp_Type = TimeTicks
_SleV2SnmpCom2secControlTimeStamp_Object = MibScalar
sleV2SnmpCom2secControlTimeStamp = _SleV2SnmpCom2secControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2, 4),
    _SleV2SnmpCom2secControlTimeStamp_Type()
)
sleV2SnmpCom2secControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secControlTimeStamp.setStatus("current")
_SleV2SnmpCom2secControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpCom2secControlReqResult_Object = MibScalar
sleV2SnmpCom2secControlReqResult = _SleV2SnmpCom2secControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2, 5),
    _SleV2SnmpCom2secControlReqResult_Type()
)
sleV2SnmpCom2secControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secControlReqResult.setStatus("current")
_SleV2SnmpCom2secControlName_Type = OctetString
_SleV2SnmpCom2secControlName_Object = MibScalar
sleV2SnmpCom2secControlName = _SleV2SnmpCom2secControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2, 6),
    _SleV2SnmpCom2secControlName_Type()
)
sleV2SnmpCom2secControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secControlName.setStatus("current")
_SleV2SnmpCom2secControlAddrType_Type = InetAddressType
_SleV2SnmpCom2secControlAddrType_Object = MibScalar
sleV2SnmpCom2secControlAddrType = _SleV2SnmpCom2secControlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2, 7),
    _SleV2SnmpCom2secControlAddrType_Type()
)
sleV2SnmpCom2secControlAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secControlAddrType.setStatus("current")
_SleV2SnmpCom2secControlAddrValue_Type = InetAddress
_SleV2SnmpCom2secControlAddrValue_Object = MibScalar
sleV2SnmpCom2secControlAddrValue = _SleV2SnmpCom2secControlAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2, 8),
    _SleV2SnmpCom2secControlAddrValue_Type()
)
sleV2SnmpCom2secControlAddrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secControlAddrValue.setStatus("current")
_SleV2SnmpCom2secControlPrefixLen_Type = InetAddressPrefixLength
_SleV2SnmpCom2secControlPrefixLen_Object = MibScalar
sleV2SnmpCom2secControlPrefixLen = _SleV2SnmpCom2secControlPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2, 9),
    _SleV2SnmpCom2secControlPrefixLen_Type()
)
sleV2SnmpCom2secControlPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secControlPrefixLen.setStatus("current")
_SleV2SnmpCom2secControlCommunity_Type = OctetString
_SleV2SnmpCom2secControlCommunity_Object = MibScalar
sleV2SnmpCom2secControlCommunity = _SleV2SnmpCom2secControlCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 2, 10),
    _SleV2SnmpCom2secControlCommunity_Type()
)
sleV2SnmpCom2secControlCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCom2secControlCommunity.setStatus("current")
_SleV2SnmpCom2secNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpCom2secNotification = _SleV2SnmpCom2secNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 3)
)
_SleV2SnmpCommunity_ObjectIdentity = ObjectIdentity
sleV2SnmpCommunity = _SleV2SnmpCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4)
)
_SleV2SnmpCommunityTable_Object = MibTable
sleV2SnmpCommunityTable = _SleV2SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 1)
)
if mibBuilder.loadTexts:
    sleV2SnmpCommunityTable.setStatus("current")
_SleV2SnmpCommunityEntry_Object = MibTableRow
sleV2SnmpCommunityEntry = _SleV2SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 1, 1)
)
sleV2SnmpCommunityEntry.setIndexNames(
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpCommunityValue"),
)
if mibBuilder.loadTexts:
    sleV2SnmpCommunityEntry.setStatus("current")
_SleV2SnmpCommunityValue_Type = OctetString
_SleV2SnmpCommunityValue_Object = MibTableColumn
sleV2SnmpCommunityValue = _SleV2SnmpCommunityValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 1, 1, 1),
    _SleV2SnmpCommunityValue_Type()
)
sleV2SnmpCommunityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityValue.setStatus("current")


class _SleV2SnmpCommunityType_Type(Integer32):
    """Custom type sleV2SnmpCommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2))
    )


_SleV2SnmpCommunityType_Type.__name__ = "Integer32"
_SleV2SnmpCommunityType_Object = MibTableColumn
sleV2SnmpCommunityType = _SleV2SnmpCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 1, 1, 2),
    _SleV2SnmpCommunityType_Type()
)
sleV2SnmpCommunityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityType.setStatus("current")
_SleV2SnmpCommunityAddrType_Type = InetAddressType
_SleV2SnmpCommunityAddrType_Object = MibTableColumn
sleV2SnmpCommunityAddrType = _SleV2SnmpCommunityAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 1, 1, 3),
    _SleV2SnmpCommunityAddrType_Type()
)
sleV2SnmpCommunityAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityAddrType.setStatus("current")
_SleV2SnmpCommunityAddrValue_Type = InetAddress
_SleV2SnmpCommunityAddrValue_Object = MibTableColumn
sleV2SnmpCommunityAddrValue = _SleV2SnmpCommunityAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 1, 1, 4),
    _SleV2SnmpCommunityAddrValue_Type()
)
sleV2SnmpCommunityAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityAddrValue.setStatus("current")
_SleV2SnmpCommunityOID_Type = ObjectIdentifier
_SleV2SnmpCommunityOID_Object = MibTableColumn
sleV2SnmpCommunityOID = _SleV2SnmpCommunityOID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 1, 1, 5),
    _SleV2SnmpCommunityOID_Type()
)
sleV2SnmpCommunityOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityOID.setStatus("current")
_SleV2SnmpCommunityControl_ObjectIdentity = ObjectIdentity
sleV2SnmpCommunityControl = _SleV2SnmpCommunityControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2)
)


class _SleV2SnmpCommunityControlRequest_Type(Integer32):
    """Custom type sleV2SnmpCommunityControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createCommunity", 1),
          ("deleteCommunity", 2),
          ("changeCommunity", 3))
    )


_SleV2SnmpCommunityControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpCommunityControlRequest_Object = MibScalar
sleV2SnmpCommunityControlRequest = _SleV2SnmpCommunityControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2, 1),
    _SleV2SnmpCommunityControlRequest_Type()
)
sleV2SnmpCommunityControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityControlRequest.setStatus("current")
_SleV2SnmpCommunityControlStatus_Type = SleControlStatusType
_SleV2SnmpCommunityControlStatus_Object = MibScalar
sleV2SnmpCommunityControlStatus = _SleV2SnmpCommunityControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2, 2),
    _SleV2SnmpCommunityControlStatus_Type()
)
sleV2SnmpCommunityControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityControlStatus.setStatus("current")
_SleV2SnmpCommunityControlTimer_Type = Gauge32
_SleV2SnmpCommunityControlTimer_Object = MibScalar
sleV2SnmpCommunityControlTimer = _SleV2SnmpCommunityControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2, 3),
    _SleV2SnmpCommunityControlTimer_Type()
)
sleV2SnmpCommunityControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityControlTimer.setStatus("current")
_SleV2SnmpCommunityControlTimeStamp_Type = TimeTicks
_SleV2SnmpCommunityControlTimeStamp_Object = MibScalar
sleV2SnmpCommunityControlTimeStamp = _SleV2SnmpCommunityControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2, 4),
    _SleV2SnmpCommunityControlTimeStamp_Type()
)
sleV2SnmpCommunityControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityControlTimeStamp.setStatus("current")
_SleV2SnmpCommunityControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpCommunityControlReqResult_Object = MibScalar
sleV2SnmpCommunityControlReqResult = _SleV2SnmpCommunityControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2, 5),
    _SleV2SnmpCommunityControlReqResult_Type()
)
sleV2SnmpCommunityControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityControlReqResult.setStatus("current")
_SleV2SnmpCommunityControlValue_Type = OctetString
_SleV2SnmpCommunityControlValue_Object = MibScalar
sleV2SnmpCommunityControlValue = _SleV2SnmpCommunityControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2, 6),
    _SleV2SnmpCommunityControlValue_Type()
)
sleV2SnmpCommunityControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityControlValue.setStatus("current")


class _SleV2SnmpCommunityControlType_Type(Integer32):
    """Custom type sleV2SnmpCommunityControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2))
    )


_SleV2SnmpCommunityControlType_Type.__name__ = "Integer32"
_SleV2SnmpCommunityControlType_Object = MibScalar
sleV2SnmpCommunityControlType = _SleV2SnmpCommunityControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2, 7),
    _SleV2SnmpCommunityControlType_Type()
)
sleV2SnmpCommunityControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityControlType.setStatus("current")
_SleV2SnmpCommunityControlAddrType_Type = InetAddressType
_SleV2SnmpCommunityControlAddrType_Object = MibScalar
sleV2SnmpCommunityControlAddrType = _SleV2SnmpCommunityControlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2, 8),
    _SleV2SnmpCommunityControlAddrType_Type()
)
sleV2SnmpCommunityControlAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityControlAddrType.setStatus("current")
_SleV2SnmpCommunityControlAddrValue_Type = InetAddress
_SleV2SnmpCommunityControlAddrValue_Object = MibScalar
sleV2SnmpCommunityControlAddrValue = _SleV2SnmpCommunityControlAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2, 9),
    _SleV2SnmpCommunityControlAddrValue_Type()
)
sleV2SnmpCommunityControlAddrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityControlAddrValue.setStatus("current")
_SleV2SnmpCommunityControlOID_Type = ObjectIdentifier
_SleV2SnmpCommunityControlOID_Object = MibScalar
sleV2SnmpCommunityControlOID = _SleV2SnmpCommunityControlOID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 2, 10),
    _SleV2SnmpCommunityControlOID_Type()
)
sleV2SnmpCommunityControlOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpCommunityControlOID.setStatus("current")
_SleV2SnmpCommunityNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpCommunityNotification = _SleV2SnmpCommunityNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 3)
)
_SleV2SnmpGroup_ObjectIdentity = ObjectIdentity
sleV2SnmpGroup = _SleV2SnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5)
)
_SleV2SnmpGroupTable_Object = MibTable
sleV2SnmpGroupTable = _SleV2SnmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 1)
)
if mibBuilder.loadTexts:
    sleV2SnmpGroupTable.setStatus("current")
_SleV2SnmpGroupEntry_Object = MibTableRow
sleV2SnmpGroupEntry = _SleV2SnmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 1, 1)
)
sleV2SnmpGroupEntry.setIndexNames(
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpGroupName"),
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpGroupSecModel"),
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpGroupSecName"),
)
if mibBuilder.loadTexts:
    sleV2SnmpGroupEntry.setStatus("current")
_SleV2SnmpGroupName_Type = OctetString
_SleV2SnmpGroupName_Object = MibTableColumn
sleV2SnmpGroupName = _SleV2SnmpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 1, 1, 1),
    _SleV2SnmpGroupName_Type()
)
sleV2SnmpGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpGroupName.setStatus("current")


class _SleV2SnmpGroupSecModel_Type(Integer32):
    """Custom type sleV2SnmpGroupSecModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SleV2SnmpGroupSecModel_Type.__name__ = "Integer32"
_SleV2SnmpGroupSecModel_Object = MibTableColumn
sleV2SnmpGroupSecModel = _SleV2SnmpGroupSecModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 1, 1, 2),
    _SleV2SnmpGroupSecModel_Type()
)
sleV2SnmpGroupSecModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpGroupSecModel.setStatus("current")
_SleV2SnmpGroupSecName_Type = OctetString
_SleV2SnmpGroupSecName_Object = MibTableColumn
sleV2SnmpGroupSecName = _SleV2SnmpGroupSecName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 1, 1, 3),
    _SleV2SnmpGroupSecName_Type()
)
sleV2SnmpGroupSecName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpGroupSecName.setStatus("current")
_SleV2SnmpGroupControl_ObjectIdentity = ObjectIdentity
sleV2SnmpGroupControl = _SleV2SnmpGroupControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 2)
)


class _SleV2SnmpGroupControlRequest_Type(Integer32):
    """Custom type sleV2SnmpGroupControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createGroup", 1),
          ("deleteGroup", 2))
    )


_SleV2SnmpGroupControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpGroupControlRequest_Object = MibScalar
sleV2SnmpGroupControlRequest = _SleV2SnmpGroupControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 2, 1),
    _SleV2SnmpGroupControlRequest_Type()
)
sleV2SnmpGroupControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpGroupControlRequest.setStatus("current")
_SleV2SnmpGroupControlStatus_Type = SleControlStatusType
_SleV2SnmpGroupControlStatus_Object = MibScalar
sleV2SnmpGroupControlStatus = _SleV2SnmpGroupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 2, 2),
    _SleV2SnmpGroupControlStatus_Type()
)
sleV2SnmpGroupControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpGroupControlStatus.setStatus("current")
_SleV2SnmpGroupControlTimer_Type = Gauge32
_SleV2SnmpGroupControlTimer_Object = MibScalar
sleV2SnmpGroupControlTimer = _SleV2SnmpGroupControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 2, 3),
    _SleV2SnmpGroupControlTimer_Type()
)
sleV2SnmpGroupControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpGroupControlTimer.setStatus("current")
_SleV2SnmpGroupControlTimeStamp_Type = TimeTicks
_SleV2SnmpGroupControlTimeStamp_Object = MibScalar
sleV2SnmpGroupControlTimeStamp = _SleV2SnmpGroupControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 2, 4),
    _SleV2SnmpGroupControlTimeStamp_Type()
)
sleV2SnmpGroupControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpGroupControlTimeStamp.setStatus("current")
_SleV2SnmpGroupControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpGroupControlReqResult_Object = MibScalar
sleV2SnmpGroupControlReqResult = _SleV2SnmpGroupControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 2, 5),
    _SleV2SnmpGroupControlReqResult_Type()
)
sleV2SnmpGroupControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpGroupControlReqResult.setStatus("current")
_SleV2SnmpGroupControlName_Type = OctetString
_SleV2SnmpGroupControlName_Object = MibScalar
sleV2SnmpGroupControlName = _SleV2SnmpGroupControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 2, 6),
    _SleV2SnmpGroupControlName_Type()
)
sleV2SnmpGroupControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpGroupControlName.setStatus("current")


class _SleV2SnmpGroupControlSecModel_Type(Integer32):
    """Custom type sleV2SnmpGroupControlSecModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SleV2SnmpGroupControlSecModel_Type.__name__ = "Integer32"
_SleV2SnmpGroupControlSecModel_Object = MibScalar
sleV2SnmpGroupControlSecModel = _SleV2SnmpGroupControlSecModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 2, 7),
    _SleV2SnmpGroupControlSecModel_Type()
)
sleV2SnmpGroupControlSecModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpGroupControlSecModel.setStatus("current")
_SleV2SnmpGroupControlSecName_Type = OctetString
_SleV2SnmpGroupControlSecName_Object = MibScalar
sleV2SnmpGroupControlSecName = _SleV2SnmpGroupControlSecName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 2, 8),
    _SleV2SnmpGroupControlSecName_Type()
)
sleV2SnmpGroupControlSecName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpGroupControlSecName.setStatus("current")
_SleV2SnmpGroupNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpGroupNotification = _SleV2SnmpGroupNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 3)
)
_SleV2SnmpNotify_ObjectIdentity = ObjectIdentity
sleV2SnmpNotify = _SleV2SnmpNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6)
)
_SleV2SnmpNotifyTable_Object = MibTable
sleV2SnmpNotifyTable = _SleV2SnmpNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 1)
)
if mibBuilder.loadTexts:
    sleV2SnmpNotifyTable.setStatus("current")
_SleV2SnmpNotifyEntry_Object = MibTableRow
sleV2SnmpNotifyEntry = _SleV2SnmpNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 1, 1)
)
sleV2SnmpNotifyEntry.setIndexNames(
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpNotifyName"),
)
if mibBuilder.loadTexts:
    sleV2SnmpNotifyEntry.setStatus("current")
_SleV2SnmpNotifyName_Type = OctetString
_SleV2SnmpNotifyName_Object = MibTableColumn
sleV2SnmpNotifyName = _SleV2SnmpNotifyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 1, 1, 1),
    _SleV2SnmpNotifyName_Type()
)
sleV2SnmpNotifyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyName.setStatus("current")
_SleV2SnmpNotifyTag_Type = OctetString
_SleV2SnmpNotifyTag_Object = MibTableColumn
sleV2SnmpNotifyTag = _SleV2SnmpNotifyTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 1, 1, 2),
    _SleV2SnmpNotifyTag_Type()
)
sleV2SnmpNotifyTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyTag.setStatus("current")


class _SleV2SnmpNotifyType_Type(Integer32):
    """Custom type sleV2SnmpNotifyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("inform", 1),
          ("trap", 2))
    )


_SleV2SnmpNotifyType_Type.__name__ = "Integer32"
_SleV2SnmpNotifyType_Object = MibTableColumn
sleV2SnmpNotifyType = _SleV2SnmpNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 1, 1, 3),
    _SleV2SnmpNotifyType_Type()
)
sleV2SnmpNotifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyType.setStatus("current")
_SleV2SnmpNotifyControl_ObjectIdentity = ObjectIdentity
sleV2SnmpNotifyControl = _SleV2SnmpNotifyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 2)
)


class _SleV2SnmpNotifyControlRequest_Type(Integer32):
    """Custom type sleV2SnmpNotifyControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createNotify", 1),
          ("deleteNotify", 2))
    )


_SleV2SnmpNotifyControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpNotifyControlRequest_Object = MibScalar
sleV2SnmpNotifyControlRequest = _SleV2SnmpNotifyControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 2, 1),
    _SleV2SnmpNotifyControlRequest_Type()
)
sleV2SnmpNotifyControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyControlRequest.setStatus("current")
_SleV2SnmpNotifyControlStatus_Type = SleControlStatusType
_SleV2SnmpNotifyControlStatus_Object = MibScalar
sleV2SnmpNotifyControlStatus = _SleV2SnmpNotifyControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 2, 2),
    _SleV2SnmpNotifyControlStatus_Type()
)
sleV2SnmpNotifyControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyControlStatus.setStatus("current")
_SleV2SnmpNotifyControlTimer_Type = Gauge32
_SleV2SnmpNotifyControlTimer_Object = MibScalar
sleV2SnmpNotifyControlTimer = _SleV2SnmpNotifyControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 2, 3),
    _SleV2SnmpNotifyControlTimer_Type()
)
sleV2SnmpNotifyControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyControlTimer.setStatus("current")
_SleV2SnmpNotifyControlTimeStamp_Type = TimeTicks
_SleV2SnmpNotifyControlTimeStamp_Object = MibScalar
sleV2SnmpNotifyControlTimeStamp = _SleV2SnmpNotifyControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 2, 4),
    _SleV2SnmpNotifyControlTimeStamp_Type()
)
sleV2SnmpNotifyControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyControlTimeStamp.setStatus("current")
_SleV2SnmpNotifyControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpNotifyControlReqResult_Object = MibScalar
sleV2SnmpNotifyControlReqResult = _SleV2SnmpNotifyControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 2, 5),
    _SleV2SnmpNotifyControlReqResult_Type()
)
sleV2SnmpNotifyControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyControlReqResult.setStatus("current")
_SleV2SnmpNotifyControlName_Type = OctetString
_SleV2SnmpNotifyControlName_Object = MibScalar
sleV2SnmpNotifyControlName = _SleV2SnmpNotifyControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 2, 6),
    _SleV2SnmpNotifyControlName_Type()
)
sleV2SnmpNotifyControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyControlName.setStatus("current")
_SleV2SnmpNotifyControlTag_Type = OctetString
_SleV2SnmpNotifyControlTag_Object = MibScalar
sleV2SnmpNotifyControlTag = _SleV2SnmpNotifyControlTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 2, 7),
    _SleV2SnmpNotifyControlTag_Type()
)
sleV2SnmpNotifyControlTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyControlTag.setStatus("current")


class _SleV2SnmpNotifyControlType_Type(Integer32):
    """Custom type sleV2SnmpNotifyControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("inform", 1),
          ("trap", 2))
    )


_SleV2SnmpNotifyControlType_Type.__name__ = "Integer32"
_SleV2SnmpNotifyControlType_Object = MibScalar
sleV2SnmpNotifyControlType = _SleV2SnmpNotifyControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 2, 8),
    _SleV2SnmpNotifyControlType_Type()
)
sleV2SnmpNotifyControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpNotifyControlType.setStatus("current")
_SleV2SnmpNotifyNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpNotifyNotification = _SleV2SnmpNotifyNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 3)
)
_SleV2SnmpTargetAddr_ObjectIdentity = ObjectIdentity
sleV2SnmpTargetAddr = _SleV2SnmpTargetAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7)
)
_SleV2SnmpTargetAddrTable_Object = MibTable
sleV2SnmpTargetAddrTable = _SleV2SnmpTargetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 1)
)
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrTable.setStatus("current")
_SleV2SnmpTargetAddrEntry_Object = MibTableRow
sleV2SnmpTargetAddrEntry = _SleV2SnmpTargetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 1, 1)
)
sleV2SnmpTargetAddrEntry.setIndexNames(
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrName"),
)
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrEntry.setStatus("current")
_SleV2SnmpTargetAddrName_Type = OctetString
_SleV2SnmpTargetAddrName_Object = MibTableColumn
sleV2SnmpTargetAddrName = _SleV2SnmpTargetAddrName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 1, 1, 1),
    _SleV2SnmpTargetAddrName_Type()
)
sleV2SnmpTargetAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrName.setStatus("current")
_SleV2SnmpTargetAddrParams_Type = OctetString
_SleV2SnmpTargetAddrParams_Object = MibTableColumn
sleV2SnmpTargetAddrParams = _SleV2SnmpTargetAddrParams_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 1, 1, 2),
    _SleV2SnmpTargetAddrParams_Type()
)
sleV2SnmpTargetAddrParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrParams.setStatus("current")
_SleV2SnmpTargetAddrHostType_Type = InetAddressType
_SleV2SnmpTargetAddrHostType_Object = MibTableColumn
sleV2SnmpTargetAddrHostType = _SleV2SnmpTargetAddrHostType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 1, 1, 3),
    _SleV2SnmpTargetAddrHostType_Type()
)
sleV2SnmpTargetAddrHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrHostType.setStatus("current")
_SleV2SnmpTargetAddrHostAddr_Type = InetAddress
_SleV2SnmpTargetAddrHostAddr_Object = MibTableColumn
sleV2SnmpTargetAddrHostAddr = _SleV2SnmpTargetAddrHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 1, 1, 4),
    _SleV2SnmpTargetAddrHostAddr_Type()
)
sleV2SnmpTargetAddrHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrHostAddr.setStatus("current")
_SleV2SnmpTargetAddrPort_Type = Integer32
_SleV2SnmpTargetAddrPort_Object = MibTableColumn
sleV2SnmpTargetAddrPort = _SleV2SnmpTargetAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 1, 1, 5),
    _SleV2SnmpTargetAddrPort_Type()
)
sleV2SnmpTargetAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrPort.setStatus("current")
_SleV2SnmpTargetAddrTimeout_Type = Integer32
_SleV2SnmpTargetAddrTimeout_Object = MibTableColumn
sleV2SnmpTargetAddrTimeout = _SleV2SnmpTargetAddrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 1, 1, 6),
    _SleV2SnmpTargetAddrTimeout_Type()
)
sleV2SnmpTargetAddrTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrTimeout.setStatus("current")
_SleV2SnmpTargetAddrRetryCnt_Type = Integer32
_SleV2SnmpTargetAddrRetryCnt_Object = MibTableColumn
sleV2SnmpTargetAddrRetryCnt = _SleV2SnmpTargetAddrRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 1, 1, 7),
    _SleV2SnmpTargetAddrRetryCnt_Type()
)
sleV2SnmpTargetAddrRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrRetryCnt.setStatus("current")
_SleV2SnmpTargetAddrTagList_Type = OctetString
_SleV2SnmpTargetAddrTagList_Object = MibTableColumn
sleV2SnmpTargetAddrTagList = _SleV2SnmpTargetAddrTagList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 1, 1, 8),
    _SleV2SnmpTargetAddrTagList_Type()
)
sleV2SnmpTargetAddrTagList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrTagList.setStatus("current")
_SleV2SnmpTargetAddrControl_ObjectIdentity = ObjectIdentity
sleV2SnmpTargetAddrControl = _SleV2SnmpTargetAddrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2)
)


class _SleV2SnmpTargetAddrControlRequest_Type(Integer32):
    """Custom type sleV2SnmpTargetAddrControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createTargetAddr", 1),
          ("deleteTargetAddr", 2),
          ("setTartgetAddrProfile", 3))
    )


_SleV2SnmpTargetAddrControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpTargetAddrControlRequest_Object = MibScalar
sleV2SnmpTargetAddrControlRequest = _SleV2SnmpTargetAddrControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 1),
    _SleV2SnmpTargetAddrControlRequest_Type()
)
sleV2SnmpTargetAddrControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlRequest.setStatus("current")
_SleV2SnmpTargetAddrControlStatus_Type = SleControlStatusType
_SleV2SnmpTargetAddrControlStatus_Object = MibScalar
sleV2SnmpTargetAddrControlStatus = _SleV2SnmpTargetAddrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 2),
    _SleV2SnmpTargetAddrControlStatus_Type()
)
sleV2SnmpTargetAddrControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlStatus.setStatus("current")
_SleV2SnmpTargetAddrControlTimer_Type = Gauge32
_SleV2SnmpTargetAddrControlTimer_Object = MibScalar
sleV2SnmpTargetAddrControlTimer = _SleV2SnmpTargetAddrControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 3),
    _SleV2SnmpTargetAddrControlTimer_Type()
)
sleV2SnmpTargetAddrControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlTimer.setStatus("current")
_SleV2SnmpTargetAddrControlTimeStamp_Type = TimeTicks
_SleV2SnmpTargetAddrControlTimeStamp_Object = MibScalar
sleV2SnmpTargetAddrControlTimeStamp = _SleV2SnmpTargetAddrControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 4),
    _SleV2SnmpTargetAddrControlTimeStamp_Type()
)
sleV2SnmpTargetAddrControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlTimeStamp.setStatus("current")
_SleV2SnmpTargetAddrControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpTargetAddrControlReqResult_Object = MibScalar
sleV2SnmpTargetAddrControlReqResult = _SleV2SnmpTargetAddrControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 5),
    _SleV2SnmpTargetAddrControlReqResult_Type()
)
sleV2SnmpTargetAddrControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlReqResult.setStatus("current")
_SleV2SnmpTargetAddrControlName_Type = OctetString
_SleV2SnmpTargetAddrControlName_Object = MibScalar
sleV2SnmpTargetAddrControlName = _SleV2SnmpTargetAddrControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 6),
    _SleV2SnmpTargetAddrControlName_Type()
)
sleV2SnmpTargetAddrControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlName.setStatus("current")
_SleV2SnmpTargetAddrControlParams_Type = OctetString
_SleV2SnmpTargetAddrControlParams_Object = MibScalar
sleV2SnmpTargetAddrControlParams = _SleV2SnmpTargetAddrControlParams_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 7),
    _SleV2SnmpTargetAddrControlParams_Type()
)
sleV2SnmpTargetAddrControlParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlParams.setStatus("current")
_SleV2SnmpTargetAddrControlHostType_Type = InetAddressType
_SleV2SnmpTargetAddrControlHostType_Object = MibScalar
sleV2SnmpTargetAddrControlHostType = _SleV2SnmpTargetAddrControlHostType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 8),
    _SleV2SnmpTargetAddrControlHostType_Type()
)
sleV2SnmpTargetAddrControlHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlHostType.setStatus("current")
_SleV2SnmpTargetAddrControlHostAddr_Type = InetAddress
_SleV2SnmpTargetAddrControlHostAddr_Object = MibScalar
sleV2SnmpTargetAddrControlHostAddr = _SleV2SnmpTargetAddrControlHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 9),
    _SleV2SnmpTargetAddrControlHostAddr_Type()
)
sleV2SnmpTargetAddrControlHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlHostAddr.setStatus("current")
_SleV2SnmpTargetAddrControlPort_Type = Integer32
_SleV2SnmpTargetAddrControlPort_Object = MibScalar
sleV2SnmpTargetAddrControlPort = _SleV2SnmpTargetAddrControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 10),
    _SleV2SnmpTargetAddrControlPort_Type()
)
sleV2SnmpTargetAddrControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlPort.setStatus("current")
_SleV2SnmpTargetAddrControlTimeout_Type = Integer32
_SleV2SnmpTargetAddrControlTimeout_Object = MibScalar
sleV2SnmpTargetAddrControlTimeout = _SleV2SnmpTargetAddrControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 11),
    _SleV2SnmpTargetAddrControlTimeout_Type()
)
sleV2SnmpTargetAddrControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlTimeout.setStatus("current")
_SleV2SnmpTargetAddrControlRetryCnt_Type = Integer32
_SleV2SnmpTargetAddrControlRetryCnt_Object = MibScalar
sleV2SnmpTargetAddrControlRetryCnt = _SleV2SnmpTargetAddrControlRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 12),
    _SleV2SnmpTargetAddrControlRetryCnt_Type()
)
sleV2SnmpTargetAddrControlRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlRetryCnt.setStatus("current")
_SleV2SnmpTargetAddrControlTagList_Type = OctetString
_SleV2SnmpTargetAddrControlTagList_Object = MibScalar
sleV2SnmpTargetAddrControlTagList = _SleV2SnmpTargetAddrControlTagList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 2, 13),
    _SleV2SnmpTargetAddrControlTagList_Type()
)
sleV2SnmpTargetAddrControlTagList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrControlTagList.setStatus("current")
_SleV2SnmpTargetAddrNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpTargetAddrNotification = _SleV2SnmpTargetAddrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 3)
)
_SleV2SnmpTargetParam_ObjectIdentity = ObjectIdentity
sleV2SnmpTargetParam = _SleV2SnmpTargetParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8)
)
_SleV2SnmpTargetParamTable_Object = MibTable
sleV2SnmpTargetParamTable = _SleV2SnmpTargetParamTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 1)
)
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamTable.setStatus("current")
_SleV2SnmpTargetParamEntry_Object = MibTableRow
sleV2SnmpTargetParamEntry = _SleV2SnmpTargetParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 1, 1)
)
sleV2SnmpTargetParamEntry.setIndexNames(
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpTargetParamName"),
)
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamEntry.setStatus("current")
_SleV2SnmpTargetParamName_Type = OctetString
_SleV2SnmpTargetParamName_Object = MibTableColumn
sleV2SnmpTargetParamName = _SleV2SnmpTargetParamName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 1, 1, 1),
    _SleV2SnmpTargetParamName_Type()
)
sleV2SnmpTargetParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamName.setStatus("current")


class _SleV2SnmpTargetParamSecModel_Type(Integer32):
    """Custom type sleV2SnmpTargetParamSecModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SleV2SnmpTargetParamSecModel_Type.__name__ = "Integer32"
_SleV2SnmpTargetParamSecModel_Object = MibTableColumn
sleV2SnmpTargetParamSecModel = _SleV2SnmpTargetParamSecModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 1, 1, 2),
    _SleV2SnmpTargetParamSecModel_Type()
)
sleV2SnmpTargetParamSecModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamSecModel.setStatus("current")
_SleV2SnmpTargetParamSecName_Type = OctetString
_SleV2SnmpTargetParamSecName_Object = MibTableColumn
sleV2SnmpTargetParamSecName = _SleV2SnmpTargetParamSecName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 1, 1, 3),
    _SleV2SnmpTargetParamSecName_Type()
)
sleV2SnmpTargetParamSecName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamSecName.setStatus("current")


class _SleV2SnmpTargetParamSecLevel_Type(Integer32):
    """Custom type sleV2SnmpTargetParamSecLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noauth", 1),
          ("auth", 2),
          ("priv", 3))
    )


_SleV2SnmpTargetParamSecLevel_Type.__name__ = "Integer32"
_SleV2SnmpTargetParamSecLevel_Object = MibTableColumn
sleV2SnmpTargetParamSecLevel = _SleV2SnmpTargetParamSecLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 1, 1, 4),
    _SleV2SnmpTargetParamSecLevel_Type()
)
sleV2SnmpTargetParamSecLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamSecLevel.setStatus("current")
_SleV2SnmpTargetParamControl_ObjectIdentity = ObjectIdentity
sleV2SnmpTargetParamControl = _SleV2SnmpTargetParamControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 2)
)


class _SleV2SnmpTargetParamControlRequest_Type(Integer32):
    """Custom type sleV2SnmpTargetParamControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createTargetParam", 1),
          ("deleteTargetParam", 2),
          ("setTargetParamProfile", 3))
    )


_SleV2SnmpTargetParamControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpTargetParamControlRequest_Object = MibScalar
sleV2SnmpTargetParamControlRequest = _SleV2SnmpTargetParamControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 2, 1),
    _SleV2SnmpTargetParamControlRequest_Type()
)
sleV2SnmpTargetParamControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamControlRequest.setStatus("current")
_SleV2SnmpTargetParamControlStatus_Type = SleControlStatusType
_SleV2SnmpTargetParamControlStatus_Object = MibScalar
sleV2SnmpTargetParamControlStatus = _SleV2SnmpTargetParamControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 2, 2),
    _SleV2SnmpTargetParamControlStatus_Type()
)
sleV2SnmpTargetParamControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamControlStatus.setStatus("current")
_SleV2SnmpTargetParamControlTimer_Type = Gauge32
_SleV2SnmpTargetParamControlTimer_Object = MibScalar
sleV2SnmpTargetParamControlTimer = _SleV2SnmpTargetParamControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 2, 3),
    _SleV2SnmpTargetParamControlTimer_Type()
)
sleV2SnmpTargetParamControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamControlTimer.setStatus("current")
_SleV2SnmpTargetParamControlTimeStamp_Type = TimeTicks
_SleV2SnmpTargetParamControlTimeStamp_Object = MibScalar
sleV2SnmpTargetParamControlTimeStamp = _SleV2SnmpTargetParamControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 2, 4),
    _SleV2SnmpTargetParamControlTimeStamp_Type()
)
sleV2SnmpTargetParamControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamControlTimeStamp.setStatus("current")
_SleV2SnmpTargetParamControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpTargetParamControlReqResult_Object = MibScalar
sleV2SnmpTargetParamControlReqResult = _SleV2SnmpTargetParamControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 2, 5),
    _SleV2SnmpTargetParamControlReqResult_Type()
)
sleV2SnmpTargetParamControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamControlReqResult.setStatus("current")
_SleV2SnmpTargetParamControlName_Type = OctetString
_SleV2SnmpTargetParamControlName_Object = MibScalar
sleV2SnmpTargetParamControlName = _SleV2SnmpTargetParamControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 2, 6),
    _SleV2SnmpTargetParamControlName_Type()
)
sleV2SnmpTargetParamControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamControlName.setStatus("current")


class _SleV2SnmpTargetParamControlSecModel_Type(Integer32):
    """Custom type sleV2SnmpTargetParamControlSecModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SleV2SnmpTargetParamControlSecModel_Type.__name__ = "Integer32"
_SleV2SnmpTargetParamControlSecModel_Object = MibScalar
sleV2SnmpTargetParamControlSecModel = _SleV2SnmpTargetParamControlSecModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 2, 7),
    _SleV2SnmpTargetParamControlSecModel_Type()
)
sleV2SnmpTargetParamControlSecModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamControlSecModel.setStatus("current")
_SleV2SnmpTargetParamControlSecName_Type = OctetString
_SleV2SnmpTargetParamControlSecName_Object = MibScalar
sleV2SnmpTargetParamControlSecName = _SleV2SnmpTargetParamControlSecName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 2, 8),
    _SleV2SnmpTargetParamControlSecName_Type()
)
sleV2SnmpTargetParamControlSecName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamControlSecName.setStatus("current")


class _SleV2SnmpTargetParamControlSecLevel_Type(Integer32):
    """Custom type sleV2SnmpTargetParamControlSecLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noauth", 1),
          ("auth", 2),
          ("priv", 3))
    )


_SleV2SnmpTargetParamControlSecLevel_Type.__name__ = "Integer32"
_SleV2SnmpTargetParamControlSecLevel_Object = MibScalar
sleV2SnmpTargetParamControlSecLevel = _SleV2SnmpTargetParamControlSecLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 2, 9),
    _SleV2SnmpTargetParamControlSecLevel_Type()
)
sleV2SnmpTargetParamControlSecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamControlSecLevel.setStatus("current")
_SleV2SnmpTargetParamNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpTargetParamNotification = _SleV2SnmpTargetParamNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 3)
)
_SleV2SnmpTraphost_ObjectIdentity = ObjectIdentity
sleV2SnmpTraphost = _SleV2SnmpTraphost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9)
)
_SleV2SnmpTraphostTable_Object = MibTable
sleV2SnmpTraphostTable = _SleV2SnmpTraphostTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 1)
)
if mibBuilder.loadTexts:
    sleV2SnmpTraphostTable.setStatus("current")
_SleV2SnmpTraphostEntry_Object = MibTableRow
sleV2SnmpTraphostEntry = _SleV2SnmpTraphostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 1, 1)
)
sleV2SnmpTraphostEntry.setIndexNames(
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpTraphostType"),
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpTraphostAddrType"),
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpTraphostAddrValue"),
)
if mibBuilder.loadTexts:
    sleV2SnmpTraphostEntry.setStatus("current")


class _SleV2SnmpTraphostType_Type(Integer32):
    """Custom type sleV2SnmpTraphostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trapHost", 1),
          ("trap2Host", 2),
          ("informTrapHost", 3))
    )


_SleV2SnmpTraphostType_Type.__name__ = "Integer32"
_SleV2SnmpTraphostType_Object = MibTableColumn
sleV2SnmpTraphostType = _SleV2SnmpTraphostType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 1, 1, 1),
    _SleV2SnmpTraphostType_Type()
)
sleV2SnmpTraphostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostType.setStatus("current")
_SleV2SnmpTraphostAddrType_Type = InetAddressType
_SleV2SnmpTraphostAddrType_Object = MibTableColumn
sleV2SnmpTraphostAddrType = _SleV2SnmpTraphostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 1, 1, 2),
    _SleV2SnmpTraphostAddrType_Type()
)
sleV2SnmpTraphostAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostAddrType.setStatus("current")
_SleV2SnmpTraphostAddrValue_Type = InetAddress
_SleV2SnmpTraphostAddrValue_Object = MibTableColumn
sleV2SnmpTraphostAddrValue = _SleV2SnmpTraphostAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 1, 1, 3),
    _SleV2SnmpTraphostAddrValue_Type()
)
sleV2SnmpTraphostAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostAddrValue.setStatus("current")
_SleV2SnmpTraphostCommunity_Type = OctetString
_SleV2SnmpTraphostCommunity_Object = MibTableColumn
sleV2SnmpTraphostCommunity = _SleV2SnmpTraphostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 1, 1, 4),
    _SleV2SnmpTraphostCommunity_Type()
)
sleV2SnmpTraphostCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostCommunity.setStatus("current")
_SleV2SnmpTraphostVrfName_Type = OctetString
_SleV2SnmpTraphostVrfName_Object = MibTableColumn
sleV2SnmpTraphostVrfName = _SleV2SnmpTraphostVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 1, 1, 5),
    _SleV2SnmpTraphostVrfName_Type()
)
sleV2SnmpTraphostVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostVrfName.setStatus("current")
_SleV2SnmpTraphostControl_ObjectIdentity = ObjectIdentity
sleV2SnmpTraphostControl = _SleV2SnmpTraphostControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2)
)


class _SleV2SnmpTraphostControlRequest_Type(Integer32):
    """Custom type sleV2SnmpTraphostControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createTraphost", 1),
          ("deleteTraphost", 2))
    )


_SleV2SnmpTraphostControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpTraphostControlRequest_Object = MibScalar
sleV2SnmpTraphostControlRequest = _SleV2SnmpTraphostControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2, 1),
    _SleV2SnmpTraphostControlRequest_Type()
)
sleV2SnmpTraphostControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostControlRequest.setStatus("current")
_SleV2SnmpTraphostControlStatus_Type = SleControlStatusType
_SleV2SnmpTraphostControlStatus_Object = MibScalar
sleV2SnmpTraphostControlStatus = _SleV2SnmpTraphostControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2, 2),
    _SleV2SnmpTraphostControlStatus_Type()
)
sleV2SnmpTraphostControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostControlStatus.setStatus("current")
_SleV2SnmpTraphostControlTimer_Type = Gauge32
_SleV2SnmpTraphostControlTimer_Object = MibScalar
sleV2SnmpTraphostControlTimer = _SleV2SnmpTraphostControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2, 3),
    _SleV2SnmpTraphostControlTimer_Type()
)
sleV2SnmpTraphostControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostControlTimer.setStatus("current")
_SleV2SnmpTraphostControlTimeStamp_Type = TimeTicks
_SleV2SnmpTraphostControlTimeStamp_Object = MibScalar
sleV2SnmpTraphostControlTimeStamp = _SleV2SnmpTraphostControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2, 4),
    _SleV2SnmpTraphostControlTimeStamp_Type()
)
sleV2SnmpTraphostControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostControlTimeStamp.setStatus("current")
_SleV2SnmpTraphostControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpTraphostControlReqResult_Object = MibScalar
sleV2SnmpTraphostControlReqResult = _SleV2SnmpTraphostControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2, 5),
    _SleV2SnmpTraphostControlReqResult_Type()
)
sleV2SnmpTraphostControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostControlReqResult.setStatus("current")


class _SleV2SnmpTraphostControlType_Type(Integer32):
    """Custom type sleV2SnmpTraphostControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trapHost", 1),
          ("trap2Host", 2),
          ("informTraphost", 3))
    )


_SleV2SnmpTraphostControlType_Type.__name__ = "Integer32"
_SleV2SnmpTraphostControlType_Object = MibScalar
sleV2SnmpTraphostControlType = _SleV2SnmpTraphostControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2, 6),
    _SleV2SnmpTraphostControlType_Type()
)
sleV2SnmpTraphostControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostControlType.setStatus("current")
_SleV2SnmpTraphostControlAddrType_Type = InetAddressType
_SleV2SnmpTraphostControlAddrType_Object = MibScalar
sleV2SnmpTraphostControlAddrType = _SleV2SnmpTraphostControlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2, 7),
    _SleV2SnmpTraphostControlAddrType_Type()
)
sleV2SnmpTraphostControlAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostControlAddrType.setStatus("current")
_SleV2SnmpTraphostControlAddrValue_Type = InetAddress
_SleV2SnmpTraphostControlAddrValue_Object = MibScalar
sleV2SnmpTraphostControlAddrValue = _SleV2SnmpTraphostControlAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2, 8),
    _SleV2SnmpTraphostControlAddrValue_Type()
)
sleV2SnmpTraphostControlAddrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostControlAddrValue.setStatus("current")
_SleV2SnmpTraphostControlCommunity_Type = OctetString
_SleV2SnmpTraphostControlCommunity_Object = MibScalar
sleV2SnmpTraphostControlCommunity = _SleV2SnmpTraphostControlCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2, 9),
    _SleV2SnmpTraphostControlCommunity_Type()
)
sleV2SnmpTraphostControlCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostControlCommunity.setStatus("current")
_SleV2SnmpTraphostControlVrfName_Type = OctetString
_SleV2SnmpTraphostControlVrfName_Object = MibScalar
sleV2SnmpTraphostControlVrfName = _SleV2SnmpTraphostControlVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 2, 10),
    _SleV2SnmpTraphostControlVrfName_Type()
)
sleV2SnmpTraphostControlVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpTraphostControlVrfName.setStatus("current")
_SleV2SnmpTraphostNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpTraphostNotification = _SleV2SnmpTraphostNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 3)
)
_SleV2SnmpUser_ObjectIdentity = ObjectIdentity
sleV2SnmpUser = _SleV2SnmpUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10)
)
_SleV2SnmpUserTable_Object = MibTable
sleV2SnmpUserTable = _SleV2SnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 1)
)
if mibBuilder.loadTexts:
    sleV2SnmpUserTable.setStatus("current")
_SleV2SnmpUserEntry_Object = MibTableRow
sleV2SnmpUserEntry = _SleV2SnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 1, 1)
)
sleV2SnmpUserEntry.setIndexNames(
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpUserName"),
)
if mibBuilder.loadTexts:
    sleV2SnmpUserEntry.setStatus("current")
_SleV2SnmpUserName_Type = OctetString
_SleV2SnmpUserName_Object = MibTableColumn
sleV2SnmpUserName = _SleV2SnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 1, 1, 1),
    _SleV2SnmpUserName_Type()
)
sleV2SnmpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpUserName.setStatus("current")


class _SleV2SnmpUserAuthType_Type(Integer32):
    """Custom type sleV2SnmpUserAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_SleV2SnmpUserAuthType_Type.__name__ = "Integer32"
_SleV2SnmpUserAuthType_Object = MibTableColumn
sleV2SnmpUserAuthType = _SleV2SnmpUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 1, 1, 2),
    _SleV2SnmpUserAuthType_Type()
)
sleV2SnmpUserAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpUserAuthType.setStatus("current")
_SleV2SnmpUserAuthKey_Type = OctetString
_SleV2SnmpUserAuthKey_Object = MibTableColumn
sleV2SnmpUserAuthKey = _SleV2SnmpUserAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 1, 1, 3),
    _SleV2SnmpUserAuthKey_Type()
)
sleV2SnmpUserAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpUserAuthKey.setStatus("current")


class _SleV2SnmpUserPrivType_Type(Integer32):
    """Custom type sleV2SnmpUserPrivType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("des", 1))
    )


_SleV2SnmpUserPrivType_Type.__name__ = "Integer32"
_SleV2SnmpUserPrivType_Object = MibTableColumn
sleV2SnmpUserPrivType = _SleV2SnmpUserPrivType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 1, 1, 4),
    _SleV2SnmpUserPrivType_Type()
)
sleV2SnmpUserPrivType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpUserPrivType.setStatus("current")
_SleV2SnmpUserPrivKey_Type = OctetString
_SleV2SnmpUserPrivKey_Object = MibTableColumn
sleV2SnmpUserPrivKey = _SleV2SnmpUserPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 1, 1, 5),
    _SleV2SnmpUserPrivKey_Type()
)
sleV2SnmpUserPrivKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpUserPrivKey.setStatus("current")
_SleV2SnmpUserControl_ObjectIdentity = ObjectIdentity
sleV2SnmpUserControl = _SleV2SnmpUserControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2)
)


class _SleV2SnmpUserControlRequest_Type(Integer32):
    """Custom type sleV2SnmpUserControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createUser", 1),
          ("deleteUser", 2))
    )


_SleV2SnmpUserControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpUserControlRequest_Object = MibScalar
sleV2SnmpUserControlRequest = _SleV2SnmpUserControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2, 1),
    _SleV2SnmpUserControlRequest_Type()
)
sleV2SnmpUserControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpUserControlRequest.setStatus("current")
_SleV2SnmpUserControlStatus_Type = SleControlStatusType
_SleV2SnmpUserControlStatus_Object = MibScalar
sleV2SnmpUserControlStatus = _SleV2SnmpUserControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2, 2),
    _SleV2SnmpUserControlStatus_Type()
)
sleV2SnmpUserControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpUserControlStatus.setStatus("current")
_SleV2SnmpUserControlTimer_Type = Gauge32
_SleV2SnmpUserControlTimer_Object = MibScalar
sleV2SnmpUserControlTimer = _SleV2SnmpUserControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2, 3),
    _SleV2SnmpUserControlTimer_Type()
)
sleV2SnmpUserControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpUserControlTimer.setStatus("current")
_SleV2SnmpUserControlTimeStamp_Type = TimeTicks
_SleV2SnmpUserControlTimeStamp_Object = MibScalar
sleV2SnmpUserControlTimeStamp = _SleV2SnmpUserControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2, 4),
    _SleV2SnmpUserControlTimeStamp_Type()
)
sleV2SnmpUserControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpUserControlTimeStamp.setStatus("current")
_SleV2SnmpUserControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpUserControlReqResult_Object = MibScalar
sleV2SnmpUserControlReqResult = _SleV2SnmpUserControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2, 5),
    _SleV2SnmpUserControlReqResult_Type()
)
sleV2SnmpUserControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpUserControlReqResult.setStatus("current")
_SleV2SnmpUserControlName_Type = OctetString
_SleV2SnmpUserControlName_Object = MibScalar
sleV2SnmpUserControlName = _SleV2SnmpUserControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2, 6),
    _SleV2SnmpUserControlName_Type()
)
sleV2SnmpUserControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpUserControlName.setStatus("current")


class _SleV2SnmpUserControlAuthType_Type(Integer32):
    """Custom type sleV2SnmpUserControlAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_SleV2SnmpUserControlAuthType_Type.__name__ = "Integer32"
_SleV2SnmpUserControlAuthType_Object = MibScalar
sleV2SnmpUserControlAuthType = _SleV2SnmpUserControlAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2, 7),
    _SleV2SnmpUserControlAuthType_Type()
)
sleV2SnmpUserControlAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpUserControlAuthType.setStatus("current")
_SleV2SnmpUserControlAuthKey_Type = OctetString
_SleV2SnmpUserControlAuthKey_Object = MibScalar
sleV2SnmpUserControlAuthKey = _SleV2SnmpUserControlAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2, 8),
    _SleV2SnmpUserControlAuthKey_Type()
)
sleV2SnmpUserControlAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpUserControlAuthKey.setStatus("current")


class _SleV2SnmpUserControlPrivType_Type(Integer32):
    """Custom type sleV2SnmpUserControlPrivType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("des", 1))
    )


_SleV2SnmpUserControlPrivType_Type.__name__ = "Integer32"
_SleV2SnmpUserControlPrivType_Object = MibScalar
sleV2SnmpUserControlPrivType = _SleV2SnmpUserControlPrivType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2, 9),
    _SleV2SnmpUserControlPrivType_Type()
)
sleV2SnmpUserControlPrivType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpUserControlPrivType.setStatus("current")
_SleV2SnmpUserControlPrivKey_Type = OctetString
_SleV2SnmpUserControlPrivKey_Object = MibScalar
sleV2SnmpUserControlPrivKey = _SleV2SnmpUserControlPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 2, 10),
    _SleV2SnmpUserControlPrivKey_Type()
)
sleV2SnmpUserControlPrivKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpUserControlPrivKey.setStatus("current")
_SleV2SnmpUserNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpUserNotification = _SleV2SnmpUserNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 3)
)
_SleV2SnmpView_ObjectIdentity = ObjectIdentity
sleV2SnmpView = _SleV2SnmpView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11)
)
_SleV2SnmpViewTable_Object = MibTable
sleV2SnmpViewTable = _SleV2SnmpViewTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 1)
)
if mibBuilder.loadTexts:
    sleV2SnmpViewTable.setStatus("current")
_SleV2SnmpViewEntry_Object = MibTableRow
sleV2SnmpViewEntry = _SleV2SnmpViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 1, 1)
)
sleV2SnmpViewEntry.setIndexNames(
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpViewName"),
    (0, "SLEV2-SNMP-MIB", "sleV2SnmpViewOid"),
)
if mibBuilder.loadTexts:
    sleV2SnmpViewEntry.setStatus("current")
_SleV2SnmpViewName_Type = OctetString
_SleV2SnmpViewName_Object = MibTableColumn
sleV2SnmpViewName = _SleV2SnmpViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 1, 1, 1),
    _SleV2SnmpViewName_Type()
)
sleV2SnmpViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpViewName.setStatus("current")
_SleV2SnmpViewOid_Type = ObjectIdentifier
_SleV2SnmpViewOid_Object = MibTableColumn
sleV2SnmpViewOid = _SleV2SnmpViewOid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 1, 1, 2),
    _SleV2SnmpViewOid_Type()
)
sleV2SnmpViewOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpViewOid.setStatus("current")
_SleV2SnmpViewMask_Type = OctetString
_SleV2SnmpViewMask_Object = MibTableColumn
sleV2SnmpViewMask = _SleV2SnmpViewMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 1, 1, 3),
    _SleV2SnmpViewMask_Type()
)
sleV2SnmpViewMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpViewMask.setStatus("current")


class _SleV2SnmpViewType_Type(Integer32):
    """Custom type sleV2SnmpViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_SleV2SnmpViewType_Type.__name__ = "Integer32"
_SleV2SnmpViewType_Object = MibTableColumn
sleV2SnmpViewType = _SleV2SnmpViewType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 1, 1, 4),
    _SleV2SnmpViewType_Type()
)
sleV2SnmpViewType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpViewType.setStatus("current")
_SleV2SnmpViewControl_ObjectIdentity = ObjectIdentity
sleV2SnmpViewControl = _SleV2SnmpViewControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 2)
)


class _SleV2SnmpViewControlRequest_Type(Integer32):
    """Custom type sleV2SnmpViewControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createView", 1),
          ("deleteView", 2))
    )


_SleV2SnmpViewControlRequest_Type.__name__ = "Integer32"
_SleV2SnmpViewControlRequest_Object = MibScalar
sleV2SnmpViewControlRequest = _SleV2SnmpViewControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 2, 1),
    _SleV2SnmpViewControlRequest_Type()
)
sleV2SnmpViewControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpViewControlRequest.setStatus("current")
_SleV2SnmpViewControlStatus_Type = SleControlStatusType
_SleV2SnmpViewControlStatus_Object = MibScalar
sleV2SnmpViewControlStatus = _SleV2SnmpViewControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 2, 2),
    _SleV2SnmpViewControlStatus_Type()
)
sleV2SnmpViewControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpViewControlStatus.setStatus("current")
_SleV2SnmpViewControlTimer_Type = Gauge32
_SleV2SnmpViewControlTimer_Object = MibScalar
sleV2SnmpViewControlTimer = _SleV2SnmpViewControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 2, 3),
    _SleV2SnmpViewControlTimer_Type()
)
sleV2SnmpViewControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpViewControlTimer.setStatus("current")
_SleV2SnmpViewControlTimeStamp_Type = TimeTicks
_SleV2SnmpViewControlTimeStamp_Object = MibScalar
sleV2SnmpViewControlTimeStamp = _SleV2SnmpViewControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 2, 4),
    _SleV2SnmpViewControlTimeStamp_Type()
)
sleV2SnmpViewControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpViewControlTimeStamp.setStatus("current")
_SleV2SnmpViewControlReqResult_Type = SleControlRequestResultType
_SleV2SnmpViewControlReqResult_Object = MibScalar
sleV2SnmpViewControlReqResult = _SleV2SnmpViewControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 2, 5),
    _SleV2SnmpViewControlReqResult_Type()
)
sleV2SnmpViewControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2SnmpViewControlReqResult.setStatus("current")
_SleV2SnmpViewControlName_Type = OctetString
_SleV2SnmpViewControlName_Object = MibScalar
sleV2SnmpViewControlName = _SleV2SnmpViewControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 2, 6),
    _SleV2SnmpViewControlName_Type()
)
sleV2SnmpViewControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpViewControlName.setStatus("current")
_SleV2SnmpViewControlOid_Type = ObjectIdentifier
_SleV2SnmpViewControlOid_Object = MibScalar
sleV2SnmpViewControlOid = _SleV2SnmpViewControlOid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 2, 7),
    _SleV2SnmpViewControlOid_Type()
)
sleV2SnmpViewControlOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpViewControlOid.setStatus("current")
_SleV2SnmpViewControlMask_Type = OctetString
_SleV2SnmpViewControlMask_Object = MibScalar
sleV2SnmpViewControlMask = _SleV2SnmpViewControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 2, 8),
    _SleV2SnmpViewControlMask_Type()
)
sleV2SnmpViewControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpViewControlMask.setStatus("current")


class _SleV2SnmpViewControlType_Type(Integer32):
    """Custom type sleV2SnmpViewControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_SleV2SnmpViewControlType_Type.__name__ = "Integer32"
_SleV2SnmpViewControlType_Object = MibScalar
sleV2SnmpViewControlType = _SleV2SnmpViewControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 2, 9),
    _SleV2SnmpViewControlType_Type()
)
sleV2SnmpViewControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2SnmpViewControlType.setStatus("current")
_SleV2SnmpViewNotification_ObjectIdentity = ObjectIdentity
sleV2SnmpViewNotification = _SleV2SnmpViewNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 3)
)

# Managed Objects groups

sleV2SnmpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 12)
)
sleV2SnmpObjectGroup.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseAgentAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseAgentAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseContacts"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseEngineIdType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseEngineIdValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseLocation"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseLogStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseTrapLogStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseTrapLogThreshold"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseTrapMode"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlAgentAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlAgentAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlContacts"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlEngineIdType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlEngineIdValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlLocation"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlLogStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTrapLogStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTrapLogThreshold"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secPrefixLen"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secCommunity"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlPrefixLen"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlCommunity"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityOID"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlOID"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupSecModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupSecName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlSecModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlSecName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyTag"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlTag"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrParams"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrHostType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrHostAddr"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrPort"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrTimeout"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrRetryCnt"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrTagList"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlParams"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlHostType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlHostAddr"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlPort"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlTimeout"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlRetryCnt"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlTagList"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamSecModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamSecName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamSecLevel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlSecModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlSecName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlSecLevel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostCommunity"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostVrfName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlCommunity"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlVrfName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserAuthType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserAuthKey"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserPrivType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserPrivKey"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlAuthType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlAuthKey"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlPrivType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlPrivKey"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewOid"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewMask"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlOid"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlMask"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTrapMode"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessGroupName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessSecurityModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessSecurityLevel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessReadViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessWriteViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessNotifyViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlTimer"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlGroupName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlSecurityModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlSecurityLevel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlReadViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlWriteViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlNotifyViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseVrfName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlVrfName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseNotifyStatus"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpLogIndex"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpLogText"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTrapLogIndex"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTrapLogText"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlNotifyStatus"))
)
if mibBuilder.loadTexts:
    sleV2SnmpObjectGroup.setStatus("current")


# Notification objects

sleV2SnmpCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 1)
)
sleV2SnmpCleared.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SnmpCleared.setStatus(
        "current"
    )

sleV2SnmpAlarmHistoryCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 2)
)
sleV2SnmpAlarmHistoryCleared.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SnmpAlarmHistoryCleared.setStatus(
        "current"
    )

sleV2SnmpAlarmReportCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 3)
)
sleV2SnmpAlarmReportCleared.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SnmpAlarmReportCleared.setStatus(
        "current"
    )

sleV2SnmpLogCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 4)
)
sleV2SnmpLogCleared.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SnmpLogCleared.setStatus(
        "current"
    )

sleV2SnmpTrapLogCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 5)
)
sleV2SnmpTrapLogCleared.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTrapLogCleared.setStatus(
        "current"
    )

sleV2SnmpAgentAddrCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 6)
)
sleV2SnmpAgentAddrCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseAgentAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseAgentAddrValue"))
)
if mibBuilder.loadTexts:
    sleV2SnmpAgentAddrCreated.setStatus(
        "current"
    )

sleV2SnmpAgentAddrDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 7)
)
sleV2SnmpAgentAddrDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SnmpAgentAddrDeleted.setStatus(
        "current"
    )

sleV2SnmpContactsCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 8)
)
sleV2SnmpContactsCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseContacts"))
)
if mibBuilder.loadTexts:
    sleV2SnmpContactsCreated.setStatus(
        "current"
    )

sleV2SnmpContactsDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 9)
)
sleV2SnmpContactsDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SnmpContactsDeleted.setStatus(
        "current"
    )

sleV2SnmpLocationCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 10)
)
sleV2SnmpLocationCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseLocation"))
)
if mibBuilder.loadTexts:
    sleV2SnmpLocationCreated.setStatus(
        "current"
    )

sleV2SnmpLocationDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 11)
)
sleV2SnmpLocationDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SnmpLocationDeleted.setStatus(
        "current"
    )

sleV2SnmpTrapLogStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 12)
)
sleV2SnmpTrapLogStatusChanged.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseTrapLogStatus"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTrapLogStatusChanged.setStatus(
        "current"
    )

sleV2SnmpTrapModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 13)
)
sleV2SnmpTrapModeChanged.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseTrapMode"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTrapModeChanged.setStatus(
        "current"
    )

sleV2SnmpEngineIdCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 14)
)
sleV2SnmpEngineIdCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseEngineIdType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseEngineIdValue"))
)
if mibBuilder.loadTexts:
    sleV2SnmpEngineIdCreated.setStatus(
        "current"
    )

sleV2SnmpEngineIdDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 15)
)
sleV2SnmpEngineIdDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SnmpEngineIdDeleted.setStatus(
        "current"
    )

sleV2SnmpLogStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 16)
)
sleV2SnmpLogStatusChanged.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseLogStatus"))
)
if mibBuilder.loadTexts:
    sleV2SnmpLogStatusChanged.setStatus(
        "current"
    )

sleV2SnmpVrfSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 17)
)
sleV2SnmpVrfSet.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseVrfName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpVrfSet.setStatus(
        "current"
    )

sleV2SnmpVrfUnset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 1, 3, 18)
)
sleV2SnmpVrfUnset.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2SnmpVrfUnset.setStatus(
        "current"
    )

sleV2SnmpAccessCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 3, 1)
)
sleV2SnmpAccessCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessGroupName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessSecurityModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessSecurityLevel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessReadViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessWriteViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessNotifyViewName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpAccessCreated.setStatus(
        "current"
    )

sleV2SnmpAccessDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 3, 2)
)
sleV2SnmpAccessDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlGroupName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpAccessDeleted.setStatus(
        "current"
    )

sleV2SnmpAccessProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 2, 3, 3)
)
sleV2SnmpAccessProfileChanged.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessGroupName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessSecurityModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessSecurityLevel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessReadViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessWriteViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessNotifyViewName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpAccessProfileChanged.setStatus(
        "current"
    )

sleV2SnmpCom2secCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 3, 1)
)
sleV2SnmpCom2secCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secPrefixLen"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secCommunity"))
)
if mibBuilder.loadTexts:
    sleV2SnmpCom2secCreated.setStatus(
        "current"
    )

sleV2SnmpCom2secDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 3, 2)
)
sleV2SnmpCom2secDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpCom2secDeleted.setStatus(
        "current"
    )

sleV2SnmpCom2secChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 3, 3, 3)
)
sleV2SnmpCom2secChanged.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secPrefixLen"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secCommunity"))
)
if mibBuilder.loadTexts:
    sleV2SnmpCom2secChanged.setStatus(
        "current"
    )

sleV2SnmpCommunityCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 3, 1)
)
sleV2SnmpCommunityCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityOID"))
)
if mibBuilder.loadTexts:
    sleV2SnmpCommunityCreated.setStatus(
        "current"
    )

sleV2SnmpCommunityDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 3, 2)
)
sleV2SnmpCommunityDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlValue"))
)
if mibBuilder.loadTexts:
    sleV2SnmpCommunityDeleted.setStatus(
        "current"
    )

sleV2SnmpCommunityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 4, 3, 3)
)
sleV2SnmpCommunityChanged.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityOID"))
)
if mibBuilder.loadTexts:
    sleV2SnmpCommunityChanged.setStatus(
        "current"
    )

sleV2SnmpGroupCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 3, 1)
)
sleV2SnmpGroupCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupSecModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupSecName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpGroupCreated.setStatus(
        "current"
    )

sleV2SnmpGroupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 5, 3, 2)
)
sleV2SnmpGroupDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlSecModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupControlSecName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpGroupDeleted.setStatus(
        "current"
    )

sleV2SnmpNotifyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 3, 1)
)
sleV2SnmpNotifyCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyTag"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyType"))
)
if mibBuilder.loadTexts:
    sleV2SnmpNotifyCreated.setStatus(
        "current"
    )

sleV2SnmpNotifyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 6, 3, 2)
)
sleV2SnmpNotifyDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyControlName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpNotifyDeleted.setStatus(
        "current"
    )

sleV2SnmpTargetAddrCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 3, 1)
)
sleV2SnmpTargetAddrCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrParams"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrHostType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrHostAddr"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrPort"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrTimeout"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrRetryCnt"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrTagList"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrCreated.setStatus(
        "current"
    )

sleV2SnmpTargetAddrDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 3, 2)
)
sleV2SnmpTargetAddrDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrDeleted.setStatus(
        "current"
    )

sleV2SnmpTargetAddrChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 7, 3, 3)
)
sleV2SnmpTargetAddrChanged.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrParams"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrHostType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrHostAddr"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrPort"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrTimeout"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrRetryCnt"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrTagList"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTargetAddrChanged.setStatus(
        "current"
    )

sleV2SnmpTargetParamCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 3, 1)
)
sleV2SnmpTargetParamCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamSecModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamSecName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamSecLevel"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamCreated.setStatus(
        "current"
    )

sleV2SnmpTargetParamDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 3, 2)
)
sleV2SnmpTargetParamDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamDeleted.setStatus(
        "current"
    )

sleV2SnmpTargetParamChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 8, 3, 3)
)
sleV2SnmpTargetParamChanged.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamSecModel"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamSecName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamSecLevel"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTargetParamChanged.setStatus(
        "current"
    )

sleV2SnmpTraphostCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 3, 1)
)
sleV2SnmpTraphostCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostAddrValue"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostCommunity"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostVrfName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTraphostCreated.setStatus(
        "current"
    )

sleV2SnmpTraphostDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 9, 3, 2)
)
sleV2SnmpTraphostDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlAddrType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostControlAddrValue"))
)
if mibBuilder.loadTexts:
    sleV2SnmpTraphostDeleted.setStatus(
        "current"
    )

sleV2SnmpUserCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 3, 1)
)
sleV2SnmpUserCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpUserControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserAuthType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserAuthKey"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserPrivType"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserPrivKey"))
)
if mibBuilder.loadTexts:
    sleV2SnmpUserCreated.setStatus(
        "current"
    )

sleV2SnmpUserDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 10, 3, 2)
)
sleV2SnmpUserDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpUserControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserControlName"))
)
if mibBuilder.loadTexts:
    sleV2SnmpUserDeleted.setStatus(
        "current"
    )

sleV2SnmpViewCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 3, 1)
)
sleV2SnmpViewCreated.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpViewControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewOid"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewMask"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewType"))
)
if mibBuilder.loadTexts:
    sleV2SnmpViewCreated.setStatus(
        "current"
    )

sleV2SnmpViewDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 11, 3, 2)
)
sleV2SnmpViewDeleted.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpViewControlRequest"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlTimeStamp"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlReqResult"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlName"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewControlOid"))
)
if mibBuilder.loadTexts:
    sleV2SnmpViewDeleted.setStatus(
        "current"
    )


# Notifications groups

sleV2SnmpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 8, 13)
)
sleV2SnmpNotificationGroup.setObjects(
      *(("SLEV2-SNMP-MIB", "sleV2SnmpCleared"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAlarmHistoryCleared"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAlarmReportCleared"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpLogCleared"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTrapLogCleared"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAgentAddrCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAgentAddrDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpContactsCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpContactsDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpLocationCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpLocationDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTrapLogStatusChanged"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTrapModeChanged"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpEngineIdCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpEngineIdDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpLogStatusChanged"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpAccessProfileChanged"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCom2secChanged"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpCommunityChanged"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpGroupDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetAddrChanged"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTargetParamChanged"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTraphostDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpUserDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewCreated"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpNotifyActivityStatusChanged"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpViewDeleted"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpVrfSet"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpVrfUnset"),
        ("SLEV2-SNMP-MIB", "sleV2SnmpTrapLogThresholdChanged"))
)
if mibBuilder.loadTexts:
    sleV2SnmpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLEV2-SNMP-MIB",
    **{"sleV2Snmp": sleV2Snmp,
       "sleV2SnmpBase": sleV2SnmpBase,
       "sleV2SnmpBaseInfo": sleV2SnmpBaseInfo,
       "sleV2SnmpBaseAgentAddrType": sleV2SnmpBaseAgentAddrType,
       "sleV2SnmpBaseAgentAddrValue": sleV2SnmpBaseAgentAddrValue,
       "sleV2SnmpBaseContacts": sleV2SnmpBaseContacts,
       "sleV2SnmpBaseEngineIdType": sleV2SnmpBaseEngineIdType,
       "sleV2SnmpBaseEngineIdValue": sleV2SnmpBaseEngineIdValue,
       "sleV2SnmpBaseLocation": sleV2SnmpBaseLocation,
       "sleV2SnmpBaseLogStatus": sleV2SnmpBaseLogStatus,
       "sleV2SnmpBaseTrapLogStatus": sleV2SnmpBaseTrapLogStatus,
       "sleV2SnmpBaseTrapLogThreshold": sleV2SnmpBaseTrapLogThreshold,
       "sleV2SnmpBaseTrapMode": sleV2SnmpBaseTrapMode,
       "sleV2SnmpBaseVrfName": sleV2SnmpBaseVrfName,
       "sleV2SnmpBaseControl": sleV2SnmpBaseControl,
       "sleV2SnmpBaseControlRequest": sleV2SnmpBaseControlRequest,
       "sleV2SnmpBaseControlStatus": sleV2SnmpBaseControlStatus,
       "sleV2SnmpBaseControlTimer": sleV2SnmpBaseControlTimer,
       "sleV2SnmpBaseControlTimeStamp": sleV2SnmpBaseControlTimeStamp,
       "sleV2SnmpBaseControlReqResult": sleV2SnmpBaseControlReqResult,
       "sleV2SnmpBaseControlAgentAddrType": sleV2SnmpBaseControlAgentAddrType,
       "sleV2SnmpBaseControlAgentAddrValue": sleV2SnmpBaseControlAgentAddrValue,
       "sleV2SnmpBaseControlContacts": sleV2SnmpBaseControlContacts,
       "sleV2SnmpBaseControlEngineIdType": sleV2SnmpBaseControlEngineIdType,
       "sleV2SnmpBaseControlEngineIdValue": sleV2SnmpBaseControlEngineIdValue,
       "sleV2SnmpBaseControlLocation": sleV2SnmpBaseControlLocation,
       "sleV2SnmpBaseControlLogStatus": sleV2SnmpBaseControlLogStatus,
       "sleV2SnmpBaseControlTrapLogStatus": sleV2SnmpBaseControlTrapLogStatus,
       "sleV2SnmpBaseControlTrapLogThreshold": sleV2SnmpBaseControlTrapLogThreshold,
       "sleV2SnmpBaseControlTrapMode": sleV2SnmpBaseControlTrapMode,
       "sleV2SnmpBaseControlVrfName": sleV2SnmpBaseControlVrfName,
       "sleV2SnmpBaseNotification": sleV2SnmpBaseNotification,
       "sleV2SnmpCleared": sleV2SnmpCleared,
       "sleV2SnmpAlarmHistoryCleared": sleV2SnmpAlarmHistoryCleared,
       "sleV2SnmpAlarmReportCleared": sleV2SnmpAlarmReportCleared,
       "sleV2SnmpLogCleared": sleV2SnmpLogCleared,
       "sleV2SnmpTrapLogCleared": sleV2SnmpTrapLogCleared,
       "sleV2SnmpAgentAddrCreated": sleV2SnmpAgentAddrCreated,
       "sleV2SnmpAgentAddrDeleted": sleV2SnmpAgentAddrDeleted,
       "sleV2SnmpContactsCreated": sleV2SnmpContactsCreated,
       "sleV2SnmpContactsDeleted": sleV2SnmpContactsDeleted,
       "sleV2SnmpLocationCreated": sleV2SnmpLocationCreated,
       "sleV2SnmpLocationDeleted": sleV2SnmpLocationDeleted,
       "sleV2SnmpTrapLogStatusChanged": sleV2SnmpTrapLogStatusChanged,
       "sleV2SnmpTrapModeChanged": sleV2SnmpTrapModeChanged,
       "sleV2SnmpEngineIdCreated": sleV2SnmpEngineIdCreated,
       "sleV2SnmpEngineIdDeleted": sleV2SnmpEngineIdDeleted,
       "sleV2SnmpLogStatusChanged": sleV2SnmpLogStatusChanged,
       "sleV2SnmpVrfSet": sleV2SnmpVrfSet,
       "sleV2SnmpVrfUnset": sleV2SnmpVrfUnset,
       "sleV2SnmpAccess": sleV2SnmpAccess,
       "sleV2SnmpAccessTable": sleV2SnmpAccessTable,
       "sleV2SnmpAccessEntry": sleV2SnmpAccessEntry,
       "sleV2SnmpAccessGroupName": sleV2SnmpAccessGroupName,
       "sleV2SnmpAccessSecurityModel": sleV2SnmpAccessSecurityModel,
       "sleV2SnmpAccessSecurityLevel": sleV2SnmpAccessSecurityLevel,
       "sleV2SnmpAccessReadViewName": sleV2SnmpAccessReadViewName,
       "sleV2SnmpAccessWriteViewName": sleV2SnmpAccessWriteViewName,
       "sleV2SnmpAccessNotifyViewName": sleV2SnmpAccessNotifyViewName,
       "sleV2SnmpAccessControl": sleV2SnmpAccessControl,
       "sleV2SnmpAccessControlRequest": sleV2SnmpAccessControlRequest,
       "sleV2SnmpAccessControlStatus": sleV2SnmpAccessControlStatus,
       "sleV2SnmpAccessControlTimer": sleV2SnmpAccessControlTimer,
       "sleV2SnmpAccessControlTimeStamp": sleV2SnmpAccessControlTimeStamp,
       "sleV2SnmpAccessControlReqResult": sleV2SnmpAccessControlReqResult,
       "sleV2SnmpAccessControlGroupName": sleV2SnmpAccessControlGroupName,
       "sleV2SnmpAccessControlSecurityModel": sleV2SnmpAccessControlSecurityModel,
       "sleV2SnmpAccessControlSecurityLevel": sleV2SnmpAccessControlSecurityLevel,
       "sleV2SnmpAccessControlReadViewName": sleV2SnmpAccessControlReadViewName,
       "sleV2SnmpAccessControlWriteViewName": sleV2SnmpAccessControlWriteViewName,
       "sleV2SnmpAccessControlNotifyViewName": sleV2SnmpAccessControlNotifyViewName,
       "sleV2SnmpAccessNotification": sleV2SnmpAccessNotification,
       "sleV2SnmpAccessCreated": sleV2SnmpAccessCreated,
       "sleV2SnmpAccessDeleted": sleV2SnmpAccessDeleted,
       "sleV2SnmpAccessProfileChanged": sleV2SnmpAccessProfileChanged,
       "sleV2SnmpCom2sec": sleV2SnmpCom2sec,
       "sleV2SnmpCom2secTable": sleV2SnmpCom2secTable,
       "sleV2SnmpCom2secEntry": sleV2SnmpCom2secEntry,
       "sleV2SnmpCom2secName": sleV2SnmpCom2secName,
       "sleV2SnmpCom2secAddrType": sleV2SnmpCom2secAddrType,
       "sleV2SnmpCom2secAddrValue": sleV2SnmpCom2secAddrValue,
       "sleV2SnmpCom2secPrefixLen": sleV2SnmpCom2secPrefixLen,
       "sleV2SnmpCom2secCommunity": sleV2SnmpCom2secCommunity,
       "sleV2SnmpCom2secControl": sleV2SnmpCom2secControl,
       "sleV2SnmpCom2secControlRequest": sleV2SnmpCom2secControlRequest,
       "sleV2SnmpCom2secControlStatus": sleV2SnmpCom2secControlStatus,
       "sleV2SnmpCom2secControlTimer": sleV2SnmpCom2secControlTimer,
       "sleV2SnmpCom2secControlTimeStamp": sleV2SnmpCom2secControlTimeStamp,
       "sleV2SnmpCom2secControlReqResult": sleV2SnmpCom2secControlReqResult,
       "sleV2SnmpCom2secControlName": sleV2SnmpCom2secControlName,
       "sleV2SnmpCom2secControlAddrType": sleV2SnmpCom2secControlAddrType,
       "sleV2SnmpCom2secControlAddrValue": sleV2SnmpCom2secControlAddrValue,
       "sleV2SnmpCom2secControlPrefixLen": sleV2SnmpCom2secControlPrefixLen,
       "sleV2SnmpCom2secControlCommunity": sleV2SnmpCom2secControlCommunity,
       "sleV2SnmpCom2secNotification": sleV2SnmpCom2secNotification,
       "sleV2SnmpCom2secCreated": sleV2SnmpCom2secCreated,
       "sleV2SnmpCom2secDeleted": sleV2SnmpCom2secDeleted,
       "sleV2SnmpCom2secChanged": sleV2SnmpCom2secChanged,
       "sleV2SnmpCommunity": sleV2SnmpCommunity,
       "sleV2SnmpCommunityTable": sleV2SnmpCommunityTable,
       "sleV2SnmpCommunityEntry": sleV2SnmpCommunityEntry,
       "sleV2SnmpCommunityValue": sleV2SnmpCommunityValue,
       "sleV2SnmpCommunityType": sleV2SnmpCommunityType,
       "sleV2SnmpCommunityAddrType": sleV2SnmpCommunityAddrType,
       "sleV2SnmpCommunityAddrValue": sleV2SnmpCommunityAddrValue,
       "sleV2SnmpCommunityOID": sleV2SnmpCommunityOID,
       "sleV2SnmpCommunityControl": sleV2SnmpCommunityControl,
       "sleV2SnmpCommunityControlRequest": sleV2SnmpCommunityControlRequest,
       "sleV2SnmpCommunityControlStatus": sleV2SnmpCommunityControlStatus,
       "sleV2SnmpCommunityControlTimer": sleV2SnmpCommunityControlTimer,
       "sleV2SnmpCommunityControlTimeStamp": sleV2SnmpCommunityControlTimeStamp,
       "sleV2SnmpCommunityControlReqResult": sleV2SnmpCommunityControlReqResult,
       "sleV2SnmpCommunityControlValue": sleV2SnmpCommunityControlValue,
       "sleV2SnmpCommunityControlType": sleV2SnmpCommunityControlType,
       "sleV2SnmpCommunityControlAddrType": sleV2SnmpCommunityControlAddrType,
       "sleV2SnmpCommunityControlAddrValue": sleV2SnmpCommunityControlAddrValue,
       "sleV2SnmpCommunityControlOID": sleV2SnmpCommunityControlOID,
       "sleV2SnmpCommunityNotification": sleV2SnmpCommunityNotification,
       "sleV2SnmpCommunityCreated": sleV2SnmpCommunityCreated,
       "sleV2SnmpCommunityDeleted": sleV2SnmpCommunityDeleted,
       "sleV2SnmpCommunityChanged": sleV2SnmpCommunityChanged,
       "sleV2SnmpGroup": sleV2SnmpGroup,
       "sleV2SnmpGroupTable": sleV2SnmpGroupTable,
       "sleV2SnmpGroupEntry": sleV2SnmpGroupEntry,
       "sleV2SnmpGroupName": sleV2SnmpGroupName,
       "sleV2SnmpGroupSecModel": sleV2SnmpGroupSecModel,
       "sleV2SnmpGroupSecName": sleV2SnmpGroupSecName,
       "sleV2SnmpGroupControl": sleV2SnmpGroupControl,
       "sleV2SnmpGroupControlRequest": sleV2SnmpGroupControlRequest,
       "sleV2SnmpGroupControlStatus": sleV2SnmpGroupControlStatus,
       "sleV2SnmpGroupControlTimer": sleV2SnmpGroupControlTimer,
       "sleV2SnmpGroupControlTimeStamp": sleV2SnmpGroupControlTimeStamp,
       "sleV2SnmpGroupControlReqResult": sleV2SnmpGroupControlReqResult,
       "sleV2SnmpGroupControlName": sleV2SnmpGroupControlName,
       "sleV2SnmpGroupControlSecModel": sleV2SnmpGroupControlSecModel,
       "sleV2SnmpGroupControlSecName": sleV2SnmpGroupControlSecName,
       "sleV2SnmpGroupNotification": sleV2SnmpGroupNotification,
       "sleV2SnmpGroupCreated": sleV2SnmpGroupCreated,
       "sleV2SnmpGroupDeleted": sleV2SnmpGroupDeleted,
       "sleV2SnmpNotify": sleV2SnmpNotify,
       "sleV2SnmpNotifyTable": sleV2SnmpNotifyTable,
       "sleV2SnmpNotifyEntry": sleV2SnmpNotifyEntry,
       "sleV2SnmpNotifyName": sleV2SnmpNotifyName,
       "sleV2SnmpNotifyTag": sleV2SnmpNotifyTag,
       "sleV2SnmpNotifyType": sleV2SnmpNotifyType,
       "sleV2SnmpNotifyControl": sleV2SnmpNotifyControl,
       "sleV2SnmpNotifyControlRequest": sleV2SnmpNotifyControlRequest,
       "sleV2SnmpNotifyControlStatus": sleV2SnmpNotifyControlStatus,
       "sleV2SnmpNotifyControlTimer": sleV2SnmpNotifyControlTimer,
       "sleV2SnmpNotifyControlTimeStamp": sleV2SnmpNotifyControlTimeStamp,
       "sleV2SnmpNotifyControlReqResult": sleV2SnmpNotifyControlReqResult,
       "sleV2SnmpNotifyControlName": sleV2SnmpNotifyControlName,
       "sleV2SnmpNotifyControlTag": sleV2SnmpNotifyControlTag,
       "sleV2SnmpNotifyControlType": sleV2SnmpNotifyControlType,
       "sleV2SnmpNotifyNotification": sleV2SnmpNotifyNotification,
       "sleV2SnmpNotifyCreated": sleV2SnmpNotifyCreated,
       "sleV2SnmpNotifyDeleted": sleV2SnmpNotifyDeleted,
       "sleV2SnmpTargetAddr": sleV2SnmpTargetAddr,
       "sleV2SnmpTargetAddrTable": sleV2SnmpTargetAddrTable,
       "sleV2SnmpTargetAddrEntry": sleV2SnmpTargetAddrEntry,
       "sleV2SnmpTargetAddrName": sleV2SnmpTargetAddrName,
       "sleV2SnmpTargetAddrParams": sleV2SnmpTargetAddrParams,
       "sleV2SnmpTargetAddrHostType": sleV2SnmpTargetAddrHostType,
       "sleV2SnmpTargetAddrHostAddr": sleV2SnmpTargetAddrHostAddr,
       "sleV2SnmpTargetAddrPort": sleV2SnmpTargetAddrPort,
       "sleV2SnmpTargetAddrTimeout": sleV2SnmpTargetAddrTimeout,
       "sleV2SnmpTargetAddrRetryCnt": sleV2SnmpTargetAddrRetryCnt,
       "sleV2SnmpTargetAddrTagList": sleV2SnmpTargetAddrTagList,
       "sleV2SnmpTargetAddrControl": sleV2SnmpTargetAddrControl,
       "sleV2SnmpTargetAddrControlRequest": sleV2SnmpTargetAddrControlRequest,
       "sleV2SnmpTargetAddrControlStatus": sleV2SnmpTargetAddrControlStatus,
       "sleV2SnmpTargetAddrControlTimer": sleV2SnmpTargetAddrControlTimer,
       "sleV2SnmpTargetAddrControlTimeStamp": sleV2SnmpTargetAddrControlTimeStamp,
       "sleV2SnmpTargetAddrControlReqResult": sleV2SnmpTargetAddrControlReqResult,
       "sleV2SnmpTargetAddrControlName": sleV2SnmpTargetAddrControlName,
       "sleV2SnmpTargetAddrControlParams": sleV2SnmpTargetAddrControlParams,
       "sleV2SnmpTargetAddrControlHostType": sleV2SnmpTargetAddrControlHostType,
       "sleV2SnmpTargetAddrControlHostAddr": sleV2SnmpTargetAddrControlHostAddr,
       "sleV2SnmpTargetAddrControlPort": sleV2SnmpTargetAddrControlPort,
       "sleV2SnmpTargetAddrControlTimeout": sleV2SnmpTargetAddrControlTimeout,
       "sleV2SnmpTargetAddrControlRetryCnt": sleV2SnmpTargetAddrControlRetryCnt,
       "sleV2SnmpTargetAddrControlTagList": sleV2SnmpTargetAddrControlTagList,
       "sleV2SnmpTargetAddrNotification": sleV2SnmpTargetAddrNotification,
       "sleV2SnmpTargetAddrCreated": sleV2SnmpTargetAddrCreated,
       "sleV2SnmpTargetAddrDeleted": sleV2SnmpTargetAddrDeleted,
       "sleV2SnmpTargetAddrChanged": sleV2SnmpTargetAddrChanged,
       "sleV2SnmpTargetParam": sleV2SnmpTargetParam,
       "sleV2SnmpTargetParamTable": sleV2SnmpTargetParamTable,
       "sleV2SnmpTargetParamEntry": sleV2SnmpTargetParamEntry,
       "sleV2SnmpTargetParamName": sleV2SnmpTargetParamName,
       "sleV2SnmpTargetParamSecModel": sleV2SnmpTargetParamSecModel,
       "sleV2SnmpTargetParamSecName": sleV2SnmpTargetParamSecName,
       "sleV2SnmpTargetParamSecLevel": sleV2SnmpTargetParamSecLevel,
       "sleV2SnmpTargetParamControl": sleV2SnmpTargetParamControl,
       "sleV2SnmpTargetParamControlRequest": sleV2SnmpTargetParamControlRequest,
       "sleV2SnmpTargetParamControlStatus": sleV2SnmpTargetParamControlStatus,
       "sleV2SnmpTargetParamControlTimer": sleV2SnmpTargetParamControlTimer,
       "sleV2SnmpTargetParamControlTimeStamp": sleV2SnmpTargetParamControlTimeStamp,
       "sleV2SnmpTargetParamControlReqResult": sleV2SnmpTargetParamControlReqResult,
       "sleV2SnmpTargetParamControlName": sleV2SnmpTargetParamControlName,
       "sleV2SnmpTargetParamControlSecModel": sleV2SnmpTargetParamControlSecModel,
       "sleV2SnmpTargetParamControlSecName": sleV2SnmpTargetParamControlSecName,
       "sleV2SnmpTargetParamControlSecLevel": sleV2SnmpTargetParamControlSecLevel,
       "sleV2SnmpTargetParamNotification": sleV2SnmpTargetParamNotification,
       "sleV2SnmpTargetParamCreated": sleV2SnmpTargetParamCreated,
       "sleV2SnmpTargetParamDeleted": sleV2SnmpTargetParamDeleted,
       "sleV2SnmpTargetParamChanged": sleV2SnmpTargetParamChanged,
       "sleV2SnmpTraphost": sleV2SnmpTraphost,
       "sleV2SnmpTraphostTable": sleV2SnmpTraphostTable,
       "sleV2SnmpTraphostEntry": sleV2SnmpTraphostEntry,
       "sleV2SnmpTraphostType": sleV2SnmpTraphostType,
       "sleV2SnmpTraphostAddrType": sleV2SnmpTraphostAddrType,
       "sleV2SnmpTraphostAddrValue": sleV2SnmpTraphostAddrValue,
       "sleV2SnmpTraphostCommunity": sleV2SnmpTraphostCommunity,
       "sleV2SnmpTraphostVrfName": sleV2SnmpTraphostVrfName,
       "sleV2SnmpTraphostControl": sleV2SnmpTraphostControl,
       "sleV2SnmpTraphostControlRequest": sleV2SnmpTraphostControlRequest,
       "sleV2SnmpTraphostControlStatus": sleV2SnmpTraphostControlStatus,
       "sleV2SnmpTraphostControlTimer": sleV2SnmpTraphostControlTimer,
       "sleV2SnmpTraphostControlTimeStamp": sleV2SnmpTraphostControlTimeStamp,
       "sleV2SnmpTraphostControlReqResult": sleV2SnmpTraphostControlReqResult,
       "sleV2SnmpTraphostControlType": sleV2SnmpTraphostControlType,
       "sleV2SnmpTraphostControlAddrType": sleV2SnmpTraphostControlAddrType,
       "sleV2SnmpTraphostControlAddrValue": sleV2SnmpTraphostControlAddrValue,
       "sleV2SnmpTraphostControlCommunity": sleV2SnmpTraphostControlCommunity,
       "sleV2SnmpTraphostControlVrfName": sleV2SnmpTraphostControlVrfName,
       "sleV2SnmpTraphostNotification": sleV2SnmpTraphostNotification,
       "sleV2SnmpTraphostCreated": sleV2SnmpTraphostCreated,
       "sleV2SnmpTraphostDeleted": sleV2SnmpTraphostDeleted,
       "sleV2SnmpUser": sleV2SnmpUser,
       "sleV2SnmpUserTable": sleV2SnmpUserTable,
       "sleV2SnmpUserEntry": sleV2SnmpUserEntry,
       "sleV2SnmpUserName": sleV2SnmpUserName,
       "sleV2SnmpUserAuthType": sleV2SnmpUserAuthType,
       "sleV2SnmpUserAuthKey": sleV2SnmpUserAuthKey,
       "sleV2SnmpUserPrivType": sleV2SnmpUserPrivType,
       "sleV2SnmpUserPrivKey": sleV2SnmpUserPrivKey,
       "sleV2SnmpUserControl": sleV2SnmpUserControl,
       "sleV2SnmpUserControlRequest": sleV2SnmpUserControlRequest,
       "sleV2SnmpUserControlStatus": sleV2SnmpUserControlStatus,
       "sleV2SnmpUserControlTimer": sleV2SnmpUserControlTimer,
       "sleV2SnmpUserControlTimeStamp": sleV2SnmpUserControlTimeStamp,
       "sleV2SnmpUserControlReqResult": sleV2SnmpUserControlReqResult,
       "sleV2SnmpUserControlName": sleV2SnmpUserControlName,
       "sleV2SnmpUserControlAuthType": sleV2SnmpUserControlAuthType,
       "sleV2SnmpUserControlAuthKey": sleV2SnmpUserControlAuthKey,
       "sleV2SnmpUserControlPrivType": sleV2SnmpUserControlPrivType,
       "sleV2SnmpUserControlPrivKey": sleV2SnmpUserControlPrivKey,
       "sleV2SnmpUserNotification": sleV2SnmpUserNotification,
       "sleV2SnmpUserCreated": sleV2SnmpUserCreated,
       "sleV2SnmpUserDeleted": sleV2SnmpUserDeleted,
       "sleV2SnmpView": sleV2SnmpView,
       "sleV2SnmpViewTable": sleV2SnmpViewTable,
       "sleV2SnmpViewEntry": sleV2SnmpViewEntry,
       "sleV2SnmpViewName": sleV2SnmpViewName,
       "sleV2SnmpViewOid": sleV2SnmpViewOid,
       "sleV2SnmpViewMask": sleV2SnmpViewMask,
       "sleV2SnmpViewType": sleV2SnmpViewType,
       "sleV2SnmpViewControl": sleV2SnmpViewControl,
       "sleV2SnmpViewControlRequest": sleV2SnmpViewControlRequest,
       "sleV2SnmpViewControlStatus": sleV2SnmpViewControlStatus,
       "sleV2SnmpViewControlTimer": sleV2SnmpViewControlTimer,
       "sleV2SnmpViewControlTimeStamp": sleV2SnmpViewControlTimeStamp,
       "sleV2SnmpViewControlReqResult": sleV2SnmpViewControlReqResult,
       "sleV2SnmpViewControlName": sleV2SnmpViewControlName,
       "sleV2SnmpViewControlOid": sleV2SnmpViewControlOid,
       "sleV2SnmpViewControlMask": sleV2SnmpViewControlMask,
       "sleV2SnmpViewControlType": sleV2SnmpViewControlType,
       "sleV2SnmpViewNotification": sleV2SnmpViewNotification,
       "sleV2SnmpViewCreated": sleV2SnmpViewCreated,
       "sleV2SnmpViewDeleted": sleV2SnmpViewDeleted,
       "sleV2SnmpObjectGroup": sleV2SnmpObjectGroup,
       "sleV2SnmpNotificationGroup": sleV2SnmpNotificationGroup}
)
