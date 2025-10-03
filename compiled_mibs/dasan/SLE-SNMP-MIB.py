# SNMP MIB module (SLE-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-SNMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:04 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

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

sleSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleSnmpBase_ObjectIdentity = ObjectIdentity
sleSnmpBase = _SleSnmpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1)
)
_SleSnmpBaseInfo_ObjectIdentity = ObjectIdentity
sleSnmpBaseInfo = _SleSnmpBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 1)
)
_SleSnmpSysContact_Type = OctetString
_SleSnmpSysContact_Object = MibScalar
sleSnmpSysContact = _SleSnmpSysContact_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 1, 1),
    _SleSnmpSysContact_Type()
)
sleSnmpSysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpSysContact.setStatus("current")
_SleSnmpSysLocation_Type = OctetString
_SleSnmpSysLocation_Object = MibScalar
sleSnmpSysLocation = _SleSnmpSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 1, 2),
    _SleSnmpSysLocation_Type()
)
sleSnmpSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpSysLocation.setStatus("current")


class _SleSnmpLogStatus_Type(Integer32):
    """Custom type sleSnmpLogStatus based on Integer32"""
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


_SleSnmpLogStatus_Type.__name__ = "Integer32"
_SleSnmpLogStatus_Object = MibScalar
sleSnmpLogStatus = _SleSnmpLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 1, 3),
    _SleSnmpLogStatus_Type()
)
sleSnmpLogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpLogStatus.setStatus("current")


class _SleSnmpConnectionType_Type(Integer32):
    """Custom type sleSnmpConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("lct", 2),
          ("tmn", 3),
          ("unknown", 255))
    )


_SleSnmpConnectionType_Type.__name__ = "Integer32"
_SleSnmpConnectionType_Object = MibScalar
sleSnmpConnectionType = _SleSnmpConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 1, 4),
    _SleSnmpConnectionType_Type()
)
sleSnmpConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpConnectionType.setStatus("current")
_SleSnmpInformTrapRetry_Type = Integer32
_SleSnmpInformTrapRetry_Object = MibScalar
sleSnmpInformTrapRetry = _SleSnmpInformTrapRetry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 1, 5),
    _SleSnmpInformTrapRetry_Type()
)
sleSnmpInformTrapRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpInformTrapRetry.setStatus("current")
_SlesnmpInformTrapInterval_Type = Integer32
_SlesnmpInformTrapInterval_Object = MibScalar
slesnmpInformTrapInterval = _SlesnmpInformTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 1, 6),
    _SlesnmpInformTrapInterval_Type()
)
slesnmpInformTrapInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slesnmpInformTrapInterval.setStatus("current")


class _SleSnmpTrapModeStatus_Type(Integer32):
    """Custom type sleSnmpTrapModeStatus based on Integer32"""
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


_SleSnmpTrapModeStatus_Type.__name__ = "Integer32"
_SleSnmpTrapModeStatus_Object = MibScalar
sleSnmpTrapModeStatus = _SleSnmpTrapModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 1, 7),
    _SleSnmpTrapModeStatus_Type()
)
sleSnmpTrapModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapModeStatus.setStatus("current")
_SleSnmpBaseControl_ObjectIdentity = ObjectIdentity
sleSnmpBaseControl = _SleSnmpBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2)
)


class _SleSnmpControlRequest_Type(Integer32):
    """Custom type sleSnmpControlRequest based on Integer32"""
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
        *(("setSnmpSysInfoProfile", 1),
          ("setSnmpLogStatus", 2),
          ("setSnmpConnectionType", 3),
          ("setInformTrapConf", 4),
          ("setSnmpTrapMode", 5))
    )


_SleSnmpControlRequest_Type.__name__ = "Integer32"
_SleSnmpControlRequest_Object = MibScalar
sleSnmpControlRequest = _SleSnmpControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 1),
    _SleSnmpControlRequest_Type()
)
sleSnmpControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpControlRequest.setStatus("current")
_SleSnmpControlStatus_Type = Integer32
_SleSnmpControlStatus_Object = MibScalar
sleSnmpControlStatus = _SleSnmpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 2),
    _SleSnmpControlStatus_Type()
)
sleSnmpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpControlStatus.setStatus("current")
_SleSnmpControlTimer_Type = Gauge32
_SleSnmpControlTimer_Object = MibScalar
sleSnmpControlTimer = _SleSnmpControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 3),
    _SleSnmpControlTimer_Type()
)
sleSnmpControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpControlTimer.setStatus("current")
_SleSnmpControlTimeStamp_Type = TimeTicks
_SleSnmpControlTimeStamp_Object = MibScalar
sleSnmpControlTimeStamp = _SleSnmpControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 4),
    _SleSnmpControlTimeStamp_Type()
)
sleSnmpControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpControlTimeStamp.setStatus("current")
_SleSnmpControlReqResult_Type = Integer32
_SleSnmpControlReqResult_Object = MibScalar
sleSnmpControlReqResult = _SleSnmpControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 5),
    _SleSnmpControlReqResult_Type()
)
sleSnmpControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpControlReqResult.setStatus("current")
_SleSnmpControlSysContact_Type = OctetString
_SleSnmpControlSysContact_Object = MibScalar
sleSnmpControlSysContact = _SleSnmpControlSysContact_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 6),
    _SleSnmpControlSysContact_Type()
)
sleSnmpControlSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpControlSysContact.setStatus("current")
_SleSnmpControlSysLocation_Type = OctetString
_SleSnmpControlSysLocation_Object = MibScalar
sleSnmpControlSysLocation = _SleSnmpControlSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 7),
    _SleSnmpControlSysLocation_Type()
)
sleSnmpControlSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpControlSysLocation.setStatus("current")


class _SleSnmpControlLogStatus_Type(Integer32):
    """Custom type sleSnmpControlLogStatus based on Integer32"""
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


_SleSnmpControlLogStatus_Type.__name__ = "Integer32"
_SleSnmpControlLogStatus_Object = MibScalar
sleSnmpControlLogStatus = _SleSnmpControlLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 8),
    _SleSnmpControlLogStatus_Type()
)
sleSnmpControlLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpControlLogStatus.setStatus("current")


class _SleSnmpControlConnectionType_Type(Integer32):
    """Custom type sleSnmpControlConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("lct", 2),
          ("tmn", 3),
          ("unknown", 255))
    )


_SleSnmpControlConnectionType_Type.__name__ = "Integer32"
_SleSnmpControlConnectionType_Object = MibScalar
sleSnmpControlConnectionType = _SleSnmpControlConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 9),
    _SleSnmpControlConnectionType_Type()
)
sleSnmpControlConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpControlConnectionType.setStatus("current")
_SleSnmpControlInformTrapRetry_Type = Integer32
_SleSnmpControlInformTrapRetry_Object = MibScalar
sleSnmpControlInformTrapRetry = _SleSnmpControlInformTrapRetry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 10),
    _SleSnmpControlInformTrapRetry_Type()
)
sleSnmpControlInformTrapRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpControlInformTrapRetry.setStatus("current")
_SleSnmpControlInformTrapInterval_Type = Integer32
_SleSnmpControlInformTrapInterval_Object = MibScalar
sleSnmpControlInformTrapInterval = _SleSnmpControlInformTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 11),
    _SleSnmpControlInformTrapInterval_Type()
)
sleSnmpControlInformTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpControlInformTrapInterval.setStatus("current")


class _SleSnmpControlTrapModeStatus_Type(Integer32):
    """Custom type sleSnmpControlTrapModeStatus based on Integer32"""
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


_SleSnmpControlTrapModeStatus_Type.__name__ = "Integer32"
_SleSnmpControlTrapModeStatus_Object = MibScalar
sleSnmpControlTrapModeStatus = _SleSnmpControlTrapModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 2, 12),
    _SleSnmpControlTrapModeStatus_Type()
)
sleSnmpControlTrapModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpControlTrapModeStatus.setStatus("current")
_SleSnmpBaseNotification_ObjectIdentity = ObjectIdentity
sleSnmpBaseNotification = _SleSnmpBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 3)
)
_SleCom2Sec_ObjectIdentity = ObjectIdentity
sleCom2Sec = _SleCom2Sec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2)
)
_SleCom2SecTable_Object = MibTable
sleCom2SecTable = _SleCom2SecTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 1)
)
if mibBuilder.loadTexts:
    sleCom2SecTable.setStatus("current")
_SleCom2SecEntry_Object = MibTableRow
sleCom2SecEntry = _SleCom2SecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 1, 1)
)
sleCom2SecEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleCom2SecName"),
)
if mibBuilder.loadTexts:
    sleCom2SecEntry.setStatus("current")
_SleCom2SecName_Type = OctetString
_SleCom2SecName_Object = MibTableColumn
sleCom2SecName = _SleCom2SecName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 1, 1, 1),
    _SleCom2SecName_Type()
)
sleCom2SecName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCom2SecName.setStatus("current")
_SleCom2SecHost_Type = IpAddress
_SleCom2SecHost_Object = MibTableColumn
sleCom2SecHost = _SleCom2SecHost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 1, 1, 2),
    _SleCom2SecHost_Type()
)
sleCom2SecHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCom2SecHost.setStatus("current")
_SleCom2SecHostMaskLen_Type = Integer32
_SleCom2SecHostMaskLen_Object = MibTableColumn
sleCom2SecHostMaskLen = _SleCom2SecHostMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 1, 1, 3),
    _SleCom2SecHostMaskLen_Type()
)
sleCom2SecHostMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCom2SecHostMaskLen.setStatus("current")
_SleCom2SecCommunity_Type = OctetString
_SleCom2SecCommunity_Object = MibTableColumn
sleCom2SecCommunity = _SleCom2SecCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 1, 1, 4),
    _SleCom2SecCommunity_Type()
)
sleCom2SecCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCom2SecCommunity.setStatus("current")
_SleCom2SecControl_ObjectIdentity = ObjectIdentity
sleCom2SecControl = _SleCom2SecControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 2)
)


class _SleCom2SecControlRequest_Type(Integer32):
    """Custom type sleCom2SecControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createCom2Sec", 1),
          ("destroyCom2Sec", 2),
          ("setCom2SecProfile", 3))
    )


_SleCom2SecControlRequest_Type.__name__ = "Integer32"
_SleCom2SecControlRequest_Object = MibScalar
sleCom2SecControlRequest = _SleCom2SecControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 2, 1),
    _SleCom2SecControlRequest_Type()
)
sleCom2SecControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCom2SecControlRequest.setStatus("current")
_SleCom2SecControlStatus_Type = Integer32
_SleCom2SecControlStatus_Object = MibScalar
sleCom2SecControlStatus = _SleCom2SecControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 2, 2),
    _SleCom2SecControlStatus_Type()
)
sleCom2SecControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCom2SecControlStatus.setStatus("current")
_SleCom2SecControlTimer_Type = Gauge32
_SleCom2SecControlTimer_Object = MibScalar
sleCom2SecControlTimer = _SleCom2SecControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 2, 3),
    _SleCom2SecControlTimer_Type()
)
sleCom2SecControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCom2SecControlTimer.setStatus("current")
_SleCom2SecControlTimeStamp_Type = TimeTicks
_SleCom2SecControlTimeStamp_Object = MibScalar
sleCom2SecControlTimeStamp = _SleCom2SecControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 2, 4),
    _SleCom2SecControlTimeStamp_Type()
)
sleCom2SecControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCom2SecControlTimeStamp.setStatus("current")
_SleCom2SecControlReqResult_Type = Integer32
_SleCom2SecControlReqResult_Object = MibScalar
sleCom2SecControlReqResult = _SleCom2SecControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 2, 5),
    _SleCom2SecControlReqResult_Type()
)
sleCom2SecControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCom2SecControlReqResult.setStatus("current")
_SleCom2SecControlName_Type = OctetString
_SleCom2SecControlName_Object = MibScalar
sleCom2SecControlName = _SleCom2SecControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 2, 6),
    _SleCom2SecControlName_Type()
)
sleCom2SecControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCom2SecControlName.setStatus("current")
_SleCom2SecControlHost_Type = IpAddress
_SleCom2SecControlHost_Object = MibScalar
sleCom2SecControlHost = _SleCom2SecControlHost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 2, 7),
    _SleCom2SecControlHost_Type()
)
sleCom2SecControlHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCom2SecControlHost.setStatus("current")
_SleCom2secControlHostMaskLen_Type = Integer32
_SleCom2secControlHostMaskLen_Object = MibScalar
sleCom2secControlHostMaskLen = _SleCom2secControlHostMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 2, 8),
    _SleCom2secControlHostMaskLen_Type()
)
sleCom2secControlHostMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCom2secControlHostMaskLen.setStatus("current")
_SleCom2SecControlCommunity_Type = OctetString
_SleCom2SecControlCommunity_Object = MibScalar
sleCom2SecControlCommunity = _SleCom2SecControlCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 2, 9),
    _SleCom2SecControlCommunity_Type()
)
sleCom2SecControlCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCom2SecControlCommunity.setStatus("current")
_SleCom2SecNotification_ObjectIdentity = ObjectIdentity
sleCom2SecNotification = _SleCom2SecNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 3)
)
_SleTrapHost_ObjectIdentity = ObjectIdentity
sleTrapHost = _SleTrapHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3)
)
_SleTrapHostTable_Object = MibTable
sleTrapHostTable = _SleTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 1)
)
if mibBuilder.loadTexts:
    sleTrapHostTable.setStatus("current")
_SleTrapHostEntry_Object = MibTableRow
sleTrapHostEntry = _SleTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 1, 1)
)
sleTrapHostEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleTrapHostType"),
    (0, "SLE-SNMP-MIB", "sleTrapHostAddress"),
)
if mibBuilder.loadTexts:
    sleTrapHostEntry.setStatus("current")


class _SleTrapHostType_Type(Integer32):
    """Custom type sleTrapHostType based on Integer32"""
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
        *(("trapHost", 1),
          ("trap2Host", 2),
          ("informTrapHost", 3),
          ("trap3Host", 4))
    )


_SleTrapHostType_Type.__name__ = "Integer32"
_SleTrapHostType_Object = MibTableColumn
sleTrapHostType = _SleTrapHostType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 1, 1, 1),
    _SleTrapHostType_Type()
)
sleTrapHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostType.setStatus("current")
_SleTrapHostAddress_Type = IpAddress
_SleTrapHostAddress_Object = MibTableColumn
sleTrapHostAddress = _SleTrapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 1, 1, 2),
    _SleTrapHostAddress_Type()
)
sleTrapHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostAddress.setStatus("current")
_SleTrapHostCommunity_Type = OctetString
_SleTrapHostCommunity_Object = MibTableColumn
sleTrapHostCommunity = _SleTrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 1, 1, 3),
    _SleTrapHostCommunity_Type()
)
sleTrapHostCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostCommunity.setStatus("current")
_SleTrapHostPort_Type = Integer32
_SleTrapHostPort_Object = MibTableColumn
sleTrapHostPort = _SleTrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 1, 1, 4),
    _SleTrapHostPort_Type()
)
sleTrapHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostPort.setStatus("current")
_SleTrapHostVrfName_Type = OctetString
_SleTrapHostVrfName_Object = MibTableColumn
sleTrapHostVrfName = _SleTrapHostVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 1, 1, 5),
    _SleTrapHostVrfName_Type()
)
sleTrapHostVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostVrfName.setStatus("current")
_SleTrapHostUser_Type = OctetString
_SleTrapHostUser_Object = MibTableColumn
sleTrapHostUser = _SleTrapHostUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 1, 1, 6),
    _SleTrapHostUser_Type()
)
sleTrapHostUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostUser.setStatus("current")
_SleTrapHostControl_ObjectIdentity = ObjectIdentity
sleTrapHostControl = _SleTrapHostControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2)
)


class _SleTrapHostControlRequest_Type(Integer32):
    """Custom type sleTrapHostControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createTrapHost", 1),
          ("destroyTrapHost", 2))
    )


_SleTrapHostControlRequest_Type.__name__ = "Integer32"
_SleTrapHostControlRequest_Object = MibScalar
sleTrapHostControlRequest = _SleTrapHostControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 1),
    _SleTrapHostControlRequest_Type()
)
sleTrapHostControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostControlRequest.setStatus("current")
_SleTrapHostControlStatus_Type = Integer32
_SleTrapHostControlStatus_Object = MibScalar
sleTrapHostControlStatus = _SleTrapHostControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 2),
    _SleTrapHostControlStatus_Type()
)
sleTrapHostControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostControlStatus.setStatus("current")
_SleTrapHostControlTimer_Type = Gauge32
_SleTrapHostControlTimer_Object = MibScalar
sleTrapHostControlTimer = _SleTrapHostControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 3),
    _SleTrapHostControlTimer_Type()
)
sleTrapHostControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostControlTimer.setStatus("current")
_SleTrapHostControlTimeStamp_Type = TimeTicks
_SleTrapHostControlTimeStamp_Object = MibScalar
sleTrapHostControlTimeStamp = _SleTrapHostControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 4),
    _SleTrapHostControlTimeStamp_Type()
)
sleTrapHostControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostControlTimeStamp.setStatus("current")
_SleTrapHostControlReqResult_Type = Integer32
_SleTrapHostControlReqResult_Object = MibScalar
sleTrapHostControlReqResult = _SleTrapHostControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 5),
    _SleTrapHostControlReqResult_Type()
)
sleTrapHostControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostControlReqResult.setStatus("current")


class _SleTrapHostControlType_Type(Integer32):
    """Custom type sleTrapHostControlType based on Integer32"""
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
        *(("trapHost", 1),
          ("trap2Host", 2),
          ("informTrapHost", 3),
          ("trap3Host", 4))
    )


_SleTrapHostControlType_Type.__name__ = "Integer32"
_SleTrapHostControlType_Object = MibScalar
sleTrapHostControlType = _SleTrapHostControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 6),
    _SleTrapHostControlType_Type()
)
sleTrapHostControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostControlType.setStatus("current")
_SleTrapHostControlAddress_Type = IpAddress
_SleTrapHostControlAddress_Object = MibScalar
sleTrapHostControlAddress = _SleTrapHostControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 7),
    _SleTrapHostControlAddress_Type()
)
sleTrapHostControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostControlAddress.setStatus("current")
_SleTrapHostControlCommunity_Type = OctetString
_SleTrapHostControlCommunity_Object = MibScalar
sleTrapHostControlCommunity = _SleTrapHostControlCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 8),
    _SleTrapHostControlCommunity_Type()
)
sleTrapHostControlCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostControlCommunity.setStatus("current")


class _SleTrapHostControlPort_Type(Integer32):
    """Custom type sleTrapHostControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleTrapHostControlPort_Type.__name__ = "Integer32"
_SleTrapHostControlPort_Object = MibScalar
sleTrapHostControlPort = _SleTrapHostControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 9),
    _SleTrapHostControlPort_Type()
)
sleTrapHostControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostControlPort.setStatus("current")
_SleTrapHostControlVrfName_Type = OctetString
_SleTrapHostControlVrfName_Object = MibScalar
sleTrapHostControlVrfName = _SleTrapHostControlVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 10),
    _SleTrapHostControlVrfName_Type()
)
sleTrapHostControlVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostControlVrfName.setStatus("current")
_SleTrapHostControlUser_Type = OctetString
_SleTrapHostControlUser_Object = MibScalar
sleTrapHostControlUser = _SleTrapHostControlUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 2, 11),
    _SleTrapHostControlUser_Type()
)
sleTrapHostControlUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostControlUser.setStatus("current")
_SleTrapHostNotification_ObjectIdentity = ObjectIdentity
sleTrapHostNotification = _SleTrapHostNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 3)
)
_SleCommunity_ObjectIdentity = ObjectIdentity
sleCommunity = _SleCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4)
)
_SleCommunityTable_Object = MibTable
sleCommunityTable = _SleCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 1)
)
if mibBuilder.loadTexts:
    sleCommunityTable.setStatus("current")
_SleCommunityEntry_Object = MibTableRow
sleCommunityEntry = _SleCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 1, 1)
)
sleCommunityEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleCommunityType"),
    (0, "SLE-SNMP-MIB", "sleCommunityValue"),
)
if mibBuilder.loadTexts:
    sleCommunityEntry.setStatus("current")


class _SleCommunityType_Type(Integer32):
    """Custom type sleCommunityType based on Integer32"""
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


_SleCommunityType_Type.__name__ = "Integer32"
_SleCommunityType_Object = MibTableColumn
sleCommunityType = _SleCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 1, 1, 1),
    _SleCommunityType_Type()
)
sleCommunityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCommunityType.setStatus("current")
_SleCommunityValue_Type = OctetString
_SleCommunityValue_Object = MibTableColumn
sleCommunityValue = _SleCommunityValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 1, 1, 2),
    _SleCommunityValue_Type()
)
sleCommunityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCommunityValue.setStatus("current")
_SleCommunityHost_Type = IpAddress
_SleCommunityHost_Object = MibTableColumn
sleCommunityHost = _SleCommunityHost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 1, 1, 3),
    _SleCommunityHost_Type()
)
sleCommunityHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCommunityHost.setStatus("current")
_SleCommunityOID_Type = ObjectIdentifier
_SleCommunityOID_Object = MibTableColumn
sleCommunityOID = _SleCommunityOID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 1, 1, 4),
    _SleCommunityOID_Type()
)
sleCommunityOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCommunityOID.setStatus("current")
_SleCommunityHostMaskLen_Type = Integer32
_SleCommunityHostMaskLen_Object = MibTableColumn
sleCommunityHostMaskLen = _SleCommunityHostMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 1, 1, 5),
    _SleCommunityHostMaskLen_Type()
)
sleCommunityHostMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCommunityHostMaskLen.setStatus("current")
_SleCommunityControl_ObjectIdentity = ObjectIdentity
sleCommunityControl = _SleCommunityControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2)
)


class _SleCommunityControlRequest_Type(Integer32):
    """Custom type sleCommunityControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createCommunity", 1),
          ("destroyCommunity", 2))
    )


_SleCommunityControlRequest_Type.__name__ = "Integer32"
_SleCommunityControlRequest_Object = MibScalar
sleCommunityControlRequest = _SleCommunityControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2, 1),
    _SleCommunityControlRequest_Type()
)
sleCommunityControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCommunityControlRequest.setStatus("current")
_SleCommunityControlStatus_Type = Integer32
_SleCommunityControlStatus_Object = MibScalar
sleCommunityControlStatus = _SleCommunityControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2, 2),
    _SleCommunityControlStatus_Type()
)
sleCommunityControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCommunityControlStatus.setStatus("current")
_SleCommunityControlTimer_Type = Gauge32
_SleCommunityControlTimer_Object = MibScalar
sleCommunityControlTimer = _SleCommunityControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2, 3),
    _SleCommunityControlTimer_Type()
)
sleCommunityControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCommunityControlTimer.setStatus("current")
_SleCommunityControlTimeStamp_Type = TimeTicks
_SleCommunityControlTimeStamp_Object = MibScalar
sleCommunityControlTimeStamp = _SleCommunityControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2, 4),
    _SleCommunityControlTimeStamp_Type()
)
sleCommunityControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCommunityControlTimeStamp.setStatus("current")
_SleCommunityControlReqResult_Type = Integer32
_SleCommunityControlReqResult_Object = MibScalar
sleCommunityControlReqResult = _SleCommunityControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2, 5),
    _SleCommunityControlReqResult_Type()
)
sleCommunityControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCommunityControlReqResult.setStatus("current")


class _SleCommunityControlType_Type(Integer32):
    """Custom type sleCommunityControlType based on Integer32"""
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


_SleCommunityControlType_Type.__name__ = "Integer32"
_SleCommunityControlType_Object = MibScalar
sleCommunityControlType = _SleCommunityControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2, 6),
    _SleCommunityControlType_Type()
)
sleCommunityControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCommunityControlType.setStatus("current")
_SleCommunityControlValue_Type = OctetString
_SleCommunityControlValue_Object = MibScalar
sleCommunityControlValue = _SleCommunityControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2, 7),
    _SleCommunityControlValue_Type()
)
sleCommunityControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCommunityControlValue.setStatus("current")
_SleCommunityControlHost_Type = IpAddress
_SleCommunityControlHost_Object = MibScalar
sleCommunityControlHost = _SleCommunityControlHost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2, 8),
    _SleCommunityControlHost_Type()
)
sleCommunityControlHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCommunityControlHost.setStatus("current")
_SleCommunityControlOID_Type = ObjectIdentifier
_SleCommunityControlOID_Object = MibScalar
sleCommunityControlOID = _SleCommunityControlOID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2, 9),
    _SleCommunityControlOID_Type()
)
sleCommunityControlOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCommunityControlOID.setStatus("current")
_SleCommunityControlHostMaskLen_Type = Integer32
_SleCommunityControlHostMaskLen_Object = MibScalar
sleCommunityControlHostMaskLen = _SleCommunityControlHostMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 2, 10),
    _SleCommunityControlHostMaskLen_Type()
)
sleCommunityControlHostMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCommunityControlHostMaskLen.setStatus("current")
_SleCommunityNotification_ObjectIdentity = ObjectIdentity
sleCommunityNotification = _SleCommunityNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 3)
)
_SleViewTreeFamily_ObjectIdentity = ObjectIdentity
sleViewTreeFamily = _SleViewTreeFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5)
)
_SleViewTreeFamilyTable_Object = MibTable
sleViewTreeFamilyTable = _SleViewTreeFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 1)
)
if mibBuilder.loadTexts:
    sleViewTreeFamilyTable.setStatus("current")
_SleViewTreeFamilyEntry_Object = MibTableRow
sleViewTreeFamilyEntry = _SleViewTreeFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 1, 1)
)
sleViewTreeFamilyEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleViewTreeFamilyName"),
    (0, "SLE-SNMP-MIB", "sleViewTreeFamilySubtree"),
)
if mibBuilder.loadTexts:
    sleViewTreeFamilyEntry.setStatus("current")
_SleViewTreeFamilyName_Type = OctetString
_SleViewTreeFamilyName_Object = MibTableColumn
sleViewTreeFamilyName = _SleViewTreeFamilyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 1, 1, 1),
    _SleViewTreeFamilyName_Type()
)
sleViewTreeFamilyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleViewTreeFamilyName.setStatus("current")
_SleViewTreeFamilySubtree_Type = ObjectIdentifier
_SleViewTreeFamilySubtree_Object = MibTableColumn
sleViewTreeFamilySubtree = _SleViewTreeFamilySubtree_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 1, 1, 2),
    _SleViewTreeFamilySubtree_Type()
)
sleViewTreeFamilySubtree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleViewTreeFamilySubtree.setStatus("current")
_SleViewTreeFamilyMask_Type = OctetString
_SleViewTreeFamilyMask_Object = MibTableColumn
sleViewTreeFamilyMask = _SleViewTreeFamilyMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 1, 1, 3),
    _SleViewTreeFamilyMask_Type()
)
sleViewTreeFamilyMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleViewTreeFamilyMask.setStatus("current")


class _SleViewTreeFamilyType_Type(Integer32):
    """Custom type sleViewTreeFamilyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("included", 1),
          ("excluded", 2))
    )


_SleViewTreeFamilyType_Type.__name__ = "Integer32"
_SleViewTreeFamilyType_Object = MibTableColumn
sleViewTreeFamilyType = _SleViewTreeFamilyType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 1, 1, 4),
    _SleViewTreeFamilyType_Type()
)
sleViewTreeFamilyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleViewTreeFamilyType.setStatus("current")
_SleViewTreeFamilyControl_ObjectIdentity = ObjectIdentity
sleViewTreeFamilyControl = _SleViewTreeFamilyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 2)
)


class _SleViewTreeFamilyControlRequest_Type(Integer32):
    """Custom type sleViewTreeFamilyControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createViewTreeFamily", 1),
          ("destroyViewTreeFamily", 2))
    )


_SleViewTreeFamilyControlRequest_Type.__name__ = "Integer32"
_SleViewTreeFamilyControlRequest_Object = MibScalar
sleViewTreeFamilyControlRequest = _SleViewTreeFamilyControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 2, 1),
    _SleViewTreeFamilyControlRequest_Type()
)
sleViewTreeFamilyControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleViewTreeFamilyControlRequest.setStatus("current")
_SleViewTreeFamilyControlStatus_Type = Integer32
_SleViewTreeFamilyControlStatus_Object = MibScalar
sleViewTreeFamilyControlStatus = _SleViewTreeFamilyControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 2, 2),
    _SleViewTreeFamilyControlStatus_Type()
)
sleViewTreeFamilyControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleViewTreeFamilyControlStatus.setStatus("current")
_SleViewTreeFamilyControlTimer_Type = Gauge32
_SleViewTreeFamilyControlTimer_Object = MibScalar
sleViewTreeFamilyControlTimer = _SleViewTreeFamilyControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 2, 3),
    _SleViewTreeFamilyControlTimer_Type()
)
sleViewTreeFamilyControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleViewTreeFamilyControlTimer.setStatus("current")
_SleViewTreeFamilyControlTimeStamp_Type = TimeTicks
_SleViewTreeFamilyControlTimeStamp_Object = MibScalar
sleViewTreeFamilyControlTimeStamp = _SleViewTreeFamilyControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 2, 4),
    _SleViewTreeFamilyControlTimeStamp_Type()
)
sleViewTreeFamilyControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleViewTreeFamilyControlTimeStamp.setStatus("current")
_SleViewTreeFamilyControlReqResult_Type = Integer32
_SleViewTreeFamilyControlReqResult_Object = MibScalar
sleViewTreeFamilyControlReqResult = _SleViewTreeFamilyControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 2, 5),
    _SleViewTreeFamilyControlReqResult_Type()
)
sleViewTreeFamilyControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleViewTreeFamilyControlReqResult.setStatus("current")
_SleViewTreeFamilyControlName_Type = OctetString
_SleViewTreeFamilyControlName_Object = MibScalar
sleViewTreeFamilyControlName = _SleViewTreeFamilyControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 2, 6),
    _SleViewTreeFamilyControlName_Type()
)
sleViewTreeFamilyControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleViewTreeFamilyControlName.setStatus("current")
_SleViewTreeFamilyControlSubtree_Type = ObjectIdentifier
_SleViewTreeFamilyControlSubtree_Object = MibScalar
sleViewTreeFamilyControlSubtree = _SleViewTreeFamilyControlSubtree_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 2, 7),
    _SleViewTreeFamilyControlSubtree_Type()
)
sleViewTreeFamilyControlSubtree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleViewTreeFamilyControlSubtree.setStatus("current")
_SleViewTreeFamilyControlMask_Type = OctetString
_SleViewTreeFamilyControlMask_Object = MibScalar
sleViewTreeFamilyControlMask = _SleViewTreeFamilyControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 2, 8),
    _SleViewTreeFamilyControlMask_Type()
)
sleViewTreeFamilyControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleViewTreeFamilyControlMask.setStatus("current")


class _SleViewTreeFamilyControlType_Type(Integer32):
    """Custom type sleViewTreeFamilyControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("included", 1),
          ("excluded", 2))
    )


_SleViewTreeFamilyControlType_Type.__name__ = "Integer32"
_SleViewTreeFamilyControlType_Object = MibScalar
sleViewTreeFamilyControlType = _SleViewTreeFamilyControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 2, 9),
    _SleViewTreeFamilyControlType_Type()
)
sleViewTreeFamilyControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleViewTreeFamilyControlType.setStatus("current")
_SleViewTreeFamilyNotification_ObjectIdentity = ObjectIdentity
sleViewTreeFamilyNotification = _SleViewTreeFamilyNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 3)
)
_SleAccess_ObjectIdentity = ObjectIdentity
sleAccess = _SleAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6)
)
_SleAccessTable_Object = MibTable
sleAccessTable = _SleAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 1)
)
if mibBuilder.loadTexts:
    sleAccessTable.setStatus("current")
_SleAccessEntry_Object = MibTableRow
sleAccessEntry = _SleAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 1, 1)
)
sleAccessEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleAccessGroupName"),
)
if mibBuilder.loadTexts:
    sleAccessEntry.setStatus("current")
_SleAccessGroupName_Type = OctetString
_SleAccessGroupName_Object = MibTableColumn
sleAccessGroupName = _SleAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 1, 1, 1),
    _SleAccessGroupName_Type()
)
sleAccessGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAccessGroupName.setStatus("current")


class _SleAccessSecurityModel_Type(Integer32):
    """Custom type sleAccessSecurityModel based on Integer32"""
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
        *(("any", 0),
          ("snmpV1", 1),
          ("snmpV2", 2),
          ("usm", 3))
    )


_SleAccessSecurityModel_Type.__name__ = "Integer32"
_SleAccessSecurityModel_Object = MibTableColumn
sleAccessSecurityModel = _SleAccessSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 1, 1, 2),
    _SleAccessSecurityModel_Type()
)
sleAccessSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAccessSecurityModel.setStatus("current")


class _SleAccessSecurityLevel_Type(Integer32):
    """Custom type sleAccessSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPrivn", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_SleAccessSecurityLevel_Type.__name__ = "Integer32"
_SleAccessSecurityLevel_Object = MibTableColumn
sleAccessSecurityLevel = _SleAccessSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 1, 1, 3),
    _SleAccessSecurityLevel_Type()
)
sleAccessSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAccessSecurityLevel.setStatus("current")
_SleAccessReadViewName_Type = OctetString
_SleAccessReadViewName_Object = MibTableColumn
sleAccessReadViewName = _SleAccessReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 1, 1, 4),
    _SleAccessReadViewName_Type()
)
sleAccessReadViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAccessReadViewName.setStatus("current")
_SleAccessWriteViewName_Type = OctetString
_SleAccessWriteViewName_Object = MibTableColumn
sleAccessWriteViewName = _SleAccessWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 1, 1, 5),
    _SleAccessWriteViewName_Type()
)
sleAccessWriteViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAccessWriteViewName.setStatus("current")
_SleAccessNotifyViewName_Type = OctetString
_SleAccessNotifyViewName_Object = MibTableColumn
sleAccessNotifyViewName = _SleAccessNotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 1, 1, 6),
    _SleAccessNotifyViewName_Type()
)
sleAccessNotifyViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAccessNotifyViewName.setStatus("current")
_SleAccessControl_ObjectIdentity = ObjectIdentity
sleAccessControl = _SleAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2)
)


class _SleAccessControlRequest_Type(Integer32):
    """Custom type sleAccessControlRequest based on Integer32"""
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
          ("destroyAccess", 2),
          ("setAccessProfile", 3))
    )


_SleAccessControlRequest_Type.__name__ = "Integer32"
_SleAccessControlRequest_Object = MibScalar
sleAccessControlRequest = _SleAccessControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 1),
    _SleAccessControlRequest_Type()
)
sleAccessControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAccessControlRequest.setStatus("current")
_SleAccessControlStatus_Type = Integer32
_SleAccessControlStatus_Object = MibScalar
sleAccessControlStatus = _SleAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 2),
    _SleAccessControlStatus_Type()
)
sleAccessControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAccessControlStatus.setStatus("current")
_SleAccessControlTimer_Type = Gauge32
_SleAccessControlTimer_Object = MibScalar
sleAccessControlTimer = _SleAccessControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 3),
    _SleAccessControlTimer_Type()
)
sleAccessControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAccessControlTimer.setStatus("current")
_SleAccessControlTimeStamp_Type = TimeTicks
_SleAccessControlTimeStamp_Object = MibScalar
sleAccessControlTimeStamp = _SleAccessControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 4),
    _SleAccessControlTimeStamp_Type()
)
sleAccessControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAccessControlTimeStamp.setStatus("current")
_SleAccessControlReqResult_Type = Integer32
_SleAccessControlReqResult_Object = MibScalar
sleAccessControlReqResult = _SleAccessControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 5),
    _SleAccessControlReqResult_Type()
)
sleAccessControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAccessControlReqResult.setStatus("current")
_SleAccessControlGroupName_Type = OctetString
_SleAccessControlGroupName_Object = MibScalar
sleAccessControlGroupName = _SleAccessControlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 6),
    _SleAccessControlGroupName_Type()
)
sleAccessControlGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAccessControlGroupName.setStatus("current")


class _SleAccessControlSecurityModel_Type(Integer32):
    """Custom type sleAccessControlSecurityModel based on Integer32"""
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
        *(("any", 0),
          ("snmpV1", 1),
          ("snmpV2", 2),
          ("usm", 3))
    )


_SleAccessControlSecurityModel_Type.__name__ = "Integer32"
_SleAccessControlSecurityModel_Object = MibScalar
sleAccessControlSecurityModel = _SleAccessControlSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 7),
    _SleAccessControlSecurityModel_Type()
)
sleAccessControlSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAccessControlSecurityModel.setStatus("current")


class _SleAccessControlSecurityLevel_Type(Integer32):
    """Custom type sleAccessControlSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPrivn", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_SleAccessControlSecurityLevel_Type.__name__ = "Integer32"
_SleAccessControlSecurityLevel_Object = MibScalar
sleAccessControlSecurityLevel = _SleAccessControlSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 8),
    _SleAccessControlSecurityLevel_Type()
)
sleAccessControlSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAccessControlSecurityLevel.setStatus("current")
_SleAccessControlReadViewName_Type = OctetString
_SleAccessControlReadViewName_Object = MibScalar
sleAccessControlReadViewName = _SleAccessControlReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 9),
    _SleAccessControlReadViewName_Type()
)
sleAccessControlReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAccessControlReadViewName.setStatus("current")
_SleAccessControlWriteViewName_Type = OctetString
_SleAccessControlWriteViewName_Object = MibScalar
sleAccessControlWriteViewName = _SleAccessControlWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 10),
    _SleAccessControlWriteViewName_Type()
)
sleAccessControlWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAccessControlWriteViewName.setStatus("current")
_SleAccessControlNotifyViewName_Type = OctetString
_SleAccessControlNotifyViewName_Object = MibScalar
sleAccessControlNotifyViewName = _SleAccessControlNotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 2, 11),
    _SleAccessControlNotifyViewName_Type()
)
sleAccessControlNotifyViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAccessControlNotifyViewName.setStatus("current")
_SleAccessNotification_ObjectIdentity = ObjectIdentity
sleAccessNotification = _SleAccessNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 3)
)
_SleSecurityToGroup_ObjectIdentity = ObjectIdentity
sleSecurityToGroup = _SleSecurityToGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7)
)
_SleSecurityToGroupTable_Object = MibTable
sleSecurityToGroupTable = _SleSecurityToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 1)
)
if mibBuilder.loadTexts:
    sleSecurityToGroupTable.setStatus("current")
_SleSecurityToGroupEntry_Object = MibTableRow
sleSecurityToGroupEntry = _SleSecurityToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 1, 1)
)
sleSecurityToGroupEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleSecurityToGroupSName"),
    (0, "SLE-SNMP-MIB", "sleSecurityToGroupModel"),
)
if mibBuilder.loadTexts:
    sleSecurityToGroupEntry.setStatus("current")
_SleSecurityToGroupSName_Type = OctetString
_SleSecurityToGroupSName_Object = MibTableColumn
sleSecurityToGroupSName = _SleSecurityToGroupSName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 1, 1, 1),
    _SleSecurityToGroupSName_Type()
)
sleSecurityToGroupSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityToGroupSName.setStatus("current")


class _SleSecurityToGroupModel_Type(Integer32):
    """Custom type sleSecurityToGroupModel based on Integer32"""
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
        *(("any", 0),
          ("snmpV1", 1),
          ("snmpV2", 2),
          ("usm", 3))
    )


_SleSecurityToGroupModel_Type.__name__ = "Integer32"
_SleSecurityToGroupModel_Object = MibTableColumn
sleSecurityToGroupModel = _SleSecurityToGroupModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 1, 1, 2),
    _SleSecurityToGroupModel_Type()
)
sleSecurityToGroupModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityToGroupModel.setStatus("current")
_SleSecurityToGroupGName_Type = OctetString
_SleSecurityToGroupGName_Object = MibTableColumn
sleSecurityToGroupGName = _SleSecurityToGroupGName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 1, 1, 3),
    _SleSecurityToGroupGName_Type()
)
sleSecurityToGroupGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityToGroupGName.setStatus("current")
_SleSecurityToGroupControl_ObjectIdentity = ObjectIdentity
sleSecurityToGroupControl = _SleSecurityToGroupControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 2)
)


class _SleSecurityToGroupControlRequest_Type(Integer32):
    """Custom type sleSecurityToGroupControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createSecurityToGroup", 1),
          ("destroySecurityToGroup", 2),
          ("setSecurityToGroupProfile", 3))
    )


_SleSecurityToGroupControlRequest_Type.__name__ = "Integer32"
_SleSecurityToGroupControlRequest_Object = MibScalar
sleSecurityToGroupControlRequest = _SleSecurityToGroupControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 2, 1),
    _SleSecurityToGroupControlRequest_Type()
)
sleSecurityToGroupControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityToGroupControlRequest.setStatus("current")
_SleSecurityToGroupControlStatus_Type = Integer32
_SleSecurityToGroupControlStatus_Object = MibScalar
sleSecurityToGroupControlStatus = _SleSecurityToGroupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 2, 2),
    _SleSecurityToGroupControlStatus_Type()
)
sleSecurityToGroupControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityToGroupControlStatus.setStatus("current")
_SleSecurityToGroupControlTimer_Type = Gauge32
_SleSecurityToGroupControlTimer_Object = MibScalar
sleSecurityToGroupControlTimer = _SleSecurityToGroupControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 2, 3),
    _SleSecurityToGroupControlTimer_Type()
)
sleSecurityToGroupControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityToGroupControlTimer.setStatus("current")
_SleSecurityToGroupControlTimeStamp_Type = TimeTicks
_SleSecurityToGroupControlTimeStamp_Object = MibScalar
sleSecurityToGroupControlTimeStamp = _SleSecurityToGroupControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 2, 4),
    _SleSecurityToGroupControlTimeStamp_Type()
)
sleSecurityToGroupControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityToGroupControlTimeStamp.setStatus("current")
_SleSecurityToGroupControlReqResult_Type = Integer32
_SleSecurityToGroupControlReqResult_Object = MibScalar
sleSecurityToGroupControlReqResult = _SleSecurityToGroupControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 2, 5),
    _SleSecurityToGroupControlReqResult_Type()
)
sleSecurityToGroupControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityToGroupControlReqResult.setStatus("current")
_SleSecurityToGroupControlGName_Type = OctetString
_SleSecurityToGroupControlGName_Object = MibScalar
sleSecurityToGroupControlGName = _SleSecurityToGroupControlGName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 2, 6),
    _SleSecurityToGroupControlGName_Type()
)
sleSecurityToGroupControlGName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityToGroupControlGName.setStatus("current")


class _SleSecurityToGroupControlModel_Type(Integer32):
    """Custom type sleSecurityToGroupControlModel based on Integer32"""
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
        *(("any", 0),
          ("snmpV1", 1),
          ("snmpV2", 2),
          ("usm", 3))
    )


_SleSecurityToGroupControlModel_Type.__name__ = "Integer32"
_SleSecurityToGroupControlModel_Object = MibScalar
sleSecurityToGroupControlModel = _SleSecurityToGroupControlModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 2, 7),
    _SleSecurityToGroupControlModel_Type()
)
sleSecurityToGroupControlModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityToGroupControlModel.setStatus("current")
_SleSecurityToGroupControlSName_Type = OctetString
_SleSecurityToGroupControlSName_Object = MibScalar
sleSecurityToGroupControlSName = _SleSecurityToGroupControlSName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 2, 8),
    _SleSecurityToGroupControlSName_Type()
)
sleSecurityToGroupControlSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityToGroupControlSName.setStatus("current")
_SleSecurityToGroupNotification_ObjectIdentity = ObjectIdentity
sleSecurityToGroupNotification = _SleSecurityToGroupNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 3)
)
_SleUser_ObjectIdentity = ObjectIdentity
sleUser = _SleUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8)
)
_SleUserTable_Object = MibTable
sleUserTable = _SleUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 1)
)
if mibBuilder.loadTexts:
    sleUserTable.setStatus("current")
_SleUserEntry_Object = MibTableRow
sleUserEntry = _SleUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 1, 1)
)
sleUserEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleUserName"),
)
if mibBuilder.loadTexts:
    sleUserEntry.setStatus("current")
_SleUserName_Type = OctetString
_SleUserName_Object = MibTableColumn
sleUserName = _SleUserName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 1, 1, 1),
    _SleUserName_Type()
)
sleUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserName.setStatus("current")


class _SleUserAuthType_Type(Integer32):
    """Custom type sleUserAuthType based on Integer32"""
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


_SleUserAuthType_Type.__name__ = "Integer32"
_SleUserAuthType_Object = MibTableColumn
sleUserAuthType = _SleUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 1, 1, 2),
    _SleUserAuthType_Type()
)
sleUserAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserAuthType.setStatus("current")
_SleUserAuthKey_Type = OctetString
_SleUserAuthKey_Object = MibTableColumn
sleUserAuthKey = _SleUserAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 1, 1, 3),
    _SleUserAuthKey_Type()
)
sleUserAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserAuthKey.setStatus("current")


class _SleUserPrivType_Type(Integer32):
    """Custom type sleUserPrivType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPrivacy", 1),
          ("des", 2))
    )


_SleUserPrivType_Type.__name__ = "Integer32"
_SleUserPrivType_Object = MibTableColumn
sleUserPrivType = _SleUserPrivType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 1, 1, 4),
    _SleUserPrivType_Type()
)
sleUserPrivType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserPrivType.setStatus("current")
_SleUserPrivKey_Type = OctetString
_SleUserPrivKey_Object = MibTableColumn
sleUserPrivKey = _SleUserPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 1, 1, 5),
    _SleUserPrivKey_Type()
)
sleUserPrivKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserPrivKey.setStatus("current")
_SleUserControl_ObjectIdentity = ObjectIdentity
sleUserControl = _SleUserControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2)
)


class _SleUserControlRequest_Type(Integer32):
    """Custom type sleUserControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createUser", 1),
          ("destroyUser", 2))
    )


_SleUserControlRequest_Type.__name__ = "Integer32"
_SleUserControlRequest_Object = MibScalar
sleUserControlRequest = _SleUserControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2, 1),
    _SleUserControlRequest_Type()
)
sleUserControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserControlRequest.setStatus("current")
_SleUserControlStatus_Type = Integer32
_SleUserControlStatus_Object = MibScalar
sleUserControlStatus = _SleUserControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2, 2),
    _SleUserControlStatus_Type()
)
sleUserControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserControlStatus.setStatus("current")
_SleUserControlTimer_Type = Gauge32
_SleUserControlTimer_Object = MibScalar
sleUserControlTimer = _SleUserControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2, 3),
    _SleUserControlTimer_Type()
)
sleUserControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserControlTimer.setStatus("current")
_SleUserControlTimeStamp_Type = TimeTicks
_SleUserControlTimeStamp_Object = MibScalar
sleUserControlTimeStamp = _SleUserControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2, 4),
    _SleUserControlTimeStamp_Type()
)
sleUserControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserControlTimeStamp.setStatus("current")
_SleUserControlReqResult_Type = Integer32
_SleUserControlReqResult_Object = MibScalar
sleUserControlReqResult = _SleUserControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2, 5),
    _SleUserControlReqResult_Type()
)
sleUserControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleUserControlReqResult.setStatus("current")
_SleUserControlName_Type = OctetString
_SleUserControlName_Object = MibScalar
sleUserControlName = _SleUserControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2, 6),
    _SleUserControlName_Type()
)
sleUserControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserControlName.setStatus("current")


class _SleUserControlAuthType_Type(Integer32):
    """Custom type sleUserControlAuthType based on Integer32"""
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


_SleUserControlAuthType_Type.__name__ = "Integer32"
_SleUserControlAuthType_Object = MibScalar
sleUserControlAuthType = _SleUserControlAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2, 7),
    _SleUserControlAuthType_Type()
)
sleUserControlAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserControlAuthType.setStatus("current")
_SleUserControlAuthKey_Type = OctetString
_SleUserControlAuthKey_Object = MibScalar
sleUserControlAuthKey = _SleUserControlAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2, 8),
    _SleUserControlAuthKey_Type()
)
sleUserControlAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserControlAuthKey.setStatus("current")


class _SleUserControlPrivType_Type(Integer32):
    """Custom type sleUserControlPrivType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPrivacy", 1),
          ("des", 2))
    )


_SleUserControlPrivType_Type.__name__ = "Integer32"
_SleUserControlPrivType_Object = MibScalar
sleUserControlPrivType = _SleUserControlPrivType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2, 9),
    _SleUserControlPrivType_Type()
)
sleUserControlPrivType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserControlPrivType.setStatus("current")
_SleUserControlPrivKey_Type = OctetString
_SleUserControlPrivKey_Object = MibScalar
sleUserControlPrivKey = _SleUserControlPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 2, 10),
    _SleUserControlPrivKey_Type()
)
sleUserControlPrivKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleUserControlPrivKey.setStatus("current")
_SleUserNotification_ObjectIdentity = ObjectIdentity
sleUserNotification = _SleUserNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 3)
)
_SleAgent_ObjectIdentity = ObjectIdentity
sleAgent = _SleAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9)
)
_SleAgentInfo_ObjectIdentity = ObjectIdentity
sleAgentInfo = _SleAgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 1)
)
_SleAgentAddress_Type = IpAddress
_SleAgentAddress_Object = MibScalar
sleAgentAddress = _SleAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 1, 1),
    _SleAgentAddress_Type()
)
sleAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAgentAddress.setStatus("current")
_SleAgentInterface_Type = OctetString
_SleAgentInterface_Object = MibScalar
sleAgentInterface = _SleAgentInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 1, 2),
    _SleAgentInterface_Type()
)
sleAgentInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAgentInterface.setStatus("current")
_SleAgentControl_ObjectIdentity = ObjectIdentity
sleAgentControl = _SleAgentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 2)
)


class _SleAgentControlRequest_Type(Integer32):
    """Custom type sleAgentControlRequest based on Integer32"""
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
        *(("setSnmpAgentAddress", 1),
          ("setSnmpAgentInterface", 2),
          ("destroySnmpAgentAddress", 3),
          ("destroySnmpAgentInterface", 4))
    )


_SleAgentControlRequest_Type.__name__ = "Integer32"
_SleAgentControlRequest_Object = MibScalar
sleAgentControlRequest = _SleAgentControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 2, 1),
    _SleAgentControlRequest_Type()
)
sleAgentControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAgentControlRequest.setStatus("current")
_SleAgentControlStatus_Type = Integer32
_SleAgentControlStatus_Object = MibScalar
sleAgentControlStatus = _SleAgentControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 2, 2),
    _SleAgentControlStatus_Type()
)
sleAgentControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAgentControlStatus.setStatus("current")
_SleAgentControlTimer_Type = Gauge32
_SleAgentControlTimer_Object = MibScalar
sleAgentControlTimer = _SleAgentControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 2, 3),
    _SleAgentControlTimer_Type()
)
sleAgentControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAgentControlTimer.setStatus("current")
_SleAgentControlTimeStamp_Type = TimeTicks
_SleAgentControlTimeStamp_Object = MibScalar
sleAgentControlTimeStamp = _SleAgentControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 2, 4),
    _SleAgentControlTimeStamp_Type()
)
sleAgentControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAgentControlTimeStamp.setStatus("current")
_SleAgentControlReqResult_Type = Integer32
_SleAgentControlReqResult_Object = MibScalar
sleAgentControlReqResult = _SleAgentControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 2, 5),
    _SleAgentControlReqResult_Type()
)
sleAgentControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAgentControlReqResult.setStatus("current")
_SleAgentControlAddress_Type = IpAddress
_SleAgentControlAddress_Object = MibScalar
sleAgentControlAddress = _SleAgentControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 2, 6),
    _SleAgentControlAddress_Type()
)
sleAgentControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAgentControlAddress.setStatus("current")
_SleAgentControlInterface_Type = OctetString
_SleAgentControlInterface_Object = MibScalar
sleAgentControlInterface = _SleAgentControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 2, 7),
    _SleAgentControlInterface_Type()
)
sleAgentControlInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAgentControlInterface.setStatus("current")
_SleAgentNotification_ObjectIdentity = ObjectIdentity
sleAgentNotification = _SleAgentNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 3)
)
_SleSnmpSesson_ObjectIdentity = ObjectIdentity
sleSnmpSesson = _SleSnmpSesson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10)
)
_SleSnmpSessionInfo_ObjectIdentity = ObjectIdentity
sleSnmpSessionInfo = _SleSnmpSessionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 1)
)
_SleSnmpSessionTimeout_Type = Integer32
_SleSnmpSessionTimeout_Object = MibScalar
sleSnmpSessionTimeout = _SleSnmpSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 1, 1),
    _SleSnmpSessionTimeout_Type()
)
sleSnmpSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sleSnmpSessionTimeout.setUnits("sec")
_SleSnmpSessionTable_Object = MibTable
sleSnmpSessionTable = _SleSnmpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 2)
)
if mibBuilder.loadTexts:
    sleSnmpSessionTable.setStatus("current")
_SleSnmpSessionEntry_Object = MibTableRow
sleSnmpSessionEntry = _SleSnmpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 2, 1)
)
sleSnmpSessionEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleSnmpSessionIpAddr"),
    (0, "SLE-SNMP-MIB", "sleSnmpSessionCommunity"),
)
if mibBuilder.loadTexts:
    sleSnmpSessionEntry.setStatus("current")
_SleSnmpSessionIpAddr_Type = IpAddress
_SleSnmpSessionIpAddr_Object = MibTableColumn
sleSnmpSessionIpAddr = _SleSnmpSessionIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 2, 1, 1),
    _SleSnmpSessionIpAddr_Type()
)
sleSnmpSessionIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpSessionIpAddr.setStatus("current")
_SleSnmpSessionCommunity_Type = OctetString
_SleSnmpSessionCommunity_Object = MibTableColumn
sleSnmpSessionCommunity = _SleSnmpSessionCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 2, 1, 2),
    _SleSnmpSessionCommunity_Type()
)
sleSnmpSessionCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpSessionCommunity.setStatus("current")
_SleSnmpSessionSnmpVersion_Type = Integer32
_SleSnmpSessionSnmpVersion_Object = MibTableColumn
sleSnmpSessionSnmpVersion = _SleSnmpSessionSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 2, 1, 3),
    _SleSnmpSessionSnmpVersion_Type()
)
sleSnmpSessionSnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpSessionSnmpVersion.setStatus("current")
_SleSnmpSessionAccessTIme_Type = OctetString
_SleSnmpSessionAccessTIme_Object = MibTableColumn
sleSnmpSessionAccessTIme = _SleSnmpSessionAccessTIme_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 2, 1, 4),
    _SleSnmpSessionAccessTIme_Type()
)
sleSnmpSessionAccessTIme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpSessionAccessTIme.setStatus("current")
_SleSnmpSessiontControl_ObjectIdentity = ObjectIdentity
sleSnmpSessiontControl = _SleSnmpSessiontControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 3)
)


class _SleSnmpSessionControlRequest_Type(Integer32):
    """Custom type sleSnmpSessionControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setSnmpsessionTimeout", 1)
    )


_SleSnmpSessionControlRequest_Type.__name__ = "Integer32"
_SleSnmpSessionControlRequest_Object = MibScalar
sleSnmpSessionControlRequest = _SleSnmpSessionControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 3, 1),
    _SleSnmpSessionControlRequest_Type()
)
sleSnmpSessionControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpSessionControlRequest.setStatus("current")
_SleSnmpSessionControlStatus_Type = Integer32
_SleSnmpSessionControlStatus_Object = MibScalar
sleSnmpSessionControlStatus = _SleSnmpSessionControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 3, 2),
    _SleSnmpSessionControlStatus_Type()
)
sleSnmpSessionControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpSessionControlStatus.setStatus("current")
_SleSnmpSessionControlTimer_Type = Gauge32
_SleSnmpSessionControlTimer_Object = MibScalar
sleSnmpSessionControlTimer = _SleSnmpSessionControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 3, 3),
    _SleSnmpSessionControlTimer_Type()
)
sleSnmpSessionControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpSessionControlTimer.setStatus("current")
_SleSnmpSessionControlTimeStamp_Type = TimeTicks
_SleSnmpSessionControlTimeStamp_Object = MibScalar
sleSnmpSessionControlTimeStamp = _SleSnmpSessionControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 3, 4),
    _SleSnmpSessionControlTimeStamp_Type()
)
sleSnmpSessionControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpSessionControlTimeStamp.setStatus("current")
_SleSnmpSessionControlReqResult_Type = Integer32
_SleSnmpSessionControlReqResult_Object = MibScalar
sleSnmpSessionControlReqResult = _SleSnmpSessionControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 3, 5),
    _SleSnmpSessionControlReqResult_Type()
)
sleSnmpSessionControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpSessionControlReqResult.setStatus("current")
_SleSnmpSessionControlTimeout_Type = Integer32
_SleSnmpSessionControlTimeout_Object = MibScalar
sleSnmpSessionControlTimeout = _SleSnmpSessionControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 3, 6),
    _SleSnmpSessionControlTimeout_Type()
)
sleSnmpSessionControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpSessionControlTimeout.setStatus("current")
_SleSnmpSessionNotifications_ObjectIdentity = ObjectIdentity
sleSnmpSessionNotifications = _SleSnmpSessionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 4)
)
_SleSnmpTrap_ObjectIdentity = ObjectIdentity
sleSnmpTrap = _SleSnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11)
)
_SleSnmpTrapTable_Object = MibTable
sleSnmpTrapTable = _SleSnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 1)
)
if mibBuilder.loadTexts:
    sleSnmpTrapTable.setStatus("current")
_SleSnmpTrapEntry_Object = MibTableRow
sleSnmpTrapEntry = _SleSnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 1, 1)
)
sleSnmpTrapEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleSnmpTrapIndex"),
)
if mibBuilder.loadTexts:
    sleSnmpTrapEntry.setStatus("current")


class _SleSnmpTrapIndex_Type(Integer32):
    """Custom type sleSnmpTrapIndex based on Integer32"""
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
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("linkUp", 1),
          ("linkDown", 2),
          ("authFail", 3),
          ("coldStart", 4),
          ("cpuThreshold", 5),
          ("portThreshold", 6),
          ("power", 7),
          ("module", 8),
          ("fan", 9),
          ("dhcpLease", 10),
          ("temperThreshold", 11),
          ("memoryThreshold", 12),
          ("igmp", 13),
          ("autoCli", 14),
          ("autoReset", 15),
          ("door", 16),
          ("battery", 17),
          ("epon", 18),
          ("adminAccess", 19),
          ("swWatchdog", 20),
          ("cliHistory", 50),
          ("commandLog", 51))
    )


_SleSnmpTrapIndex_Type.__name__ = "Integer32"
_SleSnmpTrapIndex_Object = MibTableColumn
sleSnmpTrapIndex = _SleSnmpTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 1, 1, 1),
    _SleSnmpTrapIndex_Type()
)
sleSnmpTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapIndex.setStatus("current")


class _SleSnmpTrapStatus_Type(Integer32):
    """Custom type sleSnmpTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSnmpTrapStatus_Type.__name__ = "Integer32"
_SleSnmpTrapStatus_Object = MibTableColumn
sleSnmpTrapStatus = _SleSnmpTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 1, 1, 2),
    _SleSnmpTrapStatus_Type()
)
sleSnmpTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapStatus.setStatus("current")
_SleSnmpTrapPortTable_Object = MibTable
sleSnmpTrapPortTable = _SleSnmpTrapPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 2)
)
if mibBuilder.loadTexts:
    sleSnmpTrapPortTable.setStatus("current")
_SleSnmpTrapPortEntry_Object = MibTableRow
sleSnmpTrapPortEntry = _SleSnmpTrapPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 2, 1)
)
sleSnmpTrapPortEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleSnmpTrapPortIndex"),
    (0, "SLE-SNMP-MIB", "sleSnmpTrapPortType"),
)
if mibBuilder.loadTexts:
    sleSnmpTrapPortEntry.setStatus("current")


class _SleSnmpTrapPortIndex_Type(Integer32):
    """Custom type sleSnmpTrapPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SleSnmpTrapPortIndex_Type.__name__ = "Integer32"
_SleSnmpTrapPortIndex_Object = MibTableColumn
sleSnmpTrapPortIndex = _SleSnmpTrapPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 2, 1, 1),
    _SleSnmpTrapPortIndex_Type()
)
sleSnmpTrapPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapPortIndex.setStatus("current")


class _SleSnmpTrapPortType_Type(Integer32):
    """Custom type sleSnmpTrapPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkUp", 1),
          ("linkDown", 2))
    )


_SleSnmpTrapPortType_Type.__name__ = "Integer32"
_SleSnmpTrapPortType_Object = MibTableColumn
sleSnmpTrapPortType = _SleSnmpTrapPortType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 2, 1, 2),
    _SleSnmpTrapPortType_Type()
)
sleSnmpTrapPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapPortType.setStatus("current")


class _SleSnmpTrapPortStatus_Type(Integer32):
    """Custom type sleSnmpTrapPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSnmpTrapPortStatus_Type.__name__ = "Integer32"
_SleSnmpTrapPortStatus_Object = MibTableColumn
sleSnmpTrapPortStatus = _SleSnmpTrapPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 2, 1, 3),
    _SleSnmpTrapPortStatus_Type()
)
sleSnmpTrapPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapPortStatus.setStatus("current")
_SleSnmpTrapControl_ObjectIdentity = ObjectIdentity
sleSnmpTrapControl = _SleSnmpTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 3)
)


class _SleSnmpTrapControlRequest_Type(Integer32):
    """Custom type sleSnmpTrapControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setSnmpTrapStatus", 1),
          ("setSnmpTrapStatusByport", 2))
    )


_SleSnmpTrapControlRequest_Type.__name__ = "Integer32"
_SleSnmpTrapControlRequest_Object = MibScalar
sleSnmpTrapControlRequest = _SleSnmpTrapControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 3, 1),
    _SleSnmpTrapControlRequest_Type()
)
sleSnmpTrapControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapControlRequest.setStatus("current")
_SleSnmpTrapControlStatus_Type = Integer32
_SleSnmpTrapControlStatus_Object = MibScalar
sleSnmpTrapControlStatus = _SleSnmpTrapControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 3, 2),
    _SleSnmpTrapControlStatus_Type()
)
sleSnmpTrapControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapControlStatus.setStatus("current")
_SleSnmpTrapControlTimer_Type = Gauge32
_SleSnmpTrapControlTimer_Object = MibScalar
sleSnmpTrapControlTimer = _SleSnmpTrapControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 3, 3),
    _SleSnmpTrapControlTimer_Type()
)
sleSnmpTrapControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapControlTimer.setStatus("current")
_SleSnmpTrapControlTimeStamp_Type = TimeTicks
_SleSnmpTrapControlTimeStamp_Object = MibScalar
sleSnmpTrapControlTimeStamp = _SleSnmpTrapControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 3, 4),
    _SleSnmpTrapControlTimeStamp_Type()
)
sleSnmpTrapControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapControlTimeStamp.setStatus("current")
_SleSnmpTrapControlReqResult_Type = Integer32
_SleSnmpTrapControlReqResult_Object = MibScalar
sleSnmpTrapControlReqResult = _SleSnmpTrapControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 3, 5),
    _SleSnmpTrapControlReqResult_Type()
)
sleSnmpTrapControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapControlReqResult.setStatus("current")


class _SleSnmpTrapControlTrapIndex_Type(Integer32):
    """Custom type sleSnmpTrapControlTrapIndex based on Integer32"""
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
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("linkUp", 1),
          ("linkDown", 2),
          ("authFail", 3),
          ("coldStart", 4),
          ("cpuThreshold", 5),
          ("portThreshold", 6),
          ("power", 7),
          ("module", 8),
          ("fan", 9),
          ("dhcpLease", 10),
          ("temperThreshold", 11),
          ("memoryThreshold", 12),
          ("igmp", 13),
          ("autoCli", 14),
          ("autoReset", 15),
          ("door", 16),
          ("battery", 17),
          ("epon", 18),
          ("adminAccess", 19),
          ("swWatchdog", 20),
          ("cliHistory", 50),
          ("commandLog", 51))
    )


_SleSnmpTrapControlTrapIndex_Type.__name__ = "Integer32"
_SleSnmpTrapControlTrapIndex_Object = MibScalar
sleSnmpTrapControlTrapIndex = _SleSnmpTrapControlTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 3, 6),
    _SleSnmpTrapControlTrapIndex_Type()
)
sleSnmpTrapControlTrapIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapControlTrapIndex.setStatus("current")
_SleSnmpTrapControlPortIndex_Type = Integer32
_SleSnmpTrapControlPortIndex_Object = MibScalar
sleSnmpTrapControlPortIndex = _SleSnmpTrapControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 3, 7),
    _SleSnmpTrapControlPortIndex_Type()
)
sleSnmpTrapControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapControlPortIndex.setStatus("current")


class _SleSnmpTrapControlTrapStatus_Type(Integer32):
    """Custom type sleSnmpTrapControlTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSnmpTrapControlTrapStatus_Type.__name__ = "Integer32"
_SleSnmpTrapControlTrapStatus_Object = MibScalar
sleSnmpTrapControlTrapStatus = _SleSnmpTrapControlTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 3, 8),
    _SleSnmpTrapControlTrapStatus_Type()
)
sleSnmpTrapControlTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapControlTrapStatus.setStatus("current")
_SleSnmpTrapNotification_ObjectIdentity = ObjectIdentity
sleSnmpTrapNotification = _SleSnmpTrapNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 4)
)
_SleSnmpTrapSource_ObjectIdentity = ObjectIdentity
sleSnmpTrapSource = _SleSnmpTrapSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12)
)
_SleSnmpTrapSourceInfo_ObjectIdentity = ObjectIdentity
sleSnmpTrapSourceInfo = _SleSnmpTrapSourceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 1)
)
_SleSnmpTrapSourceAddress_Type = IpAddress
_SleSnmpTrapSourceAddress_Object = MibScalar
sleSnmpTrapSourceAddress = _SleSnmpTrapSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 1, 1),
    _SleSnmpTrapSourceAddress_Type()
)
sleSnmpTrapSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapSourceAddress.setStatus("current")
_SleSnmpTrapSourceInterface_Type = OctetString
_SleSnmpTrapSourceInterface_Object = MibScalar
sleSnmpTrapSourceInterface = _SleSnmpTrapSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 1, 2),
    _SleSnmpTrapSourceInterface_Type()
)
sleSnmpTrapSourceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapSourceInterface.setStatus("current")
_SleSnmpTrapSourceControl_ObjectIdentity = ObjectIdentity
sleSnmpTrapSourceControl = _SleSnmpTrapSourceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 2)
)


class _SleSnmpTrapSourceControlRequest_Type(Integer32):
    """Custom type sleSnmpTrapSourceControlRequest based on Integer32"""
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
        *(("setSnmpTrapSourceAddress", 1),
          ("setSnmpTrapSourceInterface", 2),
          ("destroySnmpTrapSourceAddress", 3),
          ("destroySnmpTrapSourceInterface", 4))
    )


_SleSnmpTrapSourceControlRequest_Type.__name__ = "Integer32"
_SleSnmpTrapSourceControlRequest_Object = MibScalar
sleSnmpTrapSourceControlRequest = _SleSnmpTrapSourceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 2, 1),
    _SleSnmpTrapSourceControlRequest_Type()
)
sleSnmpTrapSourceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapSourceControlRequest.setStatus("current")
_SleSnmpTrapSourceControlStatus_Type = Integer32
_SleSnmpTrapSourceControlStatus_Object = MibScalar
sleSnmpTrapSourceControlStatus = _SleSnmpTrapSourceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 2, 2),
    _SleSnmpTrapSourceControlStatus_Type()
)
sleSnmpTrapSourceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapSourceControlStatus.setStatus("current")
_SleSnmpTrapSourceControlTimer_Type = Gauge32
_SleSnmpTrapSourceControlTimer_Object = MibScalar
sleSnmpTrapSourceControlTimer = _SleSnmpTrapSourceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 2, 3),
    _SleSnmpTrapSourceControlTimer_Type()
)
sleSnmpTrapSourceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapSourceControlTimer.setStatus("current")
_SleSnmpTrapSourceControlTimeStamp_Type = TimeTicks
_SleSnmpTrapSourceControlTimeStamp_Object = MibScalar
sleSnmpTrapSourceControlTimeStamp = _SleSnmpTrapSourceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 2, 4),
    _SleSnmpTrapSourceControlTimeStamp_Type()
)
sleSnmpTrapSourceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapSourceControlTimeStamp.setStatus("current")
_SleSnmpTrapSourceControlReqResult_Type = Integer32
_SleSnmpTrapSourceControlReqResult_Object = MibScalar
sleSnmpTrapSourceControlReqResult = _SleSnmpTrapSourceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 2, 5),
    _SleSnmpTrapSourceControlReqResult_Type()
)
sleSnmpTrapSourceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpTrapSourceControlReqResult.setStatus("current")
_SleSnmpTrapSourceControlAddress_Type = IpAddress
_SleSnmpTrapSourceControlAddress_Object = MibScalar
sleSnmpTrapSourceControlAddress = _SleSnmpTrapSourceControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 2, 6),
    _SleSnmpTrapSourceControlAddress_Type()
)
sleSnmpTrapSourceControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapSourceControlAddress.setStatus("current")
_SleSnmpTrapSourceControlInterface_Type = OctetString
_SleSnmpTrapSourceControlInterface_Object = MibScalar
sleSnmpTrapSourceControlInterface = _SleSnmpTrapSourceControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 2, 7),
    _SleSnmpTrapSourceControlInterface_Type()
)
sleSnmpTrapSourceControlInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpTrapSourceControlInterface.setStatus("current")
_SleSnmpTrapSourceNotification_ObjectIdentity = ObjectIdentity
sleSnmpTrapSourceNotification = _SleSnmpTrapSourceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 3)
)
_SleSnmpLog_ObjectIdentity = ObjectIdentity
sleSnmpLog = _SleSnmpLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13)
)
_SleSnmpLogTable_Object = MibTable
sleSnmpLogTable = _SleSnmpLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 1)
)
if mibBuilder.loadTexts:
    sleSnmpLogTable.setStatus("current")
_SleSnmpLogEntry_Object = MibTableRow
sleSnmpLogEntry = _SleSnmpLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 1, 1)
)
sleSnmpLogEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleSnmpLogIndex"),
)
if mibBuilder.loadTexts:
    sleSnmpLogEntry.setStatus("current")


class _SleSnmpLogIndex_Type(Integer32):
    """Custom type sleSnmpLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SleSnmpLogIndex_Type.__name__ = "Integer32"
_SleSnmpLogIndex_Object = MibTableColumn
sleSnmpLogIndex = _SleSnmpLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 1, 1, 1),
    _SleSnmpLogIndex_Type()
)
sleSnmpLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpLogIndex.setStatus("current")
_SleSnmpLogText_Type = Integer32
_SleSnmpLogText_Object = MibTableColumn
sleSnmpLogText = _SleSnmpLogText_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 1, 1, 2),
    _SleSnmpLogText_Type()
)
sleSnmpLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpLogText.setStatus("current")
_SleSnmpLogControl_ObjectIdentity = ObjectIdentity
sleSnmpLogControl = _SleSnmpLogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 2)
)


class _SleSnmpLogControlRequest_Type(Integer32):
    """Custom type sleSnmpLogControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearSnmpLog", 1)
    )


_SleSnmpLogControlRequest_Type.__name__ = "Integer32"
_SleSnmpLogControlRequest_Object = MibScalar
sleSnmpLogControlRequest = _SleSnmpLogControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 2, 1),
    _SleSnmpLogControlRequest_Type()
)
sleSnmpLogControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpLogControlRequest.setStatus("current")
_SleSnmpLogControlStatus_Type = Integer32
_SleSnmpLogControlStatus_Object = MibScalar
sleSnmpLogControlStatus = _SleSnmpLogControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 2, 2),
    _SleSnmpLogControlStatus_Type()
)
sleSnmpLogControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpLogControlStatus.setStatus("current")
_SleSnmpLogControlTimer_Type = Gauge32
_SleSnmpLogControlTimer_Object = MibScalar
sleSnmpLogControlTimer = _SleSnmpLogControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 2, 3),
    _SleSnmpLogControlTimer_Type()
)
sleSnmpLogControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpLogControlTimer.setStatus("current")
_SleSnmpLogControlTimeStamp_Type = TimeTicks
_SleSnmpLogControlTimeStamp_Object = MibScalar
sleSnmpLogControlTimeStamp = _SleSnmpLogControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 2, 4),
    _SleSnmpLogControlTimeStamp_Type()
)
sleSnmpLogControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpLogControlTimeStamp.setStatus("current")
_SleSnmpLogControlReqResult_Type = Integer32
_SleSnmpLogControlReqResult_Object = MibScalar
sleSnmpLogControlReqResult = _SleSnmpLogControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 2, 5),
    _SleSnmpLogControlReqResult_Type()
)
sleSnmpLogControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpLogControlReqResult.setStatus("current")
_SleSnmpLogNotifications_ObjectIdentity = ObjectIdentity
sleSnmpLogNotifications = _SleSnmpLogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 3)
)
_SleTrapHostDomainName_ObjectIdentity = ObjectIdentity
sleTrapHostDomainName = _SleTrapHostDomainName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14)
)
_SleTrapHostDNTable_Object = MibTable
sleTrapHostDNTable = _SleTrapHostDNTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 1)
)
if mibBuilder.loadTexts:
    sleTrapHostDNTable.setStatus("current")
_SleTrapHostDNEntry_Object = MibTableRow
sleTrapHostDNEntry = _SleTrapHostDNEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 1, 1)
)
sleTrapHostDNEntry.setIndexNames(
    (0, "SLE-SNMP-MIB", "sleTrapHostDNType"),
    (0, "SLE-SNMP-MIB", "sleTrapHostDNName"),
)
if mibBuilder.loadTexts:
    sleTrapHostDNEntry.setStatus("current")


class _SleTrapHostDNType_Type(Integer32):
    """Custom type sleTrapHostDNType based on Integer32"""
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


_SleTrapHostDNType_Type.__name__ = "Integer32"
_SleTrapHostDNType_Object = MibTableColumn
sleTrapHostDNType = _SleTrapHostDNType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 1, 1, 1),
    _SleTrapHostDNType_Type()
)
sleTrapHostDNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostDNType.setStatus("current")


class _SleTrapHostDNName_Type(OctetString):
    """Custom type sleTrapHostDNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_SleTrapHostDNName_Type.__name__ = "OctetString"
_SleTrapHostDNName_Object = MibTableColumn
sleTrapHostDNName = _SleTrapHostDNName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 1, 1, 2),
    _SleTrapHostDNName_Type()
)
sleTrapHostDNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostDNName.setStatus("current")
_SleTrapHostDNCommunity_Type = OctetString
_SleTrapHostDNCommunity_Object = MibTableColumn
sleTrapHostDNCommunity = _SleTrapHostDNCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 1, 1, 3),
    _SleTrapHostDNCommunity_Type()
)
sleTrapHostDNCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostDNCommunity.setStatus("current")
_SleTrapHostDNControl_ObjectIdentity = ObjectIdentity
sleTrapHostDNControl = _SleTrapHostDNControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 2)
)


class _SleTrapHostDNControlRequest_Type(Integer32):
    """Custom type sleTrapHostDNControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createTrapHost", 1),
          ("destroyTrapHost", 2))
    )


_SleTrapHostDNControlRequest_Type.__name__ = "Integer32"
_SleTrapHostDNControlRequest_Object = MibScalar
sleTrapHostDNControlRequest = _SleTrapHostDNControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 2, 1),
    _SleTrapHostDNControlRequest_Type()
)
sleTrapHostDNControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostDNControlRequest.setStatus("current")
_SleTrapHostDNControlStatus_Type = Integer32
_SleTrapHostDNControlStatus_Object = MibScalar
sleTrapHostDNControlStatus = _SleTrapHostDNControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 2, 2),
    _SleTrapHostDNControlStatus_Type()
)
sleTrapHostDNControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostDNControlStatus.setStatus("current")
_SleTrapHostDNControlTimer_Type = Gauge32
_SleTrapHostDNControlTimer_Object = MibScalar
sleTrapHostDNControlTimer = _SleTrapHostDNControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 2, 3),
    _SleTrapHostDNControlTimer_Type()
)
sleTrapHostDNControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostDNControlTimer.setStatus("current")
_SleTrapHostDNControlTimeStamp_Type = TimeTicks
_SleTrapHostDNControlTimeStamp_Object = MibScalar
sleTrapHostDNControlTimeStamp = _SleTrapHostDNControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 2, 4),
    _SleTrapHostDNControlTimeStamp_Type()
)
sleTrapHostDNControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostDNControlTimeStamp.setStatus("current")
_SleTrapHostDNControlReqResult_Type = Integer32
_SleTrapHostDNControlReqResult_Object = MibScalar
sleTrapHostDNControlReqResult = _SleTrapHostDNControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 2, 5),
    _SleTrapHostDNControlReqResult_Type()
)
sleTrapHostDNControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTrapHostDNControlReqResult.setStatus("current")


class _SleTrapHostDNControlType_Type(Integer32):
    """Custom type sleTrapHostDNControlType based on Integer32"""
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


_SleTrapHostDNControlType_Type.__name__ = "Integer32"
_SleTrapHostDNControlType_Object = MibScalar
sleTrapHostDNControlType = _SleTrapHostDNControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 2, 6),
    _SleTrapHostDNControlType_Type()
)
sleTrapHostDNControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostDNControlType.setStatus("current")


class _SleTrapHostDNControlName_Type(OctetString):
    """Custom type sleTrapHostDNControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_SleTrapHostDNControlName_Type.__name__ = "OctetString"
_SleTrapHostDNControlName_Object = MibScalar
sleTrapHostDNControlName = _SleTrapHostDNControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 2, 7),
    _SleTrapHostDNControlName_Type()
)
sleTrapHostDNControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostDNControlName.setStatus("current")
_SleTrapHostDNControlCommunity_Type = OctetString
_SleTrapHostDNControlCommunity_Object = MibScalar
sleTrapHostDNControlCommunity = _SleTrapHostDNControlCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 2, 8),
    _SleTrapHostDNControlCommunity_Type()
)
sleTrapHostDNControlCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTrapHostDNControlCommunity.setStatus("current")
_SleTrapHostDNNotification_ObjectIdentity = ObjectIdentity
sleTrapHostDNNotification = _SleTrapHostDNNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 3)
)
_SleSnmpPing_ObjectIdentity = ObjectIdentity
sleSnmpPing = _SleSnmpPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15)
)
_SleSnmpPingTable_ObjectIdentity = ObjectIdentity
sleSnmpPingTable = _SleSnmpPingTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 1)
)
_SleSnmpPingSourceIp_Type = OctetString
_SleSnmpPingSourceIp_Object = MibScalar
sleSnmpPingSourceIp = _SleSnmpPingSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 1, 1),
    _SleSnmpPingSourceIp_Type()
)
sleSnmpPingSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpPingSourceIp.setStatus("current")
_SleSnmpPingDestinationIp_Type = OctetString
_SleSnmpPingDestinationIp_Object = MibScalar
sleSnmpPingDestinationIp = _SleSnmpPingDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 1, 2),
    _SleSnmpPingDestinationIp_Type()
)
sleSnmpPingDestinationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpPingDestinationIp.setStatus("current")
_SleSnmpPingPacketLossResult_Type = Integer32
_SleSnmpPingPacketLossResult_Object = MibScalar
sleSnmpPingPacketLossResult = _SleSnmpPingPacketLossResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 1, 3),
    _SleSnmpPingPacketLossResult_Type()
)
sleSnmpPingPacketLossResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpPingPacketLossResult.setStatus("current")
_SleSnmpPingControl_ObjectIdentity = ObjectIdentity
sleSnmpPingControl = _SleSnmpPingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 2)
)


class _SleSnmpPingControlRequest_Type(Integer32):
    """Custom type sleSnmpPingControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setPingDefault", 1),
          ("setPingWithSourceIp", 2))
    )


_SleSnmpPingControlRequest_Type.__name__ = "Integer32"
_SleSnmpPingControlRequest_Object = MibScalar
sleSnmpPingControlRequest = _SleSnmpPingControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 2, 1),
    _SleSnmpPingControlRequest_Type()
)
sleSnmpPingControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpPingControlRequest.setStatus("current")
_SleSnmpPingControlStatus_Type = Integer32
_SleSnmpPingControlStatus_Object = MibScalar
sleSnmpPingControlStatus = _SleSnmpPingControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 2, 2),
    _SleSnmpPingControlStatus_Type()
)
sleSnmpPingControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpPingControlStatus.setStatus("current")
_SleSnmpPingControlTimer_Type = Gauge32
_SleSnmpPingControlTimer_Object = MibScalar
sleSnmpPingControlTimer = _SleSnmpPingControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 2, 3),
    _SleSnmpPingControlTimer_Type()
)
sleSnmpPingControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpPingControlTimer.setStatus("current")
_SleSnmpPingControlTimeStamp_Type = TimeTicks
_SleSnmpPingControlTimeStamp_Object = MibScalar
sleSnmpPingControlTimeStamp = _SleSnmpPingControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 2, 4),
    _SleSnmpPingControlTimeStamp_Type()
)
sleSnmpPingControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpPingControlTimeStamp.setStatus("current")
_SleSnmpPingControlReqResult_Type = Integer32
_SleSnmpPingControlReqResult_Object = MibScalar
sleSnmpPingControlReqResult = _SleSnmpPingControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 2, 5),
    _SleSnmpPingControlReqResult_Type()
)
sleSnmpPingControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpPingControlReqResult.setStatus("current")
_SleSnmpPingControlSourceIp_Type = OctetString
_SleSnmpPingControlSourceIp_Object = MibScalar
sleSnmpPingControlSourceIp = _SleSnmpPingControlSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 2, 6),
    _SleSnmpPingControlSourceIp_Type()
)
sleSnmpPingControlSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpPingControlSourceIp.setStatus("current")
_SleSnmpPingControlDestinationIp_Type = OctetString
_SleSnmpPingControlDestinationIp_Object = MibScalar
sleSnmpPingControlDestinationIp = _SleSnmpPingControlDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 2, 7),
    _SleSnmpPingControlDestinationIp_Type()
)
sleSnmpPingControlDestinationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSnmpPingControlDestinationIp.setStatus("current")
_SleSnmpPingNotification_ObjectIdentity = ObjectIdentity
sleSnmpPingNotification = _SleSnmpPingNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 3)
)

# Managed Objects groups

sleSnmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 16)
)
sleSnmpGroup.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpSysContact"),
        ("SLE-SNMP-MIB", "sleSnmpControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpControlStatus"),
        ("SLE-SNMP-MIB", "sleSnmpControlTimer"),
        ("SLE-SNMP-MIB", "sleSnmpControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpControlSysContact"),
        ("SLE-SNMP-MIB", "sleCom2SecName"),
        ("SLE-SNMP-MIB", "sleCom2SecHost"),
        ("SLE-SNMP-MIB", "sleCom2SecHostMaskLen"),
        ("SLE-SNMP-MIB", "sleCom2SecCommunity"),
        ("SLE-SNMP-MIB", "sleCom2SecControlRequest"),
        ("SLE-SNMP-MIB", "sleCom2SecControlStatus"),
        ("SLE-SNMP-MIB", "sleCom2SecControlTimer"),
        ("SLE-SNMP-MIB", "sleCom2SecControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleCom2SecControlReqResult"),
        ("SLE-SNMP-MIB", "sleCom2SecControlName"),
        ("SLE-SNMP-MIB", "sleCom2SecControlHost"),
        ("SLE-SNMP-MIB", "sleCom2secControlHostMaskLen"),
        ("SLE-SNMP-MIB", "sleCom2SecControlCommunity"),
        ("SLE-SNMP-MIB", "sleTrapHostType"),
        ("SLE-SNMP-MIB", "sleTrapHostAddress"),
        ("SLE-SNMP-MIB", "sleTrapHostCommunity"),
        ("SLE-SNMP-MIB", "sleTrapHostPort"),
        ("SLE-SNMP-MIB", "sleTrapHostControlRequest"),
        ("SLE-SNMP-MIB", "sleTrapHostControlStatus"),
        ("SLE-SNMP-MIB", "sleTrapHostControlTimer"),
        ("SLE-SNMP-MIB", "sleTrapHostControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleTrapHostControlReqResult"),
        ("SLE-SNMP-MIB", "sleTrapHostControlType"),
        ("SLE-SNMP-MIB", "sleTrapHostControlAddress"),
        ("SLE-SNMP-MIB", "sleTrapHostControlCommunity"),
        ("SLE-SNMP-MIB", "sleTrapHostControlPort"),
        ("SLE-SNMP-MIB", "sleCommunityType"),
        ("SLE-SNMP-MIB", "sleCommunityValue"),
        ("SLE-SNMP-MIB", "sleCommunityHost"),
        ("SLE-SNMP-MIB", "sleCommunityOID"),
        ("SLE-SNMP-MIB", "sleCommunityHostMaskLen"),
        ("SLE-SNMP-MIB", "sleCommunityControlRequest"),
        ("SLE-SNMP-MIB", "sleCommunityControlStatus"),
        ("SLE-SNMP-MIB", "sleCommunityControlTimer"),
        ("SLE-SNMP-MIB", "sleCommunityControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleCommunityControlReqResult"),
        ("SLE-SNMP-MIB", "sleCommunityControlType"),
        ("SLE-SNMP-MIB", "sleCommunityControlValue"),
        ("SLE-SNMP-MIB", "sleCommunityControlHost"),
        ("SLE-SNMP-MIB", "sleCommunityControlOID"),
        ("SLE-SNMP-MIB", "sleCommunityControlHostMaskLen"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyName"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilySubtree"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyMask"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyType"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlRequest"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlStatus"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlTimer"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlReqResult"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlName"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlSubtree"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlMask"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlType"),
        ("SLE-SNMP-MIB", "sleAccessGroupName"),
        ("SLE-SNMP-MIB", "sleAccessSecurityModel"),
        ("SLE-SNMP-MIB", "sleAccessSecurityLevel"),
        ("SLE-SNMP-MIB", "sleAccessReadViewName"),
        ("SLE-SNMP-MIB", "sleAccessWriteViewName"),
        ("SLE-SNMP-MIB", "sleAccessNotifyViewName"),
        ("SLE-SNMP-MIB", "sleAccessControlRequest"),
        ("SLE-SNMP-MIB", "sleAccessControlStatus"),
        ("SLE-SNMP-MIB", "sleAccessControlTimer"),
        ("SLE-SNMP-MIB", "sleAccessControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleAccessControlReqResult"),
        ("SLE-SNMP-MIB", "sleAccessControlGroupName"),
        ("SLE-SNMP-MIB", "sleAccessControlSecurityModel"),
        ("SLE-SNMP-MIB", "sleAccessControlSecurityLevel"),
        ("SLE-SNMP-MIB", "sleAccessControlReadViewName"),
        ("SLE-SNMP-MIB", "sleAccessControlWriteViewName"),
        ("SLE-SNMP-MIB", "sleAccessControlNotifyViewName"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupGName"),
        ("SLE-SNMP-MIB", "sleSnmpLogStatus"),
        ("SLE-SNMP-MIB", "sleSnmpControlLogStatus"),
        ("SLE-SNMP-MIB", "sleSnmpLogIndex"),
        ("SLE-SNMP-MIB", "sleSnmpLogText"),
        ("SLE-SNMP-MIB", "sleSnmpLogControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpLogControlStatus"),
        ("SLE-SNMP-MIB", "sleSnmpLogControlTimer"),
        ("SLE-SNMP-MIB", "sleSnmpLogControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpLogControlReqResult"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupModel"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupSName"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlRequest"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlStatus"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlTimer"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlReqResult"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlGName"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlModel"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlSName"),
        ("SLE-SNMP-MIB", "sleUserName"),
        ("SLE-SNMP-MIB", "sleUserAuthType"),
        ("SLE-SNMP-MIB", "sleUserAuthKey"),
        ("SLE-SNMP-MIB", "sleUserPrivType"),
        ("SLE-SNMP-MIB", "sleUserPrivKey"),
        ("SLE-SNMP-MIB", "sleUserControlRequest"),
        ("SLE-SNMP-MIB", "sleUserControlStatus"),
        ("SLE-SNMP-MIB", "sleUserControlTimer"),
        ("SLE-SNMP-MIB", "sleUserControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleUserControlReqResult"),
        ("SLE-SNMP-MIB", "sleUserControlName"),
        ("SLE-SNMP-MIB", "sleUserControlAuthType"),
        ("SLE-SNMP-MIB", "sleUserControlAuthKey"),
        ("SLE-SNMP-MIB", "sleUserControlPrivType"),
        ("SLE-SNMP-MIB", "sleUserControlPrivKey"),
        ("SLE-SNMP-MIB", "sleAgentAddress"),
        ("SLE-SNMP-MIB", "sleAgentInterface"),
        ("SLE-SNMP-MIB", "sleAgentControlRequest"),
        ("SLE-SNMP-MIB", "sleAgentControlStatus"),
        ("SLE-SNMP-MIB", "sleAgentControlTimer"),
        ("SLE-SNMP-MIB", "sleAgentControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleAgentControlReqResult"),
        ("SLE-SNMP-MIB", "sleAgentControlAddress"),
        ("SLE-SNMP-MIB", "sleAgentControlInterface"),
        ("SLE-SNMP-MIB", "sleSnmpSessionTimeout"),
        ("SLE-SNMP-MIB", "sleSnmpSessionIpAddr"),
        ("SLE-SNMP-MIB", "sleSnmpSessionCommunity"),
        ("SLE-SNMP-MIB", "sleSnmpSessionSnmpVersion"),
        ("SLE-SNMP-MIB", "sleSnmpSessionAccessTIme"),
        ("SLE-SNMP-MIB", "sleSnmpSessionControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpSessionControlStatus"),
        ("SLE-SNMP-MIB", "sleSnmpSessionControlTimer"),
        ("SLE-SNMP-MIB", "sleSnmpSessionControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpSessionControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpSessionControlTimeout"),
        ("SLE-SNMP-MIB", "sleSnmpTrapIndex"),
        ("SLE-SNMP-MIB", "sleSnmpTrapStatus"),
        ("SLE-SNMP-MIB", "sleSnmpTrapPortIndex"),
        ("SLE-SNMP-MIB", "sleSnmpTrapPortType"),
        ("SLE-SNMP-MIB", "sleSnmpTrapPortStatus"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlStatus"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlTimer"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlTrapIndex"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlPortIndex"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlTrapStatus"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceAddress"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceInterface"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlStatus"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlTimer"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlAddress"),
        ("SLE-SNMP-MIB", "sleSnmpConnectionType"),
        ("SLE-SNMP-MIB", "sleSnmpControlConnectionType"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlInterface"),
        ("SLE-SNMP-MIB", "sleSnmpSysLocation"),
        ("SLE-SNMP-MIB", "sleSnmpPingSourceIp"),
        ("SLE-SNMP-MIB", "sleSnmpPingDestinationIp"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlStatus"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlTimer"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlSourceIp"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlDestinationIp"),
        ("SLE-SNMP-MIB", "sleSnmpTrapModeStatus"),
        ("SLE-SNMP-MIB", "sleSnmpControlTrapModeStatus"),
        ("SLE-SNMP-MIB", "sleTrapHostVrfName"),
        ("SLE-SNMP-MIB", "sleTrapHostControlVrfName"),
        ("SLE-SNMP-MIB", "sleTrapHostControlUser"),
        ("SLE-SNMP-MIB", "sleTrapHostUser"),
        ("SLE-SNMP-MIB", "sleSnmpControlSysLocation"),
        ("SLE-SNMP-MIB", "sleSnmpInformTrapRetry"),
        ("SLE-SNMP-MIB", "slesnmpInformTrapInterval"),
        ("SLE-SNMP-MIB", "sleSnmpControlInformTrapRetry"),
        ("SLE-SNMP-MIB", "sleSnmpControlInformTrapInterval"),
        ("SLE-SNMP-MIB", "sleTrapHostDNType"),
        ("SLE-SNMP-MIB", "sleTrapHostDNName"),
        ("SLE-SNMP-MIB", "sleTrapHostDNCommunity"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlRequest"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlStatus"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlTimer"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlReqResult"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlType"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlName"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlCommunity"),
        ("SLE-SNMP-MIB", "sleSnmpPingPacketLossResult"))
)
if mibBuilder.loadTexts:
    sleSnmpGroup.setStatus("current")


# Notification objects

sleSnmpSysInfoProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 3, 1)
)
sleSnmpSysInfoProfileChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpControlSysContact"),
        ("SLE-SNMP-MIB", "sleSnmpControlSysLocation"),
        ("SLE-SNMP-MIB", "sleSnmpControlTimeStamp"))
)
if mibBuilder.loadTexts:
    sleSnmpSysInfoProfileChanged.setStatus(
        "current"
    )

sleSnmpSysInfoLogStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 3, 2)
)
sleSnmpSysInfoLogStatusChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpControlLogStatus"))
)
if mibBuilder.loadTexts:
    sleSnmpSysInfoLogStatusChanged.setStatus(
        "current"
    )

sleSnmpSysInfoConnectionTypeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 3, 3)
)
sleSnmpSysInfoConnectionTypeChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpControlConnectionType"))
)
if mibBuilder.loadTexts:
    sleSnmpSysInfoConnectionTypeChanged.setStatus(
        "current"
    )

sleSnmpInformTrapConfChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 3, 4)
)
sleSnmpInformTrapConfChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpControlInformTrapRetry"),
        ("SLE-SNMP-MIB", "sleSnmpControlInformTrapInterval"))
)
if mibBuilder.loadTexts:
    sleSnmpInformTrapConfChanged.setStatus(
        "current"
    )

sleSnmpTrapModeStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 1, 3, 5)
)
sleSnmpTrapModeStatusChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpControlTrapModeStatus"))
)
if mibBuilder.loadTexts:
    sleSnmpTrapModeStatusChanged.setStatus(
        "current"
    )

sleCom2SecCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 3, 1)
)
sleCom2SecCreated.setObjects(
      *(("SLE-SNMP-MIB", "sleCom2SecControlRequest"),
        ("SLE-SNMP-MIB", "sleCom2SecControlReqResult"),
        ("SLE-SNMP-MIB", "sleCom2SecControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleCom2SecHost"),
        ("SLE-SNMP-MIB", "sleCom2SecHostMaskLen"),
        ("SLE-SNMP-MIB", "sleCom2SecCommunity"))
)
if mibBuilder.loadTexts:
    sleCom2SecCreated.setStatus(
        "current"
    )

sleCom2SecDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 3, 2)
)
sleCom2SecDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleCom2SecControlRequest"),
        ("SLE-SNMP-MIB", "sleCom2SecControlReqResult"),
        ("SLE-SNMP-MIB", "sleCom2SecControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleCom2SecControlName"))
)
if mibBuilder.loadTexts:
    sleCom2SecDestroyed.setStatus(
        "current"
    )

sleCom2SecProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 2, 3, 3)
)
sleCom2SecProfileChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleCom2SecControlRequest"),
        ("SLE-SNMP-MIB", "sleCom2SecControlReqResult"),
        ("SLE-SNMP-MIB", "sleCom2SecControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleCom2SecHost"),
        ("SLE-SNMP-MIB", "sleCom2SecHostMaskLen"),
        ("SLE-SNMP-MIB", "sleCom2SecCommunity"))
)
if mibBuilder.loadTexts:
    sleCom2SecProfileChanged.setStatus(
        "current"
    )

sleTrapHostCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 3, 1)
)
sleTrapHostCreated.setObjects(
      *(("SLE-SNMP-MIB", "sleTrapHostControlRequest"),
        ("SLE-SNMP-MIB", "sleTrapHostControlReqResult"),
        ("SLE-SNMP-MIB", "sleTrapHostControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleTrapHostCommunity"))
)
if mibBuilder.loadTexts:
    sleTrapHostCreated.setStatus(
        "current"
    )

sleTrapHostDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 3, 3, 2)
)
sleTrapHostDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleTrapHostControlRequest"),
        ("SLE-SNMP-MIB", "sleTrapHostControlReqResult"),
        ("SLE-SNMP-MIB", "sleTrapHostControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleTrapHostControlType"),
        ("SLE-SNMP-MIB", "sleTrapHostControlAddress"))
)
if mibBuilder.loadTexts:
    sleTrapHostDestroyed.setStatus(
        "current"
    )

sleCommunityCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 3, 1)
)
sleCommunityCreated.setObjects(
      *(("SLE-SNMP-MIB", "sleCommunityControlRequest"),
        ("SLE-SNMP-MIB", "sleCommunityControlReqResult"),
        ("SLE-SNMP-MIB", "sleCommunityControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleCommunityHostMaskLen"),
        ("SLE-SNMP-MIB", "sleCommunityHost"),
        ("SLE-SNMP-MIB", "sleCommunityOID"))
)
if mibBuilder.loadTexts:
    sleCommunityCreated.setStatus(
        "current"
    )

sleCommunityDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 4, 3, 2)
)
sleCommunityDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleCommunityControlRequest"),
        ("SLE-SNMP-MIB", "sleCommunityControlReqResult"),
        ("SLE-SNMP-MIB", "sleCommunityControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleCommunityControlType"),
        ("SLE-SNMP-MIB", "sleCommunityControlValue"))
)
if mibBuilder.loadTexts:
    sleCommunityDestroyed.setStatus(
        "current"
    )

sleViewTreeFamilyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 3, 1)
)
sleViewTreeFamilyCreated.setObjects(
      *(("SLE-SNMP-MIB", "sleViewTreeFamilyControlRequest"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlReqResult"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyMask"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyType"))
)
if mibBuilder.loadTexts:
    sleViewTreeFamilyCreated.setStatus(
        "current"
    )

sleViewTreeFamilyDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 5, 3, 2)
)
sleViewTreeFamilyDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleViewTreeFamilyControlRequest"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlReqResult"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlName"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyControlSubtree"))
)
if mibBuilder.loadTexts:
    sleViewTreeFamilyDestroyed.setStatus(
        "current"
    )

sleAccessCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 3, 1)
)
sleAccessCreated.setObjects(
      *(("SLE-SNMP-MIB", "sleAccessControlRequest"),
        ("SLE-SNMP-MIB", "sleAccessControlReqResult"),
        ("SLE-SNMP-MIB", "sleAccessControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleAccessSecurityModel"),
        ("SLE-SNMP-MIB", "sleAccessSecurityLevel"),
        ("SLE-SNMP-MIB", "sleAccessReadViewName"),
        ("SLE-SNMP-MIB", "sleAccessWriteViewName"),
        ("SLE-SNMP-MIB", "sleAccessNotifyViewName"))
)
if mibBuilder.loadTexts:
    sleAccessCreated.setStatus(
        "current"
    )

sleAccessDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 3, 2)
)
sleAccessDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleAccessControlRequest"),
        ("SLE-SNMP-MIB", "sleAccessControlReqResult"),
        ("SLE-SNMP-MIB", "sleAccessControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleAccessControlGroupName"))
)
if mibBuilder.loadTexts:
    sleAccessDestroyed.setStatus(
        "current"
    )

sleAccessProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 6, 3, 3)
)
sleAccessProfileChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleAccessControlRequest"),
        ("SLE-SNMP-MIB", "sleAccessControlReqResult"),
        ("SLE-SNMP-MIB", "sleAccessControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleAccessSecurityModel"),
        ("SLE-SNMP-MIB", "sleAccessSecurityLevel"),
        ("SLE-SNMP-MIB", "sleAccessReadViewName"),
        ("SLE-SNMP-MIB", "sleAccessWriteViewName"),
        ("SLE-SNMP-MIB", "sleAccessNotifyViewName"))
)
if mibBuilder.loadTexts:
    sleAccessProfileChanged.setStatus(
        "current"
    )

sleSecurityToGroupCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 3, 1)
)
sleSecurityToGroupCreated.setObjects(
      *(("SLE-SNMP-MIB", "sleSecurityToGroupControlRequest"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlReqResult"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupSName"))
)
if mibBuilder.loadTexts:
    sleSecurityToGroupCreated.setStatus(
        "current"
    )

sleSecurityToGroupDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 3, 2)
)
sleSecurityToGroupDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleSecurityToGroupControlRequest"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlReqResult"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlGName"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlModel"))
)
if mibBuilder.loadTexts:
    sleSecurityToGroupDestroyed.setStatus(
        "current"
    )

sleSecurityToGroupProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 7, 3, 3)
)
sleSecurityToGroupProfileChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSecurityToGroupControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlReqResult"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupControlRequest"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupSName"))
)
if mibBuilder.loadTexts:
    sleSecurityToGroupProfileChanged.setStatus(
        "current"
    )

sleUserCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 3, 1)
)
sleUserCreated.setObjects(
      *(("SLE-SNMP-MIB", "sleUserControlRequest"),
        ("SLE-SNMP-MIB", "sleUserControlReqResult"),
        ("SLE-SNMP-MIB", "sleUserControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleUserAuthType"),
        ("SLE-SNMP-MIB", "sleUserAuthKey"),
        ("SLE-SNMP-MIB", "sleUserPrivType"),
        ("SLE-SNMP-MIB", "sleUserPrivKey"))
)
if mibBuilder.loadTexts:
    sleUserCreated.setStatus(
        "current"
    )

sleUserDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 8, 3, 2)
)
sleUserDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleUserControlRequest"),
        ("SLE-SNMP-MIB", "sleUserControlReqResult"),
        ("SLE-SNMP-MIB", "sleUserControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleUserControlName"))
)
if mibBuilder.loadTexts:
    sleUserDestroyed.setStatus(
        "current"
    )

sleAgentAddressChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 3, 1)
)
sleAgentAddressChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleAgentControlRequest"),
        ("SLE-SNMP-MIB", "sleAgentControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleAgentControlReqResult"),
        ("SLE-SNMP-MIB", "sleAgentAddress"))
)
if mibBuilder.loadTexts:
    sleAgentAddressChanged.setStatus(
        "current"
    )

sleAgentInterfaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 3, 2)
)
sleAgentInterfaceChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleAgentControlRequest"),
        ("SLE-SNMP-MIB", "sleAgentControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleAgentControlReqResult"),
        ("SLE-SNMP-MIB", "sleAgentInterface"))
)
if mibBuilder.loadTexts:
    sleAgentInterfaceChanged.setStatus(
        "current"
    )

sleAgentAddressDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 3, 3)
)
sleAgentAddressDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleAgentControlRequest"),
        ("SLE-SNMP-MIB", "sleAgentControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleAgentControlReqResult"))
)
if mibBuilder.loadTexts:
    sleAgentAddressDestroyed.setStatus(
        "current"
    )

sleAgentInterfaceDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 9, 3, 4)
)
sleAgentInterfaceDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleAgentControlRequest"),
        ("SLE-SNMP-MIB", "sleAgentControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleAgentControlReqResult"))
)
if mibBuilder.loadTexts:
    sleAgentInterfaceDestroyed.setStatus(
        "current"
    )

sleSnmpSessionTimeoutChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 10, 4, 1)
)
sleSnmpSessionTimeoutChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpSessionControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpSessionControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpSessionControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpSessionTimeout"))
)
if mibBuilder.loadTexts:
    sleSnmpSessionTimeoutChanged.setStatus(
        "current"
    )

sleSnmpTrapStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 4, 1)
)
sleSnmpTrapStatusChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpTrapControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlTrapStatus"))
)
if mibBuilder.loadTexts:
    sleSnmpTrapStatusChanged.setStatus(
        "current"
    )

sleSnmpTrapPortStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 11, 4, 2)
)
sleSnmpTrapPortStatusChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpTrapControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpTrapControlTrapStatus"))
)
if mibBuilder.loadTexts:
    sleSnmpTrapPortStatusChanged.setStatus(
        "current"
    )

sleSnmpTrapSourceAddressChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 3, 1)
)
sleSnmpTrapSourceAddressChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpTrapSourceControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceAddress"))
)
if mibBuilder.loadTexts:
    sleSnmpTrapSourceAddressChanged.setStatus(
        "current"
    )

sleSnmpTrapSourceInterfaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 3, 2)
)
sleSnmpTrapSourceInterfaceChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpTrapSourceControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceInterface"))
)
if mibBuilder.loadTexts:
    sleSnmpTrapSourceInterfaceChanged.setStatus(
        "current"
    )

sleSnmpTrapSourcetAddressDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 3, 3)
)
sleSnmpTrapSourcetAddressDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpTrapSourceControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSnmpTrapSourcetAddressDestroyed.setStatus(
        "current"
    )

sleSnmpTrapSourceInterfaceDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 12, 3, 4)
)
sleSnmpTrapSourceInterfaceDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpTrapSourceControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSnmpTrapSourceInterfaceDestroyed.setStatus(
        "current"
    )

sleSnmpLogCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 13, 3, 1)
)
sleSnmpLogCleared.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpLogControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpLogControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpLogControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSnmpLogCleared.setStatus(
        "current"
    )

sleTrapHostDNCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 3, 1)
)
sleTrapHostDNCreated.setObjects(
      *(("SLE-SNMP-MIB", "sleTrapHostDNControlRequest"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlReqResult"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlType"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlName"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlCommunity"))
)
if mibBuilder.loadTexts:
    sleTrapHostDNCreated.setStatus(
        "current"
    )

sleTrapHostDNDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 14, 3, 2)
)
sleTrapHostDNDestroyed.setObjects(
      *(("SLE-SNMP-MIB", "sleTrapHostDNControlRequest"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlReqResult"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlType"),
        ("SLE-SNMP-MIB", "sleTrapHostDNControlName"))
)
if mibBuilder.loadTexts:
    sleTrapHostDNDestroyed.setStatus(
        "current"
    )

sleSnmpPingDefaultChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 3, 1)
)
sleSnmpPingDefaultChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpPingControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlDestinationIp"),
        ("SLE-SNMP-MIB", "sleSnmpPingPacketLossResult"))
)
if mibBuilder.loadTexts:
    sleSnmpPingDefaultChanged.setStatus(
        "current"
    )

sleSnmpPingWithSourceIpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 15, 3, 2)
)
sleSnmpPingWithSourceIpChanged.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpPingControlRequest"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlTimeStamp"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlReqResult"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlSourceIp"),
        ("SLE-SNMP-MIB", "sleSnmpPingControlDestinationIp"),
        ("SLE-SNMP-MIB", "sleSnmpPingPacketLossResult"))
)
if mibBuilder.loadTexts:
    sleSnmpPingWithSourceIpChanged.setStatus(
        "current"
    )


# Notifications groups

sleSnmpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 8, 17)
)
sleSnmpNotificationGroup.setObjects(
      *(("SLE-SNMP-MIB", "sleSnmpSysInfoProfileChanged"),
        ("SLE-SNMP-MIB", "sleCom2SecCreated"),
        ("SLE-SNMP-MIB", "sleCom2SecDestroyed"),
        ("SLE-SNMP-MIB", "sleCom2SecProfileChanged"),
        ("SLE-SNMP-MIB", "sleTrapHostCreated"),
        ("SLE-SNMP-MIB", "sleTrapHostDestroyed"),
        ("SLE-SNMP-MIB", "sleCommunityCreated"),
        ("SLE-SNMP-MIB", "sleCommunityDestroyed"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyCreated"),
        ("SLE-SNMP-MIB", "sleViewTreeFamilyDestroyed"),
        ("SLE-SNMP-MIB", "sleAccessCreated"),
        ("SLE-SNMP-MIB", "sleAccessDestroyed"),
        ("SLE-SNMP-MIB", "sleAccessProfileChanged"),
        ("SLE-SNMP-MIB", "sleUserCreated"),
        ("SLE-SNMP-MIB", "sleUserDestroyed"),
        ("SLE-SNMP-MIB", "sleAgentAddressChanged"),
        ("SLE-SNMP-MIB", "sleAgentInterfaceChanged"),
        ("SLE-SNMP-MIB", "sleAgentAddressDestroyed"),
        ("SLE-SNMP-MIB", "sleAgentInterfaceDestroyed"),
        ("SLE-SNMP-MIB", "sleSnmpSessionTimeoutChanged"),
        ("SLE-SNMP-MIB", "sleSnmpTrapStatusChanged"),
        ("SLE-SNMP-MIB", "sleSnmpTrapPortStatusChanged"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceInterfaceChanged"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourcetAddressDestroyed"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceInterfaceDestroyed"),
        ("SLE-SNMP-MIB", "sleSnmpTrapSourceAddressChanged"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupProfileChanged"),
        ("SLE-SNMP-MIB", "sleSnmpSysInfoLogStatusChanged"),
        ("SLE-SNMP-MIB", "sleSnmpLogCleared"),
        ("SLE-SNMP-MIB", "sleSnmpSysInfoConnectionTypeChanged"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupDestroyed"),
        ("SLE-SNMP-MIB", "sleTrapHostDNCreated"),
        ("SLE-SNMP-MIB", "sleTrapHostDNDestroyed"),
        ("SLE-SNMP-MIB", "sleSnmpPingDefaultChanged"),
        ("SLE-SNMP-MIB", "sleSnmpPingWithSourceIpChanged"),
        ("SLE-SNMP-MIB", "sleSnmpTrapModeStatusChanged"),
        ("SLE-SNMP-MIB", "sleSecurityToGroupCreated"),
        ("SLE-SNMP-MIB", "sleSnmpInformTrapConfChanged"))
)
if mibBuilder.loadTexts:
    sleSnmpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-SNMP-MIB",
    **{"sleSnmp": sleSnmp,
       "sleSnmpBase": sleSnmpBase,
       "sleSnmpBaseInfo": sleSnmpBaseInfo,
       "sleSnmpSysContact": sleSnmpSysContact,
       "sleSnmpSysLocation": sleSnmpSysLocation,
       "sleSnmpLogStatus": sleSnmpLogStatus,
       "sleSnmpConnectionType": sleSnmpConnectionType,
       "sleSnmpInformTrapRetry": sleSnmpInformTrapRetry,
       "slesnmpInformTrapInterval": slesnmpInformTrapInterval,
       "sleSnmpTrapModeStatus": sleSnmpTrapModeStatus,
       "sleSnmpBaseControl": sleSnmpBaseControl,
       "sleSnmpControlRequest": sleSnmpControlRequest,
       "sleSnmpControlStatus": sleSnmpControlStatus,
       "sleSnmpControlTimer": sleSnmpControlTimer,
       "sleSnmpControlTimeStamp": sleSnmpControlTimeStamp,
       "sleSnmpControlReqResult": sleSnmpControlReqResult,
       "sleSnmpControlSysContact": sleSnmpControlSysContact,
       "sleSnmpControlSysLocation": sleSnmpControlSysLocation,
       "sleSnmpControlLogStatus": sleSnmpControlLogStatus,
       "sleSnmpControlConnectionType": sleSnmpControlConnectionType,
       "sleSnmpControlInformTrapRetry": sleSnmpControlInformTrapRetry,
       "sleSnmpControlInformTrapInterval": sleSnmpControlInformTrapInterval,
       "sleSnmpControlTrapModeStatus": sleSnmpControlTrapModeStatus,
       "sleSnmpBaseNotification": sleSnmpBaseNotification,
       "sleSnmpSysInfoProfileChanged": sleSnmpSysInfoProfileChanged,
       "sleSnmpSysInfoLogStatusChanged": sleSnmpSysInfoLogStatusChanged,
       "sleSnmpSysInfoConnectionTypeChanged": sleSnmpSysInfoConnectionTypeChanged,
       "sleSnmpInformTrapConfChanged": sleSnmpInformTrapConfChanged,
       "sleSnmpTrapModeStatusChanged": sleSnmpTrapModeStatusChanged,
       "sleCom2Sec": sleCom2Sec,
       "sleCom2SecTable": sleCom2SecTable,
       "sleCom2SecEntry": sleCom2SecEntry,
       "sleCom2SecName": sleCom2SecName,
       "sleCom2SecHost": sleCom2SecHost,
       "sleCom2SecHostMaskLen": sleCom2SecHostMaskLen,
       "sleCom2SecCommunity": sleCom2SecCommunity,
       "sleCom2SecControl": sleCom2SecControl,
       "sleCom2SecControlRequest": sleCom2SecControlRequest,
       "sleCom2SecControlStatus": sleCom2SecControlStatus,
       "sleCom2SecControlTimer": sleCom2SecControlTimer,
       "sleCom2SecControlTimeStamp": sleCom2SecControlTimeStamp,
       "sleCom2SecControlReqResult": sleCom2SecControlReqResult,
       "sleCom2SecControlName": sleCom2SecControlName,
       "sleCom2SecControlHost": sleCom2SecControlHost,
       "sleCom2secControlHostMaskLen": sleCom2secControlHostMaskLen,
       "sleCom2SecControlCommunity": sleCom2SecControlCommunity,
       "sleCom2SecNotification": sleCom2SecNotification,
       "sleCom2SecCreated": sleCom2SecCreated,
       "sleCom2SecDestroyed": sleCom2SecDestroyed,
       "sleCom2SecProfileChanged": sleCom2SecProfileChanged,
       "sleTrapHost": sleTrapHost,
       "sleTrapHostTable": sleTrapHostTable,
       "sleTrapHostEntry": sleTrapHostEntry,
       "sleTrapHostType": sleTrapHostType,
       "sleTrapHostAddress": sleTrapHostAddress,
       "sleTrapHostCommunity": sleTrapHostCommunity,
       "sleTrapHostPort": sleTrapHostPort,
       "sleTrapHostVrfName": sleTrapHostVrfName,
       "sleTrapHostUser": sleTrapHostUser,
       "sleTrapHostControl": sleTrapHostControl,
       "sleTrapHostControlRequest": sleTrapHostControlRequest,
       "sleTrapHostControlStatus": sleTrapHostControlStatus,
       "sleTrapHostControlTimer": sleTrapHostControlTimer,
       "sleTrapHostControlTimeStamp": sleTrapHostControlTimeStamp,
       "sleTrapHostControlReqResult": sleTrapHostControlReqResult,
       "sleTrapHostControlType": sleTrapHostControlType,
       "sleTrapHostControlAddress": sleTrapHostControlAddress,
       "sleTrapHostControlCommunity": sleTrapHostControlCommunity,
       "sleTrapHostControlPort": sleTrapHostControlPort,
       "sleTrapHostControlVrfName": sleTrapHostControlVrfName,
       "sleTrapHostControlUser": sleTrapHostControlUser,
       "sleTrapHostNotification": sleTrapHostNotification,
       "sleTrapHostCreated": sleTrapHostCreated,
       "sleTrapHostDestroyed": sleTrapHostDestroyed,
       "sleCommunity": sleCommunity,
       "sleCommunityTable": sleCommunityTable,
       "sleCommunityEntry": sleCommunityEntry,
       "sleCommunityType": sleCommunityType,
       "sleCommunityValue": sleCommunityValue,
       "sleCommunityHost": sleCommunityHost,
       "sleCommunityOID": sleCommunityOID,
       "sleCommunityHostMaskLen": sleCommunityHostMaskLen,
       "sleCommunityControl": sleCommunityControl,
       "sleCommunityControlRequest": sleCommunityControlRequest,
       "sleCommunityControlStatus": sleCommunityControlStatus,
       "sleCommunityControlTimer": sleCommunityControlTimer,
       "sleCommunityControlTimeStamp": sleCommunityControlTimeStamp,
       "sleCommunityControlReqResult": sleCommunityControlReqResult,
       "sleCommunityControlType": sleCommunityControlType,
       "sleCommunityControlValue": sleCommunityControlValue,
       "sleCommunityControlHost": sleCommunityControlHost,
       "sleCommunityControlOID": sleCommunityControlOID,
       "sleCommunityControlHostMaskLen": sleCommunityControlHostMaskLen,
       "sleCommunityNotification": sleCommunityNotification,
       "sleCommunityCreated": sleCommunityCreated,
       "sleCommunityDestroyed": sleCommunityDestroyed,
       "sleViewTreeFamily": sleViewTreeFamily,
       "sleViewTreeFamilyTable": sleViewTreeFamilyTable,
       "sleViewTreeFamilyEntry": sleViewTreeFamilyEntry,
       "sleViewTreeFamilyName": sleViewTreeFamilyName,
       "sleViewTreeFamilySubtree": sleViewTreeFamilySubtree,
       "sleViewTreeFamilyMask": sleViewTreeFamilyMask,
       "sleViewTreeFamilyType": sleViewTreeFamilyType,
       "sleViewTreeFamilyControl": sleViewTreeFamilyControl,
       "sleViewTreeFamilyControlRequest": sleViewTreeFamilyControlRequest,
       "sleViewTreeFamilyControlStatus": sleViewTreeFamilyControlStatus,
       "sleViewTreeFamilyControlTimer": sleViewTreeFamilyControlTimer,
       "sleViewTreeFamilyControlTimeStamp": sleViewTreeFamilyControlTimeStamp,
       "sleViewTreeFamilyControlReqResult": sleViewTreeFamilyControlReqResult,
       "sleViewTreeFamilyControlName": sleViewTreeFamilyControlName,
       "sleViewTreeFamilyControlSubtree": sleViewTreeFamilyControlSubtree,
       "sleViewTreeFamilyControlMask": sleViewTreeFamilyControlMask,
       "sleViewTreeFamilyControlType": sleViewTreeFamilyControlType,
       "sleViewTreeFamilyNotification": sleViewTreeFamilyNotification,
       "sleViewTreeFamilyCreated": sleViewTreeFamilyCreated,
       "sleViewTreeFamilyDestroyed": sleViewTreeFamilyDestroyed,
       "sleAccess": sleAccess,
       "sleAccessTable": sleAccessTable,
       "sleAccessEntry": sleAccessEntry,
       "sleAccessGroupName": sleAccessGroupName,
       "sleAccessSecurityModel": sleAccessSecurityModel,
       "sleAccessSecurityLevel": sleAccessSecurityLevel,
       "sleAccessReadViewName": sleAccessReadViewName,
       "sleAccessWriteViewName": sleAccessWriteViewName,
       "sleAccessNotifyViewName": sleAccessNotifyViewName,
       "sleAccessControl": sleAccessControl,
       "sleAccessControlRequest": sleAccessControlRequest,
       "sleAccessControlStatus": sleAccessControlStatus,
       "sleAccessControlTimer": sleAccessControlTimer,
       "sleAccessControlTimeStamp": sleAccessControlTimeStamp,
       "sleAccessControlReqResult": sleAccessControlReqResult,
       "sleAccessControlGroupName": sleAccessControlGroupName,
       "sleAccessControlSecurityModel": sleAccessControlSecurityModel,
       "sleAccessControlSecurityLevel": sleAccessControlSecurityLevel,
       "sleAccessControlReadViewName": sleAccessControlReadViewName,
       "sleAccessControlWriteViewName": sleAccessControlWriteViewName,
       "sleAccessControlNotifyViewName": sleAccessControlNotifyViewName,
       "sleAccessNotification": sleAccessNotification,
       "sleAccessCreated": sleAccessCreated,
       "sleAccessDestroyed": sleAccessDestroyed,
       "sleAccessProfileChanged": sleAccessProfileChanged,
       "sleSecurityToGroup": sleSecurityToGroup,
       "sleSecurityToGroupTable": sleSecurityToGroupTable,
       "sleSecurityToGroupEntry": sleSecurityToGroupEntry,
       "sleSecurityToGroupSName": sleSecurityToGroupSName,
       "sleSecurityToGroupModel": sleSecurityToGroupModel,
       "sleSecurityToGroupGName": sleSecurityToGroupGName,
       "sleSecurityToGroupControl": sleSecurityToGroupControl,
       "sleSecurityToGroupControlRequest": sleSecurityToGroupControlRequest,
       "sleSecurityToGroupControlStatus": sleSecurityToGroupControlStatus,
       "sleSecurityToGroupControlTimer": sleSecurityToGroupControlTimer,
       "sleSecurityToGroupControlTimeStamp": sleSecurityToGroupControlTimeStamp,
       "sleSecurityToGroupControlReqResult": sleSecurityToGroupControlReqResult,
       "sleSecurityToGroupControlGName": sleSecurityToGroupControlGName,
       "sleSecurityToGroupControlModel": sleSecurityToGroupControlModel,
       "sleSecurityToGroupControlSName": sleSecurityToGroupControlSName,
       "sleSecurityToGroupNotification": sleSecurityToGroupNotification,
       "sleSecurityToGroupCreated": sleSecurityToGroupCreated,
       "sleSecurityToGroupDestroyed": sleSecurityToGroupDestroyed,
       "sleSecurityToGroupProfileChanged": sleSecurityToGroupProfileChanged,
       "sleUser": sleUser,
       "sleUserTable": sleUserTable,
       "sleUserEntry": sleUserEntry,
       "sleUserName": sleUserName,
       "sleUserAuthType": sleUserAuthType,
       "sleUserAuthKey": sleUserAuthKey,
       "sleUserPrivType": sleUserPrivType,
       "sleUserPrivKey": sleUserPrivKey,
       "sleUserControl": sleUserControl,
       "sleUserControlRequest": sleUserControlRequest,
       "sleUserControlStatus": sleUserControlStatus,
       "sleUserControlTimer": sleUserControlTimer,
       "sleUserControlTimeStamp": sleUserControlTimeStamp,
       "sleUserControlReqResult": sleUserControlReqResult,
       "sleUserControlName": sleUserControlName,
       "sleUserControlAuthType": sleUserControlAuthType,
       "sleUserControlAuthKey": sleUserControlAuthKey,
       "sleUserControlPrivType": sleUserControlPrivType,
       "sleUserControlPrivKey": sleUserControlPrivKey,
       "sleUserNotification": sleUserNotification,
       "sleUserCreated": sleUserCreated,
       "sleUserDestroyed": sleUserDestroyed,
       "sleAgent": sleAgent,
       "sleAgentInfo": sleAgentInfo,
       "sleAgentAddress": sleAgentAddress,
       "sleAgentInterface": sleAgentInterface,
       "sleAgentControl": sleAgentControl,
       "sleAgentControlRequest": sleAgentControlRequest,
       "sleAgentControlStatus": sleAgentControlStatus,
       "sleAgentControlTimer": sleAgentControlTimer,
       "sleAgentControlTimeStamp": sleAgentControlTimeStamp,
       "sleAgentControlReqResult": sleAgentControlReqResult,
       "sleAgentControlAddress": sleAgentControlAddress,
       "sleAgentControlInterface": sleAgentControlInterface,
       "sleAgentNotification": sleAgentNotification,
       "sleAgentAddressChanged": sleAgentAddressChanged,
       "sleAgentInterfaceChanged": sleAgentInterfaceChanged,
       "sleAgentAddressDestroyed": sleAgentAddressDestroyed,
       "sleAgentInterfaceDestroyed": sleAgentInterfaceDestroyed,
       "sleSnmpSesson": sleSnmpSesson,
       "sleSnmpSessionInfo": sleSnmpSessionInfo,
       "sleSnmpSessionTimeout": sleSnmpSessionTimeout,
       "sleSnmpSessionTable": sleSnmpSessionTable,
       "sleSnmpSessionEntry": sleSnmpSessionEntry,
       "sleSnmpSessionIpAddr": sleSnmpSessionIpAddr,
       "sleSnmpSessionCommunity": sleSnmpSessionCommunity,
       "sleSnmpSessionSnmpVersion": sleSnmpSessionSnmpVersion,
       "sleSnmpSessionAccessTIme": sleSnmpSessionAccessTIme,
       "sleSnmpSessiontControl": sleSnmpSessiontControl,
       "sleSnmpSessionControlRequest": sleSnmpSessionControlRequest,
       "sleSnmpSessionControlStatus": sleSnmpSessionControlStatus,
       "sleSnmpSessionControlTimer": sleSnmpSessionControlTimer,
       "sleSnmpSessionControlTimeStamp": sleSnmpSessionControlTimeStamp,
       "sleSnmpSessionControlReqResult": sleSnmpSessionControlReqResult,
       "sleSnmpSessionControlTimeout": sleSnmpSessionControlTimeout,
       "sleSnmpSessionNotifications": sleSnmpSessionNotifications,
       "sleSnmpSessionTimeoutChanged": sleSnmpSessionTimeoutChanged,
       "sleSnmpTrap": sleSnmpTrap,
       "sleSnmpTrapTable": sleSnmpTrapTable,
       "sleSnmpTrapEntry": sleSnmpTrapEntry,
       "sleSnmpTrapIndex": sleSnmpTrapIndex,
       "sleSnmpTrapStatus": sleSnmpTrapStatus,
       "sleSnmpTrapPortTable": sleSnmpTrapPortTable,
       "sleSnmpTrapPortEntry": sleSnmpTrapPortEntry,
       "sleSnmpTrapPortIndex": sleSnmpTrapPortIndex,
       "sleSnmpTrapPortType": sleSnmpTrapPortType,
       "sleSnmpTrapPortStatus": sleSnmpTrapPortStatus,
       "sleSnmpTrapControl": sleSnmpTrapControl,
       "sleSnmpTrapControlRequest": sleSnmpTrapControlRequest,
       "sleSnmpTrapControlStatus": sleSnmpTrapControlStatus,
       "sleSnmpTrapControlTimer": sleSnmpTrapControlTimer,
       "sleSnmpTrapControlTimeStamp": sleSnmpTrapControlTimeStamp,
       "sleSnmpTrapControlReqResult": sleSnmpTrapControlReqResult,
       "sleSnmpTrapControlTrapIndex": sleSnmpTrapControlTrapIndex,
       "sleSnmpTrapControlPortIndex": sleSnmpTrapControlPortIndex,
       "sleSnmpTrapControlTrapStatus": sleSnmpTrapControlTrapStatus,
       "sleSnmpTrapNotification": sleSnmpTrapNotification,
       "sleSnmpTrapStatusChanged": sleSnmpTrapStatusChanged,
       "sleSnmpTrapPortStatusChanged": sleSnmpTrapPortStatusChanged,
       "sleSnmpTrapSource": sleSnmpTrapSource,
       "sleSnmpTrapSourceInfo": sleSnmpTrapSourceInfo,
       "sleSnmpTrapSourceAddress": sleSnmpTrapSourceAddress,
       "sleSnmpTrapSourceInterface": sleSnmpTrapSourceInterface,
       "sleSnmpTrapSourceControl": sleSnmpTrapSourceControl,
       "sleSnmpTrapSourceControlRequest": sleSnmpTrapSourceControlRequest,
       "sleSnmpTrapSourceControlStatus": sleSnmpTrapSourceControlStatus,
       "sleSnmpTrapSourceControlTimer": sleSnmpTrapSourceControlTimer,
       "sleSnmpTrapSourceControlTimeStamp": sleSnmpTrapSourceControlTimeStamp,
       "sleSnmpTrapSourceControlReqResult": sleSnmpTrapSourceControlReqResult,
       "sleSnmpTrapSourceControlAddress": sleSnmpTrapSourceControlAddress,
       "sleSnmpTrapSourceControlInterface": sleSnmpTrapSourceControlInterface,
       "sleSnmpTrapSourceNotification": sleSnmpTrapSourceNotification,
       "sleSnmpTrapSourceAddressChanged": sleSnmpTrapSourceAddressChanged,
       "sleSnmpTrapSourceInterfaceChanged": sleSnmpTrapSourceInterfaceChanged,
       "sleSnmpTrapSourcetAddressDestroyed": sleSnmpTrapSourcetAddressDestroyed,
       "sleSnmpTrapSourceInterfaceDestroyed": sleSnmpTrapSourceInterfaceDestroyed,
       "sleSnmpLog": sleSnmpLog,
       "sleSnmpLogTable": sleSnmpLogTable,
       "sleSnmpLogEntry": sleSnmpLogEntry,
       "sleSnmpLogIndex": sleSnmpLogIndex,
       "sleSnmpLogText": sleSnmpLogText,
       "sleSnmpLogControl": sleSnmpLogControl,
       "sleSnmpLogControlRequest": sleSnmpLogControlRequest,
       "sleSnmpLogControlStatus": sleSnmpLogControlStatus,
       "sleSnmpLogControlTimer": sleSnmpLogControlTimer,
       "sleSnmpLogControlTimeStamp": sleSnmpLogControlTimeStamp,
       "sleSnmpLogControlReqResult": sleSnmpLogControlReqResult,
       "sleSnmpLogNotifications": sleSnmpLogNotifications,
       "sleSnmpLogCleared": sleSnmpLogCleared,
       "sleTrapHostDomainName": sleTrapHostDomainName,
       "sleTrapHostDNTable": sleTrapHostDNTable,
       "sleTrapHostDNEntry": sleTrapHostDNEntry,
       "sleTrapHostDNType": sleTrapHostDNType,
       "sleTrapHostDNName": sleTrapHostDNName,
       "sleTrapHostDNCommunity": sleTrapHostDNCommunity,
       "sleTrapHostDNControl": sleTrapHostDNControl,
       "sleTrapHostDNControlRequest": sleTrapHostDNControlRequest,
       "sleTrapHostDNControlStatus": sleTrapHostDNControlStatus,
       "sleTrapHostDNControlTimer": sleTrapHostDNControlTimer,
       "sleTrapHostDNControlTimeStamp": sleTrapHostDNControlTimeStamp,
       "sleTrapHostDNControlReqResult": sleTrapHostDNControlReqResult,
       "sleTrapHostDNControlType": sleTrapHostDNControlType,
       "sleTrapHostDNControlName": sleTrapHostDNControlName,
       "sleTrapHostDNControlCommunity": sleTrapHostDNControlCommunity,
       "sleTrapHostDNNotification": sleTrapHostDNNotification,
       "sleTrapHostDNCreated": sleTrapHostDNCreated,
       "sleTrapHostDNDestroyed": sleTrapHostDNDestroyed,
       "sleSnmpPing": sleSnmpPing,
       "sleSnmpPingTable": sleSnmpPingTable,
       "sleSnmpPingSourceIp": sleSnmpPingSourceIp,
       "sleSnmpPingDestinationIp": sleSnmpPingDestinationIp,
       "sleSnmpPingPacketLossResult": sleSnmpPingPacketLossResult,
       "sleSnmpPingControl": sleSnmpPingControl,
       "sleSnmpPingControlRequest": sleSnmpPingControlRequest,
       "sleSnmpPingControlStatus": sleSnmpPingControlStatus,
       "sleSnmpPingControlTimer": sleSnmpPingControlTimer,
       "sleSnmpPingControlTimeStamp": sleSnmpPingControlTimeStamp,
       "sleSnmpPingControlReqResult": sleSnmpPingControlReqResult,
       "sleSnmpPingControlSourceIp": sleSnmpPingControlSourceIp,
       "sleSnmpPingControlDestinationIp": sleSnmpPingControlDestinationIp,
       "sleSnmpPingNotification": sleSnmpPingNotification,
       "sleSnmpPingDefaultChanged": sleSnmpPingDefaultChanged,
       "sleSnmpPingWithSourceIpChanged": sleSnmpPingWithSourceIpChanged,
       "sleSnmpGroup": sleSnmpGroup,
       "sleSnmpNotificationGroup": sleSnmpNotificationGroup}
)
