# SNMP MIB module (TIMETRA-CELLULAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-CELLULAR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:16:58 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxCardSlotNum,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxMDASlotNum")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxPortNotifyPortId,
 tmnxPortPortID) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxPortNotifyPortId",
    "tmnxPortPortID")

(TItemDescription,
 TNamedItemOrEmpty,
 TmnxAuthPassword,
 TmnxEnabledDisabled,
 TmnxEnabledDisabledAdminState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItemOrEmpty",
    "TmnxAuthPassword",
    "TmnxEnabledDisabled",
    "TmnxEnabledDisabledAdminState")


# MODULE-IDENTITY

timetraCellularMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 109)
)
if mibBuilder.loadTexts:
    timetraCellularMIBModule.setRevisions(
        ("2016-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxCellularPdnProfileId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class TmnxCellularAccessPointName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )



class TmnxCellularImei(DisplayString):
    status = "current"
    displayHint = "2a-6a-6a-2a"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(15, 16),
    )



class TmnxCellularSimCardNumber(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )



class TmnxCellularSimCardIccid(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class TmnxCellularImsi(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )



class TmnxCellularPdnId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )



class TmnxCellularChannelNumber(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )



class TmnxCellularBearerRate(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxCellularConformance_ObjectIdentity = ObjectIdentity
tmnxCellularConformance = _TmnxCellularConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109)
)
_TmnxCellularCompliances_ObjectIdentity = ObjectIdentity
tmnxCellularCompliances = _TmnxCellularCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 1)
)
_TmnxCellularGroups_ObjectIdentity = ObjectIdentity
tmnxCellularGroups = _TmnxCellularGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2)
)
_TmnxCellularV15v0Groups_ObjectIdentity = ObjectIdentity
tmnxCellularV15v0Groups = _TmnxCellularV15v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 1)
)
_TmnxCellularV16v0Groups_ObjectIdentity = ObjectIdentity
tmnxCellularV16v0Groups = _TmnxCellularV16v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 2)
)
_TmnxCellularV19Groups_ObjectIdentity = ObjectIdentity
tmnxCellularV19Groups = _TmnxCellularV19Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 3)
)
_TmnxCellularV20Groups_ObjectIdentity = ObjectIdentity
tmnxCellularV20Groups = _TmnxCellularV20Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 4)
)
_TmnxCellularV21Groups_ObjectIdentity = ObjectIdentity
tmnxCellularV21Groups = _TmnxCellularV21Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 5)
)
_TmnxCellularObjs_ObjectIdentity = ObjectIdentity
tmnxCellularObjs = _TmnxCellularObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109)
)
_TmnxCellularConfigObjs_ObjectIdentity = ObjectIdentity
tmnxCellularConfigObjs = _TmnxCellularConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2)
)
_TmnxCellularConfigTimestamps_ObjectIdentity = ObjectIdentity
tmnxCellularConfigTimestamps = _TmnxCellularConfigTimestamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 1)
)
_TmnxCellPdnProfileTblLastChanged_Type = TimeStamp
_TmnxCellPdnProfileTblLastChanged_Object = MibScalar
tmnxCellPdnProfileTblLastChanged = _TmnxCellPdnProfileTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 1, 1),
    _TmnxCellPdnProfileTblLastChanged_Type()
)
tmnxCellPdnProfileTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnProfileTblLastChanged.setStatus("current")
_TmnxCellSimCardTableLastChanged_Type = TimeStamp
_TmnxCellSimCardTableLastChanged_Object = MibScalar
tmnxCellSimCardTableLastChanged = _TmnxCellSimCardTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 1, 2),
    _TmnxCellSimCardTableLastChanged_Type()
)
tmnxCellSimCardTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellSimCardTableLastChanged.setStatus("current")
_TmnxCellPdnTblLastChanged_Type = TimeStamp
_TmnxCellPdnTblLastChanged_Object = MibScalar
tmnxCellPdnTblLastChanged = _TmnxCellPdnTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 1, 3),
    _TmnxCellPdnTblLastChanged_Type()
)
tmnxCellPdnTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnTblLastChanged.setStatus("current")
_TmnxCellPortTblLastChanged_Type = TimeStamp
_TmnxCellPortTblLastChanged_Object = MibScalar
tmnxCellPortTblLastChanged = _TmnxCellPortTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 1, 4),
    _TmnxCellPortTblLastChanged_Type()
)
tmnxCellPortTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortTblLastChanged.setStatus("current")
_TmnxCellPortCbsdAuthCfgTblLstChg_Type = TimeStamp
_TmnxCellPortCbsdAuthCfgTblLstChg_Object = MibScalar
tmnxCellPortCbsdAuthCfgTblLstChg = _TmnxCellPortCbsdAuthCfgTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 1, 5),
    _TmnxCellPortCbsdAuthCfgTblLstChg_Type()
)
tmnxCellPortCbsdAuthCfgTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthCfgTblLstChg.setStatus("current")
_TmnxCellularSystemConfigObjs_ObjectIdentity = ObjectIdentity
tmnxCellularSystemConfigObjs = _TmnxCellularSystemConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2)
)
_TmnxCellularPdnProfileTable_Object = MibTable
tmnxCellularPdnProfileTable = _TmnxCellularPdnProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxCellularPdnProfileTable.setStatus("current")
_TmnxCellPdnProfileEntry_Object = MibTableRow
tmnxCellPdnProfileEntry = _TmnxCellPdnProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1, 1)
)
tmnxCellPdnProfileEntry.setIndexNames(
    (0, "TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfileId"),
)
if mibBuilder.loadTexts:
    tmnxCellPdnProfileEntry.setStatus("current")
_TmnxCellPdnProfileId_Type = TmnxCellularPdnProfileId
_TmnxCellPdnProfileId_Object = MibTableColumn
tmnxCellPdnProfileId = _TmnxCellPdnProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1, 1, 1),
    _TmnxCellPdnProfileId_Type()
)
tmnxCellPdnProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCellPdnProfileId.setStatus("current")
_TmnxCellPdnProfRowStatus_Type = RowStatus
_TmnxCellPdnProfRowStatus_Object = MibTableColumn
tmnxCellPdnProfRowStatus = _TmnxCellPdnProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1, 1, 2),
    _TmnxCellPdnProfRowStatus_Type()
)
tmnxCellPdnProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCellPdnProfRowStatus.setStatus("current")
_TmnxCellPdnProfLastChanged_Type = TimeStamp
_TmnxCellPdnProfLastChanged_Object = MibTableColumn
tmnxCellPdnProfLastChanged = _TmnxCellPdnProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1, 1, 3),
    _TmnxCellPdnProfLastChanged_Type()
)
tmnxCellPdnProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnProfLastChanged.setStatus("current")


class _TmnxCellPdnProfDescription_Type(TItemDescription):
    """Custom type tmnxCellPdnProfDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxCellPdnProfDescription_Type.__name__ = "TItemDescription"
_TmnxCellPdnProfDescription_Object = MibTableColumn
tmnxCellPdnProfDescription = _TmnxCellPdnProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1, 1, 4),
    _TmnxCellPdnProfDescription_Type()
)
tmnxCellPdnProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCellPdnProfDescription.setStatus("current")


class _TmnxCellPdnProfApn_Type(TmnxCellularAccessPointName):
    """Custom type tmnxCellPdnProfApn based on TmnxCellularAccessPointName"""
    defaultHexValue = ""


_TmnxCellPdnProfApn_Type.__name__ = "TmnxCellularAccessPointName"
_TmnxCellPdnProfApn_Object = MibTableColumn
tmnxCellPdnProfApn = _TmnxCellPdnProfApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1, 1, 5),
    _TmnxCellPdnProfApn_Type()
)
tmnxCellPdnProfApn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCellPdnProfApn.setStatus("current")


class _TmnxCellPdnProfAuthType_Type(Integer32):
    """Custom type tmnxCellPdnProfAuthType based on Integer32"""
    defaultValue = 0

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
          ("pap", 1),
          ("chap", 2))
    )


_TmnxCellPdnProfAuthType_Type.__name__ = "Integer32"
_TmnxCellPdnProfAuthType_Object = MibTableColumn
tmnxCellPdnProfAuthType = _TmnxCellPdnProfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1, 1, 6),
    _TmnxCellPdnProfAuthType_Type()
)
tmnxCellPdnProfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCellPdnProfAuthType.setStatus("current")


class _TmnxCellPdnProfUsername_Type(DisplayString):
    """Custom type tmnxCellPdnProfUsername based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxCellPdnProfUsername_Type.__name__ = "DisplayString"
_TmnxCellPdnProfUsername_Object = MibTableColumn
tmnxCellPdnProfUsername = _TmnxCellPdnProfUsername_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1, 1, 7),
    _TmnxCellPdnProfUsername_Type()
)
tmnxCellPdnProfUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCellPdnProfUsername.setStatus("current")


class _TmnxCellPdnProfPassword_Type(TmnxAuthPassword):
    """Custom type tmnxCellPdnProfPassword based on TmnxAuthPassword"""
    defaultHexValue = ""


_TmnxCellPdnProfPassword_Type.__name__ = "TmnxAuthPassword"
_TmnxCellPdnProfPassword_Object = MibTableColumn
tmnxCellPdnProfPassword = _TmnxCellPdnProfPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1, 1, 8),
    _TmnxCellPdnProfPassword_Type()
)
tmnxCellPdnProfPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCellPdnProfPassword.setStatus("current")


class _TmnxCellPdnProfProtocol_Type(Integer32):
    """Custom type tmnxCellPdnProfProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_TmnxCellPdnProfProtocol_Type.__name__ = "Integer32"
_TmnxCellPdnProfProtocol_Object = MibTableColumn
tmnxCellPdnProfProtocol = _TmnxCellPdnProfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 2, 1, 1, 9),
    _TmnxCellPdnProfProtocol_Type()
)
tmnxCellPdnProfProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCellPdnProfProtocol.setStatus("current")
_TmnxCellularPortConfigObjs_ObjectIdentity = ObjectIdentity
tmnxCellularPortConfigObjs = _TmnxCellularPortConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3)
)
_TmnxCellularSimCardTable_Object = MibTable
tmnxCellularSimCardTable = _TmnxCellularSimCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxCellularSimCardTable.setStatus("current")
_TmnxCellularSimCardEntry_Object = MibTableRow
tmnxCellularSimCardEntry = _TmnxCellularSimCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 1, 1)
)
tmnxCellularSimCardEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-CELLULAR-MIB", "tmnxCellSimCardId"),
)
if mibBuilder.loadTexts:
    tmnxCellularSimCardEntry.setStatus("current")
_TmnxCellSimCardId_Type = TmnxCellularSimCardNumber
_TmnxCellSimCardId_Object = MibTableColumn
tmnxCellSimCardId = _TmnxCellSimCardId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 1, 1, 1),
    _TmnxCellSimCardId_Type()
)
tmnxCellSimCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCellSimCardId.setStatus("current")
_TmnxCellSimCardLastChanged_Type = TimeStamp
_TmnxCellSimCardLastChanged_Object = MibTableColumn
tmnxCellSimCardLastChanged = _TmnxCellSimCardLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 1, 1, 2),
    _TmnxCellSimCardLastChanged_Type()
)
tmnxCellSimCardLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellSimCardLastChanged.setStatus("current")


class _TmnxCellSimCardDescription_Type(TItemDescription):
    """Custom type tmnxCellSimCardDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxCellSimCardDescription_Type.__name__ = "TItemDescription"
_TmnxCellSimCardDescription_Object = MibTableColumn
tmnxCellSimCardDescription = _TmnxCellSimCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 1, 1, 3),
    _TmnxCellSimCardDescription_Type()
)
tmnxCellSimCardDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellSimCardDescription.setStatus("current")


class _TmnxCellSimCardPin_Type(OctetString):
    """Custom type tmnxCellSimCardPin based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 8),
    )


_TmnxCellSimCardPin_Type.__name__ = "OctetString"
_TmnxCellSimCardPin_Object = MibTableColumn
tmnxCellSimCardPin = _TmnxCellSimCardPin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 1, 1, 4),
    _TmnxCellSimCardPin_Type()
)
tmnxCellSimCardPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellSimCardPin.setStatus("current")


class _TmnxCellSimCardFailureDuration_Type(Unsigned32):
    """Custom type tmnxCellSimCardFailureDuration based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxCellSimCardFailureDuration_Type.__name__ = "Unsigned32"
_TmnxCellSimCardFailureDuration_Object = MibTableColumn
tmnxCellSimCardFailureDuration = _TmnxCellSimCardFailureDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 1, 1, 5),
    _TmnxCellSimCardFailureDuration_Type()
)
tmnxCellSimCardFailureDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellSimCardFailureDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellSimCardFailureDuration.setUnits("minutes")


class _TmnxCellSimCardPortStateSwitch_Type(TruthValue):
    """Custom type tmnxCellSimCardPortStateSwitch based on TruthValue"""
    defaultValue = 1


_TmnxCellSimCardPortStateSwitch_Type.__name__ = "TruthValue"
_TmnxCellSimCardPortStateSwitch_Object = MibTableColumn
tmnxCellSimCardPortStateSwitch = _TmnxCellSimCardPortStateSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 1, 1, 6),
    _TmnxCellSimCardPortStateSwitch_Type()
)
tmnxCellSimCardPortStateSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellSimCardPortStateSwitch.setStatus("current")


class _TmnxCellSimCardBgpStateSwitch_Type(TruthValue):
    """Custom type tmnxCellSimCardBgpStateSwitch based on TruthValue"""
    defaultValue = 2


_TmnxCellSimCardBgpStateSwitch_Type.__name__ = "TruthValue"
_TmnxCellSimCardBgpStateSwitch_Object = MibTableColumn
tmnxCellSimCardBgpStateSwitch = _TmnxCellSimCardBgpStateSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 1, 1, 7),
    _TmnxCellSimCardBgpStateSwitch_Type()
)
tmnxCellSimCardBgpStateSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellSimCardBgpStateSwitch.setStatus("current")
_TmnxCellularPdnTable_Object = MibTable
tmnxCellularPdnTable = _TmnxCellularPdnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxCellularPdnTable.setStatus("current")
_TmnxCellularPdnEntry_Object = MibTableRow
tmnxCellularPdnEntry = _TmnxCellularPdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 2, 1)
)
tmnxCellularPdnEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-CELLULAR-MIB", "tmnxCellPdnId"),
)
if mibBuilder.loadTexts:
    tmnxCellularPdnEntry.setStatus("current")
_TmnxCellPdnId_Type = TmnxCellularPdnId
_TmnxCellPdnId_Object = MibTableColumn
tmnxCellPdnId = _TmnxCellPdnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 2, 1, 1),
    _TmnxCellPdnId_Type()
)
tmnxCellPdnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCellPdnId.setStatus("current")
_TmnxCellPdnRowStatus_Type = RowStatus
_TmnxCellPdnRowStatus_Object = MibTableColumn
tmnxCellPdnRowStatus = _TmnxCellPdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 2, 1, 2),
    _TmnxCellPdnRowStatus_Type()
)
tmnxCellPdnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCellPdnRowStatus.setStatus("current")
_TmnxCellPdnLastChanged_Type = TimeStamp
_TmnxCellPdnLastChanged_Object = MibTableColumn
tmnxCellPdnLastChanged = _TmnxCellPdnLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 2, 1, 3),
    _TmnxCellPdnLastChanged_Type()
)
tmnxCellPdnLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnLastChanged.setStatus("current")


class _TmnxCellPdnProfile_Type(TmnxCellularPdnProfileId):
    """Custom type tmnxCellPdnProfile based on TmnxCellularPdnProfileId"""
    defaultValue = 0


_TmnxCellPdnProfile_Type.__name__ = "TmnxCellularPdnProfileId"
_TmnxCellPdnProfile_Object = MibTableColumn
tmnxCellPdnProfile = _TmnxCellPdnProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 2, 1, 4),
    _TmnxCellPdnProfile_Type()
)
tmnxCellPdnProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCellPdnProfile.setStatus("current")
_TmnxCellularPortTable_Object = MibTable
tmnxCellularPortTable = _TmnxCellularPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxCellularPortTable.setStatus("current")
_TmnxCellularPortEntry_Object = MibTableRow
tmnxCellularPortEntry = _TmnxCellularPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 3, 1)
)
tmnxCellularPortEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxCellularPortEntry.setStatus("current")
_TmnxCellPortLastChanged_Type = TimeStamp
_TmnxCellPortLastChanged_Object = MibTableColumn
tmnxCellPortLastChanged = _TmnxCellPortLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 3, 1, 1),
    _TmnxCellPortLastChanged_Type()
)
tmnxCellPortLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortLastChanged.setStatus("current")


class _TmnxCellPortBand125MaxPowerLevel_Type(Unsigned32):
    """Custom type tmnxCellPortBand125MaxPowerLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TmnxCellPortBand125MaxPowerLevel_Type.__name__ = "Unsigned32"
_TmnxCellPortBand125MaxPowerLevel_Object = MibTableColumn
tmnxCellPortBand125MaxPowerLevel = _TmnxCellPortBand125MaxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 3, 1, 2),
    _TmnxCellPortBand125MaxPowerLevel_Type()
)
tmnxCellPortBand125MaxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellPortBand125MaxPowerLevel.setStatus("current")


class _TmnxCellPortSyncSysTime_Type(TruthValue):
    """Custom type tmnxCellPortSyncSysTime based on TruthValue"""
    defaultValue = 2


_TmnxCellPortSyncSysTime_Type.__name__ = "TruthValue"
_TmnxCellPortSyncSysTime_Object = MibTableColumn
tmnxCellPortSyncSysTime = _TmnxCellPortSyncSysTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 3, 1, 3),
    _TmnxCellPortSyncSysTime_Type()
)
tmnxCellPortSyncSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellPortSyncSysTime.setStatus("current")
_TmnxCellularMdaTable_Object = MibTable
tmnxCellularMdaTable = _TmnxCellularMdaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxCellularMdaTable.setStatus("current")
_TmnxCellularMdaEntry_Object = MibTableRow
tmnxCellularMdaEntry = _TmnxCellularMdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1)
)
tmnxCellularMdaEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxCellularMdaEntry.setStatus("current")
_TmnxCellMdaLastChanged_Type = TimeStamp
_TmnxCellMdaLastChanged_Object = MibTableColumn
tmnxCellMdaLastChanged = _TmnxCellMdaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 1),
    _TmnxCellMdaLastChanged_Type()
)
tmnxCellMdaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellMdaLastChanged.setStatus("current")


class _TmnxCellMdaAdminActiveSim_Type(Integer32):
    """Custom type tmnxCellMdaAdminActiveSim based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sim-1", 1),
          ("sim-2", 2),
          ("automatic", 3))
    )


_TmnxCellMdaAdminActiveSim_Type.__name__ = "Integer32"
_TmnxCellMdaAdminActiveSim_Object = MibTableColumn
tmnxCellMdaAdminActiveSim = _TmnxCellMdaAdminActiveSim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 2),
    _TmnxCellMdaAdminActiveSim_Type()
)
tmnxCellMdaAdminActiveSim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellMdaAdminActiveSim.setStatus("current")


class _TmnxCellMdaDownResetInterval_Type(Unsigned32):
    """Custom type tmnxCellMdaDownResetInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_TmnxCellMdaDownResetInterval_Type.__name__ = "Unsigned32"
_TmnxCellMdaDownResetInterval_Object = MibTableColumn
tmnxCellMdaDownResetInterval = _TmnxCellMdaDownResetInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 3),
    _TmnxCellMdaDownResetInterval_Type()
)
tmnxCellMdaDownResetInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellMdaDownResetInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellMdaDownResetInterval.setUnits("minutes")


class _TmnxCellMdaDownResetCriteria_Type(Bits):
    """Custom type tmnxCellMdaDownResetCriteria based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("port", 0),
          ("bgp", 1))
    )

_TmnxCellMdaDownResetCriteria_Type.__name__ = "Bits"
_TmnxCellMdaDownResetCriteria_Object = MibTableColumn
tmnxCellMdaDownResetCriteria = _TmnxCellMdaDownResetCriteria_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 4),
    _TmnxCellMdaDownResetCriteria_Type()
)
tmnxCellMdaDownResetCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellMdaDownResetCriteria.setStatus("current")
_TmnxCellMdaDownResetPending_Type = TruthValue
_TmnxCellMdaDownResetPending_Object = MibTableColumn
tmnxCellMdaDownResetPending = _TmnxCellMdaDownResetPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 5),
    _TmnxCellMdaDownResetPending_Type()
)
tmnxCellMdaDownResetPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellMdaDownResetPending.setStatus("current")


class _TmnxCellMdaDownResetTime_Type(Unsigned32):
    """Custom type tmnxCellMdaDownResetTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_TmnxCellMdaDownResetTime_Type.__name__ = "Unsigned32"
_TmnxCellMdaDownResetTime_Object = MibTableColumn
tmnxCellMdaDownResetTime = _TmnxCellMdaDownResetTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 6),
    _TmnxCellMdaDownResetTime_Type()
)
tmnxCellMdaDownResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellMdaDownResetTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellMdaDownResetTime.setUnits("seconds")


class _TmnxCellMdaPreferredSim_Type(TmnxCellularSimCardNumber):
    """Custom type tmnxCellMdaPreferredSim based on TmnxCellularSimCardNumber"""
    defaultValue = 1


_TmnxCellMdaPreferredSim_Type.__name__ = "TmnxCellularSimCardNumber"
_TmnxCellMdaPreferredSim_Object = MibTableColumn
tmnxCellMdaPreferredSim = _TmnxCellMdaPreferredSim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 7),
    _TmnxCellMdaPreferredSim_Type()
)
tmnxCellMdaPreferredSim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellMdaPreferredSim.setStatus("current")
_TmnxCellMdaOperActiveSim_Type = TmnxCellularSimCardNumber
_TmnxCellMdaOperActiveSim_Object = MibTableColumn
tmnxCellMdaOperActiveSim = _TmnxCellMdaOperActiveSim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 8),
    _TmnxCellMdaOperActiveSim_Type()
)
tmnxCellMdaOperActiveSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellMdaOperActiveSim.setStatus("current")
_TmnxCellMdaSimCardSwitchPending_Type = TruthValue
_TmnxCellMdaSimCardSwitchPending_Object = MibTableColumn
tmnxCellMdaSimCardSwitchPending = _TmnxCellMdaSimCardSwitchPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 9),
    _TmnxCellMdaSimCardSwitchPending_Type()
)
tmnxCellMdaSimCardSwitchPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellMdaSimCardSwitchPending.setStatus("current")


class _TmnxCellMdaSimCardSwitchTime_Type(Unsigned32):
    """Custom type tmnxCellMdaSimCardSwitchTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxCellMdaSimCardSwitchTime_Type.__name__ = "Unsigned32"
_TmnxCellMdaSimCardSwitchTime_Object = MibTableColumn
tmnxCellMdaSimCardSwitchTime = _TmnxCellMdaSimCardSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 10),
    _TmnxCellMdaSimCardSwitchTime_Type()
)
tmnxCellMdaSimCardSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellMdaSimCardSwitchTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellMdaSimCardSwitchTime.setUnits("seconds")
_TmnxCellMdaSimCardLastSwitchTime_Type = TimeStamp
_TmnxCellMdaSimCardLastSwitchTime_Object = MibTableColumn
tmnxCellMdaSimCardLastSwitchTime = _TmnxCellMdaSimCardLastSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 11),
    _TmnxCellMdaSimCardLastSwitchTime_Type()
)
tmnxCellMdaSimCardLastSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellMdaSimCardLastSwitchTime.setStatus("current")


class _TmnxCellMdaSimLastSwitchReason_Type(Integer32):
    """Custom type tmnxCellMdaSimLastSwitchReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("manual-configuration", 1),
          ("forced-switch", 2),
          ("cellular-port-down", 3),
          ("no-bgp-neighbor", 4))
    )


_TmnxCellMdaSimLastSwitchReason_Type.__name__ = "Integer32"
_TmnxCellMdaSimLastSwitchReason_Object = MibTableColumn
tmnxCellMdaSimLastSwitchReason = _TmnxCellMdaSimLastSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 12),
    _TmnxCellMdaSimLastSwitchReason_Type()
)
tmnxCellMdaSimLastSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellMdaSimLastSwitchReason.setStatus("current")
_TmnxCellMdaSpecFirmwareVersion_Type = DisplayString
_TmnxCellMdaSpecFirmwareVersion_Object = MibTableColumn
tmnxCellMdaSpecFirmwareVersion = _TmnxCellMdaSpecFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 13),
    _TmnxCellMdaSpecFirmwareVersion_Type()
)
tmnxCellMdaSpecFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellMdaSpecFirmwareVersion.setStatus("current")


class _TmnxCellMdaMaxTxPower_Type(Integer32):
    """Custom type tmnxCellMdaMaxTxPower based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_TmnxCellMdaMaxTxPower_Type.__name__ = "Integer32"
_TmnxCellMdaMaxTxPower_Object = MibTableColumn
tmnxCellMdaMaxTxPower = _TmnxCellMdaMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 4, 1, 14),
    _TmnxCellMdaMaxTxPower_Type()
)
tmnxCellMdaMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellMdaMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellMdaMaxTxPower.setUnits("decibel-milliwatts")
_TmnxCellPortCbsdAuthCfgTable_Object = MibTable
tmnxCellPortCbsdAuthCfgTable = _TmnxCellPortCbsdAuthCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthCfgTable.setStatus("current")
_TmnxCellPortCbsdAuthCfgEntry_Object = MibTableRow
tmnxCellPortCbsdAuthCfgEntry = _TmnxCellPortCbsdAuthCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthCfgEntry.setStatus("current")
_TmnxCellPortCbsdAuthCfgLstChange_Type = TimeStamp
_TmnxCellPortCbsdAuthCfgLstChange_Object = MibTableColumn
tmnxCellPortCbsdAuthCfgLstChange = _TmnxCellPortCbsdAuthCfgLstChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 5, 1, 1),
    _TmnxCellPortCbsdAuthCfgLstChange_Type()
)
tmnxCellPortCbsdAuthCfgLstChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthCfgLstChange.setStatus("current")


class _TmnxCellPortCbsdAuthAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxCellPortCbsdAuthAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxCellPortCbsdAuthAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxCellPortCbsdAuthAdminState_Object = MibTableColumn
tmnxCellPortCbsdAuthAdminState = _TmnxCellPortCbsdAuthAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 5, 1, 2),
    _TmnxCellPortCbsdAuthAdminState_Type()
)
tmnxCellPortCbsdAuthAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthAdminState.setStatus("current")


class _TmnxCellPortCbsdAuthUserId_Type(DisplayString):
    """Custom type tmnxCellPortCbsdAuthUserId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_TmnxCellPortCbsdAuthUserId_Type.__name__ = "DisplayString"
_TmnxCellPortCbsdAuthUserId_Object = MibTableColumn
tmnxCellPortCbsdAuthUserId = _TmnxCellPortCbsdAuthUserId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 5, 1, 3),
    _TmnxCellPortCbsdAuthUserId_Type()
)
tmnxCellPortCbsdAuthUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthUserId.setStatus("current")


class _TmnxCellPortCbsdAuthAntennaGain_Type(Unsigned32):
    """Custom type tmnxCellPortCbsdAuthAntennaGain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_TmnxCellPortCbsdAuthAntennaGain_Type.__name__ = "Unsigned32"
_TmnxCellPortCbsdAuthAntennaGain_Object = MibTableColumn
tmnxCellPortCbsdAuthAntennaGain = _TmnxCellPortCbsdAuthAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 5, 1, 4),
    _TmnxCellPortCbsdAuthAntennaGain_Type()
)
tmnxCellPortCbsdAuthAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthAntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthAntennaGain.setUnits("decibel-milliwatts")


class _TmnxCellPortCbsdAuthClntTlsProf_Type(TNamedItemOrEmpty):
    """Custom type tmnxCellPortCbsdAuthClntTlsProf based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxCellPortCbsdAuthClntTlsProf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxCellPortCbsdAuthClntTlsProf_Object = MibTableColumn
tmnxCellPortCbsdAuthClntTlsProf = _TmnxCellPortCbsdAuthClntTlsProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 5, 1, 5),
    _TmnxCellPortCbsdAuthClntTlsProf_Type()
)
tmnxCellPortCbsdAuthClntTlsProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthClntTlsProf.setStatus("current")


class _TmnxCellPortCbsdAuthPriSasSvrUrl_Type(DisplayString):
    """Custom type tmnxCellPortCbsdAuthPriSasSvrUrl based on DisplayString"""
    defaultValue = OctetString("")


_TmnxCellPortCbsdAuthPriSasSvrUrl_Type.__name__ = "DisplayString"
_TmnxCellPortCbsdAuthPriSasSvrUrl_Object = MibTableColumn
tmnxCellPortCbsdAuthPriSasSvrUrl = _TmnxCellPortCbsdAuthPriSasSvrUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 5, 1, 6),
    _TmnxCellPortCbsdAuthPriSasSvrUrl_Type()
)
tmnxCellPortCbsdAuthPriSasSvrUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthPriSasSvrUrl.setStatus("current")


class _TmnxCellPortCbsdAuthSecSasSvrUrl_Type(DisplayString):
    """Custom type tmnxCellPortCbsdAuthSecSasSvrUrl based on DisplayString"""
    defaultValue = OctetString("")


_TmnxCellPortCbsdAuthSecSasSvrUrl_Type.__name__ = "DisplayString"
_TmnxCellPortCbsdAuthSecSasSvrUrl_Object = MibTableColumn
tmnxCellPortCbsdAuthSecSasSvrUrl = _TmnxCellPortCbsdAuthSecSasSvrUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 5, 1, 7),
    _TmnxCellPortCbsdAuthSecSasSvrUrl_Type()
)
tmnxCellPortCbsdAuthSecSasSvrUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthSecSasSvrUrl.setStatus("current")


class _TmnxCellPortCbsdAuthCategory_Type(Integer32):
    """Custom type tmnxCellPortCbsdAuthCategory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_TmnxCellPortCbsdAuthCategory_Type.__name__ = "Integer32"
_TmnxCellPortCbsdAuthCategory_Object = MibTableColumn
tmnxCellPortCbsdAuthCategory = _TmnxCellPortCbsdAuthCategory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 2, 3, 5, 1, 8),
    _TmnxCellPortCbsdAuthCategory_Type()
)
tmnxCellPortCbsdAuthCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthCategory.setStatus("current")
_TmnxCellularStatusObjs_ObjectIdentity = ObjectIdentity
tmnxCellularStatusObjs = _TmnxCellularStatusObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3)
)
_TmnxCellularPortStatusObjs_ObjectIdentity = ObjectIdentity
tmnxCellularPortStatusObjs = _TmnxCellularPortStatusObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1)
)
_TmnxCellularPortStatusTable_Object = MibTable
tmnxCellularPortStatusTable = _TmnxCellularPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxCellularPortStatusTable.setStatus("current")
_TmnxCellularPortStatusEntry_Object = MibTableRow
tmnxCellularPortStatusEntry = _TmnxCellularPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1)
)
tmnxCellularPortStatusEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxCellularPortStatusEntry.setStatus("current")
_TmnxCellPortImei_Type = TmnxCellularImei
_TmnxCellPortImei_Object = MibTableColumn
tmnxCellPortImei = _TmnxCellPortImei_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 1),
    _TmnxCellPortImei_Type()
)
tmnxCellPortImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortImei.setStatus("current")


class _TmnxCellPortRegistrationStatus_Type(Integer32):
    """Custom type tmnxCellPortRegistrationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("not-registered", 0),
          ("registered-home", 1),
          ("searching", 2),
          ("denied", 3),
          ("no-network", 4),
          ("registered-roaming", 5),
          ("sms-only-home", 6),
          ("sms-only-roaming", 7),
          ("emergency-only", 8),
          ("csfb-not-preferred-home", 9),
          ("csfb-not-preferred-roaming", 10))
    )


_TmnxCellPortRegistrationStatus_Type.__name__ = "Integer32"
_TmnxCellPortRegistrationStatus_Object = MibTableColumn
tmnxCellPortRegistrationStatus = _TmnxCellPortRegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 2),
    _TmnxCellPortRegistrationStatus_Type()
)
tmnxCellPortRegistrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortRegistrationStatus.setStatus("current")


class _TmnxCellPortWirelessTechnology_Type(Integer32):
    """Custom type tmnxCellPortWirelessTechnology based on Integer32"""
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
        *(("none", 0),
          ("lte", 1),
          ("wcdma", 2),
          ("gsm", 3))
    )


_TmnxCellPortWirelessTechnology_Type.__name__ = "Integer32"
_TmnxCellPortWirelessTechnology_Object = MibTableColumn
tmnxCellPortWirelessTechnology = _TmnxCellPortWirelessTechnology_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 3),
    _TmnxCellPortWirelessTechnology_Type()
)
tmnxCellPortWirelessTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortWirelessTechnology.setStatus("current")
_TmnxCellPortFrequencyBand_Type = Unsigned32
_TmnxCellPortFrequencyBand_Object = MibTableColumn
tmnxCellPortFrequencyBand = _TmnxCellPortFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 4),
    _TmnxCellPortFrequencyBand_Type()
)
tmnxCellPortFrequencyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortFrequencyBand.setStatus("current")
_TmnxCellPortChannelNumber_Type = TmnxCellularChannelNumber
_TmnxCellPortChannelNumber_Object = MibTableColumn
tmnxCellPortChannelNumber = _TmnxCellPortChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 5),
    _TmnxCellPortChannelNumber_Type()
)
tmnxCellPortChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortChannelNumber.setStatus("current")


class _TmnxCellPortAreaCode_Type(DisplayString):
    """Custom type tmnxCellPortAreaCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_TmnxCellPortAreaCode_Type.__name__ = "DisplayString"
_TmnxCellPortAreaCode_Object = MibTableColumn
tmnxCellPortAreaCode = _TmnxCellPortAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 6),
    _TmnxCellPortAreaCode_Type()
)
tmnxCellPortAreaCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortAreaCode.setStatus("current")


class _TmnxCellPortCellIdentity_Type(DisplayString):
    """Custom type tmnxCellPortCellIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxCellPortCellIdentity_Type.__name__ = "DisplayString"
_TmnxCellPortCellIdentity_Object = MibTableColumn
tmnxCellPortCellIdentity = _TmnxCellPortCellIdentity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 7),
    _TmnxCellPortCellIdentity_Type()
)
tmnxCellPortCellIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCellIdentity.setStatus("current")


class _TmnxCellPortRssi_Type(Integer32):
    """Custom type tmnxCellPortRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-113, -51),
        ValueRangeConstraint(0, 0),
    )


_TmnxCellPortRssi_Type.__name__ = "Integer32"
_TmnxCellPortRssi_Object = MibTableColumn
tmnxCellPortRssi = _TmnxCellPortRssi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 8),
    _TmnxCellPortRssi_Type()
)
tmnxCellPortRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortRssi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellPortRssi.setUnits("decibel-milliwatts")


class _TmnxCellPortRsrp_Type(Integer32):
    """Custom type tmnxCellPortRsrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, -44),
        ValueRangeConstraint(0, 0),
    )


_TmnxCellPortRsrp_Type.__name__ = "Integer32"
_TmnxCellPortRsrp_Object = MibTableColumn
tmnxCellPortRsrp = _TmnxCellPortRsrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 9),
    _TmnxCellPortRsrp_Type()
)
tmnxCellPortRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortRsrp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellPortRsrp.setUnits("decibel-milliwatts")


class _TmnxCellPortRscp_Type(Integer32):
    """Custom type tmnxCellPortRscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, -25),
        ValueRangeConstraint(0, 0),
    )


_TmnxCellPortRscp_Type.__name__ = "Integer32"
_TmnxCellPortRscp_Object = MibTableColumn
tmnxCellPortRscp = _TmnxCellPortRscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 10),
    _TmnxCellPortRscp_Type()
)
tmnxCellPortRscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortRscp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellPortRscp.setUnits("decibel-milliwatts")


class _TmnxCellPortRsrq_Type(Integer32):
    """Custom type tmnxCellPortRsrq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, -3),
        ValueRangeConstraint(0, 0),
    )


_TmnxCellPortRsrq_Type.__name__ = "Integer32"
_TmnxCellPortRsrq_Object = MibTableColumn
tmnxCellPortRsrq = _TmnxCellPortRsrq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 11),
    _TmnxCellPortRsrq_Type()
)
tmnxCellPortRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortRsrq.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellPortRsrq.setUnits("decibel")


class _TmnxCellPortSinr_Type(Integer32):
    """Custom type tmnxCellPortSinr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 400),
    )


_TmnxCellPortSinr_Type.__name__ = "Integer32"
_TmnxCellPortSinr_Object = MibTableColumn
tmnxCellPortSinr = _TmnxCellPortSinr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 1, 1, 12),
    _TmnxCellPortSinr_Type()
)
tmnxCellPortSinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortSinr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellPortSinr.setUnits("0.1 decibel")
_TmnxCellularSimCardStatusTable_Object = MibTable
tmnxCellularSimCardStatusTable = _TmnxCellularSimCardStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxCellularSimCardStatusTable.setStatus("current")
_TmnxCellularSimCardStatusEntry_Object = MibTableRow
tmnxCellularSimCardStatusEntry = _TmnxCellularSimCardStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxCellularSimCardStatusEntry.setStatus("current")
_TmnxCellSimCardEquipped_Type = TruthValue
_TmnxCellSimCardEquipped_Object = MibTableColumn
tmnxCellSimCardEquipped = _TmnxCellSimCardEquipped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 3, 1, 1),
    _TmnxCellSimCardEquipped_Type()
)
tmnxCellSimCardEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellSimCardEquipped.setStatus("current")
_TmnxCellSimCardIccid_Type = TmnxCellularSimCardIccid
_TmnxCellSimCardIccid_Object = MibTableColumn
tmnxCellSimCardIccid = _TmnxCellSimCardIccid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 3, 1, 2),
    _TmnxCellSimCardIccid_Type()
)
tmnxCellSimCardIccid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellSimCardIccid.setStatus("current")
_TmnxCellSimCardImsi_Type = TmnxCellularImsi
_TmnxCellSimCardImsi_Object = MibTableColumn
tmnxCellSimCardImsi = _TmnxCellSimCardImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 3, 1, 3),
    _TmnxCellSimCardImsi_Type()
)
tmnxCellSimCardImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellSimCardImsi.setStatus("current")
_TmnxCellSimCardLocked_Type = TruthValue
_TmnxCellSimCardLocked_Object = MibTableColumn
tmnxCellSimCardLocked = _TmnxCellSimCardLocked_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 3, 1, 4),
    _TmnxCellSimCardLocked_Type()
)
tmnxCellSimCardLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellSimCardLocked.setStatus("current")


class _TmnxCellSimCardPinStatus_Type(Integer32):
    """Custom type tmnxCellSimCardPinStatus based on Integer32"""
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
          ("waiting-for-pin", 1),
          ("waiting-for-puk", 2),
          ("ready", 3))
    )


_TmnxCellSimCardPinStatus_Type.__name__ = "Integer32"
_TmnxCellSimCardPinStatus_Object = MibTableColumn
tmnxCellSimCardPinStatus = _TmnxCellSimCardPinStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 3, 1, 5),
    _TmnxCellSimCardPinStatus_Type()
)
tmnxCellSimCardPinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellSimCardPinStatus.setStatus("current")
_TmnxCellSimCardPinRetries_Type = Unsigned32
_TmnxCellSimCardPinRetries_Object = MibTableColumn
tmnxCellSimCardPinRetries = _TmnxCellSimCardPinRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 3, 1, 6),
    _TmnxCellSimCardPinRetries_Type()
)
tmnxCellSimCardPinRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellSimCardPinRetries.setStatus("current")
_TmnxCellSimCardPukRetries_Type = Unsigned32
_TmnxCellSimCardPukRetries_Object = MibTableColumn
tmnxCellSimCardPukRetries = _TmnxCellSimCardPukRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 3, 1, 7),
    _TmnxCellSimCardPukRetries_Type()
)
tmnxCellSimCardPukRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellSimCardPukRetries.setStatus("current")
_TmnxCellSimCardFirmwareVersion_Type = DisplayString
_TmnxCellSimCardFirmwareVersion_Object = MibTableColumn
tmnxCellSimCardFirmwareVersion = _TmnxCellSimCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 3, 1, 8),
    _TmnxCellSimCardFirmwareVersion_Type()
)
tmnxCellSimCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellSimCardFirmwareVersion.setStatus("current")
_TmnxCellularPdnStatusTable_Object = MibTable
tmnxCellularPdnStatusTable = _TmnxCellularPdnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxCellularPdnStatusTable.setStatus("current")
_TmnxCellularPdnStatusEntry_Object = MibTableRow
tmnxCellularPdnStatusEntry = _TmnxCellularPdnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxCellularPdnStatusEntry.setStatus("current")


class _TmnxCellPdnConnectionState_Type(Integer32):
    """Custom type tmnxCellPdnConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 0),
          ("connected", 1))
    )


_TmnxCellPdnConnectionState_Type.__name__ = "Integer32"
_TmnxCellPdnConnectionState_Object = MibTableColumn
tmnxCellPdnConnectionState = _TmnxCellPdnConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4, 1, 1),
    _TmnxCellPdnConnectionState_Type()
)
tmnxCellPdnConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnConnectionState.setStatus("current")
_TmnxCellPdnIpAddrType_Type = InetAddressType
_TmnxCellPdnIpAddrType_Object = MibTableColumn
tmnxCellPdnIpAddrType = _TmnxCellPdnIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4, 1, 2),
    _TmnxCellPdnIpAddrType_Type()
)
tmnxCellPdnIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnIpAddrType.setStatus("current")


class _TmnxCellPdnIpAddress_Type(InetAddress):
    """Custom type tmnxCellPdnIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxCellPdnIpAddress_Type.__name__ = "InetAddress"
_TmnxCellPdnIpAddress_Object = MibTableColumn
tmnxCellPdnIpAddress = _TmnxCellPdnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4, 1, 3),
    _TmnxCellPdnIpAddress_Type()
)
tmnxCellPdnIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnIpAddress.setStatus("current")
_TmnxCellPdnPrimaryDnsAddrType_Type = InetAddressType
_TmnxCellPdnPrimaryDnsAddrType_Object = MibTableColumn
tmnxCellPdnPrimaryDnsAddrType = _TmnxCellPdnPrimaryDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4, 1, 4),
    _TmnxCellPdnPrimaryDnsAddrType_Type()
)
tmnxCellPdnPrimaryDnsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnPrimaryDnsAddrType.setStatus("current")


class _TmnxCellPdnPrimaryDnsAddress_Type(InetAddress):
    """Custom type tmnxCellPdnPrimaryDnsAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxCellPdnPrimaryDnsAddress_Type.__name__ = "InetAddress"
_TmnxCellPdnPrimaryDnsAddress_Object = MibTableColumn
tmnxCellPdnPrimaryDnsAddress = _TmnxCellPdnPrimaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4, 1, 5),
    _TmnxCellPdnPrimaryDnsAddress_Type()
)
tmnxCellPdnPrimaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnPrimaryDnsAddress.setStatus("current")
_TmnxCellPdnSecondaryDnsAddrType_Type = InetAddressType
_TmnxCellPdnSecondaryDnsAddrType_Object = MibTableColumn
tmnxCellPdnSecondaryDnsAddrType = _TmnxCellPdnSecondaryDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4, 1, 6),
    _TmnxCellPdnSecondaryDnsAddrType_Type()
)
tmnxCellPdnSecondaryDnsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnSecondaryDnsAddrType.setStatus("current")


class _TmnxCellPdnSecondaryDnsAddress_Type(InetAddress):
    """Custom type tmnxCellPdnSecondaryDnsAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxCellPdnSecondaryDnsAddress_Type.__name__ = "InetAddress"
_TmnxCellPdnSecondaryDnsAddress_Object = MibTableColumn
tmnxCellPdnSecondaryDnsAddress = _TmnxCellPdnSecondaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4, 1, 7),
    _TmnxCellPdnSecondaryDnsAddress_Type()
)
tmnxCellPdnSecondaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnSecondaryDnsAddress.setStatus("current")
_TmnxCellPdnApn_Type = TmnxCellularAccessPointName
_TmnxCellPdnApn_Object = MibTableColumn
tmnxCellPdnApn = _TmnxCellPdnApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4, 1, 8),
    _TmnxCellPdnApn_Type()
)
tmnxCellPdnApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnApn.setStatus("current")
_TmnxCellPdnMtu_Type = Unsigned32
_TmnxCellPdnMtu_Object = MibTableColumn
tmnxCellPdnMtu = _TmnxCellPdnMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 4, 1, 9),
    _TmnxCellPdnMtu_Type()
)
tmnxCellPdnMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPdnMtu.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellPdnMtu.setUnits("bytes")
_TmnxCellularPortBearerTable_Object = MibTable
tmnxCellularPortBearerTable = _TmnxCellularPortBearerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxCellularPortBearerTable.setStatus("current")
_TmnxCellularPortBearerEntry_Object = MibTableRow
tmnxCellularPortBearerEntry = _TmnxCellularPortBearerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 5, 1)
)
tmnxCellularPortBearerEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerId"),
)
if mibBuilder.loadTexts:
    tmnxCellularPortBearerEntry.setStatus("current")


class _TmnxCellPortBearerId_Type(Unsigned32):
    """Custom type tmnxCellPortBearerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TmnxCellPortBearerId_Type.__name__ = "Unsigned32"
_TmnxCellPortBearerId_Object = MibTableColumn
tmnxCellPortBearerId = _TmnxCellPortBearerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 5, 1, 1),
    _TmnxCellPortBearerId_Type()
)
tmnxCellPortBearerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortBearerId.setStatus("current")


class _TmnxCellPortBearerType_Type(Integer32):
    """Custom type tmnxCellPortBearerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("dedicated", 2))
    )


_TmnxCellPortBearerType_Type.__name__ = "Integer32"
_TmnxCellPortBearerType_Object = MibTableColumn
tmnxCellPortBearerType = _TmnxCellPortBearerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 5, 1, 2),
    _TmnxCellPortBearerType_Type()
)
tmnxCellPortBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortBearerType.setStatus("current")


class _TmnxCellPortBearerQci_Type(Unsigned32):
    """Custom type tmnxCellPortBearerQci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_TmnxCellPortBearerQci_Type.__name__ = "Unsigned32"
_TmnxCellPortBearerQci_Object = MibTableColumn
tmnxCellPortBearerQci = _TmnxCellPortBearerQci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 5, 1, 3),
    _TmnxCellPortBearerQci_Type()
)
tmnxCellPortBearerQci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortBearerQci.setStatus("current")
_TmnxCellPortBearerUlGbr_Type = TmnxCellularBearerRate
_TmnxCellPortBearerUlGbr_Object = MibTableColumn
tmnxCellPortBearerUlGbr = _TmnxCellPortBearerUlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 5, 1, 4),
    _TmnxCellPortBearerUlGbr_Type()
)
tmnxCellPortBearerUlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortBearerUlGbr.setStatus("current")
_TmnxCellPortBearerUlMbr_Type = TmnxCellularBearerRate
_TmnxCellPortBearerUlMbr_Object = MibTableColumn
tmnxCellPortBearerUlMbr = _TmnxCellPortBearerUlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 5, 1, 5),
    _TmnxCellPortBearerUlMbr_Type()
)
tmnxCellPortBearerUlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortBearerUlMbr.setStatus("current")
_TmnxCellPortBearerDlGbr_Type = TmnxCellularBearerRate
_TmnxCellPortBearerDlGbr_Object = MibTableColumn
tmnxCellPortBearerDlGbr = _TmnxCellPortBearerDlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 5, 1, 6),
    _TmnxCellPortBearerDlGbr_Type()
)
tmnxCellPortBearerDlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortBearerDlGbr.setStatus("current")
_TmnxCellPortBearerDlMbr_Type = TmnxCellularBearerRate
_TmnxCellPortBearerDlMbr_Object = MibTableColumn
tmnxCellPortBearerDlMbr = _TmnxCellPortBearerDlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 5, 1, 7),
    _TmnxCellPortBearerDlMbr_Type()
)
tmnxCellPortBearerDlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortBearerDlMbr.setStatus("current")
_TmnxCellularPortTftTable_Object = MibTable
tmnxCellularPortTftTable = _TmnxCellularPortTftTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxCellularPortTftTable.setStatus("current")
_TmnxCellularPortTftEntry_Object = MibTableRow
tmnxCellularPortTftEntry = _TmnxCellularPortTftEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 6, 1)
)
tmnxCellularPortTftEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerId"),
    (0, "TIMETRA-CELLULAR-MIB", "tmnxCellPortTftPacketFilterId"),
)
if mibBuilder.loadTexts:
    tmnxCellularPortTftEntry.setStatus("current")


class _TmnxCellPortTftPacketFilterId_Type(Unsigned32):
    """Custom type tmnxCellPortTftPacketFilterId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TmnxCellPortTftPacketFilterId_Type.__name__ = "Unsigned32"
_TmnxCellPortTftPacketFilterId_Object = MibTableColumn
tmnxCellPortTftPacketFilterId = _TmnxCellPortTftPacketFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 6, 1, 1),
    _TmnxCellPortTftPacketFilterId_Type()
)
tmnxCellPortTftPacketFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortTftPacketFilterId.setStatus("current")


class _TmnxCellPortTftEvalPrecedence_Type(Unsigned32):
    """Custom type tmnxCellPortTftEvalPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxCellPortTftEvalPrecedence_Type.__name__ = "Unsigned32"
_TmnxCellPortTftEvalPrecedence_Object = MibTableColumn
tmnxCellPortTftEvalPrecedence = _TmnxCellPortTftEvalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 6, 1, 2),
    _TmnxCellPortTftEvalPrecedence_Type()
)
tmnxCellPortTftEvalPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortTftEvalPrecedence.setStatus("current")


class _TmnxCellPortTftDirection_Type(Integer32):
    """Custom type tmnxCellPortTftDirection based on Integer32"""
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
        *(("pre-release-7", 0),
          ("uplink", 1),
          ("downlink", 2),
          ("bidirectional", 3))
    )


_TmnxCellPortTftDirection_Type.__name__ = "Integer32"
_TmnxCellPortTftDirection_Object = MibTableColumn
tmnxCellPortTftDirection = _TmnxCellPortTftDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 6, 1, 3),
    _TmnxCellPortTftDirection_Type()
)
tmnxCellPortTftDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortTftDirection.setStatus("current")


class _TmnxCellPortTftTos_Type(Unsigned32):
    """Custom type tmnxCellPortTftTos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxCellPortTftTos_Type.__name__ = "Unsigned32"
_TmnxCellPortTftTos_Object = MibTableColumn
tmnxCellPortTftTos = _TmnxCellPortTftTos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 6, 1, 4),
    _TmnxCellPortTftTos_Type()
)
tmnxCellPortTftTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortTftTos.setStatus("current")


class _TmnxCellPortTftTosMask_Type(Unsigned32):
    """Custom type tmnxCellPortTftTosMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxCellPortTftTosMask_Type.__name__ = "Unsigned32"
_TmnxCellPortTftTosMask_Object = MibTableColumn
tmnxCellPortTftTosMask = _TmnxCellPortTftTosMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 6, 1, 5),
    _TmnxCellPortTftTosMask_Type()
)
tmnxCellPortTftTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortTftTosMask.setStatus("current")
_TmnxCellPortCbsdAuthStatsTable_Object = MibTable
tmnxCellPortCbsdAuthStatsTable = _TmnxCellPortCbsdAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthStatsTable.setStatus("current")
_TmnxCellPortCbsdAuthStatsEntry_Object = MibTableRow
tmnxCellPortCbsdAuthStatsEntry = _TmnxCellPortCbsdAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthStatsEntry.setStatus("current")
_TmnxCellPortCbsdAuthOperState_Type = TmnxEnabledDisabled
_TmnxCellPortCbsdAuthOperState_Object = MibTableColumn
tmnxCellPortCbsdAuthOperState = _TmnxCellPortCbsdAuthOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 1),
    _TmnxCellPortCbsdAuthOperState_Type()
)
tmnxCellPortCbsdAuthOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthOperState.setStatus("current")
_TmnxCellPortCbsdAuthId_Type = DisplayString
_TmnxCellPortCbsdAuthId_Object = MibTableColumn
tmnxCellPortCbsdAuthId = _TmnxCellPortCbsdAuthId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 2),
    _TmnxCellPortCbsdAuthId_Type()
)
tmnxCellPortCbsdAuthId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthId.setStatus("current")
_TmnxCellPortCbsdAuthGrantId_Type = DisplayString
_TmnxCellPortCbsdAuthGrantId_Object = MibTableColumn
tmnxCellPortCbsdAuthGrantId = _TmnxCellPortCbsdAuthGrantId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 3),
    _TmnxCellPortCbsdAuthGrantId_Type()
)
tmnxCellPortCbsdAuthGrantId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthGrantId.setStatus("current")
_TmnxCellPortCbsdAuthFccId_Type = DisplayString
_TmnxCellPortCbsdAuthFccId_Object = MibTableColumn
tmnxCellPortCbsdAuthFccId = _TmnxCellPortCbsdAuthFccId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 4),
    _TmnxCellPortCbsdAuthFccId_Type()
)
tmnxCellPortCbsdAuthFccId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthFccId.setStatus("current")


class _TmnxCellPortCbsdAuthRegState_Type(Integer32):
    """Custom type tmnxCellPortCbsdAuthRegState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unregistered", 0),
          ("registered", 1))
    )


_TmnxCellPortCbsdAuthRegState_Type.__name__ = "Integer32"
_TmnxCellPortCbsdAuthRegState_Object = MibTableColumn
tmnxCellPortCbsdAuthRegState = _TmnxCellPortCbsdAuthRegState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 5),
    _TmnxCellPortCbsdAuthRegState_Type()
)
tmnxCellPortCbsdAuthRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthRegState.setStatus("current")


class _TmnxCellPortCbsdAuthGrantState_Type(Integer32):
    """Custom type tmnxCellPortCbsdAuthGrantState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("granted", 2),
          ("authorized", 3))
    )


_TmnxCellPortCbsdAuthGrantState_Type.__name__ = "Integer32"
_TmnxCellPortCbsdAuthGrantState_Object = MibTableColumn
tmnxCellPortCbsdAuthGrantState = _TmnxCellPortCbsdAuthGrantState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 6),
    _TmnxCellPortCbsdAuthGrantState_Type()
)
tmnxCellPortCbsdAuthGrantState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthGrantState.setStatus("current")
_TmnxCellPortCbsdAuthGrantExpTime_Type = DateAndTime
_TmnxCellPortCbsdAuthGrantExpTime_Object = MibTableColumn
tmnxCellPortCbsdAuthGrantExpTime = _TmnxCellPortCbsdAuthGrantExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 7),
    _TmnxCellPortCbsdAuthGrantExpTime_Type()
)
tmnxCellPortCbsdAuthGrantExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthGrantExpTime.setStatus("current")
_TmnxCellPortCbsdAuthTxExpTime_Type = DateAndTime
_TmnxCellPortCbsdAuthTxExpTime_Object = MibTableColumn
tmnxCellPortCbsdAuthTxExpTime = _TmnxCellPortCbsdAuthTxExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 8),
    _TmnxCellPortCbsdAuthTxExpTime_Type()
)
tmnxCellPortCbsdAuthTxExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthTxExpTime.setStatus("current")
_TmnxCellPortCbsdAuthHeartbeatInt_Type = Unsigned32
_TmnxCellPortCbsdAuthHeartbeatInt_Object = MibTableColumn
tmnxCellPortCbsdAuthHeartbeatInt = _TmnxCellPortCbsdAuthHeartbeatInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 9),
    _TmnxCellPortCbsdAuthHeartbeatInt_Type()
)
tmnxCellPortCbsdAuthHeartbeatInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthHeartbeatInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthHeartbeatInt.setUnits("seconds")


class _TmnxCellPortCbsdAuthChanType_Type(Integer32):
    """Custom type tmnxCellPortCbsdAuthChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gaa", 1),
          ("pal", 2))
    )


_TmnxCellPortCbsdAuthChanType_Type.__name__ = "Integer32"
_TmnxCellPortCbsdAuthChanType_Object = MibTableColumn
tmnxCellPortCbsdAuthChanType = _TmnxCellPortCbsdAuthChanType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 10),
    _TmnxCellPortCbsdAuthChanType_Type()
)
tmnxCellPortCbsdAuthChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthChanType.setStatus("current")


class _TmnxCellPortCbsdAuthCurSasSvr_Type(Integer32):
    """Custom type tmnxCellPortCbsdAuthCurSasSvr based on Integer32"""
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
          ("primary", 1),
          ("secondary", 2))
    )


_TmnxCellPortCbsdAuthCurSasSvr_Type.__name__ = "Integer32"
_TmnxCellPortCbsdAuthCurSasSvr_Object = MibTableColumn
tmnxCellPortCbsdAuthCurSasSvr = _TmnxCellPortCbsdAuthCurSasSvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 11),
    _TmnxCellPortCbsdAuthCurSasSvr_Type()
)
tmnxCellPortCbsdAuthCurSasSvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthCurSasSvr.setStatus("current")
_TmnxCellPortCbsdAuthCurSasSvrIpT_Type = InetAddressType
_TmnxCellPortCbsdAuthCurSasSvrIpT_Object = MibTableColumn
tmnxCellPortCbsdAuthCurSasSvrIpT = _TmnxCellPortCbsdAuthCurSasSvrIpT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 12),
    _TmnxCellPortCbsdAuthCurSasSvrIpT_Type()
)
tmnxCellPortCbsdAuthCurSasSvrIpT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthCurSasSvrIpT.setStatus("current")


class _TmnxCellPortCbsdAuthCurSasSvrIp_Type(InetAddress):
    """Custom type tmnxCellPortCbsdAuthCurSasSvrIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxCellPortCbsdAuthCurSasSvrIp_Type.__name__ = "InetAddress"
_TmnxCellPortCbsdAuthCurSasSvrIp_Object = MibTableColumn
tmnxCellPortCbsdAuthCurSasSvrIp = _TmnxCellPortCbsdAuthCurSasSvrIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 13),
    _TmnxCellPortCbsdAuthCurSasSvrIp_Type()
)
tmnxCellPortCbsdAuthCurSasSvrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthCurSasSvrIp.setStatus("current")
_TmnxCellPortCbsdAuthRegRequest_Type = Unsigned32
_TmnxCellPortCbsdAuthRegRequest_Object = MibTableColumn
tmnxCellPortCbsdAuthRegRequest = _TmnxCellPortCbsdAuthRegRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 14),
    _TmnxCellPortCbsdAuthRegRequest_Type()
)
tmnxCellPortCbsdAuthRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthRegRequest.setStatus("current")
_TmnxCellPortCbsdAuthRegRspSuc_Type = Unsigned32
_TmnxCellPortCbsdAuthRegRspSuc_Object = MibTableColumn
tmnxCellPortCbsdAuthRegRspSuc = _TmnxCellPortCbsdAuthRegRspSuc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 15),
    _TmnxCellPortCbsdAuthRegRspSuc_Type()
)
tmnxCellPortCbsdAuthRegRspSuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthRegRspSuc.setStatus("current")
_TmnxCellPortCbsdAuthRegRspFail_Type = Unsigned32
_TmnxCellPortCbsdAuthRegRspFail_Object = MibTableColumn
tmnxCellPortCbsdAuthRegRspFail = _TmnxCellPortCbsdAuthRegRspFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 16),
    _TmnxCellPortCbsdAuthRegRspFail_Type()
)
tmnxCellPortCbsdAuthRegRspFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthRegRspFail.setStatus("current")
_TmnxCellPortCbsdAuthGrantRequest_Type = Unsigned32
_TmnxCellPortCbsdAuthGrantRequest_Object = MibTableColumn
tmnxCellPortCbsdAuthGrantRequest = _TmnxCellPortCbsdAuthGrantRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 17),
    _TmnxCellPortCbsdAuthGrantRequest_Type()
)
tmnxCellPortCbsdAuthGrantRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthGrantRequest.setStatus("current")
_TmnxCellPortCbsdAuthGrantRspSuc_Type = Unsigned32
_TmnxCellPortCbsdAuthGrantRspSuc_Object = MibTableColumn
tmnxCellPortCbsdAuthGrantRspSuc = _TmnxCellPortCbsdAuthGrantRspSuc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 18),
    _TmnxCellPortCbsdAuthGrantRspSuc_Type()
)
tmnxCellPortCbsdAuthGrantRspSuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthGrantRspSuc.setStatus("current")
_TmnxCellPortCbsdAuthGrantRspFail_Type = Unsigned32
_TmnxCellPortCbsdAuthGrantRspFail_Object = MibTableColumn
tmnxCellPortCbsdAuthGrantRspFail = _TmnxCellPortCbsdAuthGrantRspFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 19),
    _TmnxCellPortCbsdAuthGrantRspFail_Type()
)
tmnxCellPortCbsdAuthGrantRspFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthGrantRspFail.setStatus("current")
_TmnxCellPortCbsdAuthHrtbtRequest_Type = Unsigned32
_TmnxCellPortCbsdAuthHrtbtRequest_Object = MibTableColumn
tmnxCellPortCbsdAuthHrtbtRequest = _TmnxCellPortCbsdAuthHrtbtRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 20),
    _TmnxCellPortCbsdAuthHrtbtRequest_Type()
)
tmnxCellPortCbsdAuthHrtbtRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthHrtbtRequest.setStatus("current")
_TmnxCellPortCbsdAuthHrtbtRspSuc_Type = Unsigned32
_TmnxCellPortCbsdAuthHrtbtRspSuc_Object = MibTableColumn
tmnxCellPortCbsdAuthHrtbtRspSuc = _TmnxCellPortCbsdAuthHrtbtRspSuc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 21),
    _TmnxCellPortCbsdAuthHrtbtRspSuc_Type()
)
tmnxCellPortCbsdAuthHrtbtRspSuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthHrtbtRspSuc.setStatus("current")
_TmnxCellPortCbsdAuthHrtbtRspFail_Type = Unsigned32
_TmnxCellPortCbsdAuthHrtbtRspFail_Object = MibTableColumn
tmnxCellPortCbsdAuthHrtbtRspFail = _TmnxCellPortCbsdAuthHrtbtRspFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 3, 1, 7, 1, 22),
    _TmnxCellPortCbsdAuthHrtbtRspFail_Type()
)
tmnxCellPortCbsdAuthHrtbtRspFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthHrtbtRspFail.setStatus("current")
_TmnxCellularNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxCellularNotifyObjects = _TmnxCellularNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 4)
)
_TmnxCellularNotifyPdnId_Type = TmnxCellularPdnId
_TmnxCellularNotifyPdnId_Object = MibScalar
tmnxCellularNotifyPdnId = _TmnxCellularNotifyPdnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 4, 1),
    _TmnxCellularNotifyPdnId_Type()
)
tmnxCellularNotifyPdnId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCellularNotifyPdnId.setStatus("current")


class _TmnxCellMdaNoServiceResetReason_Type(Integer32):
    """Custom type tmnxCellMdaNoServiceResetReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cellular-port-down", 1),
          ("no-bgp-neighbor", 2))
    )


_TmnxCellMdaNoServiceResetReason_Type.__name__ = "Integer32"
_TmnxCellMdaNoServiceResetReason_Object = MibScalar
tmnxCellMdaNoServiceResetReason = _TmnxCellMdaNoServiceResetReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 4, 2),
    _TmnxCellMdaNoServiceResetReason_Type()
)
tmnxCellMdaNoServiceResetReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCellMdaNoServiceResetReason.setStatus("current")


class _TmnxCellCbsdAuthFailReason_Type(DisplayString):
    """Custom type tmnxCellCbsdAuthFailReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TmnxCellCbsdAuthFailReason_Type.__name__ = "DisplayString"
_TmnxCellCbsdAuthFailReason_Object = MibScalar
tmnxCellCbsdAuthFailReason = _TmnxCellCbsdAuthFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 4, 3),
    _TmnxCellCbsdAuthFailReason_Type()
)
tmnxCellCbsdAuthFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCellCbsdAuthFailReason.setStatus("current")


class _TmnxCellCbsdAuthRespCode_Type(DisplayString):
    """Custom type tmnxCellCbsdAuthRespCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TmnxCellCbsdAuthRespCode_Type.__name__ = "DisplayString"
_TmnxCellCbsdAuthRespCode_Object = MibScalar
tmnxCellCbsdAuthRespCode = _TmnxCellCbsdAuthRespCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 4, 4),
    _TmnxCellCbsdAuthRespCode_Type()
)
tmnxCellCbsdAuthRespCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCellCbsdAuthRespCode.setStatus("current")


class _TmnxCellCbsdAuthPrevTransState_Type(Integer32):
    """Custom type tmnxCellCbsdAuthPrevTransState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("authorized", 2),
          ("granted", 3))
    )


_TmnxCellCbsdAuthPrevTransState_Type.__name__ = "Integer32"
_TmnxCellCbsdAuthPrevTransState_Object = MibScalar
tmnxCellCbsdAuthPrevTransState = _TmnxCellCbsdAuthPrevTransState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 4, 5),
    _TmnxCellCbsdAuthPrevTransState_Type()
)
tmnxCellCbsdAuthPrevTransState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCellCbsdAuthPrevTransState.setStatus("current")


class _TmnxCellCbsdAuthNewTransState_Type(Integer32):
    """Custom type tmnxCellCbsdAuthNewTransState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("authorized", 2),
          ("granted", 3))
    )


_TmnxCellCbsdAuthNewTransState_Type.__name__ = "Integer32"
_TmnxCellCbsdAuthNewTransState_Object = MibScalar
tmnxCellCbsdAuthNewTransState = _TmnxCellCbsdAuthNewTransState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 109, 4, 6),
    _TmnxCellCbsdAuthNewTransState_Type()
)
tmnxCellCbsdAuthNewTransState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCellCbsdAuthNewTransState.setStatus("current")
_TmnxCellularNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxCellularNotifyPrefix = _TmnxCellularNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109)
)
_TmnxCellularNotifications_ObjectIdentity = ObjectIdentity
tmnxCellularNotifications = _TmnxCellularNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0)
)
tmnxCellularPortEntry.registerAugmentions(
    ("TIMETRA-CELLULAR-MIB",
     "tmnxCellPortCbsdAuthCfgEntry")
)
tmnxCellPortCbsdAuthCfgEntry.setIndexNames(*tmnxCellularPortEntry.getIndexNames())
tmnxCellularSimCardEntry.registerAugmentions(
    ("TIMETRA-CELLULAR-MIB",
     "tmnxCellularSimCardStatusEntry")
)
tmnxCellularSimCardStatusEntry.setIndexNames(*tmnxCellularSimCardEntry.getIndexNames())
tmnxCellularPdnEntry.registerAugmentions(
    ("TIMETRA-CELLULAR-MIB",
     "tmnxCellularPdnStatusEntry")
)
tmnxCellularPdnStatusEntry.setIndexNames(*tmnxCellularPdnEntry.getIndexNames())
tmnxCellPortCbsdAuthCfgEntry.registerAugmentions(
    ("TIMETRA-CELLULAR-MIB",
     "tmnxCellPortCbsdAuthStatsEntry")
)
tmnxCellPortCbsdAuthStatsEntry.setIndexNames(*tmnxCellPortCbsdAuthCfgEntry.getIndexNames())

# Managed Objects groups

tmnxCellularConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 1, 1)
)
tmnxCellularConfigGroup.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfileTblLastChanged"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfRowStatus"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfLastChanged"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfDescription"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfApn"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfAuthType"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfUsername"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfPassword"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardTableLastChanged"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardLastChanged"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardDescription"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardPin"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnTblLastChanged"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnRowStatus"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnLastChanged"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfile"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortTblLastChanged"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortLastChanged"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortBand125MaxPowerLevel"))
)
if mibBuilder.loadTexts:
    tmnxCellularConfigGroup.setStatus("current")

tmnxCellularStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 1, 2)
)
tmnxCellularStatusGroup.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortImei"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortRegistrationStatus"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortWirelessTechnology"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortFrequencyBand"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortChannelNumber"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortAreaCode"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCellIdentity"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortRssi"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortRsrp"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortRscp"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardEquipped"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardIccid"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardImsi"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardLocked"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardPinStatus"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardPinRetries"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardPukRetries"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnConnectionState"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnIpAddrType"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnIpAddress"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnPrimaryDnsAddrType"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnPrimaryDnsAddress"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnSecondaryDnsAddrType"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnSecondaryDnsAddress"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnApn"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnMtu"))
)
if mibBuilder.loadTexts:
    tmnxCellularStatusGroup.setStatus("current")

tmnxCellularV16v0ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 2, 1)
)
tmnxCellularV16v0ConfigGroup.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellMdaLastChanged"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaAdminActiveSim"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaDownResetInterval"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaDownResetCriteria"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaDownResetPending"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaDownResetTime"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardFailureDuration"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardPortStateSwitch"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardBgpStateSwitch"))
)
if mibBuilder.loadTexts:
    tmnxCellularV16v0ConfigGroup.setStatus("current")

tmnxCellularV16v0StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 2, 2)
)
tmnxCellularV16v0StatusGroup.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerType"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerQci"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerUlGbr"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerUlMbr"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerDlGbr"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerDlMbr"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortTftPacketFilterId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortTftEvalPrecedence"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortTftDirection"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortTftTos"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortTftTosMask"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellSimCardFirmwareVersion"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaPreferredSim"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaOperActiveSim"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaSimCardSwitchPending"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaSimCardSwitchTime"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaSimCardLastSwitchTime"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaSimLastSwitchReason"))
)
if mibBuilder.loadTexts:
    tmnxCellularV16v0StatusGroup.setStatus("current")

tmnxCellularNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 2, 3)
)
tmnxCellularNotifyObjsGroup.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellularNotifyPdnId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaNoServiceResetReason"))
)
if mibBuilder.loadTexts:
    tmnxCellularNotifyObjsGroup.setStatus("current")

tmnxCellularV19ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 3, 1)
)
tmnxCellularV19ConfigGroup.setObjects(
    ("TIMETRA-CELLULAR-MIB", "tmnxCellPdnProfProtocol")
)
if mibBuilder.loadTexts:
    tmnxCellularV19ConfigGroup.setStatus("current")

tmnxCellularV20ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 4, 1)
)
tmnxCellularV20ConfigGroup.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellMdaSpecFirmwareVersion"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaMaxTxPower"))
)
if mibBuilder.loadTexts:
    tmnxCellularV20ConfigGroup.setStatus("current")

tmnxCellPortCbsdAuthGroupV21 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 5, 1)
)
tmnxCellPortCbsdAuthGroupV21.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthCfgTblLstChg"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthCfgLstChange"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthAdminState"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthUserId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthAntennaGain"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthClntTlsProf"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthPriSasSvrUrl"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthSecSasSvrUrl"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthOperState"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthCategory"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthFccId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthRegState"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantState"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantExpTime"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthTxExpTime"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthHeartbeatInt"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthChanType"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthCurSasSvr"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthCurSasSvrIp"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthCurSasSvrIpT"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthRegRequest"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthRegRspSuc"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthRegRspFail"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantRequest"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantRspSuc"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantRspFail"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthHrtbtRequest"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthHrtbtRspSuc"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthHrtbtRspFail"))
)
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthGroupV21.setStatus("current")

tmnxCellularNotifyObjsGroupV21 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 5, 2)
)
tmnxCellularNotifyObjsGroupV21.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellCbsdAuthFailReason"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellCbsdAuthRespCode"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellCbsdAuthPrevTransState"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellCbsdAuthNewTransState"))
)
if mibBuilder.loadTexts:
    tmnxCellularNotifyObjsGroupV21.setStatus("current")

tmnxCellularStatusGroupV21 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 5, 4)
)
tmnxCellularStatusGroupV21.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortRsrq"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortSinr"))
)
if mibBuilder.loadTexts:
    tmnxCellularStatusGroupV21.setStatus("current")

tmnxCellularConfigGroupV21 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 5, 5)
)
tmnxCellularConfigGroupV21.setObjects(
    ("TIMETRA-CELLULAR-MIB", "tmnxCellPortSyncSysTime")
)
if mibBuilder.loadTexts:
    tmnxCellularConfigGroupV21.setStatus("current")


# Notification objects

tmnxCellularBearerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0, 1)
)
tmnxCellularBearerCreated.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellularNotifyPdnId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerId"))
)
if mibBuilder.loadTexts:
    tmnxCellularBearerCreated.setStatus(
        "current"
    )

tmnxCellularBearerDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0, 2)
)
tmnxCellularBearerDeleted.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellularNotifyPdnId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerId"))
)
if mibBuilder.loadTexts:
    tmnxCellularBearerDeleted.setStatus(
        "current"
    )

tmnxCellularBearerModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0, 3)
)
tmnxCellularBearerModified.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellularNotifyPdnId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortBearerId"))
)
if mibBuilder.loadTexts:
    tmnxCellularBearerModified.setStatus(
        "current"
    )

tmnxCellularNoServiceReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0, 4)
)
tmnxCellularNoServiceReset.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaNoServiceResetReason"))
)
if mibBuilder.loadTexts:
    tmnxCellularNoServiceReset.setStatus(
        "current"
    )

tmnxCellularActiveSimChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0, 5)
)
tmnxCellularActiveSimChange.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellMdaAdminActiveSim"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaOperActiveSim"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellMdaSimLastSwitchReason"))
)
if mibBuilder.loadTexts:
    tmnxCellularActiveSimChange.setStatus(
        "current"
    )

tmnxCellPortCbsdRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0, 6)
)
tmnxCellPortCbsdRegistered.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthCurSasSvrIp"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthCurSasSvrIpT"))
)
if mibBuilder.loadTexts:
    tmnxCellPortCbsdRegistered.setStatus(
        "current"
    )

tmnxCellPortCbsdUnregistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0, 7)
)
tmnxCellPortCbsdUnregistered.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellCbsdAuthFailReason"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellCbsdAuthRespCode"))
)
if mibBuilder.loadTexts:
    tmnxCellPortCbsdUnregistered.setStatus(
        "current"
    )

tmnxCellPortCbsdGranted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0, 8)
)
tmnxCellPortCbsdGranted.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantExpTime"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthHeartbeatInt"))
)
if mibBuilder.loadTexts:
    tmnxCellPortCbsdGranted.setStatus(
        "current"
    )

tmnxCellPortCbsdAuthorized = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0, 9)
)
tmnxCellPortCbsdAuthorized.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantExpTime"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthHeartbeatInt"))
)
if mibBuilder.loadTexts:
    tmnxCellPortCbsdAuthorized.setStatus(
        "current"
    )

tmnxCellPortCbsdTransDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 109, 0, 10)
)
tmnxCellPortCbsdTransDown.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGrantId"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellCbsdAuthPrevTransState"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellCbsdAuthNewTransState"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellCbsdAuthFailReason"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellCbsdAuthRespCode"))
)
if mibBuilder.loadTexts:
    tmnxCellPortCbsdTransDown.setStatus(
        "current"
    )


# Notifications groups

tmnxCellNotificationV16v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 2, 4)
)
tmnxCellNotificationV16v0Group.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellularBearerCreated"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellularBearerDeleted"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellularBearerModified"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellularNoServiceReset"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellularActiveSimChange"))
)
if mibBuilder.loadTexts:
    tmnxCellNotificationV16v0Group.setStatus(
        "current"
    )

tmnxCellNotificationGroupV21 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 2, 5, 3)
)
tmnxCellNotificationGroupV21.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdRegistered"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdUnregistered"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdGranted"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthorized"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdTransDown"))
)
if mibBuilder.loadTexts:
    tmnxCellNotificationGroupV21.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxCellularCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 1, 1)
)
tmnxCellularCompliance.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellularConfigGroup"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellularStatusGroup"))
)
if mibBuilder.loadTexts:
    tmnxCellularCompliance.setStatus(
        "current"
    )

tmnxCellularComplianceV16v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 1, 2)
)
tmnxCellularComplianceV16v0.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellularV16v0ConfigGroup"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellularV16v0StatusGroup"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellNotificationV16v0Group"))
)
if mibBuilder.loadTexts:
    tmnxCellularComplianceV16v0.setStatus(
        "current"
    )

tmnxCellularComplianceV19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 1, 3)
)
tmnxCellularComplianceV19.setObjects(
    ("TIMETRA-CELLULAR-MIB", "tmnxCellularV19ConfigGroup")
)
if mibBuilder.loadTexts:
    tmnxCellularComplianceV19.setStatus(
        "current"
    )

tmnxCellularComplianceV20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 1, 4)
)
tmnxCellularComplianceV20.setObjects(
    ("TIMETRA-CELLULAR-MIB", "tmnxCellularV20ConfigGroup")
)
if mibBuilder.loadTexts:
    tmnxCellularComplianceV20.setStatus(
        "current"
    )

tmnxCellularComplianceV21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 109, 1, 5)
)
tmnxCellularComplianceV21.setObjects(
      *(("TIMETRA-CELLULAR-MIB", "tmnxCellPortCbsdAuthGroupV21"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellularNotifyObjsGroupV21"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellNotificationGroupV21"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellularStatusGroupV21"),
        ("TIMETRA-CELLULAR-MIB", "tmnxCellularConfigGroupV21"))
)
if mibBuilder.loadTexts:
    tmnxCellularComplianceV21.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-CELLULAR-MIB",
    **{"TmnxCellularPdnProfileId": TmnxCellularPdnProfileId,
       "TmnxCellularAccessPointName": TmnxCellularAccessPointName,
       "TmnxCellularImei": TmnxCellularImei,
       "TmnxCellularSimCardNumber": TmnxCellularSimCardNumber,
       "TmnxCellularSimCardIccid": TmnxCellularSimCardIccid,
       "TmnxCellularImsi": TmnxCellularImsi,
       "TmnxCellularPdnId": TmnxCellularPdnId,
       "TmnxCellularChannelNumber": TmnxCellularChannelNumber,
       "TmnxCellularBearerRate": TmnxCellularBearerRate,
       "timetraCellularMIBModule": timetraCellularMIBModule,
       "tmnxCellularConformance": tmnxCellularConformance,
       "tmnxCellularCompliances": tmnxCellularCompliances,
       "tmnxCellularCompliance": tmnxCellularCompliance,
       "tmnxCellularComplianceV16v0": tmnxCellularComplianceV16v0,
       "tmnxCellularComplianceV19": tmnxCellularComplianceV19,
       "tmnxCellularComplianceV20": tmnxCellularComplianceV20,
       "tmnxCellularComplianceV21": tmnxCellularComplianceV21,
       "tmnxCellularGroups": tmnxCellularGroups,
       "tmnxCellularV15v0Groups": tmnxCellularV15v0Groups,
       "tmnxCellularConfigGroup": tmnxCellularConfigGroup,
       "tmnxCellularStatusGroup": tmnxCellularStatusGroup,
       "tmnxCellularV16v0Groups": tmnxCellularV16v0Groups,
       "tmnxCellularV16v0ConfigGroup": tmnxCellularV16v0ConfigGroup,
       "tmnxCellularV16v0StatusGroup": tmnxCellularV16v0StatusGroup,
       "tmnxCellularNotifyObjsGroup": tmnxCellularNotifyObjsGroup,
       "tmnxCellNotificationV16v0Group": tmnxCellNotificationV16v0Group,
       "tmnxCellularV19Groups": tmnxCellularV19Groups,
       "tmnxCellularV19ConfigGroup": tmnxCellularV19ConfigGroup,
       "tmnxCellularV20Groups": tmnxCellularV20Groups,
       "tmnxCellularV20ConfigGroup": tmnxCellularV20ConfigGroup,
       "tmnxCellularV21Groups": tmnxCellularV21Groups,
       "tmnxCellPortCbsdAuthGroupV21": tmnxCellPortCbsdAuthGroupV21,
       "tmnxCellularNotifyObjsGroupV21": tmnxCellularNotifyObjsGroupV21,
       "tmnxCellNotificationGroupV21": tmnxCellNotificationGroupV21,
       "tmnxCellularStatusGroupV21": tmnxCellularStatusGroupV21,
       "tmnxCellularConfigGroupV21": tmnxCellularConfigGroupV21,
       "tmnxCellularObjs": tmnxCellularObjs,
       "tmnxCellularConfigObjs": tmnxCellularConfigObjs,
       "tmnxCellularConfigTimestamps": tmnxCellularConfigTimestamps,
       "tmnxCellPdnProfileTblLastChanged": tmnxCellPdnProfileTblLastChanged,
       "tmnxCellSimCardTableLastChanged": tmnxCellSimCardTableLastChanged,
       "tmnxCellPdnTblLastChanged": tmnxCellPdnTblLastChanged,
       "tmnxCellPortTblLastChanged": tmnxCellPortTblLastChanged,
       "tmnxCellPortCbsdAuthCfgTblLstChg": tmnxCellPortCbsdAuthCfgTblLstChg,
       "tmnxCellularSystemConfigObjs": tmnxCellularSystemConfigObjs,
       "tmnxCellularPdnProfileTable": tmnxCellularPdnProfileTable,
       "tmnxCellPdnProfileEntry": tmnxCellPdnProfileEntry,
       "tmnxCellPdnProfileId": tmnxCellPdnProfileId,
       "tmnxCellPdnProfRowStatus": tmnxCellPdnProfRowStatus,
       "tmnxCellPdnProfLastChanged": tmnxCellPdnProfLastChanged,
       "tmnxCellPdnProfDescription": tmnxCellPdnProfDescription,
       "tmnxCellPdnProfApn": tmnxCellPdnProfApn,
       "tmnxCellPdnProfAuthType": tmnxCellPdnProfAuthType,
       "tmnxCellPdnProfUsername": tmnxCellPdnProfUsername,
       "tmnxCellPdnProfPassword": tmnxCellPdnProfPassword,
       "tmnxCellPdnProfProtocol": tmnxCellPdnProfProtocol,
       "tmnxCellularPortConfigObjs": tmnxCellularPortConfigObjs,
       "tmnxCellularSimCardTable": tmnxCellularSimCardTable,
       "tmnxCellularSimCardEntry": tmnxCellularSimCardEntry,
       "tmnxCellSimCardId": tmnxCellSimCardId,
       "tmnxCellSimCardLastChanged": tmnxCellSimCardLastChanged,
       "tmnxCellSimCardDescription": tmnxCellSimCardDescription,
       "tmnxCellSimCardPin": tmnxCellSimCardPin,
       "tmnxCellSimCardFailureDuration": tmnxCellSimCardFailureDuration,
       "tmnxCellSimCardPortStateSwitch": tmnxCellSimCardPortStateSwitch,
       "tmnxCellSimCardBgpStateSwitch": tmnxCellSimCardBgpStateSwitch,
       "tmnxCellularPdnTable": tmnxCellularPdnTable,
       "tmnxCellularPdnEntry": tmnxCellularPdnEntry,
       "tmnxCellPdnId": tmnxCellPdnId,
       "tmnxCellPdnRowStatus": tmnxCellPdnRowStatus,
       "tmnxCellPdnLastChanged": tmnxCellPdnLastChanged,
       "tmnxCellPdnProfile": tmnxCellPdnProfile,
       "tmnxCellularPortTable": tmnxCellularPortTable,
       "tmnxCellularPortEntry": tmnxCellularPortEntry,
       "tmnxCellPortLastChanged": tmnxCellPortLastChanged,
       "tmnxCellPortBand125MaxPowerLevel": tmnxCellPortBand125MaxPowerLevel,
       "tmnxCellPortSyncSysTime": tmnxCellPortSyncSysTime,
       "tmnxCellularMdaTable": tmnxCellularMdaTable,
       "tmnxCellularMdaEntry": tmnxCellularMdaEntry,
       "tmnxCellMdaLastChanged": tmnxCellMdaLastChanged,
       "tmnxCellMdaAdminActiveSim": tmnxCellMdaAdminActiveSim,
       "tmnxCellMdaDownResetInterval": tmnxCellMdaDownResetInterval,
       "tmnxCellMdaDownResetCriteria": tmnxCellMdaDownResetCriteria,
       "tmnxCellMdaDownResetPending": tmnxCellMdaDownResetPending,
       "tmnxCellMdaDownResetTime": tmnxCellMdaDownResetTime,
       "tmnxCellMdaPreferredSim": tmnxCellMdaPreferredSim,
       "tmnxCellMdaOperActiveSim": tmnxCellMdaOperActiveSim,
       "tmnxCellMdaSimCardSwitchPending": tmnxCellMdaSimCardSwitchPending,
       "tmnxCellMdaSimCardSwitchTime": tmnxCellMdaSimCardSwitchTime,
       "tmnxCellMdaSimCardLastSwitchTime": tmnxCellMdaSimCardLastSwitchTime,
       "tmnxCellMdaSimLastSwitchReason": tmnxCellMdaSimLastSwitchReason,
       "tmnxCellMdaSpecFirmwareVersion": tmnxCellMdaSpecFirmwareVersion,
       "tmnxCellMdaMaxTxPower": tmnxCellMdaMaxTxPower,
       "tmnxCellPortCbsdAuthCfgTable": tmnxCellPortCbsdAuthCfgTable,
       "tmnxCellPortCbsdAuthCfgEntry": tmnxCellPortCbsdAuthCfgEntry,
       "tmnxCellPortCbsdAuthCfgLstChange": tmnxCellPortCbsdAuthCfgLstChange,
       "tmnxCellPortCbsdAuthAdminState": tmnxCellPortCbsdAuthAdminState,
       "tmnxCellPortCbsdAuthUserId": tmnxCellPortCbsdAuthUserId,
       "tmnxCellPortCbsdAuthAntennaGain": tmnxCellPortCbsdAuthAntennaGain,
       "tmnxCellPortCbsdAuthClntTlsProf": tmnxCellPortCbsdAuthClntTlsProf,
       "tmnxCellPortCbsdAuthPriSasSvrUrl": tmnxCellPortCbsdAuthPriSasSvrUrl,
       "tmnxCellPortCbsdAuthSecSasSvrUrl": tmnxCellPortCbsdAuthSecSasSvrUrl,
       "tmnxCellPortCbsdAuthCategory": tmnxCellPortCbsdAuthCategory,
       "tmnxCellularStatusObjs": tmnxCellularStatusObjs,
       "tmnxCellularPortStatusObjs": tmnxCellularPortStatusObjs,
       "tmnxCellularPortStatusTable": tmnxCellularPortStatusTable,
       "tmnxCellularPortStatusEntry": tmnxCellularPortStatusEntry,
       "tmnxCellPortImei": tmnxCellPortImei,
       "tmnxCellPortRegistrationStatus": tmnxCellPortRegistrationStatus,
       "tmnxCellPortWirelessTechnology": tmnxCellPortWirelessTechnology,
       "tmnxCellPortFrequencyBand": tmnxCellPortFrequencyBand,
       "tmnxCellPortChannelNumber": tmnxCellPortChannelNumber,
       "tmnxCellPortAreaCode": tmnxCellPortAreaCode,
       "tmnxCellPortCellIdentity": tmnxCellPortCellIdentity,
       "tmnxCellPortRssi": tmnxCellPortRssi,
       "tmnxCellPortRsrp": tmnxCellPortRsrp,
       "tmnxCellPortRscp": tmnxCellPortRscp,
       "tmnxCellPortRsrq": tmnxCellPortRsrq,
       "tmnxCellPortSinr": tmnxCellPortSinr,
       "tmnxCellularSimCardStatusTable": tmnxCellularSimCardStatusTable,
       "tmnxCellularSimCardStatusEntry": tmnxCellularSimCardStatusEntry,
       "tmnxCellSimCardEquipped": tmnxCellSimCardEquipped,
       "tmnxCellSimCardIccid": tmnxCellSimCardIccid,
       "tmnxCellSimCardImsi": tmnxCellSimCardImsi,
       "tmnxCellSimCardLocked": tmnxCellSimCardLocked,
       "tmnxCellSimCardPinStatus": tmnxCellSimCardPinStatus,
       "tmnxCellSimCardPinRetries": tmnxCellSimCardPinRetries,
       "tmnxCellSimCardPukRetries": tmnxCellSimCardPukRetries,
       "tmnxCellSimCardFirmwareVersion": tmnxCellSimCardFirmwareVersion,
       "tmnxCellularPdnStatusTable": tmnxCellularPdnStatusTable,
       "tmnxCellularPdnStatusEntry": tmnxCellularPdnStatusEntry,
       "tmnxCellPdnConnectionState": tmnxCellPdnConnectionState,
       "tmnxCellPdnIpAddrType": tmnxCellPdnIpAddrType,
       "tmnxCellPdnIpAddress": tmnxCellPdnIpAddress,
       "tmnxCellPdnPrimaryDnsAddrType": tmnxCellPdnPrimaryDnsAddrType,
       "tmnxCellPdnPrimaryDnsAddress": tmnxCellPdnPrimaryDnsAddress,
       "tmnxCellPdnSecondaryDnsAddrType": tmnxCellPdnSecondaryDnsAddrType,
       "tmnxCellPdnSecondaryDnsAddress": tmnxCellPdnSecondaryDnsAddress,
       "tmnxCellPdnApn": tmnxCellPdnApn,
       "tmnxCellPdnMtu": tmnxCellPdnMtu,
       "tmnxCellularPortBearerTable": tmnxCellularPortBearerTable,
       "tmnxCellularPortBearerEntry": tmnxCellularPortBearerEntry,
       "tmnxCellPortBearerId": tmnxCellPortBearerId,
       "tmnxCellPortBearerType": tmnxCellPortBearerType,
       "tmnxCellPortBearerQci": tmnxCellPortBearerQci,
       "tmnxCellPortBearerUlGbr": tmnxCellPortBearerUlGbr,
       "tmnxCellPortBearerUlMbr": tmnxCellPortBearerUlMbr,
       "tmnxCellPortBearerDlGbr": tmnxCellPortBearerDlGbr,
       "tmnxCellPortBearerDlMbr": tmnxCellPortBearerDlMbr,
       "tmnxCellularPortTftTable": tmnxCellularPortTftTable,
       "tmnxCellularPortTftEntry": tmnxCellularPortTftEntry,
       "tmnxCellPortTftPacketFilterId": tmnxCellPortTftPacketFilterId,
       "tmnxCellPortTftEvalPrecedence": tmnxCellPortTftEvalPrecedence,
       "tmnxCellPortTftDirection": tmnxCellPortTftDirection,
       "tmnxCellPortTftTos": tmnxCellPortTftTos,
       "tmnxCellPortTftTosMask": tmnxCellPortTftTosMask,
       "tmnxCellPortCbsdAuthStatsTable": tmnxCellPortCbsdAuthStatsTable,
       "tmnxCellPortCbsdAuthStatsEntry": tmnxCellPortCbsdAuthStatsEntry,
       "tmnxCellPortCbsdAuthOperState": tmnxCellPortCbsdAuthOperState,
       "tmnxCellPortCbsdAuthId": tmnxCellPortCbsdAuthId,
       "tmnxCellPortCbsdAuthGrantId": tmnxCellPortCbsdAuthGrantId,
       "tmnxCellPortCbsdAuthFccId": tmnxCellPortCbsdAuthFccId,
       "tmnxCellPortCbsdAuthRegState": tmnxCellPortCbsdAuthRegState,
       "tmnxCellPortCbsdAuthGrantState": tmnxCellPortCbsdAuthGrantState,
       "tmnxCellPortCbsdAuthGrantExpTime": tmnxCellPortCbsdAuthGrantExpTime,
       "tmnxCellPortCbsdAuthTxExpTime": tmnxCellPortCbsdAuthTxExpTime,
       "tmnxCellPortCbsdAuthHeartbeatInt": tmnxCellPortCbsdAuthHeartbeatInt,
       "tmnxCellPortCbsdAuthChanType": tmnxCellPortCbsdAuthChanType,
       "tmnxCellPortCbsdAuthCurSasSvr": tmnxCellPortCbsdAuthCurSasSvr,
       "tmnxCellPortCbsdAuthCurSasSvrIpT": tmnxCellPortCbsdAuthCurSasSvrIpT,
       "tmnxCellPortCbsdAuthCurSasSvrIp": tmnxCellPortCbsdAuthCurSasSvrIp,
       "tmnxCellPortCbsdAuthRegRequest": tmnxCellPortCbsdAuthRegRequest,
       "tmnxCellPortCbsdAuthRegRspSuc": tmnxCellPortCbsdAuthRegRspSuc,
       "tmnxCellPortCbsdAuthRegRspFail": tmnxCellPortCbsdAuthRegRspFail,
       "tmnxCellPortCbsdAuthGrantRequest": tmnxCellPortCbsdAuthGrantRequest,
       "tmnxCellPortCbsdAuthGrantRspSuc": tmnxCellPortCbsdAuthGrantRspSuc,
       "tmnxCellPortCbsdAuthGrantRspFail": tmnxCellPortCbsdAuthGrantRspFail,
       "tmnxCellPortCbsdAuthHrtbtRequest": tmnxCellPortCbsdAuthHrtbtRequest,
       "tmnxCellPortCbsdAuthHrtbtRspSuc": tmnxCellPortCbsdAuthHrtbtRspSuc,
       "tmnxCellPortCbsdAuthHrtbtRspFail": tmnxCellPortCbsdAuthHrtbtRspFail,
       "tmnxCellularNotifyObjects": tmnxCellularNotifyObjects,
       "tmnxCellularNotifyPdnId": tmnxCellularNotifyPdnId,
       "tmnxCellMdaNoServiceResetReason": tmnxCellMdaNoServiceResetReason,
       "tmnxCellCbsdAuthFailReason": tmnxCellCbsdAuthFailReason,
       "tmnxCellCbsdAuthRespCode": tmnxCellCbsdAuthRespCode,
       "tmnxCellCbsdAuthPrevTransState": tmnxCellCbsdAuthPrevTransState,
       "tmnxCellCbsdAuthNewTransState": tmnxCellCbsdAuthNewTransState,
       "tmnxCellularNotifyPrefix": tmnxCellularNotifyPrefix,
       "tmnxCellularNotifications": tmnxCellularNotifications,
       "tmnxCellularBearerCreated": tmnxCellularBearerCreated,
       "tmnxCellularBearerDeleted": tmnxCellularBearerDeleted,
       "tmnxCellularBearerModified": tmnxCellularBearerModified,
       "tmnxCellularNoServiceReset": tmnxCellularNoServiceReset,
       "tmnxCellularActiveSimChange": tmnxCellularActiveSimChange,
       "tmnxCellPortCbsdRegistered": tmnxCellPortCbsdRegistered,
       "tmnxCellPortCbsdUnregistered": tmnxCellPortCbsdUnregistered,
       "tmnxCellPortCbsdGranted": tmnxCellPortCbsdGranted,
       "tmnxCellPortCbsdAuthorized": tmnxCellPortCbsdAuthorized,
       "tmnxCellPortCbsdTransDown": tmnxCellPortCbsdTransDown}
)
