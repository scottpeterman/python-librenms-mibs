# SNMP MIB module (CDATA-GPON-MIB2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\CDATA-GPON-MIB2
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:48 2025
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

(gpon,) = mibBuilder.importSymbols(
    "CDATA-COMMON-SMI",
    "gpon")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(authenticationFailure,
 coldStart,
 snmpBasicCompliance,
 snmpBasicNotificationsGroup,
 snmpCommunityGroup,
 snmpEnableAuthenTraps,
 snmpGroup,
 snmpInASNParseErrs,
 snmpInBadCommunityNames,
 snmpInBadCommunityUses,
 snmpInBadValues,
 snmpInBadVersions,
 snmpInGenErrs,
 snmpInGetNexts,
 snmpInGetRequests,
 snmpInGetResponses,
 snmpInNoSuchNames,
 snmpInPkts,
 snmpInReadOnlys,
 snmpInSetRequests,
 snmpInTooBigs,
 snmpInTotalReqVars,
 snmpInTotalSetVars,
 snmpInTraps,
 snmpObsoleteGroup,
 snmpOutBadValues,
 snmpOutGenErrs,
 snmpOutGetNexts,
 snmpOutGetRequests,
 snmpOutGetResponses,
 snmpOutNoSuchNames,
 snmpOutPkts,
 snmpOutSetRequests,
 snmpOutTooBigs,
 snmpOutTraps,
 snmpProxyDrops,
 snmpSetGroup,
 snmpSetSerialNo,
 snmpSilentDrops,
 snmpTrapEnterprise,
 snmpTrapOID,
 sysContact,
 sysDescr,
 sysLocation,
 sysName,
 sysORDescr,
 sysORID,
 sysORIndex,
 sysORLastChange,
 sysORUpTime,
 sysObjectID,
 sysServices,
 sysUpTime,
 systemGroup,
 warmStart) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "authenticationFailure",
    "coldStart",
    "snmpBasicCompliance",
    "snmpBasicNotificationsGroup",
    "snmpCommunityGroup",
    "snmpEnableAuthenTraps",
    "snmpGroup",
    "snmpInASNParseErrs",
    "snmpInBadCommunityNames",
    "snmpInBadCommunityUses",
    "snmpInBadValues",
    "snmpInBadVersions",
    "snmpInGenErrs",
    "snmpInGetNexts",
    "snmpInGetRequests",
    "snmpInGetResponses",
    "snmpInNoSuchNames",
    "snmpInPkts",
    "snmpInReadOnlys",
    "snmpInSetRequests",
    "snmpInTooBigs",
    "snmpInTotalReqVars",
    "snmpInTotalSetVars",
    "snmpInTraps",
    "snmpObsoleteGroup",
    "snmpOutBadValues",
    "snmpOutGenErrs",
    "snmpOutGetNexts",
    "snmpOutGetRequests",
    "snmpOutGetResponses",
    "snmpOutNoSuchNames",
    "snmpOutPkts",
    "snmpOutSetRequests",
    "snmpOutTooBigs",
    "snmpOutTraps",
    "snmpProxyDrops",
    "snmpSetGroup",
    "snmpSetSerialNo",
    "snmpSilentDrops",
    "snmpTrapEnterprise",
    "snmpTrapOID",
    "sysContact",
    "sysDescr",
    "sysLocation",
    "sysName",
    "sysORDescr",
    "sysORID",
    "sysORIndex",
    "sysORLastChange",
    "sysORUpTime",
    "sysObjectID",
    "sysServices",
    "sysUpTime",
    "systemGroup",
    "warmStart")

(Bits,
 Bits,
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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

gponMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class GponDbaProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
        ValueRangeConstraint(65535, 65535),
    )



class GponDbaProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class GponLinePorfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )



class GponLinePorfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class GponLinePorfileTcontId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
        ValueRangeConstraint(65535, 65535),
    )



class GponLinePorfileGemId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )



class GponLinePorfileGemMapId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class GponVlanPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class GponSrvProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )



class GponSrvProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class GponVlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class GponTrafficProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )



class GponTrafficProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class GponSipAgentProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(65535, 65535),
    )



class GponSipAgentProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class GponSipUri(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class GponSipRightFlagProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(65535, 65535),
    )



class GponSipRightFlagProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class GponDigitMapProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(65535, 65535),
    )



class GponPotsProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(65535, 65535),
    )



class GponDeviceId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class GponCardId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )



class GponOltPortId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class GponSwitch(TextualConvention, Integer32):
    status = "current"
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



class GponOltAutoAuthRuleId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )



class GponOnuId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class GponOnuSn(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12



class GponOnuPassword(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )



class GponOnuLoid(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )



class GponOnuLoidPassword(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )



class GponOnuEthPortId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class GponMac(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class GponOnuPotsPortId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



# MIB Managed Objects in the order of their OIDs

_GponObjects_ObjectIdentity = ObjectIdentity
gponObjects = _GponObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1)
)
_GponProfileObjects_ObjectIdentity = ObjectIdentity
gponProfileObjects = _GponProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1)
)
_GponDbaProfileObjects_ObjectIdentity = ObjectIdentity
gponDbaProfileObjects = _GponDbaProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2)
)
_GponDbaProfileInfoTable_Object = MibTable
gponDbaProfileInfoTable = _GponDbaProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    gponDbaProfileInfoTable.setStatus("current")
_GponDbaProfileInfoEntry_Object = MibTableRow
gponDbaProfileInfoEntry = _GponDbaProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 1, 1)
)
gponDbaProfileInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponDbaProfileId"),
)
if mibBuilder.loadTexts:
    gponDbaProfileInfoEntry.setStatus("current")
_GponDbaProfileId_Type = GponDbaProfileId
_GponDbaProfileId_Object = MibTableColumn
gponDbaProfileId = _GponDbaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 1, 1, 1),
    _GponDbaProfileId_Type()
)
gponDbaProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponDbaProfileId.setStatus("current")
_GponDbaProfileRowStatus_Type = RowStatus
_GponDbaProfileRowStatus_Object = MibTableColumn
gponDbaProfileRowStatus = _GponDbaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 1, 1, 2),
    _GponDbaProfileRowStatus_Type()
)
gponDbaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponDbaProfileRowStatus.setStatus("current")
_GponDbaProfileName_Type = GponDbaProfileName
_GponDbaProfileName_Object = MibTableColumn
gponDbaProfileName = _GponDbaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 1, 1, 3),
    _GponDbaProfileName_Type()
)
gponDbaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponDbaProfileName.setStatus("current")
_GponDbaProfileBindNum_Type = Integer32
_GponDbaProfileBindNum_Object = MibTableColumn
gponDbaProfileBindNum = _GponDbaProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 1, 1, 4),
    _GponDbaProfileBindNum_Type()
)
gponDbaProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponDbaProfileBindNum.setStatus("current")
_GponDbaProfileCfgTable_Object = MibTable
gponDbaProfileCfgTable = _GponDbaProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    gponDbaProfileCfgTable.setStatus("current")
_GponDbaProfileCfgEntry_Object = MibTableRow
gponDbaProfileCfgEntry = _GponDbaProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 2, 1)
)
gponDbaProfileCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponDbaProfileId"),
)
if mibBuilder.loadTexts:
    gponDbaProfileCfgEntry.setStatus("current")


class _GponDbaProfileType_Type(Integer32):
    """Custom type gponDbaProfileType based on Integer32"""
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
        *(("fix", 1),
          ("assure", 2),
          ("assureAndMax", 3),
          ("max", 4),
          ("fixAndAssureAndMax", 5))
    )


_GponDbaProfileType_Type.__name__ = "Integer32"
_GponDbaProfileType_Object = MibTableColumn
gponDbaProfileType = _GponDbaProfileType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 2, 1, 1),
    _GponDbaProfileType_Type()
)
gponDbaProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDbaProfileType.setStatus("current")


class _GponDbaProfileFixRate_Type(Integer32):
    """Custom type gponDbaProfileFixRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 1060864),
    )


_GponDbaProfileFixRate_Type.__name__ = "Integer32"
_GponDbaProfileFixRate_Object = MibTableColumn
gponDbaProfileFixRate = _GponDbaProfileFixRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 2, 1, 2),
    _GponDbaProfileFixRate_Type()
)
gponDbaProfileFixRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDbaProfileFixRate.setStatus("current")
if mibBuilder.loadTexts:
    gponDbaProfileFixRate.setUnits("kbps")


class _GponDbaProfileAssureRate_Type(Integer32):
    """Custom type gponDbaProfileAssureRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(256, 1060864),
    )


_GponDbaProfileAssureRate_Type.__name__ = "Integer32"
_GponDbaProfileAssureRate_Object = MibTableColumn
gponDbaProfileAssureRate = _GponDbaProfileAssureRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 2, 1, 3),
    _GponDbaProfileAssureRate_Type()
)
gponDbaProfileAssureRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDbaProfileAssureRate.setStatus("current")
if mibBuilder.loadTexts:
    gponDbaProfileAssureRate.setUnits("kbps")


class _GponDbaProfileMaxRate_Type(Integer32):
    """Custom type gponDbaProfileMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 1274880),
    )


_GponDbaProfileMaxRate_Type.__name__ = "Integer32"
_GponDbaProfileMaxRate_Object = MibTableColumn
gponDbaProfileMaxRate = _GponDbaProfileMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 2, 1, 4),
    _GponDbaProfileMaxRate_Type()
)
gponDbaProfileMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDbaProfileMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    gponDbaProfileMaxRate.setUnits("kbps")
_GponDbaProfileBindInfoTable_Object = MibTable
gponDbaProfileBindInfoTable = _GponDbaProfileBindInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    gponDbaProfileBindInfoTable.setStatus("current")
_GponDbaProfileBindInfoEntry_Object = MibTableRow
gponDbaProfileBindInfoEntry = _GponDbaProfileBindInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 3, 1)
)
gponDbaProfileBindInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponDbaProfileId"),
    (0, "CDATA-GPON-MIB2", "gponLineProfileId"),
)
if mibBuilder.loadTexts:
    gponDbaProfileBindInfoEntry.setStatus("current")
_GponDbaProfileBindLineProfileTcontList_Type = DisplayString
_GponDbaProfileBindLineProfileTcontList_Object = MibTableColumn
gponDbaProfileBindLineProfileTcontList = _GponDbaProfileBindLineProfileTcontList_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 2, 3, 1, 2),
    _GponDbaProfileBindLineProfileTcontList_Type()
)
gponDbaProfileBindLineProfileTcontList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponDbaProfileBindLineProfileTcontList.setStatus("current")
_GponLineProfileObjects_ObjectIdentity = ObjectIdentity
gponLineProfileObjects = _GponLineProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3)
)
_GponLineProfileInfoTable_Object = MibTable
gponLineProfileInfoTable = _GponLineProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    gponLineProfileInfoTable.setStatus("current")
_GponLineProfileInfoEntry_Object = MibTableRow
gponLineProfileInfoEntry = _GponLineProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 1, 1)
)
gponLineProfileInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponLineProfileId"),
)
if mibBuilder.loadTexts:
    gponLineProfileInfoEntry.setStatus("current")
_GponLineProfileId_Type = GponLinePorfileId
_GponLineProfileId_Object = MibTableColumn
gponLineProfileId = _GponLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 1, 1, 1),
    _GponLineProfileId_Type()
)
gponLineProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileId.setStatus("current")
_GponLineProfileRowStatus_Type = RowStatus
_GponLineProfileRowStatus_Object = MibTableColumn
gponLineProfileRowStatus = _GponLineProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 1, 1, 2),
    _GponLineProfileRowStatus_Type()
)
gponLineProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileRowStatus.setStatus("current")
_GponLineProfileName_Type = GponLinePorfileName
_GponLineProfileName_Object = MibTableColumn
gponLineProfileName = _GponLineProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 1, 1, 3),
    _GponLineProfileName_Type()
)
gponLineProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileName.setStatus("current")


class _GponLineProfileMappingMode_Type(Integer32):
    """Custom type gponLineProfileMappingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("priority", 2),
          ("vlanAndPriority", 3))
    )


_GponLineProfileMappingMode_Type.__name__ = "Integer32"
_GponLineProfileMappingMode_Object = MibTableColumn
gponLineProfileMappingMode = _GponLineProfileMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 1, 1, 4),
    _GponLineProfileMappingMode_Type()
)
gponLineProfileMappingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileMappingMode.setStatus("current")
_GponLineProfileTcontNum_Type = Integer32
_GponLineProfileTcontNum_Object = MibTableColumn
gponLineProfileTcontNum = _GponLineProfileTcontNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 1, 1, 5),
    _GponLineProfileTcontNum_Type()
)
gponLineProfileTcontNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponLineProfileTcontNum.setStatus("current")
_GponLineProfileGemNum_Type = Integer32
_GponLineProfileGemNum_Object = MibTableColumn
gponLineProfileGemNum = _GponLineProfileGemNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 1, 1, 6),
    _GponLineProfileGemNum_Type()
)
gponLineProfileGemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponLineProfileGemNum.setStatus("current")
_GponLineProfileBindNum_Type = Integer32
_GponLineProfileBindNum_Object = MibTableColumn
gponLineProfileBindNum = _GponLineProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 1, 1, 7),
    _GponLineProfileBindNum_Type()
)
gponLineProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponLineProfileBindNum.setStatus("current")
_GponLineProfileTcontTable_Object = MibTable
gponLineProfileTcontTable = _GponLineProfileTcontTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gponLineProfileTcontTable.setStatus("current")
_GponLineProfileTcontEntry_Object = MibTableRow
gponLineProfileTcontEntry = _GponLineProfileTcontEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 2, 1)
)
gponLineProfileTcontEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponLineProfileId"),
    (0, "CDATA-GPON-MIB2", "gponLineProfileTcontId"),
)
if mibBuilder.loadTexts:
    gponLineProfileTcontEntry.setStatus("current")
_GponLineProfileTcontId_Type = GponLinePorfileTcontId
_GponLineProfileTcontId_Object = MibTableColumn
gponLineProfileTcontId = _GponLineProfileTcontId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 2, 1, 1),
    _GponLineProfileTcontId_Type()
)
gponLineProfileTcontId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileTcontId.setStatus("current")
_GponLineProfileTcontRowStatus_Type = RowStatus
_GponLineProfileTcontRowStatus_Object = MibTableColumn
gponLineProfileTcontRowStatus = _GponLineProfileTcontRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 2, 1, 2),
    _GponLineProfileTcontRowStatus_Type()
)
gponLineProfileTcontRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileTcontRowStatus.setStatus("current")


class _GponLineProfileTcontDbaProfileId_Type(Integer32):
    """Custom type gponLineProfileTcontDbaProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
        ValueRangeConstraint(65535, 65535),
    )


_GponLineProfileTcontDbaProfileId_Type.__name__ = "Integer32"
_GponLineProfileTcontDbaProfileId_Object = MibTableColumn
gponLineProfileTcontDbaProfileId = _GponLineProfileTcontDbaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 2, 1, 3),
    _GponLineProfileTcontDbaProfileId_Type()
)
gponLineProfileTcontDbaProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileTcontDbaProfileId.setStatus("current")
_GponLineProfileGemTable_Object = MibTable
gponLineProfileGemTable = _GponLineProfileGemTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    gponLineProfileGemTable.setStatus("current")
_GponLineProfileGemEntry_Object = MibTableRow
gponLineProfileGemEntry = _GponLineProfileGemEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 3, 1)
)
gponLineProfileGemEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponLineProfileId"),
    (0, "CDATA-GPON-MIB2", "gponLineProfileGemId"),
)
if mibBuilder.loadTexts:
    gponLineProfileGemEntry.setStatus("current")
_GponLineProfileGemId_Type = GponLinePorfileGemId
_GponLineProfileGemId_Object = MibTableColumn
gponLineProfileGemId = _GponLineProfileGemId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 3, 1, 1),
    _GponLineProfileGemId_Type()
)
gponLineProfileGemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileGemId.setStatus("current")
_GponLineProfileGemRowStatus_Type = RowStatus
_GponLineProfileGemRowStatus_Object = MibTableColumn
gponLineProfileGemRowStatus = _GponLineProfileGemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 3, 1, 2),
    _GponLineProfileGemRowStatus_Type()
)
gponLineProfileGemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemRowStatus.setStatus("current")


class _GponLineProfileGemTcontId_Type(Integer32):
    """Custom type gponLineProfileGemTcontId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_GponLineProfileGemTcontId_Type.__name__ = "Integer32"
_GponLineProfileGemTcontId_Object = MibTableColumn
gponLineProfileGemTcontId = _GponLineProfileGemTcontId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 3, 1, 3),
    _GponLineProfileGemTcontId_Type()
)
gponLineProfileGemTcontId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemTcontId.setStatus("current")


class _GponLineProfileGemUpCar_Type(Integer32):
    """Custom type gponLineProfileGemUpCar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_GponLineProfileGemUpCar_Type.__name__ = "Integer32"
_GponLineProfileGemUpCar_Object = MibTableColumn
gponLineProfileGemUpCar = _GponLineProfileGemUpCar_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 3, 1, 4),
    _GponLineProfileGemUpCar_Type()
)
gponLineProfileGemUpCar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemUpCar.setStatus("current")


class _GponLineProfileGemDownCar_Type(Integer32):
    """Custom type gponLineProfileGemDownCar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_GponLineProfileGemDownCar_Type.__name__ = "Integer32"
_GponLineProfileGemDownCar_Object = MibTableColumn
gponLineProfileGemDownCar = _GponLineProfileGemDownCar_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 3, 1, 5),
    _GponLineProfileGemDownCar_Type()
)
gponLineProfileGemDownCar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemDownCar.setStatus("current")
_GponLineProfileGemMapNum_Type = Integer32
_GponLineProfileGemMapNum_Object = MibTableColumn
gponLineProfileGemMapNum = _GponLineProfileGemMapNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 3, 1, 6),
    _GponLineProfileGemMapNum_Type()
)
gponLineProfileGemMapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponLineProfileGemMapNum.setStatus("current")
_GponLineProfileGemMapTable_Object = MibTable
gponLineProfileGemMapTable = _GponLineProfileGemMapTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    gponLineProfileGemMapTable.setStatus("current")
_GponLineProfileGemMapEntry_Object = MibTableRow
gponLineProfileGemMapEntry = _GponLineProfileGemMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 4, 1)
)
gponLineProfileGemMapEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponLineProfileId"),
    (0, "CDATA-GPON-MIB2", "gponLineProfileGemId"),
    (0, "CDATA-GPON-MIB2", "gponLineProfileGemMapId"),
)
if mibBuilder.loadTexts:
    gponLineProfileGemMapEntry.setStatus("current")
_GponLineProfileGemMapId_Type = GponLinePorfileGemMapId
_GponLineProfileGemMapId_Object = MibTableColumn
gponLineProfileGemMapId = _GponLineProfileGemMapId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 4, 1, 1),
    _GponLineProfileGemMapId_Type()
)
gponLineProfileGemMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileGemMapId.setStatus("current")
_GponLineProfileGemMapRowStatus_Type = RowStatus
_GponLineProfileGemMapRowStatus_Object = MibTableColumn
gponLineProfileGemMapRowStatus = _GponLineProfileGemMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 4, 1, 2),
    _GponLineProfileGemMapRowStatus_Type()
)
gponLineProfileGemMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemMapRowStatus.setStatus("current")


class _GponLineProfileGemMapVlan_Type(Integer32):
    """Custom type gponLineProfileGemMapVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_GponLineProfileGemMapVlan_Type.__name__ = "Integer32"
_GponLineProfileGemMapVlan_Object = MibTableColumn
gponLineProfileGemMapVlan = _GponLineProfileGemMapVlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 4, 1, 3),
    _GponLineProfileGemMapVlan_Type()
)
gponLineProfileGemMapVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemMapVlan.setStatus("current")
_GponLineProfileGemMapPriority_Type = GponVlanPriority
_GponLineProfileGemMapPriority_Object = MibTableColumn
gponLineProfileGemMapPriority = _GponLineProfileGemMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 4, 1, 4),
    _GponLineProfileGemMapPriority_Type()
)
gponLineProfileGemMapPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemMapPriority.setStatus("current")
_GponLineProfileBindInfoTable_Object = MibTable
gponLineProfileBindInfoTable = _GponLineProfileBindInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    gponLineProfileBindInfoTable.setStatus("current")
_GponLineProfileBindInfoEntry_Object = MibTableRow
gponLineProfileBindInfoEntry = _GponLineProfileBindInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 5, 1)
)
gponLineProfileBindInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponLineProfileId"),
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
)
if mibBuilder.loadTexts:
    gponLineProfileBindInfoEntry.setStatus("current")
_GponLineProfileBindOnuList_Type = DisplayString
_GponLineProfileBindOnuList_Object = MibTableColumn
gponLineProfileBindOnuList = _GponLineProfileBindOnuList_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 3, 5, 1, 2),
    _GponLineProfileBindOnuList_Type()
)
gponLineProfileBindOnuList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponLineProfileBindOnuList.setStatus("current")
_GponSrvProfileObjects_ObjectIdentity = ObjectIdentity
gponSrvProfileObjects = _GponSrvProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4)
)
_GponSrvProfileInfoTable_Object = MibTable
gponSrvProfileInfoTable = _GponSrvProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    gponSrvProfileInfoTable.setStatus("current")
_GponSrvProfileInfoEntry_Object = MibTableRow
gponSrvProfileInfoEntry = _GponSrvProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 1, 1)
)
gponSrvProfileInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSrvProfileId"),
)
if mibBuilder.loadTexts:
    gponSrvProfileInfoEntry.setStatus("current")
_GponSrvProfileId_Type = GponSrvProfileId
_GponSrvProfileId_Object = MibTableColumn
gponSrvProfileId = _GponSrvProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 1, 1, 1),
    _GponSrvProfileId_Type()
)
gponSrvProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileId.setStatus("current")
_GponSrvProfileRowStatus_Type = RowStatus
_GponSrvProfileRowStatus_Object = MibTableColumn
gponSrvProfileRowStatus = _GponSrvProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 1, 1, 2),
    _GponSrvProfileRowStatus_Type()
)
gponSrvProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfileRowStatus.setStatus("current")
_GponSrvProfileName_Type = GponSrvProfileName
_GponSrvProfileName_Object = MibTableColumn
gponSrvProfileName = _GponSrvProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 1, 1, 3),
    _GponSrvProfileName_Type()
)
gponSrvProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfileName.setStatus("current")
_GponSrvProfileBindNum_Type = Integer32
_GponSrvProfileBindNum_Object = MibTableColumn
gponSrvProfileBindNum = _GponSrvProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 1, 1, 8),
    _GponSrvProfileBindNum_Type()
)
gponSrvProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponSrvProfileBindNum.setStatus("current")
_GponSrvProfileCfgTable_Object = MibTable
gponSrvProfileCfgTable = _GponSrvProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    gponSrvProfileCfgTable.setStatus("current")
_GponSrvProfileCfgEntry_Object = MibTableRow
gponSrvProfileCfgEntry = _GponSrvProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 2, 1)
)
gponSrvProfileCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSrvProfileId"),
)
if mibBuilder.loadTexts:
    gponSrvProfileCfgEntry.setStatus("current")


class _GponSrvProfileMcMode_Type(Integer32):
    """Custom type gponSrvProfileMcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmp-snooping", 0),
          ("igmp-snooping-proxy", 1),
          ("igmp-proxy", 2))
    )


_GponSrvProfileMcMode_Type.__name__ = "Integer32"
_GponSrvProfileMcMode_Object = MibTableColumn
gponSrvProfileMcMode = _GponSrvProfileMcMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 2, 1, 1),
    _GponSrvProfileMcMode_Type()
)
gponSrvProfileMcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileMcMode.setStatus("current")


class _GponSrvProfileUpIgmpFwdMode_Type(Integer32):
    """Custom type gponSrvProfileUpIgmpFwdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("default", 1),
          ("translation", 2))
    )


_GponSrvProfileUpIgmpFwdMode_Type.__name__ = "Integer32"
_GponSrvProfileUpIgmpFwdMode_Object = MibTableColumn
gponSrvProfileUpIgmpFwdMode = _GponSrvProfileUpIgmpFwdMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 2, 1, 2),
    _GponSrvProfileUpIgmpFwdMode_Type()
)
gponSrvProfileUpIgmpFwdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileUpIgmpFwdMode.setStatus("current")
_GponSrvProfileUpIgmpTCI_Type = Integer32
_GponSrvProfileUpIgmpTCI_Object = MibTableColumn
gponSrvProfileUpIgmpTCI = _GponSrvProfileUpIgmpTCI_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 2, 1, 3),
    _GponSrvProfileUpIgmpTCI_Type()
)
gponSrvProfileUpIgmpTCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileUpIgmpTCI.setStatus("current")


class _GponSrvProfileDnMcMode_Type(Integer32):
    """Custom type gponSrvProfileDnMcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("untag", 1),
          ("translation", 2))
    )


_GponSrvProfileDnMcMode_Type.__name__ = "Integer32"
_GponSrvProfileDnMcMode_Object = MibTableColumn
gponSrvProfileDnMcMode = _GponSrvProfileDnMcMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 2, 1, 4),
    _GponSrvProfileDnMcMode_Type()
)
gponSrvProfileDnMcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileDnMcMode.setStatus("current")
_GponSrvProfileDnMcTCI_Type = Integer32
_GponSrvProfileDnMcTCI_Object = MibTableColumn
gponSrvProfileDnMcTCI = _GponSrvProfileDnMcTCI_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 2, 1, 5),
    _GponSrvProfileDnMcTCI_Type()
)
gponSrvProfileDnMcTCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileDnMcTCI.setStatus("current")
_GponSrvProfilePortNumTable_Object = MibTable
gponSrvProfilePortNumTable = _GponSrvProfilePortNumTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    gponSrvProfilePortNumTable.setStatus("current")
_GponSrvProfilePortNumEntry_Object = MibTableRow
gponSrvProfilePortNumEntry = _GponSrvProfilePortNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 3, 1)
)
gponSrvProfilePortNumEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSrvProfileId"),
)
if mibBuilder.loadTexts:
    gponSrvProfilePortNumEntry.setStatus("current")


class _GponSrvProfileEthNum_Type(Integer32):
    """Custom type gponSrvProfileEthNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
        ValueRangeConstraint(65535, 65535),
    )


_GponSrvProfileEthNum_Type.__name__ = "Integer32"
_GponSrvProfileEthNum_Object = MibTableColumn
gponSrvProfileEthNum = _GponSrvProfileEthNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 3, 1, 1),
    _GponSrvProfileEthNum_Type()
)
gponSrvProfileEthNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileEthNum.setStatus("current")


class _GponSrvProfilePotsNum_Type(Integer32):
    """Custom type gponSrvProfilePotsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
        ValueRangeConstraint(65535, 65535),
    )


_GponSrvProfilePotsNum_Type.__name__ = "Integer32"
_GponSrvProfilePotsNum_Object = MibTableColumn
gponSrvProfilePotsNum = _GponSrvProfilePotsNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 3, 1, 2),
    _GponSrvProfilePotsNum_Type()
)
gponSrvProfilePotsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfilePotsNum.setStatus("current")


class _GponSrvProfileCatvNum_Type(Integer32):
    """Custom type gponSrvProfileCatvNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
        ValueRangeConstraint(65535, 65535),
    )


_GponSrvProfileCatvNum_Type.__name__ = "Integer32"
_GponSrvProfileCatvNum_Object = MibTableColumn
gponSrvProfileCatvNum = _GponSrvProfileCatvNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 3, 1, 3),
    _GponSrvProfileCatvNum_Type()
)
gponSrvProfileCatvNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileCatvNum.setStatus("current")
_GponSrvProfilePortVlanCfgTable_Object = MibTable
gponSrvProfilePortVlanCfgTable = _GponSrvProfilePortVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanCfgTable.setStatus("current")
_GponSrvProfilePortVlanCfgEntry_Object = MibTableRow
gponSrvProfilePortVlanCfgEntry = _GponSrvProfilePortVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4, 1)
)
gponSrvProfilePortVlanCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSrvProfileId"),
    (0, "CDATA-GPON-MIB2", "gponSrvProfilePortType"),
    (0, "CDATA-GPON-MIB2", "gponSrvProfilePortId"),
    (0, "CDATA-GPON-MIB2", "gponSrvProfilePortVlanEntryId"),
)
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanCfgEntry.setStatus("current")


class _GponSrvProfilePortType_Type(Integer32):
    """Custom type gponSrvProfilePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eth", 1)
    )


_GponSrvProfilePortType_Type.__name__ = "Integer32"
_GponSrvProfilePortType_Object = MibTableColumn
gponSrvProfilePortType = _GponSrvProfilePortType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4, 1, 1),
    _GponSrvProfilePortType_Type()
)
gponSrvProfilePortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortType.setStatus("current")


class _GponSrvProfilePortId_Type(Integer32):
    """Custom type gponSrvProfilePortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GponSrvProfilePortId_Type.__name__ = "Integer32"
_GponSrvProfilePortId_Object = MibTableColumn
gponSrvProfilePortId = _GponSrvProfilePortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4, 1, 2),
    _GponSrvProfilePortId_Type()
)
gponSrvProfilePortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortId.setStatus("current")


class _GponSrvProfilePortVlanEntryId_Type(Integer32):
    """Custom type gponSrvProfilePortVlanEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_GponSrvProfilePortVlanEntryId_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanEntryId_Object = MibTableColumn
gponSrvProfilePortVlanEntryId = _GponSrvProfilePortVlanEntryId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4, 1, 3),
    _GponSrvProfilePortVlanEntryId_Type()
)
gponSrvProfilePortVlanEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanEntryId.setStatus("current")
_GponSrvProfilePortVlanRowStatus_Type = RowStatus
_GponSrvProfilePortVlanRowStatus_Object = MibTableColumn
gponSrvProfilePortVlanRowStatus = _GponSrvProfilePortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4, 1, 4),
    _GponSrvProfilePortVlanRowStatus_Type()
)
gponSrvProfilePortVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanRowStatus.setStatus("current")


class _GponSrvProfilePortVlanMode_Type(Integer32):
    """Custom type gponSrvProfilePortVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("qinq", 2),
          ("translation", 3))
    )


_GponSrvProfilePortVlanMode_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanMode_Object = MibTableColumn
gponSrvProfilePortVlanMode = _GponSrvProfilePortVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4, 1, 5),
    _GponSrvProfilePortVlanMode_Type()
)
gponSrvProfilePortVlanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanMode.setStatus("current")


class _GponSrvProfilePortVlanSvlan_Type(Integer32):
    """Custom type gponSrvProfilePortVlanSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_GponSrvProfilePortVlanSvlan_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanSvlan_Object = MibTableColumn
gponSrvProfilePortVlanSvlan = _GponSrvProfilePortVlanSvlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4, 1, 6),
    _GponSrvProfilePortVlanSvlan_Type()
)
gponSrvProfilePortVlanSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanSvlan.setStatus("current")


class _GponSrvProfilePortVlanSpri_Type(Integer32):
    """Custom type gponSrvProfilePortVlanSpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_GponSrvProfilePortVlanSpri_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanSpri_Object = MibTableColumn
gponSrvProfilePortVlanSpri = _GponSrvProfilePortVlanSpri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4, 1, 7),
    _GponSrvProfilePortVlanSpri_Type()
)
gponSrvProfilePortVlanSpri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanSpri.setStatus("current")


class _GponSrvProfilePortCvlan_Type(GponVlanId):
    """Custom type gponSrvProfilePortCvlan based on GponVlanId"""
    subtypeSpec = GponVlanId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_GponSrvProfilePortCvlan_Type.__name__ = "GponVlanId"
_GponSrvProfilePortCvlan_Object = MibTableColumn
gponSrvProfilePortCvlan = _GponSrvProfilePortCvlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4, 1, 8),
    _GponSrvProfilePortCvlan_Type()
)
gponSrvProfilePortCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortCvlan.setStatus("current")


class _GponSrvProfilePortVlanCpri_Type(Integer32):
    """Custom type gponSrvProfilePortVlanCpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_GponSrvProfilePortVlanCpri_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanCpri_Object = MibTableColumn
gponSrvProfilePortVlanCpri = _GponSrvProfilePortVlanCpri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 4, 1, 9),
    _GponSrvProfilePortVlanCpri_Type()
)
gponSrvProfilePortVlanCpri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanCpri.setStatus("current")
_GponSrvProfileBindInfoTable_Object = MibTable
gponSrvProfileBindInfoTable = _GponSrvProfileBindInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    gponSrvProfileBindInfoTable.setStatus("current")
_GponSrvProfileBindInfoEntry_Object = MibTableRow
gponSrvProfileBindInfoEntry = _GponSrvProfileBindInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 5, 1)
)
gponSrvProfileBindInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSrvProfileId"),
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
)
if mibBuilder.loadTexts:
    gponSrvProfileBindInfoEntry.setStatus("current")
_GponSrvProfileBindOnuList_Type = DisplayString
_GponSrvProfileBindOnuList_Object = MibTableColumn
gponSrvProfileBindOnuList = _GponSrvProfileBindOnuList_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 4, 5, 1, 2),
    _GponSrvProfileBindOnuList_Type()
)
gponSrvProfileBindOnuList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponSrvProfileBindOnuList.setStatus("current")
_GponTrafficProfileObjects_ObjectIdentity = ObjectIdentity
gponTrafficProfileObjects = _GponTrafficProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6)
)
_GponTrafficProfileInfoTable_Object = MibTable
gponTrafficProfileInfoTable = _GponTrafficProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    gponTrafficProfileInfoTable.setStatus("current")
_GponTrafficProfileInfoEntry_Object = MibTableRow
gponTrafficProfileInfoEntry = _GponTrafficProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 1, 1)
)
gponTrafficProfileInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponTrafficProfileId"),
)
if mibBuilder.loadTexts:
    gponTrafficProfileInfoEntry.setStatus("current")
_GponTrafficProfileId_Type = GponTrafficProfileId
_GponTrafficProfileId_Object = MibTableColumn
gponTrafficProfileId = _GponTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 1, 1, 1),
    _GponTrafficProfileId_Type()
)
gponTrafficProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileId.setStatus("current")
_GponTrafficProfileRowStatus_Type = RowStatus
_GponTrafficProfileRowStatus_Object = MibTableColumn
gponTrafficProfileRowStatus = _GponTrafficProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 1, 1, 2),
    _GponTrafficProfileRowStatus_Type()
)
gponTrafficProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponTrafficProfileRowStatus.setStatus("current")
_GponTrafficProfileName_Type = GponTrafficProfileName
_GponTrafficProfileName_Object = MibTableColumn
gponTrafficProfileName = _GponTrafficProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 1, 1, 3),
    _GponTrafficProfileName_Type()
)
gponTrafficProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponTrafficProfileName.setStatus("current")
_GponTrafficProfileBindNum_Type = Integer32
_GponTrafficProfileBindNum_Object = MibTableColumn
gponTrafficProfileBindNum = _GponTrafficProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 1, 1, 4),
    _GponTrafficProfileBindNum_Type()
)
gponTrafficProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTrafficProfileBindNum.setStatus("current")
_GponTrafficProfileCfgTable_Object = MibTable
gponTrafficProfileCfgTable = _GponTrafficProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    gponTrafficProfileCfgTable.setStatus("current")
_GponTrafficProfileCfgEntry_Object = MibTableRow
gponTrafficProfileCfgEntry = _GponTrafficProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 3, 1)
)
gponTrafficProfileCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponTrafficProfileId"),
)
if mibBuilder.loadTexts:
    gponTrafficProfileCfgEntry.setStatus("current")


class _GponTrafficProfileCfgCir_Type(Integer32):
    """Custom type gponTrafficProfileCfgCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 10240000),
    )


_GponTrafficProfileCfgCir_Type.__name__ = "Integer32"
_GponTrafficProfileCfgCir_Object = MibTableColumn
gponTrafficProfileCfgCir = _GponTrafficProfileCfgCir_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 3, 1, 1),
    _GponTrafficProfileCfgCir_Type()
)
gponTrafficProfileCfgCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgCir.setStatus("current")


class _GponTrafficProfileCfgPir_Type(Integer32):
    """Custom type gponTrafficProfileCfgPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 10240000),
    )


_GponTrafficProfileCfgPir_Type.__name__ = "Integer32"
_GponTrafficProfileCfgPir_Object = MibTableColumn
gponTrafficProfileCfgPir = _GponTrafficProfileCfgPir_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 3, 1, 2),
    _GponTrafficProfileCfgPir_Type()
)
gponTrafficProfileCfgPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgPir.setStatus("current")


class _GponTrafficProfileCfgCbs_Type(Integer32):
    """Custom type gponTrafficProfileCfgCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 10240000),
    )


_GponTrafficProfileCfgCbs_Type.__name__ = "Integer32"
_GponTrafficProfileCfgCbs_Object = MibTableColumn
gponTrafficProfileCfgCbs = _GponTrafficProfileCfgCbs_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 3, 1, 3),
    _GponTrafficProfileCfgCbs_Type()
)
gponTrafficProfileCfgCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgCbs.setStatus("current")


class _GponTrafficProfileCfgPbs_Type(Integer32):
    """Custom type gponTrafficProfileCfgPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 10240000),
    )


_GponTrafficProfileCfgPbs_Type.__name__ = "Integer32"
_GponTrafficProfileCfgPbs_Object = MibTableColumn
gponTrafficProfileCfgPbs = _GponTrafficProfileCfgPbs_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 3, 1, 4),
    _GponTrafficProfileCfgPbs_Type()
)
gponTrafficProfileCfgPbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgPbs.setStatus("current")


class _GponTrafficProfileCfgPriority_Type(Integer32):
    """Custom type gponTrafficProfileCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_GponTrafficProfileCfgPriority_Type.__name__ = "Integer32"
_GponTrafficProfileCfgPriority_Object = MibTableColumn
gponTrafficProfileCfgPriority = _GponTrafficProfileCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 6, 3, 1, 5),
    _GponTrafficProfileCfgPriority_Type()
)
gponTrafficProfileCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgPriority.setStatus("current")
_GponSipAgentProfileObjects_ObjectIdentity = ObjectIdentity
gponSipAgentProfileObjects = _GponSipAgentProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8)
)
_GponSipAgentProfileInfoTable_Object = MibTable
gponSipAgentProfileInfoTable = _GponSipAgentProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    gponSipAgentProfileInfoTable.setStatus("current")
_GponSipAgentProfileInfoEntry_Object = MibTableRow
gponSipAgentProfileInfoEntry = _GponSipAgentProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 1, 1)
)
gponSipAgentProfileInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSipAgentProfileId"),
)
if mibBuilder.loadTexts:
    gponSipAgentProfileInfoEntry.setStatus("current")
_GponSipAgentProfileId_Type = GponSipAgentProfileId
_GponSipAgentProfileId_Object = MibTableColumn
gponSipAgentProfileId = _GponSipAgentProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 1, 1, 1),
    _GponSipAgentProfileId_Type()
)
gponSipAgentProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSipAgentProfileId.setStatus("current")
_GponSipAgentProfileRowStatus_Type = RowStatus
_GponSipAgentProfileRowStatus_Object = MibTableColumn
gponSipAgentProfileRowStatus = _GponSipAgentProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 1, 1, 2),
    _GponSipAgentProfileRowStatus_Type()
)
gponSipAgentProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSipAgentProfileRowStatus.setStatus("current")
_GponSipAgentProfileName_Type = GponSipAgentProfileName
_GponSipAgentProfileName_Object = MibTableColumn
gponSipAgentProfileName = _GponSipAgentProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 1, 1, 3),
    _GponSipAgentProfileName_Type()
)
gponSipAgentProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSipAgentProfileName.setStatus("current")
_GponSipAgentProfileBindNum_Type = Integer32
_GponSipAgentProfileBindNum_Object = MibTableColumn
gponSipAgentProfileBindNum = _GponSipAgentProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 1, 1, 4),
    _GponSipAgentProfileBindNum_Type()
)
gponSipAgentProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponSipAgentProfileBindNum.setStatus("current")
_GponSipAgentProfileCfgTable_Object = MibTable
gponSipAgentProfileCfgTable = _GponSipAgentProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    gponSipAgentProfileCfgTable.setStatus("current")
_GponSipAgentProfileCfgEntry_Object = MibTableRow
gponSipAgentProfileCfgEntry = _GponSipAgentProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1)
)
gponSipAgentProfileCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSipAgentProfileId"),
)
if mibBuilder.loadTexts:
    gponSipAgentProfileCfgEntry.setStatus("current")
_GponSipAgentProfileProxyServerUri_Type = GponSipUri
_GponSipAgentProfileProxyServerUri_Object = MibTableColumn
gponSipAgentProfileProxyServerUri = _GponSipAgentProfileProxyServerUri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 1),
    _GponSipAgentProfileProxyServerUri_Type()
)
gponSipAgentProfileProxyServerUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileProxyServerUri.setStatus("current")


class _GponSipAgentProfileRtpDscp_Type(Integer32):
    """Custom type gponSipAgentProfileRtpDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_GponSipAgentProfileRtpDscp_Type.__name__ = "Integer32"
_GponSipAgentProfileRtpDscp_Object = MibTableColumn
gponSipAgentProfileRtpDscp = _GponSipAgentProfileRtpDscp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 2),
    _GponSipAgentProfileRtpDscp_Type()
)
gponSipAgentProfileRtpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileRtpDscp.setStatus("current")


class _GponSipAgentProfileRtpMinPort_Type(Integer32):
    """Custom type gponSipAgentProfileRtpMinPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GponSipAgentProfileRtpMinPort_Type.__name__ = "Integer32"
_GponSipAgentProfileRtpMinPort_Object = MibTableColumn
gponSipAgentProfileRtpMinPort = _GponSipAgentProfileRtpMinPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 3),
    _GponSipAgentProfileRtpMinPort_Type()
)
gponSipAgentProfileRtpMinPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileRtpMinPort.setStatus("current")


class _GponSipAgentProfileRtpMaxPort_Type(Integer32):
    """Custom type gponSipAgentProfileRtpMaxPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GponSipAgentProfileRtpMaxPort_Type.__name__ = "Integer32"
_GponSipAgentProfileRtpMaxPort_Object = MibTableColumn
gponSipAgentProfileRtpMaxPort = _GponSipAgentProfileRtpMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 4),
    _GponSipAgentProfileRtpMaxPort_Type()
)
gponSipAgentProfileRtpMaxPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileRtpMaxPort.setStatus("current")


class _GponSipAgentProfileSignalDscp_Type(Integer32):
    """Custom type gponSipAgentProfileSignalDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_GponSipAgentProfileSignalDscp_Type.__name__ = "Integer32"
_GponSipAgentProfileSignalDscp_Object = MibTableColumn
gponSipAgentProfileSignalDscp = _GponSipAgentProfileSignalDscp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 5),
    _GponSipAgentProfileSignalDscp_Type()
)
gponSipAgentProfileSignalDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileSignalDscp.setStatus("current")


class _GponSipAgentProfileSignalPort_Type(Integer32):
    """Custom type gponSipAgentProfileSignalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GponSipAgentProfileSignalPort_Type.__name__ = "Integer32"
_GponSipAgentProfileSignalPort_Object = MibTableColumn
gponSipAgentProfileSignalPort = _GponSipAgentProfileSignalPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 6),
    _GponSipAgentProfileSignalPort_Type()
)
gponSipAgentProfileSignalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileSignalPort.setStatus("current")


class _GponSipAgentProfileSignalTransferMode_Type(Integer32):
    """Custom type gponSipAgentProfileSignalTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("tcp", 1))
    )


_GponSipAgentProfileSignalTransferMode_Type.__name__ = "Integer32"
_GponSipAgentProfileSignalTransferMode_Object = MibTableColumn
gponSipAgentProfileSignalTransferMode = _GponSipAgentProfileSignalTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 7),
    _GponSipAgentProfileSignalTransferMode_Type()
)
gponSipAgentProfileSignalTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileSignalTransferMode.setStatus("current")
_GponSipAgentProfileRegistrationExpiration_Type = Unsigned32
_GponSipAgentProfileRegistrationExpiration_Object = MibTableColumn
gponSipAgentProfileRegistrationExpiration = _GponSipAgentProfileRegistrationExpiration_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 8),
    _GponSipAgentProfileRegistrationExpiration_Type()
)
gponSipAgentProfileRegistrationExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileRegistrationExpiration.setStatus("current")
_GponSipAgentProfileRegistrationReregHeadStartTime_Type = Unsigned32
_GponSipAgentProfileRegistrationReregHeadStartTime_Object = MibTableColumn
gponSipAgentProfileRegistrationReregHeadStartTime = _GponSipAgentProfileRegistrationReregHeadStartTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 9),
    _GponSipAgentProfileRegistrationReregHeadStartTime_Type()
)
gponSipAgentProfileRegistrationReregHeadStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileRegistrationReregHeadStartTime.setStatus("current")
_GponSipAgentProfileRegistrationServerUri_Type = GponSipUri
_GponSipAgentProfileRegistrationServerUri_Object = MibTableColumn
gponSipAgentProfileRegistrationServerUri = _GponSipAgentProfileRegistrationServerUri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 10),
    _GponSipAgentProfileRegistrationServerUri_Type()
)
gponSipAgentProfileRegistrationServerUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileRegistrationServerUri.setStatus("current")
_GponSipAgentProfileVoiceMailServerUri_Type = GponSipUri
_GponSipAgentProfileVoiceMailServerUri_Object = MibTableColumn
gponSipAgentProfileVoiceMailServerUri = _GponSipAgentProfileVoiceMailServerUri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 11),
    _GponSipAgentProfileVoiceMailServerUri_Type()
)
gponSipAgentProfileVoiceMailServerUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileVoiceMailServerUri.setStatus("current")
_GponSipAgentProfileVoiceMailSubscriptionExpiration_Type = Unsigned32
_GponSipAgentProfileVoiceMailSubscriptionExpiration_Object = MibTableColumn
gponSipAgentProfileVoiceMailSubscriptionExpiration = _GponSipAgentProfileVoiceMailSubscriptionExpiration_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 12),
    _GponSipAgentProfileVoiceMailSubscriptionExpiration_Type()
)
gponSipAgentProfileVoiceMailSubscriptionExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileVoiceMailSubscriptionExpiration.setStatus("current")
_GponSipAgentProfileConfFactory_Type = GponSipUri
_GponSipAgentProfileConfFactory_Object = MibTableColumn
gponSipAgentProfileConfFactory = _GponSipAgentProfileConfFactory_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 13),
    _GponSipAgentProfileConfFactory_Type()
)
gponSipAgentProfileConfFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileConfFactory.setStatus("current")
_GponSipAgentProfileBridgedLineAgent_Type = GponSipUri
_GponSipAgentProfileBridgedLineAgent_Object = MibTableColumn
gponSipAgentProfileBridgedLineAgent = _GponSipAgentProfileBridgedLineAgent_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 14),
    _GponSipAgentProfileBridgedLineAgent_Type()
)
gponSipAgentProfileBridgedLineAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileBridgedLineAgent.setStatus("current")


class _GponSipAgentProfileAuthRealm_Type(OctetString):
    """Custom type gponSipAgentProfileAuthRealm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_GponSipAgentProfileAuthRealm_Type.__name__ = "OctetString"
_GponSipAgentProfileAuthRealm_Object = MibTableColumn
gponSipAgentProfileAuthRealm = _GponSipAgentProfileAuthRealm_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 2, 1, 15),
    _GponSipAgentProfileAuthRealm_Type()
)
gponSipAgentProfileAuthRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipAgentProfileAuthRealm.setStatus("current")
_GponSipAgentProfileBindInfoTable_Object = MibTable
gponSipAgentProfileBindInfoTable = _GponSipAgentProfileBindInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    gponSipAgentProfileBindInfoTable.setStatus("current")
_GponSipAgentProfileBindInfoEntry_Object = MibTableRow
gponSipAgentProfileBindInfoEntry = _GponSipAgentProfileBindInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 3, 1)
)
gponSipAgentProfileBindInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSipAgentProfileId"),
)
if mibBuilder.loadTexts:
    gponSipAgentProfileBindInfoEntry.setStatus("current")
_GponSipAgentProfileBindInfoOnuId_Type = Integer32
_GponSipAgentProfileBindInfoOnuId_Object = MibTableColumn
gponSipAgentProfileBindInfoOnuId = _GponSipAgentProfileBindInfoOnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 3, 1, 1),
    _GponSipAgentProfileBindInfoOnuId_Type()
)
gponSipAgentProfileBindInfoOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponSipAgentProfileBindInfoOnuId.setStatus("current")
_GponSipAgentProfileBindPotsList_Type = Integer32
_GponSipAgentProfileBindPotsList_Object = MibTableColumn
gponSipAgentProfileBindPotsList = _GponSipAgentProfileBindPotsList_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 8, 3, 1, 2),
    _GponSipAgentProfileBindPotsList_Type()
)
gponSipAgentProfileBindPotsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponSipAgentProfileBindPotsList.setStatus("current")
_GponSipRightFlagProfileObjects_ObjectIdentity = ObjectIdentity
gponSipRightFlagProfileObjects = _GponSipRightFlagProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9)
)
_GponSipRightFlagProfileInfoTable_Object = MibTable
gponSipRightFlagProfileInfoTable = _GponSipRightFlagProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    gponSipRightFlagProfileInfoTable.setStatus("current")
_GponSipRightFlagProfileInfoEntry_Object = MibTableRow
gponSipRightFlagProfileInfoEntry = _GponSipRightFlagProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 1, 1)
)
gponSipRightFlagProfileInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSipRightFlagProfileId"),
)
if mibBuilder.loadTexts:
    gponSipRightFlagProfileInfoEntry.setStatus("current")
_GponSipRightFlagProfileId_Type = GponSipRightFlagProfileId
_GponSipRightFlagProfileId_Object = MibTableColumn
gponSipRightFlagProfileId = _GponSipRightFlagProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 1, 1, 1),
    _GponSipRightFlagProfileId_Type()
)
gponSipRightFlagProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileId.setStatus("current")
_GponSipRightFlagProfileRowStatus_Type = RowStatus
_GponSipRightFlagProfileRowStatus_Object = MibTableColumn
gponSipRightFlagProfileRowStatus = _GponSipRightFlagProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 1, 1, 2),
    _GponSipRightFlagProfileRowStatus_Type()
)
gponSipRightFlagProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileRowStatus.setStatus("current")
_GponSipRightFlagProfileName_Type = GponSipRightFlagProfileName
_GponSipRightFlagProfileName_Object = MibTableColumn
gponSipRightFlagProfileName = _GponSipRightFlagProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 1, 1, 3),
    _GponSipRightFlagProfileName_Type()
)
gponSipRightFlagProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileName.setStatus("current")
_GponSipRightFlagProfileBindNum_Type = Integer32
_GponSipRightFlagProfileBindNum_Object = MibTableColumn
gponSipRightFlagProfileBindNum = _GponSipRightFlagProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 1, 1, 4),
    _GponSipRightFlagProfileBindNum_Type()
)
gponSipRightFlagProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileBindNum.setStatus("current")
_GponSipRightFlagProfileCfgTable_Object = MibTable
gponSipRightFlagProfileCfgTable = _GponSipRightFlagProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    gponSipRightFlagProfileCfgTable.setStatus("current")
_GponSipRightFlagProfileCfgEntry_Object = MibTableRow
gponSipRightFlagProfileCfgEntry = _GponSipRightFlagProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 2, 1)
)
gponSipRightFlagProfileCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSipRightFlagProfileId"),
)
if mibBuilder.loadTexts:
    gponSipRightFlagProfileCfgEntry.setStatus("current")
_GponSipRightFlagProfileCallWaiting_Type = GponSwitch
_GponSipRightFlagProfileCallWaiting_Object = MibTableColumn
gponSipRightFlagProfileCallWaiting = _GponSipRightFlagProfileCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 2, 1, 1),
    _GponSipRightFlagProfileCallWaiting_Type()
)
gponSipRightFlagProfileCallWaiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileCallWaiting.setStatus("current")


class _GponSipRightFlagProfileCallProcess_Type(Bits):
    """Custom type gponSipRightFlagProfileCallProcess based on Bits"""
    namedValues = NamedValues(
        *(("threeParty", 0),
          ("callTransfer", 1),
          ("callHold", 2),
          ("callPark", 3),
          ("doNotDisturb", 4),
          ("conference", 5))
    )

_GponSipRightFlagProfileCallProcess_Type.__name__ = "Bits"
_GponSipRightFlagProfileCallProcess_Object = MibTableColumn
gponSipRightFlagProfileCallProcess = _GponSipRightFlagProfileCallProcess_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 2, 1, 2),
    _GponSipRightFlagProfileCallProcess_Type()
)
gponSipRightFlagProfileCallProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileCallProcess.setStatus("current")
_GponSipRightFlagProfileCallPresentation_Type = GponSwitch
_GponSipRightFlagProfileCallPresentation_Object = MibTableColumn
gponSipRightFlagProfileCallPresentation = _GponSipRightFlagProfileCallPresentation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 2, 1, 3),
    _GponSipRightFlagProfileCallPresentation_Type()
)
gponSipRightFlagProfileCallPresentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileCallPresentation.setStatus("current")


class _GponSipRightFlagProfileHotline_Type(Bits):
    """Custom type gponSipRightFlagProfileHotline based on Bits"""
    namedValues = NamedValues(
        *(("hotline", 0),
          ("hotlineDelay", 1))
    )

_GponSipRightFlagProfileHotline_Type.__name__ = "Bits"
_GponSipRightFlagProfileHotline_Object = MibTableColumn
gponSipRightFlagProfileHotline = _GponSipRightFlagProfileHotline_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 2, 1, 4),
    _GponSipRightFlagProfileHotline_Type()
)
gponSipRightFlagProfileHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileHotline.setStatus("current")


class _GponSipRightFlagProfileHotlineNum_Type(DisplayString):
    """Custom type gponSipRightFlagProfileHotlineNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GponSipRightFlagProfileHotlineNum_Type.__name__ = "DisplayString"
_GponSipRightFlagProfileHotlineNum_Object = MibTableColumn
gponSipRightFlagProfileHotlineNum = _GponSipRightFlagProfileHotlineNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 2, 1, 5),
    _GponSipRightFlagProfileHotlineNum_Type()
)
gponSipRightFlagProfileHotlineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileHotlineNum.setStatus("current")
_GponSipRightFlagProfileBindInfoTable_Object = MibTable
gponSipRightFlagProfileBindInfoTable = _GponSipRightFlagProfileBindInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 4)
)
if mibBuilder.loadTexts:
    gponSipRightFlagProfileBindInfoTable.setStatus("current")
_GponSipRightFlagProfileBindInfoEntry_Object = MibTableRow
gponSipRightFlagProfileBindInfoEntry = _GponSipRightFlagProfileBindInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 4, 1)
)
gponSipRightFlagProfileBindInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponSipRightFlagProfileId"),
)
if mibBuilder.loadTexts:
    gponSipRightFlagProfileBindInfoEntry.setStatus("current")
_GponSipRightFlagProfileBindInfoOnuId_Type = Integer32
_GponSipRightFlagProfileBindInfoOnuId_Object = MibTableColumn
gponSipRightFlagProfileBindInfoOnuId = _GponSipRightFlagProfileBindInfoOnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 4, 1, 1),
    _GponSipRightFlagProfileBindInfoOnuId_Type()
)
gponSipRightFlagProfileBindInfoOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileBindInfoOnuId.setStatus("current")
_GponSipRightFlagProfileBindPotsList_Type = Integer32
_GponSipRightFlagProfileBindPotsList_Object = MibTableColumn
gponSipRightFlagProfileBindPotsList = _GponSipRightFlagProfileBindPotsList_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 9, 4, 1, 2),
    _GponSipRightFlagProfileBindPotsList_Type()
)
gponSipRightFlagProfileBindPotsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponSipRightFlagProfileBindPotsList.setStatus("current")
_GponDigitMapProfileObjects_ObjectIdentity = ObjectIdentity
gponDigitMapProfileObjects = _GponDigitMapProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10)
)
_GponDigitMapProfileInfoTable_Object = MibTable
gponDigitMapProfileInfoTable = _GponDigitMapProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    gponDigitMapProfileInfoTable.setStatus("current")
_GponDigitMapProfileInfoEntry_Object = MibTableRow
gponDigitMapProfileInfoEntry = _GponDigitMapProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 1, 1)
)
gponDigitMapProfileInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponDigitMapProfileId"),
)
if mibBuilder.loadTexts:
    gponDigitMapProfileInfoEntry.setStatus("current")
_GponDigitMapProfileId_Type = GponDigitMapProfileId
_GponDigitMapProfileId_Object = MibTableColumn
gponDigitMapProfileId = _GponDigitMapProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 1, 1, 1),
    _GponDigitMapProfileId_Type()
)
gponDigitMapProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponDigitMapProfileId.setStatus("current")
_GponDigitMapProfileRowStatus_Type = RowStatus
_GponDigitMapProfileRowStatus_Object = MibTableColumn
gponDigitMapProfileRowStatus = _GponDigitMapProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 1, 1, 2),
    _GponDigitMapProfileRowStatus_Type()
)
gponDigitMapProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponDigitMapProfileRowStatus.setStatus("current")


class _GponDigitMapProfileName_Type(OctetString):
    """Custom type gponDigitMapProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GponDigitMapProfileName_Type.__name__ = "OctetString"
_GponDigitMapProfileName_Object = MibTableColumn
gponDigitMapProfileName = _GponDigitMapProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 1, 1, 3),
    _GponDigitMapProfileName_Type()
)
gponDigitMapProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponDigitMapProfileName.setStatus("current")
_GponDigitMapProfileBindNum_Type = Integer32
_GponDigitMapProfileBindNum_Object = MibTableColumn
gponDigitMapProfileBindNum = _GponDigitMapProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 1, 1, 4),
    _GponDigitMapProfileBindNum_Type()
)
gponDigitMapProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponDigitMapProfileBindNum.setStatus("current")
_GponDigitMapProfileCfgTable_Object = MibTable
gponDigitMapProfileCfgTable = _GponDigitMapProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    gponDigitMapProfileCfgTable.setStatus("current")
_GponDigitMapProfileCfgEntry_Object = MibTableRow
gponDigitMapProfileCfgEntry = _GponDigitMapProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 2, 1)
)
gponDigitMapProfileCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponDigitMapProfileId"),
)
if mibBuilder.loadTexts:
    gponDigitMapProfileCfgEntry.setStatus("current")
_GponDigitMapProfileCriticalDialTime_Type = Integer32
_GponDigitMapProfileCriticalDialTime_Object = MibTableColumn
gponDigitMapProfileCriticalDialTime = _GponDigitMapProfileCriticalDialTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 2, 1, 1),
    _GponDigitMapProfileCriticalDialTime_Type()
)
gponDigitMapProfileCriticalDialTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDigitMapProfileCriticalDialTime.setStatus("current")
_GponDigitMapProfileCfgPartialDialTime_Type = Integer32
_GponDigitMapProfileCfgPartialDialTime_Object = MibTableColumn
gponDigitMapProfileCfgPartialDialTime = _GponDigitMapProfileCfgPartialDialTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 2, 1, 2),
    _GponDigitMapProfileCfgPartialDialTime_Type()
)
gponDigitMapProfileCfgPartialDialTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDigitMapProfileCfgPartialDialTime.setStatus("current")


class _GponDigitMapProfileCfgDigitmapFormat_Type(Integer32):
    """Custom type gponDigitMapProfileCfgDigitmapFormat based on Integer32"""
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
        *(("notDefined", 0),
          ("h248", 1),
          ("ncs", 2),
          ("vendorSpecific", 3))
    )


_GponDigitMapProfileCfgDigitmapFormat_Type.__name__ = "Integer32"
_GponDigitMapProfileCfgDigitmapFormat_Object = MibTableColumn
gponDigitMapProfileCfgDigitmapFormat = _GponDigitMapProfileCfgDigitmapFormat_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 2, 1, 3),
    _GponDigitMapProfileCfgDigitmapFormat_Type()
)
gponDigitMapProfileCfgDigitmapFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDigitMapProfileCfgDigitmapFormat.setStatus("current")
_GponDigitMapProfileDialPlanTable_Object = MibTable
gponDigitMapProfileDialPlanTable = _GponDigitMapProfileDialPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    gponDigitMapProfileDialPlanTable.setStatus("current")
_GponDigitMapProfileDialPlanEntry_Object = MibTableRow
gponDigitMapProfileDialPlanEntry = _GponDigitMapProfileDialPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 3, 1)
)
gponDigitMapProfileDialPlanEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponDigitMapProfileId"),
    (0, "CDATA-GPON-MIB2", "gponDigitMapProfileDialPlanId"),
)
if mibBuilder.loadTexts:
    gponDigitMapProfileDialPlanEntry.setStatus("current")


class _GponDigitMapProfileDialPlanId_Type(Integer32):
    """Custom type gponDigitMapProfileDialPlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_GponDigitMapProfileDialPlanId_Type.__name__ = "Integer32"
_GponDigitMapProfileDialPlanId_Object = MibTableColumn
gponDigitMapProfileDialPlanId = _GponDigitMapProfileDialPlanId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 3, 1, 1),
    _GponDigitMapProfileDialPlanId_Type()
)
gponDigitMapProfileDialPlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponDigitMapProfileDialPlanId.setStatus("current")
_GponDigitMapProfileDialPlanRowStatus_Type = RowStatus
_GponDigitMapProfileDialPlanRowStatus_Object = MibTableColumn
gponDigitMapProfileDialPlanRowStatus = _GponDigitMapProfileDialPlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 3, 1, 2),
    _GponDigitMapProfileDialPlanRowStatus_Type()
)
gponDigitMapProfileDialPlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponDigitMapProfileDialPlanRowStatus.setStatus("current")


class _GponDigitMapProfileDialPlanToken_Type(DisplayString):
    """Custom type gponDigitMapProfileDialPlanToken based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 28),
    )


_GponDigitMapProfileDialPlanToken_Type.__name__ = "DisplayString"
_GponDigitMapProfileDialPlanToken_Object = MibTableColumn
gponDigitMapProfileDialPlanToken = _GponDigitMapProfileDialPlanToken_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 3, 1, 3),
    _GponDigitMapProfileDialPlanToken_Type()
)
gponDigitMapProfileDialPlanToken.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponDigitMapProfileDialPlanToken.setStatus("current")
_GponDigitMapProfileBindInfoTable_Object = MibTable
gponDigitMapProfileBindInfoTable = _GponDigitMapProfileBindInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 4)
)
if mibBuilder.loadTexts:
    gponDigitMapProfileBindInfoTable.setStatus("current")
_GponDigitMapProfileBindInfoEntry_Object = MibTableRow
gponDigitMapProfileBindInfoEntry = _GponDigitMapProfileBindInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 4, 1)
)
gponDigitMapProfileBindInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponDigitMapProfileId"),
)
if mibBuilder.loadTexts:
    gponDigitMapProfileBindInfoEntry.setStatus("current")
_GponDigitMapProfileBindInfoOnuId_Type = Integer32
_GponDigitMapProfileBindInfoOnuId_Object = MibTableColumn
gponDigitMapProfileBindInfoOnuId = _GponDigitMapProfileBindInfoOnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 4, 1, 1),
    _GponDigitMapProfileBindInfoOnuId_Type()
)
gponDigitMapProfileBindInfoOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponDigitMapProfileBindInfoOnuId.setStatus("current")
_GponDigitMapProfileBindPotsList_Type = Integer32
_GponDigitMapProfileBindPotsList_Object = MibTableColumn
gponDigitMapProfileBindPotsList = _GponDigitMapProfileBindPotsList_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 10, 4, 1, 2),
    _GponDigitMapProfileBindPotsList_Type()
)
gponDigitMapProfileBindPotsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponDigitMapProfileBindPotsList.setStatus("current")
_GponPotsProfileObjects_ObjectIdentity = ObjectIdentity
gponPotsProfileObjects = _GponPotsProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11)
)
_GponPotsProfileInfoTable_Object = MibTable
gponPotsProfileInfoTable = _GponPotsProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    gponPotsProfileInfoTable.setStatus("current")
_GponPotsProfileInfoEntry_Object = MibTableRow
gponPotsProfileInfoEntry = _GponPotsProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 1, 1)
)
gponPotsProfileInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponPotsProfileId"),
)
if mibBuilder.loadTexts:
    gponPotsProfileInfoEntry.setStatus("current")
_GponPotsProfileId_Type = GponPotsProfileId
_GponPotsProfileId_Object = MibTableColumn
gponPotsProfileId = _GponPotsProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 1, 1, 1),
    _GponPotsProfileId_Type()
)
gponPotsProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponPotsProfileId.setStatus("current")
_GponPotsProfileRowStatus_Type = RowStatus
_GponPotsProfileRowStatus_Object = MibTableColumn
gponPotsProfileRowStatus = _GponPotsProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 1, 1, 2),
    _GponPotsProfileRowStatus_Type()
)
gponPotsProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponPotsProfileRowStatus.setStatus("current")


class _GponPotsProfileName_Type(OctetString):
    """Custom type gponPotsProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_GponPotsProfileName_Type.__name__ = "OctetString"
_GponPotsProfileName_Object = MibTableColumn
gponPotsProfileName = _GponPotsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 1, 1, 3),
    _GponPotsProfileName_Type()
)
gponPotsProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponPotsProfileName.setStatus("current")
_GponPotsProfileBindNum_Type = Integer32
_GponPotsProfileBindNum_Object = MibTableColumn
gponPotsProfileBindNum = _GponPotsProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 1, 1, 4),
    _GponPotsProfileBindNum_Type()
)
gponPotsProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponPotsProfileBindNum.setStatus("current")
_GponPotsProfileCfgTable_Object = MibTable
gponPotsProfileCfgTable = _GponPotsProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    gponPotsProfileCfgTable.setStatus("current")
_GponPotsProfileCfgEntry_Object = MibTableRow
gponPotsProfileCfgEntry = _GponPotsProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 2, 1)
)
gponPotsProfileCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponPotsProfileId"),
)
if mibBuilder.loadTexts:
    gponPotsProfileCfgEntry.setStatus("current")


class _GponPotsProfileImpedance_Type(Integer32):
    """Custom type gponPotsProfileImpedance based on Integer32"""
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
        *(("imp600Ohms", 0),
          ("imp900Ohms", 1),
          ("imp150nf750Ohm270Ohm", 2),
          ("imp115nf820Ohm220Ohm", 3),
          ("imp230nf1050Ohm320Ohm", 4))
    )


_GponPotsProfileImpedance_Type.__name__ = "Integer32"
_GponPotsProfileImpedance_Object = MibTableColumn
gponPotsProfileImpedance = _GponPotsProfileImpedance_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 2, 1, 1),
    _GponPotsProfileImpedance_Type()
)
gponPotsProfileImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponPotsProfileImpedance.setStatus("current")


class _GponPotsProfileSignallingCode_Type(Integer32):
    """Custom type gponPotsProfileSignallingCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("loopStart", 1),
          ("groundStart", 2),
          ("loopReverseBattery", 3),
          ("coinFirst", 4),
          ("dialToneFirst", 5),
          ("multiParty", 6))
    )


_GponPotsProfileSignallingCode_Type.__name__ = "Integer32"
_GponPotsProfileSignallingCode_Object = MibTableColumn
gponPotsProfileSignallingCode = _GponPotsProfileSignallingCode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 2, 1, 2),
    _GponPotsProfileSignallingCode_Type()
)
gponPotsProfileSignallingCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponPotsProfileSignallingCode.setStatus("current")


class _GponPotsProfileRxGain_Type(Integer32):
    """Custom type gponPotsProfileRxGain based on Integer32"""
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
              36)
        )
    )
    namedValues = NamedValues(
        *(("gainN12d0dB", 0),
          ("gainN11d5dB", 1),
          ("gainN11d0dB", 2),
          ("gainN10d5dB", 3),
          ("gainN10d0dB", 4),
          ("gainN9d5dB", 5),
          ("gainN9d0dB", 6),
          ("gainN8d5dB", 7),
          ("gainN8d0dB", 8),
          ("gainN7d5dB", 9),
          ("gainN7d0dB", 10),
          ("gainN6d5dB", 11),
          ("gainN6d0dB", 12),
          ("gainN5d5dB", 13),
          ("gainN5d0dB", 14),
          ("gainN4d5dB", 15),
          ("gainN4d0dB", 16),
          ("gainN3d5dB", 17),
          ("gainN3d0dB", 18),
          ("gainN2d5dB", 19),
          ("gainN2d0dB", 20),
          ("gainN1d5dB", 21),
          ("gainN1d0dB", 22),
          ("gainN0d5dB", 23),
          ("gain0dB", 24),
          ("gainP0d5dB", 25),
          ("gainP1d0dB", 26),
          ("gainP1d5dB", 27),
          ("gainP2d0dB", 28),
          ("gainP2d5dB", 29),
          ("gainP3d0dB", 30),
          ("gainP3d5dB", 31),
          ("gainP4d0dB", 32),
          ("gainP4d5dB", 33),
          ("gainP5d0dB", 34),
          ("gainP5d5dB", 35),
          ("gainP6d0dB", 36))
    )


_GponPotsProfileRxGain_Type.__name__ = "Integer32"
_GponPotsProfileRxGain_Object = MibTableColumn
gponPotsProfileRxGain = _GponPotsProfileRxGain_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 2, 1, 3),
    _GponPotsProfileRxGain_Type()
)
gponPotsProfileRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponPotsProfileRxGain.setStatus("current")


class _GponPotsProfileTxGain_Type(Integer32):
    """Custom type gponPotsProfileTxGain based on Integer32"""
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
              36)
        )
    )
    namedValues = NamedValues(
        *(("gainN12d0dB", 0),
          ("gainN11d5dB", 1),
          ("gainN11d0dB", 2),
          ("gainN10d5dB", 3),
          ("gainN10d0dB", 4),
          ("gainN9d5dB", 5),
          ("gainN9d0dB", 6),
          ("gainN8d5dB", 7),
          ("gainN8d0dB", 8),
          ("gainN7d5dB", 9),
          ("gainN7d0dB", 10),
          ("gainN6d5dB", 11),
          ("gainN6d0dB", 12),
          ("gainN5d5dB", 13),
          ("gainN5d0dB", 14),
          ("gainN4d5dB", 15),
          ("gainN4d0dB", 16),
          ("gainN3d5dB", 17),
          ("gainN3d0dB", 18),
          ("gainN2d5dB", 19),
          ("gainN2d0dB", 20),
          ("gainN1d5dB", 21),
          ("gainN1d0dB", 22),
          ("gainN0d5dB", 23),
          ("gain0dB", 24),
          ("gainP0d5dB", 25),
          ("gainP1d0dB", 26),
          ("gainP1d5dB", 27),
          ("gainP2d0dB", 28),
          ("gainP2d5dB", 29),
          ("gainP3d0dB", 30),
          ("gainP3d5dB", 31),
          ("gainP4d0dB", 32),
          ("gainP4d5dB", 33),
          ("gainP5d0dB", 34),
          ("gainP5d5dB", 35),
          ("gainP6d0dB", 36))
    )


_GponPotsProfileTxGain_Type.__name__ = "Integer32"
_GponPotsProfileTxGain_Object = MibTableColumn
gponPotsProfileTxGain = _GponPotsProfileTxGain_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 2, 1, 4),
    _GponPotsProfileTxGain_Type()
)
gponPotsProfileTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponPotsProfileTxGain.setStatus("current")
_GponPotsProfileBindInfoTable_Object = MibTable
gponPotsProfileBindInfoTable = _GponPotsProfileBindInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 3)
)
if mibBuilder.loadTexts:
    gponPotsProfileBindInfoTable.setStatus("current")
_GponPotsProfileBindInfoEntry_Object = MibTableRow
gponPotsProfileBindInfoEntry = _GponPotsProfileBindInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 3, 1)
)
gponPotsProfileBindInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponPotsProfileId"),
)
if mibBuilder.loadTexts:
    gponPotsProfileBindInfoEntry.setStatus("current")
_GponPotsProfileBindInfoOnuId_Type = Integer32
_GponPotsProfileBindInfoOnuId_Object = MibTableColumn
gponPotsProfileBindInfoOnuId = _GponPotsProfileBindInfoOnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 3, 1, 1),
    _GponPotsProfileBindInfoOnuId_Type()
)
gponPotsProfileBindInfoOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponPotsProfileBindInfoOnuId.setStatus("current")
_GponPotsProfileBindPotsList_Type = Integer32
_GponPotsProfileBindPotsList_Object = MibTableColumn
gponPotsProfileBindPotsList = _GponPotsProfileBindPotsList_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1, 11, 3, 1, 2),
    _GponPotsProfileBindPotsList_Type()
)
gponPotsProfileBindPotsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponPotsProfileBindPotsList.setStatus("current")
_GponControlObjects_ObjectIdentity = ObjectIdentity
gponControlObjects = _GponControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2)
)
_GponOltObjects_ObjectIdentity = ObjectIdentity
gponOltObjects = _GponOltObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17)
)
_GponOltControlTable_Object = MibTable
gponOltControlTable = _GponOltControlTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    gponOltControlTable.setStatus("current")
_GponOltControlEntry_Object = MibTableRow
gponOltControlEntry = _GponOltControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 1, 1)
)
gponOltControlEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
)
if mibBuilder.loadTexts:
    gponOltControlEntry.setStatus("current")
_GponOltDeviceId_Type = GponDeviceId
_GponOltDeviceId_Object = MibTableColumn
gponOltDeviceId = _GponOltDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 1, 1, 1),
    _GponOltDeviceId_Type()
)
gponOltDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOltDeviceId.setStatus("current")
_GponOltCardId_Type = GponCardId
_GponOltCardId_Object = MibTableColumn
gponOltCardId = _GponOltCardId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 1, 1, 2),
    _GponOltCardId_Type()
)
gponOltCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOltCardId.setStatus("current")
_GponOltPortId_Type = GponOltPortId
_GponOltPortId_Object = MibTableColumn
gponOltPortId = _GponOltPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 1, 1, 3),
    _GponOltPortId_Type()
)
gponOltPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOltPortId.setStatus("current")
_GponOltPortAutoFindSwitch_Type = GponSwitch
_GponOltPortAutoFindSwitch_Object = MibTableColumn
gponOltPortAutoFindSwitch = _GponOltPortAutoFindSwitch_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 1, 1, 4),
    _GponOltPortAutoFindSwitch_Type()
)
gponOltPortAutoFindSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOltPortAutoFindSwitch.setStatus("current")
_GponOltPortSwitch_Type = GponSwitch
_GponOltPortSwitch_Object = MibTableColumn
gponOltPortSwitch = _GponOltPortSwitch_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 1, 1, 5),
    _GponOltPortSwitch_Type()
)
gponOltPortSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOltPortSwitch.setStatus("current")


class _GponOltPortStatus_Type(Integer32):
    """Custom type gponOltPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_GponOltPortStatus_Type.__name__ = "Integer32"
_GponOltPortStatus_Object = MibTableColumn
gponOltPortStatus = _GponOltPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 1, 1, 6),
    _GponOltPortStatus_Type()
)
gponOltPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltPortStatus.setStatus("current")
_GponOltPortDdmInfoTable_Object = MibTable
gponOltPortDdmInfoTable = _GponOltPortDdmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 2)
)
if mibBuilder.loadTexts:
    gponOltPortDdmInfoTable.setStatus("current")
_GponOltPortDdmInfoEntry_Object = MibTableRow
gponOltPortDdmInfoEntry = _GponOltPortDdmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 2, 1)
)
gponOltPortDdmInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
)
if mibBuilder.loadTexts:
    gponOltPortDdmInfoEntry.setStatus("current")


class _GponOltPortDdmTemperature_Type(OctetString):
    """Custom type gponOltPortDdmTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GponOltPortDdmTemperature_Type.__name__ = "OctetString"
_GponOltPortDdmTemperature_Object = MibTableColumn
gponOltPortDdmTemperature = _GponOltPortDdmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 2, 1, 1),
    _GponOltPortDdmTemperature_Type()
)
gponOltPortDdmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltPortDdmTemperature.setStatus("current")


class _GponOltPortDdmVoltage_Type(OctetString):
    """Custom type gponOltPortDdmVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GponOltPortDdmVoltage_Type.__name__ = "OctetString"
_GponOltPortDdmVoltage_Object = MibTableColumn
gponOltPortDdmVoltage = _GponOltPortDdmVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 2, 1, 2),
    _GponOltPortDdmVoltage_Type()
)
gponOltPortDdmVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltPortDdmVoltage.setStatus("current")


class _GponOltPortDdmTxBiasCurrent_Type(OctetString):
    """Custom type gponOltPortDdmTxBiasCurrent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GponOltPortDdmTxBiasCurrent_Type.__name__ = "OctetString"
_GponOltPortDdmTxBiasCurrent_Object = MibTableColumn
gponOltPortDdmTxBiasCurrent = _GponOltPortDdmTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 2, 1, 3),
    _GponOltPortDdmTxBiasCurrent_Type()
)
gponOltPortDdmTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltPortDdmTxBiasCurrent.setStatus("current")


class _GponOltPortDdmTxPower_Type(OctetString):
    """Custom type gponOltPortDdmTxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GponOltPortDdmTxPower_Type.__name__ = "OctetString"
_GponOltPortDdmTxPower_Object = MibTableColumn
gponOltPortDdmTxPower = _GponOltPortDdmTxPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 2, 1, 4),
    _GponOltPortDdmTxPower_Type()
)
gponOltPortDdmTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltPortDdmTxPower.setStatus("current")


class _GponOltPortDdmRxPower_Type(OctetString):
    """Custom type gponOltPortDdmRxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GponOltPortDdmRxPower_Type.__name__ = "OctetString"
_GponOltPortDdmRxPower_Object = MibTableColumn
gponOltPortDdmRxPower = _GponOltPortDdmRxPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 2, 1, 5),
    _GponOltPortDdmRxPower_Type()
)
gponOltPortDdmRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltPortDdmRxPower.setStatus("current")
_GponOltTransceiverInfoTable_Object = MibTable
gponOltTransceiverInfoTable = _GponOltTransceiverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 3)
)
if mibBuilder.loadTexts:
    gponOltTransceiverInfoTable.setStatus("current")
_GponOltTransceiverInfoEntry_Object = MibTableRow
gponOltTransceiverInfoEntry = _GponOltTransceiverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 3, 1)
)
gponOltTransceiverInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
)
if mibBuilder.loadTexts:
    gponOltTransceiverInfoEntry.setStatus("current")
_GponOltTransceiverVendor_Type = DisplayString
_GponOltTransceiverVendor_Object = MibTableColumn
gponOltTransceiverVendor = _GponOltTransceiverVendor_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 3, 1, 1),
    _GponOltTransceiverVendor_Type()
)
gponOltTransceiverVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltTransceiverVendor.setStatus("current")
_GponOltTransceiverProductName_Type = DisplayString
_GponOltTransceiverProductName_Object = MibTableColumn
gponOltTransceiverProductName = _GponOltTransceiverProductName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 3, 1, 2),
    _GponOltTransceiverProductName_Type()
)
gponOltTransceiverProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltTransceiverProductName.setStatus("current")
_GponOltTransceiverVersion_Type = DisplayString
_GponOltTransceiverVersion_Object = MibTableColumn
gponOltTransceiverVersion = _GponOltTransceiverVersion_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 3, 1, 3),
    _GponOltTransceiverVersion_Type()
)
gponOltTransceiverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltTransceiverVersion.setStatus("current")
_GponOltTransceiverSerialNumber_Type = DisplayString
_GponOltTransceiverSerialNumber_Object = MibTableColumn
gponOltTransceiverSerialNumber = _GponOltTransceiverSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 3, 1, 4),
    _GponOltTransceiverSerialNumber_Type()
)
gponOltTransceiverSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltTransceiverSerialNumber.setStatus("current")
_GponOltAutoAuthTable_ObjectIdentity = ObjectIdentity
gponOltAutoAuthTable = _GponOltAutoAuthTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4)
)
_GponOltAutoAuthControlTable_Object = MibTable
gponOltAutoAuthControlTable = _GponOltAutoAuthControlTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 1)
)
if mibBuilder.loadTexts:
    gponOltAutoAuthControlTable.setStatus("current")
_GponOltAutoAuthControlEntry_Object = MibTableRow
gponOltAutoAuthControlEntry = _GponOltAutoAuthControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 1, 1)
)
gponOltAutoAuthControlEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
)
if mibBuilder.loadTexts:
    gponOltAutoAuthControlEntry.setStatus("current")


class _GponOltAutoAuthMode_Type(Integer32):
    """Custom type gponOltAutoAuthMode based on Integer32"""
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
        *(("all", 1),
          ("equid-auth", 2),
          ("vendor-auth", 3),
          ("equid-swver-auth", 4))
    )


_GponOltAutoAuthMode_Type.__name__ = "Integer32"
_GponOltAutoAuthMode_Object = MibTableColumn
gponOltAutoAuthMode = _GponOltAutoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 1, 1, 1),
    _GponOltAutoAuthMode_Type()
)
gponOltAutoAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOltAutoAuthMode.setStatus("current")
_GponOltAutoAuthSwitch_Type = GponSwitch
_GponOltAutoAuthSwitch_Object = MibTableColumn
gponOltAutoAuthSwitch = _GponOltAutoAuthSwitch_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 1, 1, 2),
    _GponOltAutoAuthSwitch_Type()
)
gponOltAutoAuthSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOltAutoAuthSwitch.setStatus("current")


class _GponOltPortAutoAuthSwitchBitMap_Type(OctetString):
    """Custom type gponOltPortAutoAuthSwitchBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_GponOltPortAutoAuthSwitchBitMap_Type.__name__ = "OctetString"
_GponOltPortAutoAuthSwitchBitMap_Object = MibTableColumn
gponOltPortAutoAuthSwitchBitMap = _GponOltPortAutoAuthSwitchBitMap_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 1, 1, 3),
    _GponOltPortAutoAuthSwitchBitMap_Type()
)
gponOltPortAutoAuthSwitchBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOltPortAutoAuthSwitchBitMap.setStatus("current")


class _GponOltAutoAuthRuleNumber_Type(Integer32):
    """Custom type gponOltAutoAuthRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_GponOltAutoAuthRuleNumber_Type.__name__ = "Integer32"
_GponOltAutoAuthRuleNumber_Object = MibTableColumn
gponOltAutoAuthRuleNumber = _GponOltAutoAuthRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 1, 1, 4),
    _GponOltAutoAuthRuleNumber_Type()
)
gponOltAutoAuthRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltAutoAuthRuleNumber.setStatus("current")
_GponOltAutoAuthRuleTable_Object = MibTable
gponOltAutoAuthRuleTable = _GponOltAutoAuthRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 2)
)
if mibBuilder.loadTexts:
    gponOltAutoAuthRuleTable.setStatus("current")
_GponOltAutoAuthRuleEntry_Object = MibTableRow
gponOltAutoAuthRuleEntry = _GponOltAutoAuthRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 2, 1)
)
gponOltAutoAuthRuleEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltAutoAuthRuleId"),
)
if mibBuilder.loadTexts:
    gponOltAutoAuthRuleEntry.setStatus("current")
_GponOltAutoAuthRuleId_Type = GponOltAutoAuthRuleId
_GponOltAutoAuthRuleId_Object = MibTableColumn
gponOltAutoAuthRuleId = _GponOltAutoAuthRuleId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 2, 1, 2),
    _GponOltAutoAuthRuleId_Type()
)
gponOltAutoAuthRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOltAutoAuthRuleId.setStatus("current")
_GponOltAutoAuthRuleRowStatus_Type = RowStatus
_GponOltAutoAuthRuleRowStatus_Object = MibTableColumn
gponOltAutoAuthRuleRowStatus = _GponOltAutoAuthRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 2, 1, 3),
    _GponOltAutoAuthRuleRowStatus_Type()
)
gponOltAutoAuthRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOltAutoAuthRuleRowStatus.setStatus("current")


class _GponOltAutoAuthVendorId_Type(OctetString):
    """Custom type gponOltAutoAuthVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_GponOltAutoAuthVendorId_Type.__name__ = "OctetString"
_GponOltAutoAuthVendorId_Object = MibTableColumn
gponOltAutoAuthVendorId = _GponOltAutoAuthVendorId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 2, 1, 4),
    _GponOltAutoAuthVendorId_Type()
)
gponOltAutoAuthVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOltAutoAuthVendorId.setStatus("current")


class _GponOltAutoAuthEquipmentID_Type(OctetString):
    """Custom type gponOltAutoAuthEquipmentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GponOltAutoAuthEquipmentID_Type.__name__ = "OctetString"
_GponOltAutoAuthEquipmentID_Object = MibTableColumn
gponOltAutoAuthEquipmentID = _GponOltAutoAuthEquipmentID_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 2, 1, 5),
    _GponOltAutoAuthEquipmentID_Type()
)
gponOltAutoAuthEquipmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOltAutoAuthEquipmentID.setStatus("current")


class _GponOltAutoAuthSoftwareVersion_Type(OctetString):
    """Custom type gponOltAutoAuthSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_GponOltAutoAuthSoftwareVersion_Type.__name__ = "OctetString"
_GponOltAutoAuthSoftwareVersion_Object = MibTableColumn
gponOltAutoAuthSoftwareVersion = _GponOltAutoAuthSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 2, 1, 6),
    _GponOltAutoAuthSoftwareVersion_Type()
)
gponOltAutoAuthSoftwareVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOltAutoAuthSoftwareVersion.setStatus("current")
_GponOltAutoAuthLineProfileId_Type = GponLinePorfileId
_GponOltAutoAuthLineProfileId_Object = MibTableColumn
gponOltAutoAuthLineProfileId = _GponOltAutoAuthLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 2, 1, 7),
    _GponOltAutoAuthLineProfileId_Type()
)
gponOltAutoAuthLineProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOltAutoAuthLineProfileId.setStatus("current")
_GponOltAutoAuthSrvProfileId_Type = GponSrvProfileId
_GponOltAutoAuthSrvProfileId_Object = MibTableColumn
gponOltAutoAuthSrvProfileId = _GponOltAutoAuthSrvProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 2, 1, 8),
    _GponOltAutoAuthSrvProfileId_Type()
)
gponOltAutoAuthSrvProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOltAutoAuthSrvProfileId.setStatus("current")
_GponOltAutoAuthOnuNumber_Type = Integer32
_GponOltAutoAuthOnuNumber_Object = MibTableColumn
gponOltAutoAuthOnuNumber = _GponOltAutoAuthOnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 17, 4, 2, 1, 9),
    _GponOltAutoAuthOnuNumber_Type()
)
gponOltAutoAuthOnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOltAutoAuthOnuNumber.setStatus("current")
_GponOnuObjects_ObjectIdentity = ObjectIdentity
gponOnuObjects = _GponOnuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18)
)
_GponOnuConfigTable_Object = MibTable
gponOnuConfigTable = _GponOnuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    gponOnuConfigTable.setStatus("current")
_GponOnuConfigEntry_Object = MibTableRow
gponOnuConfigEntry = _GponOnuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 1, 1)
)
gponOnuConfigEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
)
if mibBuilder.loadTexts:
    gponOnuConfigEntry.setStatus("current")
_GponOnuId_Type = GponOnuId
_GponOnuId_Object = MibTableColumn
gponOnuId = _GponOnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 1, 1, 1),
    _GponOnuId_Type()
)
gponOnuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuId.setStatus("current")
_GponOnuRowStatus_Type = RowStatus
_GponOnuRowStatus_Object = MibTableColumn
gponOnuRowStatus = _GponOnuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 1, 1, 2),
    _GponOnuRowStatus_Type()
)
gponOnuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuRowStatus.setStatus("current")


class _GponOnuAuthMode_Type(Integer32):
    """Custom type gponOnuAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sn", 1),
          ("password", 2),
          ("sn-and-password", 3))
    )


_GponOnuAuthMode_Type.__name__ = "Integer32"
_GponOnuAuthMode_Object = MibTableColumn
gponOnuAuthMode = _GponOnuAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 1, 1, 3),
    _GponOnuAuthMode_Type()
)
gponOnuAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthMode.setStatus("current")
_GponOnuSn_Type = DisplayString
_GponOnuSn_Object = MibTableColumn
gponOnuSn = _GponOnuSn_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 1, 1, 4),
    _GponOnuSn_Type()
)
gponOnuSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuSn.setStatus("current")
_GponOnuPassword_Type = DisplayString
_GponOnuPassword_Object = MibTableColumn
gponOnuPassword = _GponOnuPassword_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 1, 1, 5),
    _GponOnuPassword_Type()
)
gponOnuPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuPassword.setStatus("current")
_GponOnuLineProfileId_Type = GponLinePorfileId
_GponOnuLineProfileId_Object = MibTableColumn
gponOnuLineProfileId = _GponOnuLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 1, 1, 6),
    _GponOnuLineProfileId_Type()
)
gponOnuLineProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuLineProfileId.setStatus("current")
_GponOnuServiceProfileId_Type = GponSrvProfileId
_GponOnuServiceProfileId_Object = MibTableColumn
gponOnuServiceProfileId = _GponOnuServiceProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 1, 1, 7),
    _GponOnuServiceProfileId_Type()
)
gponOnuServiceProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuServiceProfileId.setStatus("current")
_GponOnuDescription_Type = DisplayString
_GponOnuDescription_Object = MibTableColumn
gponOnuDescription = _GponOnuDescription_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 1, 1, 8),
    _GponOnuDescription_Type()
)
gponOnuDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuDescription.setStatus("current")
_GponOnuInfoTable_Object = MibTable
gponOnuInfoTable = _GponOnuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 2)
)
if mibBuilder.loadTexts:
    gponOnuInfoTable.setStatus("current")
_GponOnuInfoEntry_Object = MibTableRow
gponOnuInfoEntry = _GponOnuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 2, 1)
)
gponOnuInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
)
if mibBuilder.loadTexts:
    gponOnuInfoEntry.setStatus("current")


class _GponOnuRunState_Type(Integer32):
    """Custom type gponOnuRunState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_GponOnuRunState_Type.__name__ = "Integer32"
_GponOnuRunState_Object = MibTableColumn
gponOnuRunState = _GponOnuRunState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 2, 1, 1),
    _GponOnuRunState_Type()
)
gponOnuRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuRunState.setStatus("current")


class _GponOnuConfigState_Type(Integer32):
    """Custom type gponOnuConfigState based on Integer32"""
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
        *(("initial", 1),
          ("success", 2),
          ("failed", 3),
          ("configing", 4))
    )


_GponOnuConfigState_Type.__name__ = "Integer32"
_GponOnuConfigState_Object = MibTableColumn
gponOnuConfigState = _GponOnuConfigState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 2, 1, 2),
    _GponOnuConfigState_Type()
)
gponOnuConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuConfigState.setStatus("current")


class _GponOnuMatchState_Type(Integer32):
    """Custom type gponOnuMatchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("match", 2),
          ("mismatch", 3))
    )


_GponOnuMatchState_Type.__name__ = "Integer32"
_GponOnuMatchState_Object = MibTableColumn
gponOnuMatchState = _GponOnuMatchState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 2, 1, 3),
    _GponOnuMatchState_Type()
)
gponOnuMatchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuMatchState.setStatus("current")
_GponOnuDistance_Type = Integer32
_GponOnuDistance_Object = MibTableColumn
gponOnuDistance = _GponOnuDistance_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 2, 1, 4),
    _GponOnuDistance_Type()
)
gponOnuDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuDistance.setStatus("current")


class _GponOnuInfoDescription_Type(OctetString):
    """Custom type gponOnuInfoDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GponOnuInfoDescription_Type.__name__ = "OctetString"
_GponOnuInfoDescription_Object = MibTableColumn
gponOnuInfoDescription = _GponOnuInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 2, 1, 5),
    _GponOnuInfoDescription_Type()
)
gponOnuInfoDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuInfoDescription.setStatus("current")
_GponOnuInfoLastUpTime_Type = DisplayString
_GponOnuInfoLastUpTime_Object = MibTableColumn
gponOnuInfoLastUpTime = _GponOnuInfoLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 2, 1, 6),
    _GponOnuInfoLastUpTime_Type()
)
gponOnuInfoLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuInfoLastUpTime.setStatus("current")
_GponOnuInfoLastDownTime_Type = DisplayString
_GponOnuInfoLastDownTime_Object = MibTableColumn
gponOnuInfoLastDownTime = _GponOnuInfoLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 2, 1, 7),
    _GponOnuInfoLastDownTime_Type()
)
gponOnuInfoLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuInfoLastDownTime.setStatus("current")
_GponOnuCapabilityInfoTable_Object = MibTable
gponOnuCapabilityInfoTable = _GponOnuCapabilityInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3)
)
if mibBuilder.loadTexts:
    gponOnuCapabilityInfoTable.setStatus("current")
_GponOnuCapabilityInfoEntry_Object = MibTableRow
gponOnuCapabilityInfoEntry = _GponOnuCapabilityInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3, 1)
)
gponOnuCapabilityInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
)
if mibBuilder.loadTexts:
    gponOnuCapabilityInfoEntry.setStatus("current")


class _GponOnuType_Type(Integer32):
    """Custom type gponOnuType based on Integer32"""
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
        *(("sfu", 1),
          ("mdu", 2),
          ("hgu", 3),
          ("sfu-hgu", 4),
          ("mdu-hgu", 5))
    )


_GponOnuType_Type.__name__ = "Integer32"
_GponOnuType_Object = MibTableColumn
gponOnuType = _GponOnuType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3, 1, 1),
    _GponOnuType_Type()
)
gponOnuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuType.setStatus("current")
_GponOnuPonPortNum_Type = Integer32
_GponOnuPonPortNum_Object = MibTableColumn
gponOnuPonPortNum = _GponOnuPonPortNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3, 1, 2),
    _GponOnuPonPortNum_Type()
)
gponOnuPonPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuPonPortNum.setStatus("current")
_GponOnuEthPortNum_Type = Integer32
_GponOnuEthPortNum_Object = MibTableColumn
gponOnuEthPortNum = _GponOnuEthPortNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3, 1, 3),
    _GponOnuEthPortNum_Type()
)
gponOnuEthPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuEthPortNum.setStatus("current")
_GponOnuVeipPortNum_Type = Integer32
_GponOnuVeipPortNum_Object = MibTableColumn
gponOnuVeipPortNum = _GponOnuVeipPortNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3, 1, 4),
    _GponOnuVeipPortNum_Type()
)
gponOnuVeipPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuVeipPortNum.setStatus("current")
_GponOnuPotsPortNum_Type = Integer32
_GponOnuPotsPortNum_Object = MibTableColumn
gponOnuPotsPortNum = _GponOnuPotsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3, 1, 5),
    _GponOnuPotsPortNum_Type()
)
gponOnuPotsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuPotsPortNum.setStatus("current")
_GponOnuCatvPortNum_Type = Integer32
_GponOnuCatvPortNum_Object = MibTableColumn
gponOnuCatvPortNum = _GponOnuCatvPortNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3, 1, 6),
    _GponOnuCatvPortNum_Type()
)
gponOnuCatvPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuCatvPortNum.setStatus("current")
_GponOnuGemPortNum_Type = Integer32
_GponOnuGemPortNum_Object = MibTableColumn
gponOnuGemPortNum = _GponOnuGemPortNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3, 1, 7),
    _GponOnuGemPortNum_Type()
)
gponOnuGemPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuGemPortNum.setStatus("current")
_GponOnuTcontNum_Type = Integer32
_GponOnuTcontNum_Object = MibTableColumn
gponOnuTcontNum = _GponOnuTcontNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3, 1, 8),
    _GponOnuTcontNum_Type()
)
gponOnuTcontNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuTcontNum.setStatus("current")


class _GponOnuFlowControlType_Type(Integer32):
    """Custom type gponOnuFlowControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pq", 0),
          ("car", 1),
          ("pqAndCar", 2))
    )


_GponOnuFlowControlType_Type.__name__ = "Integer32"
_GponOnuFlowControlType_Object = MibTableColumn
gponOnuFlowControlType = _GponOnuFlowControlType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 3, 1, 9),
    _GponOnuFlowControlType_Type()
)
gponOnuFlowControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuFlowControlType.setStatus("current")
_GponOnuControlTable_Object = MibTable
gponOnuControlTable = _GponOnuControlTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 4)
)
if mibBuilder.loadTexts:
    gponOnuControlTable.setStatus("current")
_GponOnuControlEntry_Object = MibTableRow
gponOnuControlEntry = _GponOnuControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 4, 1)
)
gponOnuControlEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
)
if mibBuilder.loadTexts:
    gponOnuControlEntry.setStatus("current")


class _GponOnuReset_Type(Integer32):
    """Custom type gponOnuReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_GponOnuReset_Type.__name__ = "Integer32"
_GponOnuReset_Object = MibTableColumn
gponOnuReset = _GponOnuReset_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 4, 1, 1),
    _GponOnuReset_Type()
)
gponOnuReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuReset.setStatus("current")


class _GponOnuDeactive_Type(Integer32):
    """Custom type gponOnuDeactive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("deactive", 1))
    )


_GponOnuDeactive_Type.__name__ = "Integer32"
_GponOnuDeactive_Object = MibTableColumn
gponOnuDeactive = _GponOnuDeactive_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 4, 1, 2),
    _GponOnuDeactive_Type()
)
gponOnuDeactive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuDeactive.setStatus("current")
_GponOnuAutofindInfoTable_Object = MibTable
gponOnuAutofindInfoTable = _GponOnuAutofindInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5)
)
if mibBuilder.loadTexts:
    gponOnuAutofindInfoTable.setStatus("current")
_GponOnuAutofindInfoEntry_Object = MibTableRow
gponOnuAutofindInfoEntry = _GponOnuAutofindInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5, 1)
)
gponOnuAutofindInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuAutofindId"),
)
if mibBuilder.loadTexts:
    gponOnuAutofindInfoEntry.setStatus("current")


class _GponOnuAutofindId_Type(Integer32):
    """Custom type gponOnuAutofindId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_GponOnuAutofindId_Type.__name__ = "Integer32"
_GponOnuAutofindId_Object = MibTableColumn
gponOnuAutofindId = _GponOnuAutofindId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5, 1, 1),
    _GponOnuAutofindId_Type()
)
gponOnuAutofindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuAutofindId.setStatus("current")


class _GponOnuAutofindRowStatus_Type(Integer32):
    """Custom type gponOnuAutofindRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destory", 6))
    )


_GponOnuAutofindRowStatus_Type.__name__ = "Integer32"
_GponOnuAutofindRowStatus_Object = MibTableColumn
gponOnuAutofindRowStatus = _GponOnuAutofindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5, 1, 2),
    _GponOnuAutofindRowStatus_Type()
)
gponOnuAutofindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAutofindRowStatus.setStatus("current")
_GponOnuAutofindSn_Type = GponOnuSn
_GponOnuAutofindSn_Object = MibTableColumn
gponOnuAutofindSn = _GponOnuAutofindSn_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5, 1, 3),
    _GponOnuAutofindSn_Type()
)
gponOnuAutofindSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAutofindSn.setStatus("current")
_GponOnuAutofindPassword_Type = GponOnuPassword
_GponOnuAutofindPassword_Object = MibTableColumn
gponOnuAutofindPassword = _GponOnuAutofindPassword_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5, 1, 4),
    _GponOnuAutofindPassword_Type()
)
gponOnuAutofindPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAutofindPassword.setStatus("current")


class _GponOnuAutofindVendorId_Type(OctetString):
    """Custom type gponOnuAutofindVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_GponOnuAutofindVendorId_Type.__name__ = "OctetString"
_GponOnuAutofindVendorId_Object = MibTableColumn
gponOnuAutofindVendorId = _GponOnuAutofindVendorId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5, 1, 5),
    _GponOnuAutofindVendorId_Type()
)
gponOnuAutofindVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAutofindVendorId.setStatus("current")


class _GponOnuAutofindVersion_Type(OctetString):
    """Custom type gponOnuAutofindVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_GponOnuAutofindVersion_Type.__name__ = "OctetString"
_GponOnuAutofindVersion_Object = MibTableColumn
gponOnuAutofindVersion = _GponOnuAutofindVersion_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5, 1, 6),
    _GponOnuAutofindVersion_Type()
)
gponOnuAutofindVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAutofindVersion.setStatus("current")


class _GponOnuAutofindEquipmentID_Type(OctetString):
    """Custom type gponOnuAutofindEquipmentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GponOnuAutofindEquipmentID_Type.__name__ = "OctetString"
_GponOnuAutofindEquipmentID_Object = MibTableColumn
gponOnuAutofindEquipmentID = _GponOnuAutofindEquipmentID_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5, 1, 7),
    _GponOnuAutofindEquipmentID_Type()
)
gponOnuAutofindEquipmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAutofindEquipmentID.setStatus("current")


class _GponOnuAutofindSoftwareVersion_Type(OctetString):
    """Custom type gponOnuAutofindSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_GponOnuAutofindSoftwareVersion_Type.__name__ = "OctetString"
_GponOnuAutofindSoftwareVersion_Object = MibTableColumn
gponOnuAutofindSoftwareVersion = _GponOnuAutofindSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5, 1, 8),
    _GponOnuAutofindSoftwareVersion_Type()
)
gponOnuAutofindSoftwareVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAutofindSoftwareVersion.setStatus("current")
_GponOnuAutofindTime_Type = DisplayString
_GponOnuAutofindTime_Object = MibTableColumn
gponOnuAutofindTime = _GponOnuAutofindTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 5, 1, 9),
    _GponOnuAutofindTime_Type()
)
gponOnuAutofindTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAutofindTime.setStatus("current")
_GponOnuOpticalInfoTable_Object = MibTable
gponOnuOpticalInfoTable = _GponOnuOpticalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 6)
)
if mibBuilder.loadTexts:
    gponOnuOpticalInfoTable.setStatus("current")
_GponOnuOpticalInfoEntry_Object = MibTableRow
gponOnuOpticalInfoEntry = _GponOnuOpticalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 6, 1)
)
gponOnuOpticalInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
)
if mibBuilder.loadTexts:
    gponOnuOpticalInfoEntry.setStatus("current")
_GponOnuOpticalVoltage_Type = DisplayString
_GponOnuOpticalVoltage_Object = MibTableColumn
gponOnuOpticalVoltage = _GponOnuOpticalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 6, 1, 1),
    _GponOnuOpticalVoltage_Type()
)
gponOnuOpticalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuOpticalVoltage.setStatus("current")
_GponOnuOpticalTxPower_Type = DisplayString
_GponOnuOpticalTxPower_Object = MibTableColumn
gponOnuOpticalTxPower = _GponOnuOpticalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 6, 1, 2),
    _GponOnuOpticalTxPower_Type()
)
gponOnuOpticalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuOpticalTxPower.setStatus("current")
_GponOnuOpticalRxPower_Type = DisplayString
_GponOnuOpticalRxPower_Object = MibTableColumn
gponOnuOpticalRxPower = _GponOnuOpticalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 6, 1, 4),
    _GponOnuOpticalRxPower_Type()
)
gponOnuOpticalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuOpticalRxPower.setStatus("current")
_GponOnuOpticalLaserBiasCurrent_Type = DisplayString
_GponOnuOpticalLaserBiasCurrent_Object = MibTableColumn
gponOnuOpticalLaserBiasCurrent = _GponOnuOpticalLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 6, 1, 5),
    _GponOnuOpticalLaserBiasCurrent_Type()
)
gponOnuOpticalLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuOpticalLaserBiasCurrent.setStatus("current")
_GponOnuOpticalTemperature_Type = DisplayString
_GponOnuOpticalTemperature_Object = MibTableColumn
gponOnuOpticalTemperature = _GponOnuOpticalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 6, 1, 6),
    _GponOnuOpticalTemperature_Type()
)
gponOnuOpticalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuOpticalTemperature.setStatus("current")
_GponOnuVersionTable_Object = MibTable
gponOnuVersionTable = _GponOnuVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 7)
)
if mibBuilder.loadTexts:
    gponOnuVersionTable.setStatus("current")
_GponOnuVersionEntry_Object = MibTableRow
gponOnuVersionEntry = _GponOnuVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 7, 1)
)
gponOnuVersionEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
)
if mibBuilder.loadTexts:
    gponOnuVersionEntry.setStatus("current")
_GponOnuMainSoftwareVersion_Type = DisplayString
_GponOnuMainSoftwareVersion_Object = MibTableColumn
gponOnuMainSoftwareVersion = _GponOnuMainSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 7, 1, 1),
    _GponOnuMainSoftwareVersion_Type()
)
gponOnuMainSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuMainSoftwareVersion.setStatus("current")
_GponOnuStandbySoftwareVersion_Type = DisplayString
_GponOnuStandbySoftwareVersion_Object = MibTableColumn
gponOnuStandbySoftwareVersion = _GponOnuStandbySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 7, 1, 2),
    _GponOnuStandbySoftwareVersion_Type()
)
gponOnuStandbySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuStandbySoftwareVersion.setStatus("current")
_GponOnuAuthenticationManagement_ObjectIdentity = ObjectIdentity
gponOnuAuthenticationManagement = _GponOnuAuthenticationManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8)
)
_GponOnuAuthenticationConfirmTable_Object = MibTable
gponOnuAuthenticationConfirmTable = _GponOnuAuthenticationConfirmTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2)
)
if mibBuilder.loadTexts:
    gponOnuAuthenticationConfirmTable.setStatus("current")
_GponOnuAuthenticationConfirmEntry_Object = MibTableRow
gponOnuAuthenticationConfirmEntry = _GponOnuAuthenticationConfirmEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1)
)
gponOnuAuthenticationConfirmEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOnuAuthenticationConfirmDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOnuAuthenticationConfirmCardId"),
    (0, "CDATA-GPON-MIB2", "gponOnuAuthenticationConfirmPortId"),
)
if mibBuilder.loadTexts:
    gponOnuAuthenticationConfirmEntry.setStatus("current")
_GponOnuAuthenticationConfirmDeviceId_Type = Integer32
_GponOnuAuthenticationConfirmDeviceId_Object = MibTableColumn
gponOnuAuthenticationConfirmDeviceId = _GponOnuAuthenticationConfirmDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 1),
    _GponOnuAuthenticationConfirmDeviceId_Type()
)
gponOnuAuthenticationConfirmDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuAuthenticationConfirmDeviceId.setStatus("current")
_GponOnuAuthenticationConfirmCardId_Type = Integer32
_GponOnuAuthenticationConfirmCardId_Object = MibTableColumn
gponOnuAuthenticationConfirmCardId = _GponOnuAuthenticationConfirmCardId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 2),
    _GponOnuAuthenticationConfirmCardId_Type()
)
gponOnuAuthenticationConfirmCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuAuthenticationConfirmCardId.setStatus("current")
_GponOnuAuthenticationConfirmPortId_Type = Integer32
_GponOnuAuthenticationConfirmPortId_Object = MibTableColumn
gponOnuAuthenticationConfirmPortId = _GponOnuAuthenticationConfirmPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 3),
    _GponOnuAuthenticationConfirmPortId_Type()
)
gponOnuAuthenticationConfirmPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuAuthenticationConfirmPortId.setStatus("current")


class _GponOnuAuthenConfirmType_Type(Integer32):
    """Custom type gponOnuAuthenConfirmType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("snAuth", 1),
          ("snPwdAuth", 2),
          ("pwdAuth", 3),
          ("loidAuth", 4),
          ("loidPwdAuth", 5),
          ("snAuthAll", 6),
          ("snPwdAuthAll", 7),
          ("pwdAuthAll", 8),
          ("loidAuthAll", 9),
          ("loidPwdAuthAll", 10))
    )


_GponOnuAuthenConfirmType_Type.__name__ = "Integer32"
_GponOnuAuthenConfirmType_Object = MibTableColumn
gponOnuAuthenConfirmType = _GponOnuAuthenConfirmType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 4),
    _GponOnuAuthenConfirmType_Type()
)
gponOnuAuthenConfirmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthenConfirmType.setStatus("current")
_GponOnuAuthenConfirmSn_Type = DisplayString
_GponOnuAuthenConfirmSn_Object = MibTableColumn
gponOnuAuthenConfirmSn = _GponOnuAuthenConfirmSn_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 5),
    _GponOnuAuthenConfirmSn_Type()
)
gponOnuAuthenConfirmSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthenConfirmSn.setStatus("current")
_GponOnuAuthenConfirmPassword_Type = DisplayString
_GponOnuAuthenConfirmPassword_Object = MibTableColumn
gponOnuAuthenConfirmPassword = _GponOnuAuthenConfirmPassword_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 6),
    _GponOnuAuthenConfirmPassword_Type()
)
gponOnuAuthenConfirmPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthenConfirmPassword.setStatus("current")
_GponOnuAuthenConfirmLoid_Type = GponOnuLoid
_GponOnuAuthenConfirmLoid_Object = MibTableColumn
gponOnuAuthenConfirmLoid = _GponOnuAuthenConfirmLoid_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 7),
    _GponOnuAuthenConfirmLoid_Type()
)
gponOnuAuthenConfirmLoid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthenConfirmLoid.setStatus("current")
_GponOnuAuthenConfirmLoidPassword_Type = GponOnuLoidPassword
_GponOnuAuthenConfirmLoidPassword_Object = MibTableColumn
gponOnuAuthenConfirmLoidPassword = _GponOnuAuthenConfirmLoidPassword_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 8),
    _GponOnuAuthenConfirmLoidPassword_Type()
)
gponOnuAuthenConfirmLoidPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthenConfirmLoidPassword.setStatus("current")
_GponOnuAuthenConfirmLineProfileId_Type = Unsigned32
_GponOnuAuthenConfirmLineProfileId_Object = MibTableColumn
gponOnuAuthenConfirmLineProfileId = _GponOnuAuthenConfirmLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 9),
    _GponOnuAuthenConfirmLineProfileId_Type()
)
gponOnuAuthenConfirmLineProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthenConfirmLineProfileId.setStatus("current")
_GponOnuAuthenConfirmServiceProfileId_Type = Unsigned32
_GponOnuAuthenConfirmServiceProfileId_Object = MibTableColumn
gponOnuAuthenConfirmServiceProfileId = _GponOnuAuthenConfirmServiceProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 10),
    _GponOnuAuthenConfirmServiceProfileId_Type()
)
gponOnuAuthenConfirmServiceProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthenConfirmServiceProfileId.setStatus("current")


class _GponOnuAuthenConfirmTimeMode_Type(Integer32):
    """Custom type gponOnuAuthenConfirmTimeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 0),
          ("onceAging", 1),
          ("onceNoAging", 2))
    )


_GponOnuAuthenConfirmTimeMode_Type.__name__ = "Integer32"
_GponOnuAuthenConfirmTimeMode_Object = MibTableColumn
gponOnuAuthenConfirmTimeMode = _GponOnuAuthenConfirmTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 11),
    _GponOnuAuthenConfirmTimeMode_Type()
)
gponOnuAuthenConfirmTimeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthenConfirmTimeMode.setStatus("current")
_GponOnuAuthenConfirmAgingDuration_Type = Unsigned32
_GponOnuAuthenConfirmAgingDuration_Object = MibTableColumn
gponOnuAuthenConfirmAgingDuration = _GponOnuAuthenConfirmAgingDuration_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 12),
    _GponOnuAuthenConfirmAgingDuration_Type()
)
gponOnuAuthenConfirmAgingDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthenConfirmAgingDuration.setStatus("current")
_GponOnuAuthenticationConfirmRowStatus_Type = RowStatus
_GponOnuAuthenticationConfirmRowStatus_Object = MibTableColumn
gponOnuAuthenticationConfirmRowStatus = _GponOnuAuthenticationConfirmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 2, 1, 13),
    _GponOnuAuthenticationConfirmRowStatus_Type()
)
gponOnuAuthenticationConfirmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuAuthenticationConfirmRowStatus.setStatus("current")
_GponOnuPolicyAuthTable_ObjectIdentity = ObjectIdentity
gponOnuPolicyAuthTable = _GponOnuPolicyAuthTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3)
)
_GponOnuPolicyAuthControlTable_Object = MibTable
gponOnuPolicyAuthControlTable = _GponOnuPolicyAuthControlTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 1)
)
if mibBuilder.loadTexts:
    gponOnuPolicyAuthControlTable.setStatus("current")
_GponOnuPolicyAuthControlEntry_Object = MibTableRow
gponOnuPolicyAuthControlEntry = _GponOnuPolicyAuthControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 1, 1)
)
gponOnuPolicyAuthControlEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOnuPolicyAuthControlDeviceId"),
)
if mibBuilder.loadTexts:
    gponOnuPolicyAuthControlEntry.setStatus("current")
_GponOnuPolicyAuthControlDeviceId_Type = Integer32
_GponOnuPolicyAuthControlDeviceId_Object = MibTableColumn
gponOnuPolicyAuthControlDeviceId = _GponOnuPolicyAuthControlDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 1, 1, 1),
    _GponOnuPolicyAuthControlDeviceId_Type()
)
gponOnuPolicyAuthControlDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthControlDeviceId.setStatus("current")
_GponOnuPolicyAuthSwitch_Type = GponSwitch
_GponOnuPolicyAuthSwitch_Object = MibTableColumn
gponOnuPolicyAuthSwitch = _GponOnuPolicyAuthSwitch_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 1, 1, 2),
    _GponOnuPolicyAuthSwitch_Type()
)
gponOnuPolicyAuthSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthSwitch.setStatus("current")


class _GponOnuPolicyAuthPortSwtichBitMap_Type(OctetString):
    """Custom type gponOnuPolicyAuthPortSwtichBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GponOnuPolicyAuthPortSwtichBitMap_Type.__name__ = "OctetString"
_GponOnuPolicyAuthPortSwtichBitMap_Object = MibTableColumn
gponOnuPolicyAuthPortSwtichBitMap = _GponOnuPolicyAuthPortSwtichBitMap_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 1, 1, 3),
    _GponOnuPolicyAuthPortSwtichBitMap_Type()
)
gponOnuPolicyAuthPortSwtichBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthPortSwtichBitMap.setStatus("current")


class _GponOnuPolicyAuthMode_Type(Integer32):
    """Custom type gponOnuPolicyAuthMode based on Integer32"""
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
        *(("all", 0),
          ("equid", 1),
          ("vendor", 2),
          ("equidAndSwver", 3))
    )


_GponOnuPolicyAuthMode_Type.__name__ = "Integer32"
_GponOnuPolicyAuthMode_Object = MibTableColumn
gponOnuPolicyAuthMode = _GponOnuPolicyAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 1, 1, 4),
    _GponOnuPolicyAuthMode_Type()
)
gponOnuPolicyAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthMode.setStatus("current")


class _GponOnuPolicyAuthTargetMode_Type(Integer32):
    """Custom type gponOnuPolicyAuthTargetMode based on Integer32"""
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
        *(("snAuth", 0),
          ("snPasswordAuth", 1),
          ("passwordAuth", 2),
          ("loidAuth", 3),
          ("loidPasswordAuth", 4))
    )


_GponOnuPolicyAuthTargetMode_Type.__name__ = "Integer32"
_GponOnuPolicyAuthTargetMode_Object = MibTableColumn
gponOnuPolicyAuthTargetMode = _GponOnuPolicyAuthTargetMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 1, 1, 5),
    _GponOnuPolicyAuthTargetMode_Type()
)
gponOnuPolicyAuthTargetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthTargetMode.setStatus("current")


class _GponOnuPolicyAuthTimeMode_Type(Integer32):
    """Custom type gponOnuPolicyAuthTimeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always", 0),
          ("onceNoAging", 1))
    )


_GponOnuPolicyAuthTimeMode_Type.__name__ = "Integer32"
_GponOnuPolicyAuthTimeMode_Object = MibTableColumn
gponOnuPolicyAuthTimeMode = _GponOnuPolicyAuthTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 1, 1, 6),
    _GponOnuPolicyAuthTimeMode_Type()
)
gponOnuPolicyAuthTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthTimeMode.setStatus("current")
_GponOnuPolicyAuthRuleTable_Object = MibTable
gponOnuPolicyAuthRuleTable = _GponOnuPolicyAuthRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2)
)
if mibBuilder.loadTexts:
    gponOnuPolicyAuthRuleTable.setStatus("current")
_GponOnuPolicyAuthRuleEntry_Object = MibTableRow
gponOnuPolicyAuthRuleEntry = _GponOnuPolicyAuthRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2, 1)
)
gponOnuPolicyAuthRuleEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOnuPolicyAuthCardId"),
    (0, "CDATA-GPON-MIB2", "gponOnuPolicyAuthRuleId"),
)
if mibBuilder.loadTexts:
    gponOnuPolicyAuthRuleEntry.setStatus("current")
_GponOnuPolicyAuthCardId_Type = Unsigned32
_GponOnuPolicyAuthCardId_Object = MibTableColumn
gponOnuPolicyAuthCardId = _GponOnuPolicyAuthCardId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2, 1, 1),
    _GponOnuPolicyAuthCardId_Type()
)
gponOnuPolicyAuthCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthCardId.setStatus("current")
_GponOnuPolicyAuthRuleId_Type = Unsigned32
_GponOnuPolicyAuthRuleId_Object = MibTableColumn
gponOnuPolicyAuthRuleId = _GponOnuPolicyAuthRuleId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2, 1, 2),
    _GponOnuPolicyAuthRuleId_Type()
)
gponOnuPolicyAuthRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthRuleId.setStatus("current")


class _GponOnuPolicyAuthRuleMatchMode_Type(Integer32):
    """Custom type gponOnuPolicyAuthRuleMatchMode based on Integer32"""
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
        *(("all", 0),
          ("equid", 1),
          ("vendor", 2),
          ("equidAndSwver", 3))
    )


_GponOnuPolicyAuthRuleMatchMode_Type.__name__ = "Integer32"
_GponOnuPolicyAuthRuleMatchMode_Object = MibTableColumn
gponOnuPolicyAuthRuleMatchMode = _GponOnuPolicyAuthRuleMatchMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2, 1, 3),
    _GponOnuPolicyAuthRuleMatchMode_Type()
)
gponOnuPolicyAuthRuleMatchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthRuleMatchMode.setStatus("current")


class _GponOnuPolicyAuthRuleEquid_Type(OctetString):
    """Custom type gponOnuPolicyAuthRuleEquid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GponOnuPolicyAuthRuleEquid_Type.__name__ = "OctetString"
_GponOnuPolicyAuthRuleEquid_Object = MibTableColumn
gponOnuPolicyAuthRuleEquid = _GponOnuPolicyAuthRuleEquid_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2, 1, 4),
    _GponOnuPolicyAuthRuleEquid_Type()
)
gponOnuPolicyAuthRuleEquid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthRuleEquid.setStatus("current")


class _GponOnuPolicyAuthRuleVendorid_Type(OctetString):
    """Custom type gponOnuPolicyAuthRuleVendorid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_GponOnuPolicyAuthRuleVendorid_Type.__name__ = "OctetString"
_GponOnuPolicyAuthRuleVendorid_Object = MibTableColumn
gponOnuPolicyAuthRuleVendorid = _GponOnuPolicyAuthRuleVendorid_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2, 1, 5),
    _GponOnuPolicyAuthRuleVendorid_Type()
)
gponOnuPolicyAuthRuleVendorid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthRuleVendorid.setStatus("current")


class _GponOnuPolicyAuthRuleSoftwareVersion_Type(OctetString):
    """Custom type gponOnuPolicyAuthRuleSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_GponOnuPolicyAuthRuleSoftwareVersion_Type.__name__ = "OctetString"
_GponOnuPolicyAuthRuleSoftwareVersion_Object = MibTableColumn
gponOnuPolicyAuthRuleSoftwareVersion = _GponOnuPolicyAuthRuleSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2, 1, 6),
    _GponOnuPolicyAuthRuleSoftwareVersion_Type()
)
gponOnuPolicyAuthRuleSoftwareVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthRuleSoftwareVersion.setStatus("current")
_GponOnuPolicyAuthRuleLineProfileId_Type = Unsigned32
_GponOnuPolicyAuthRuleLineProfileId_Object = MibTableColumn
gponOnuPolicyAuthRuleLineProfileId = _GponOnuPolicyAuthRuleLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2, 1, 7),
    _GponOnuPolicyAuthRuleLineProfileId_Type()
)
gponOnuPolicyAuthRuleLineProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthRuleLineProfileId.setStatus("current")
_GponOnuPolicyAuthRuleSrvProfileId_Type = Unsigned32
_GponOnuPolicyAuthRuleSrvProfileId_Object = MibTableColumn
gponOnuPolicyAuthRuleSrvProfileId = _GponOnuPolicyAuthRuleSrvProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2, 1, 8),
    _GponOnuPolicyAuthRuleSrvProfileId_Type()
)
gponOnuPolicyAuthRuleSrvProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthRuleSrvProfileId.setStatus("current")
_GponOnuPolicyAuthRuleRowStatus_Type = RowStatus
_GponOnuPolicyAuthRuleRowStatus_Object = MibTableColumn
gponOnuPolicyAuthRuleRowStatus = _GponOnuPolicyAuthRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 18, 8, 3, 2, 1, 9),
    _GponOnuPolicyAuthRuleRowStatus_Type()
)
gponOnuPolicyAuthRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuPolicyAuthRuleRowStatus.setStatus("current")
_GponOnuEthPortObjects_ObjectIdentity = ObjectIdentity
gponOnuEthPortObjects = _GponOnuEthPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19)
)
_GponOnuEthPortCfgTable_Object = MibTable
gponOnuEthPortCfgTable = _GponOnuEthPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 1)
)
if mibBuilder.loadTexts:
    gponOnuEthPortCfgTable.setStatus("current")
_GponOnuEthPortCfgEntry_Object = MibTableRow
gponOnuEthPortCfgEntry = _GponOnuEthPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 1, 1)
)
gponOnuEthPortCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
    (0, "CDATA-GPON-MIB2", "gponOnuEthPortId"),
)
if mibBuilder.loadTexts:
    gponOnuEthPortCfgEntry.setStatus("current")
_GponOnuEthPortId_Type = GponOnuEthPortId
_GponOnuEthPortId_Object = MibTableColumn
gponOnuEthPortId = _GponOnuEthPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 1, 1, 1),
    _GponOnuEthPortId_Type()
)
gponOnuEthPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuEthPortId.setStatus("current")
_GponOnuEthPortNativeVlanId_Type = GponVlanId
_GponOnuEthPortNativeVlanId_Object = MibTableColumn
gponOnuEthPortNativeVlanId = _GponOnuEthPortNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 1, 1, 2),
    _GponOnuEthPortNativeVlanId_Type()
)
gponOnuEthPortNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuEthPortNativeVlanId.setStatus("current")
_GponOnuEthPortNativeVlanPriority_Type = GponVlanPriority
_GponOnuEthPortNativeVlanPriority_Object = MibTableColumn
gponOnuEthPortNativeVlanPriority = _GponOnuEthPortNativeVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 1, 1, 3),
    _GponOnuEthPortNativeVlanPriority_Type()
)
gponOnuEthPortNativeVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuEthPortNativeVlanPriority.setStatus("current")


class _GponOnuEthPortInboundCarId_Type(Integer32):
    """Custom type gponOnuEthPortInboundCarId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
        ValueRangeConstraint(65535, 65535),
    )


_GponOnuEthPortInboundCarId_Type.__name__ = "Integer32"
_GponOnuEthPortInboundCarId_Object = MibTableColumn
gponOnuEthPortInboundCarId = _GponOnuEthPortInboundCarId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 1, 1, 4),
    _GponOnuEthPortInboundCarId_Type()
)
gponOnuEthPortInboundCarId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuEthPortInboundCarId.setStatus("current")


class _GponOnuEthPortOutboundCarId_Type(Integer32):
    """Custom type gponOnuEthPortOutboundCarId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
        ValueRangeConstraint(65535, 65535),
    )


_GponOnuEthPortOutboundCarId_Type.__name__ = "Integer32"
_GponOnuEthPortOutboundCarId_Object = MibTableColumn
gponOnuEthPortOutboundCarId = _GponOnuEthPortOutboundCarId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 1, 1, 5),
    _GponOnuEthPortOutboundCarId_Type()
)
gponOnuEthPortOutboundCarId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuEthPortOutboundCarId.setStatus("current")


class _GponOnuEthPortSpeedAndDuplex_Type(Integer32):
    """Custom type gponOnuEthPortSpeedAndDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("autoNeg", 0),
          ("full10", 1),
          ("full100", 2),
          ("full1000", 3),
          ("half10", 17),
          ("half100", 18),
          ("half1000", 19))
    )


_GponOnuEthPortSpeedAndDuplex_Type.__name__ = "Integer32"
_GponOnuEthPortSpeedAndDuplex_Object = MibTableColumn
gponOnuEthPortSpeedAndDuplex = _GponOnuEthPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 1, 1, 6),
    _GponOnuEthPortSpeedAndDuplex_Type()
)
gponOnuEthPortSpeedAndDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuEthPortSpeedAndDuplex.setStatus("current")
_GponOnuEthPortFlowCtrl_Type = GponSwitch
_GponOnuEthPortFlowCtrl_Object = MibTableColumn
gponOnuEthPortFlowCtrl = _GponOnuEthPortFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 1, 1, 8),
    _GponOnuEthPortFlowCtrl_Type()
)
gponOnuEthPortFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuEthPortFlowCtrl.setStatus("current")
_GponOnuEthPortOperationalState_Type = GponSwitch
_GponOnuEthPortOperationalState_Object = MibTableColumn
gponOnuEthPortOperationalState = _GponOnuEthPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 1, 1, 9),
    _GponOnuEthPortOperationalState_Type()
)
gponOnuEthPortOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuEthPortOperationalState.setStatus("current")
_GponOnuEthPortInfoTable_Object = MibTable
gponOnuEthPortInfoTable = _GponOnuEthPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 2)
)
if mibBuilder.loadTexts:
    gponOnuEthPortInfoTable.setStatus("current")
_GponOnuEthPortInfoEntry_Object = MibTableRow
gponOnuEthPortInfoEntry = _GponOnuEthPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 2, 1)
)
gponOnuEthPortInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
    (0, "CDATA-GPON-MIB2", "gponOnuEthPortId"),
)
if mibBuilder.loadTexts:
    gponOnuEthPortInfoEntry.setStatus("current")


class _GponOnuEthPortSpeedAndDuplexInfo_Type(Integer32):
    """Custom type gponOnuEthPortSpeedAndDuplexInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("full10", 1),
          ("full100", 2),
          ("full1000", 3),
          ("half10", 17),
          ("half100", 18),
          ("half1000", 19))
    )


_GponOnuEthPortSpeedAndDuplexInfo_Type.__name__ = "Integer32"
_GponOnuEthPortSpeedAndDuplexInfo_Object = MibTableColumn
gponOnuEthPortSpeedAndDuplexInfo = _GponOnuEthPortSpeedAndDuplexInfo_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 2, 1, 1),
    _GponOnuEthPortSpeedAndDuplexInfo_Type()
)
gponOnuEthPortSpeedAndDuplexInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuEthPortSpeedAndDuplexInfo.setStatus("current")


class _GponOnuEthPortState_Type(Integer32):
    """Custom type gponOnuEthPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_GponOnuEthPortState_Type.__name__ = "Integer32"
_GponOnuEthPortState_Object = MibTableColumn
gponOnuEthPortState = _GponOnuEthPortState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 2, 1, 2),
    _GponOnuEthPortState_Type()
)
gponOnuEthPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuEthPortState.setStatus("current")
_GponOnuEthPortMacAddressTable_Object = MibTable
gponOnuEthPortMacAddressTable = _GponOnuEthPortMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 3)
)
if mibBuilder.loadTexts:
    gponOnuEthPortMacAddressTable.setStatus("current")
_GponOnuEthPortMacAddressEntry_Object = MibTableRow
gponOnuEthPortMacAddressEntry = _GponOnuEthPortMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 3, 1)
)
gponOnuEthPortMacAddressEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
    (0, "CDATA-GPON-MIB2", "gponOnuEthPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuEthPortMacAddressId"),
)
if mibBuilder.loadTexts:
    gponOnuEthPortMacAddressEntry.setStatus("current")
_GponOnuEthPortMacAddressId_Type = Integer32
_GponOnuEthPortMacAddressId_Object = MibTableColumn
gponOnuEthPortMacAddressId = _GponOnuEthPortMacAddressId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 3, 1, 1),
    _GponOnuEthPortMacAddressId_Type()
)
gponOnuEthPortMacAddressId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuEthPortMacAddressId.setStatus("current")
_GponOnuEthPortMacAddress_Type = GponMac
_GponOnuEthPortMacAddress_Object = MibTableColumn
gponOnuEthPortMacAddress = _GponOnuEthPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 19, 3, 1, 2),
    _GponOnuEthPortMacAddress_Type()
)
gponOnuEthPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuEthPortMacAddress.setStatus("current")
_GponOnuPotsPortObjects_ObjectIdentity = ObjectIdentity
gponOnuPotsPortObjects = _GponOnuPotsPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20)
)
_GponOnuPotsPortCfgTable_Object = MibTable
gponOnuPotsPortCfgTable = _GponOnuPotsPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 1)
)
if mibBuilder.loadTexts:
    gponOnuPotsPortCfgTable.setStatus("current")
_GponOnuPotsPortCfgEntry_Object = MibTableRow
gponOnuPotsPortCfgEntry = _GponOnuPotsPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 1, 1)
)
gponOnuPotsPortCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
    (0, "CDATA-GPON-MIB2", "gponOnuPotsPortId"),
)
if mibBuilder.loadTexts:
    gponOnuPotsPortCfgEntry.setStatus("current")
_GponOnuPotsPortId_Type = GponOnuPotsPortId
_GponOnuPotsPortId_Object = MibTableColumn
gponOnuPotsPortId = _GponOnuPotsPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 1, 1, 1),
    _GponOnuPotsPortId_Type()
)
gponOnuPotsPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuPotsPortId.setStatus("current")
_GponOnuPotsPortOperationalState_Type = GponSwitch
_GponOnuPotsPortOperationalState_Object = MibTableColumn
gponOnuPotsPortOperationalState = _GponOnuPotsPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 1, 1, 2),
    _GponOnuPotsPortOperationalState_Type()
)
gponOnuPotsPortOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuPotsPortOperationalState.setStatus("current")


class _GponOnuPotsPortCfgPotsProfileId_Type(GponPotsProfileId):
    """Custom type gponOnuPotsPortCfgPotsProfileId based on GponPotsProfileId"""
    defaultValue = 65535


_GponOnuPotsPortCfgPotsProfileId_Type.__name__ = "GponPotsProfileId"
_GponOnuPotsPortCfgPotsProfileId_Object = MibTableColumn
gponOnuPotsPortCfgPotsProfileId = _GponOnuPotsPortCfgPotsProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 1, 1, 3),
    _GponOnuPotsPortCfgPotsProfileId_Type()
)
gponOnuPotsPortCfgPotsProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuPotsPortCfgPotsProfileId.setStatus("current")
_GponOnuIpCfgTable_Object = MibTable
gponOnuIpCfgTable = _GponOnuIpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2)
)
if mibBuilder.loadTexts:
    gponOnuIpCfgTable.setStatus("current")
_GponOnuIpCfgEntry_Object = MibTableRow
gponOnuIpCfgEntry = _GponOnuIpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1)
)
gponOnuIpCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
    (0, "CDATA-GPON-MIB2", "gponOnuIpHostId"),
)
if mibBuilder.loadTexts:
    gponOnuIpCfgEntry.setStatus("current")


class _GponOnuIpHostId_Type(Integer32):
    """Custom type gponOnuIpHostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GponOnuIpHostId_Type.__name__ = "Integer32"
_GponOnuIpHostId_Object = MibTableColumn
gponOnuIpHostId = _GponOnuIpHostId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 1),
    _GponOnuIpHostId_Type()
)
gponOnuIpHostId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuIpHostId.setStatus("current")
_GponOnuIpCfgRowStatus_Type = RowStatus
_GponOnuIpCfgRowStatus_Object = MibTableColumn
gponOnuIpCfgRowStatus = _GponOnuIpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 2),
    _GponOnuIpCfgRowStatus_Type()
)
gponOnuIpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIpCfgRowStatus.setStatus("current")


class _GponOnuIpCfgMode_Type(Integer32):
    """Custom type gponOnuIpCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2))
    )


_GponOnuIpCfgMode_Type.__name__ = "Integer32"
_GponOnuIpCfgMode_Object = MibTableColumn
gponOnuIpCfgMode = _GponOnuIpCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 3),
    _GponOnuIpCfgMode_Type()
)
gponOnuIpCfgMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIpCfgMode.setStatus("current")
_GponOnuIpCfgVlanId_Type = Integer32
_GponOnuIpCfgVlanId_Object = MibTableColumn
gponOnuIpCfgVlanId = _GponOnuIpCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 4),
    _GponOnuIpCfgVlanId_Type()
)
gponOnuIpCfgVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIpCfgVlanId.setStatus("current")
_GponOnuIpCfgVlanPri_Type = Integer32
_GponOnuIpCfgVlanPri_Object = MibTableColumn
gponOnuIpCfgVlanPri = _GponOnuIpCfgVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 5),
    _GponOnuIpCfgVlanPri_Type()
)
gponOnuIpCfgVlanPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIpCfgVlanPri.setStatus("current")
_GponOnuIpCfgIp_Type = IpAddress
_GponOnuIpCfgIp_Object = MibTableColumn
gponOnuIpCfgIp = _GponOnuIpCfgIp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 6),
    _GponOnuIpCfgIp_Type()
)
gponOnuIpCfgIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIpCfgIp.setStatus("current")
_GponOnuIpCfgMask_Type = IpAddress
_GponOnuIpCfgMask_Object = MibTableColumn
gponOnuIpCfgMask = _GponOnuIpCfgMask_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 7),
    _GponOnuIpCfgMask_Type()
)
gponOnuIpCfgMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIpCfgMask.setStatus("current")
_GponOnuIpCfgGateway_Type = IpAddress
_GponOnuIpCfgGateway_Object = MibTableColumn
gponOnuIpCfgGateway = _GponOnuIpCfgGateway_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 8),
    _GponOnuIpCfgGateway_Type()
)
gponOnuIpCfgGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIpCfgGateway.setStatus("current")
_GponOnuIpCfgPriDns_Type = IpAddress
_GponOnuIpCfgPriDns_Object = MibTableColumn
gponOnuIpCfgPriDns = _GponOnuIpCfgPriDns_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 9),
    _GponOnuIpCfgPriDns_Type()
)
gponOnuIpCfgPriDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIpCfgPriDns.setStatus("current")
_GponOnuIpCfgSlaveDns_Type = IpAddress
_GponOnuIpCfgSlaveDns_Object = MibTableColumn
gponOnuIpCfgSlaveDns = _GponOnuIpCfgSlaveDns_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 10),
    _GponOnuIpCfgSlaveDns_Type()
)
gponOnuIpCfgSlaveDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIpCfgSlaveDns.setStatus("current")
_GponOnuIpCfgMacAddress_Type = GponMac
_GponOnuIpCfgMacAddress_Object = MibTableColumn
gponOnuIpCfgMacAddress = _GponOnuIpCfgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 2, 1, 11),
    _GponOnuIpCfgMacAddress_Type()
)
gponOnuIpCfgMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIpCfgMacAddress.setStatus("current")
_GponOnuSipPstnUserTable_Object = MibTable
gponOnuSipPstnUserTable = _GponOnuSipPstnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 3)
)
if mibBuilder.loadTexts:
    gponOnuSipPstnUserTable.setStatus("current")
_GponOnuSipPstnUserEntry_Object = MibTableRow
gponOnuSipPstnUserEntry = _GponOnuSipPstnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 3, 1)
)
gponOnuSipPstnUserEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
    (0, "CDATA-GPON-MIB2", "gponOnuSipPstnUserId"),
)
if mibBuilder.loadTexts:
    gponOnuSipPstnUserEntry.setStatus("current")
_GponOnuSipPstnUserId_Type = GponOnuPotsPortId
_GponOnuSipPstnUserId_Object = MibTableColumn
gponOnuSipPstnUserId = _GponOnuSipPstnUserId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 3, 1, 2),
    _GponOnuSipPstnUserId_Type()
)
gponOnuSipPstnUserId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserId.setStatus("current")
_GponOnuSipPstnUserRowStatus_Type = RowStatus
_GponOnuSipPstnUserRowStatus_Object = MibTableColumn
gponOnuSipPstnUserRowStatus = _GponOnuSipPstnUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 3, 1, 3),
    _GponOnuSipPstnUserRowStatus_Type()
)
gponOnuSipPstnUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserRowStatus.setStatus("current")


class _GponOnuSipPstnUserName_Type(OctetString):
    """Custom type gponOnuSipPstnUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_GponOnuSipPstnUserName_Type.__name__ = "OctetString"
_GponOnuSipPstnUserName_Object = MibTableColumn
gponOnuSipPstnUserName = _GponOnuSipPstnUserName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 3, 1, 4),
    _GponOnuSipPstnUserName_Type()
)
gponOnuSipPstnUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserName.setStatus("current")


class _GponOnuSipPstnUserPassword_Type(OctetString):
    """Custom type gponOnuSipPstnUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_GponOnuSipPstnUserPassword_Type.__name__ = "OctetString"
_GponOnuSipPstnUserPassword_Object = MibTableColumn
gponOnuSipPstnUserPassword = _GponOnuSipPstnUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 3, 1, 5),
    _GponOnuSipPstnUserPassword_Type()
)
gponOnuSipPstnUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserPassword.setStatus("current")


class _GponOnuSipPstnUserTelephoneNumber_Type(OctetString):
    """Custom type gponOnuSipPstnUserTelephoneNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GponOnuSipPstnUserTelephoneNumber_Type.__name__ = "OctetString"
_GponOnuSipPstnUserTelephoneNumber_Object = MibTableColumn
gponOnuSipPstnUserTelephoneNumber = _GponOnuSipPstnUserTelephoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 3, 1, 6),
    _GponOnuSipPstnUserTelephoneNumber_Type()
)
gponOnuSipPstnUserTelephoneNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserTelephoneNumber.setStatus("current")


class _GponOnuSipPstnUserAgentProfileId_Type(GponSipAgentProfileId):
    """Custom type gponOnuSipPstnUserAgentProfileId based on GponSipAgentProfileId"""
    defaultValue = 65535


_GponOnuSipPstnUserAgentProfileId_Type.__name__ = "GponSipAgentProfileId"
_GponOnuSipPstnUserAgentProfileId_Object = MibTableColumn
gponOnuSipPstnUserAgentProfileId = _GponOnuSipPstnUserAgentProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 3, 1, 7),
    _GponOnuSipPstnUserAgentProfileId_Type()
)
gponOnuSipPstnUserAgentProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserAgentProfileId.setStatus("current")


class _GponOnuSipPstnUserDigitMapProfileId_Type(GponDigitMapProfileId):
    """Custom type gponOnuSipPstnUserDigitMapProfileId based on GponDigitMapProfileId"""
    defaultValue = 65535


_GponOnuSipPstnUserDigitMapProfileId_Type.__name__ = "GponDigitMapProfileId"
_GponOnuSipPstnUserDigitMapProfileId_Object = MibTableColumn
gponOnuSipPstnUserDigitMapProfileId = _GponOnuSipPstnUserDigitMapProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 3, 1, 8),
    _GponOnuSipPstnUserDigitMapProfileId_Type()
)
gponOnuSipPstnUserDigitMapProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserDigitMapProfileId.setStatus("current")


class _GponOnuSipPstnUserSipRightFlagProfileId_Type(GponSipRightFlagProfileId):
    """Custom type gponOnuSipPstnUserSipRightFlagProfileId based on GponSipRightFlagProfileId"""
    defaultValue = 65535


_GponOnuSipPstnUserSipRightFlagProfileId_Type.__name__ = "GponSipRightFlagProfileId"
_GponOnuSipPstnUserSipRightFlagProfileId_Object = MibTableColumn
gponOnuSipPstnUserSipRightFlagProfileId = _GponOnuSipPstnUserSipRightFlagProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 3, 1, 9),
    _GponOnuSipPstnUserSipRightFlagProfileId_Type()
)
gponOnuSipPstnUserSipRightFlagProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserSipRightFlagProfileId.setStatus("current")
_GponOnuSipPstnUserInfoTable_Object = MibTable
gponOnuSipPstnUserInfoTable = _GponOnuSipPstnUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 4)
)
if mibBuilder.loadTexts:
    gponOnuSipPstnUserInfoTable.setStatus("current")
_GponOnuSipPstnUserInfoEntry_Object = MibTableRow
gponOnuSipPstnUserInfoEntry = _GponOnuSipPstnUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 4, 1)
)
gponOnuSipPstnUserInfoEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
    (0, "CDATA-GPON-MIB2", "gponOnuSipPstnUserId"),
)
if mibBuilder.loadTexts:
    gponOnuSipPstnUserInfoEntry.setStatus("current")


class _GponOnuSipPstnUserState_Type(Integer32):
    """Custom type gponOnuSipPstnUserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_GponOnuSipPstnUserState_Type.__name__ = "Integer32"
_GponOnuSipPstnUserState_Object = MibTableColumn
gponOnuSipPstnUserState = _GponOnuSipPstnUserState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 4, 1, 1),
    _GponOnuSipPstnUserState_Type()
)
gponOnuSipPstnUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserState.setStatus("current")


class _GponOnuSipPstnUserHookState_Type(Integer32):
    """Custom type gponOnuSipPstnUserHookState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onhook", 1),
          ("offhook", 2))
    )


_GponOnuSipPstnUserHookState_Type.__name__ = "Integer32"
_GponOnuSipPstnUserHookState_Object = MibTableColumn
gponOnuSipPstnUserHookState = _GponOnuSipPstnUserHookState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 4, 1, 2),
    _GponOnuSipPstnUserHookState_Type()
)
gponOnuSipPstnUserHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserHookState.setStatus("current")
_GponOnuSipPstnUserCodec_Type = DisplayString
_GponOnuSipPstnUserCodec_Object = MibTableColumn
gponOnuSipPstnUserCodec = _GponOnuSipPstnUserCodec_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 4, 1, 3),
    _GponOnuSipPstnUserCodec_Type()
)
gponOnuSipPstnUserCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserCodec.setStatus("current")
_GponOnuSipPstnUserServerStatus_Type = DisplayString
_GponOnuSipPstnUserServerStatus_Object = MibTableColumn
gponOnuSipPstnUserServerStatus = _GponOnuSipPstnUserServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 4, 1, 4),
    _GponOnuSipPstnUserServerStatus_Type()
)
gponOnuSipPstnUserServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserServerStatus.setStatus("current")
_GponOnuSipPstnUserSessionType_Type = DisplayString
_GponOnuSipPstnUserSessionType_Object = MibTableColumn
gponOnuSipPstnUserSessionType = _GponOnuSipPstnUserSessionType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 20, 4, 1, 5),
    _GponOnuSipPstnUserSessionType_Type()
)
gponOnuSipPstnUserSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuSipPstnUserSessionType.setStatus("current")
_GponOnuCatvPortObjects_ObjectIdentity = ObjectIdentity
gponOnuCatvPortObjects = _GponOnuCatvPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 21)
)
_GponOnuCatvPortCfgTable_Object = MibTable
gponOnuCatvPortCfgTable = _GponOnuCatvPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 21, 1)
)
if mibBuilder.loadTexts:
    gponOnuCatvPortCfgTable.setStatus("current")
_GponOnuCatvPortCfgEntry_Object = MibTableRow
gponOnuCatvPortCfgEntry = _GponOnuCatvPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 21, 1, 1)
)
gponOnuCatvPortCfgEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponOltDeviceId"),
    (0, "CDATA-GPON-MIB2", "gponOltCardId"),
    (0, "CDATA-GPON-MIB2", "gponOltPortId"),
    (0, "CDATA-GPON-MIB2", "gponOnuId"),
    (0, "CDATA-GPON-MIB2", "gponOnuCatvPortId"),
)
if mibBuilder.loadTexts:
    gponOnuCatvPortCfgEntry.setStatus("current")


class _GponOnuCatvPortId_Type(Integer32):
    """Custom type gponOnuCatvPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GponOnuCatvPortId_Type.__name__ = "Integer32"
_GponOnuCatvPortId_Object = MibTableColumn
gponOnuCatvPortId = _GponOnuCatvPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 21, 1, 1, 1),
    _GponOnuCatvPortId_Type()
)
gponOnuCatvPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuCatvPortId.setStatus("current")
_GponOnuCatvPortOperationalState_Type = GponSwitch
_GponOnuCatvPortOperationalState_Object = MibTableColumn
gponOnuCatvPortOperationalState = _GponOnuCatvPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2, 21, 1, 1, 2),
    _GponOnuCatvPortOperationalState_Type()
)
gponOnuCatvPortOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuCatvPortOperationalState.setStatus("current")
_GponAlarmObjects_ObjectIdentity = ObjectIdentity
gponAlarmObjects = _GponAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4)
)
_GponNotifications_ObjectIdentity = ObjectIdentity
gponNotifications = _GponNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 1)
)
_GponTrapObjects_ObjectIdentity = ObjectIdentity
gponTrapObjects = _GponTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 6)
)
_GponTrapId_Type = Integer32
_GponTrapId_Object = MibScalar
gponTrapId = _GponTrapId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 6, 1),
    _GponTrapId_Type()
)
gponTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTrapId.setStatus("current")


class _GponTrapState_Type(Integer32):
    """Custom type gponTrapState based on Integer32"""
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
          ("report", 1),
          ("clear", 2))
    )


_GponTrapState_Type.__name__ = "Integer32"
_GponTrapState_Object = MibScalar
gponTrapState = _GponTrapState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 6, 2),
    _GponTrapState_Type()
)
gponTrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTrapState.setStatus("current")


class _GponTrapParameters_Type(Bits):
    """Custom type gponTrapParameters based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("oltPortId", 1),
          ("onuId", 2),
          ("onuSn", 3),
          ("password", 4),
          ("rogueOnuSn", 5))
    )

_GponTrapParameters_Type.__name__ = "Bits"
_GponTrapParameters_Object = MibScalar
gponTrapParameters = _GponTrapParameters_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 6, 3),
    _GponTrapParameters_Type()
)
gponTrapParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTrapParameters.setStatus("current")


class _GponTrapOltPortId_Type(Integer32):
    """Custom type gponTrapOltPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
        ValueRangeConstraint(65535, 65535),
    )


_GponTrapOltPortId_Type.__name__ = "Integer32"
_GponTrapOltPortId_Object = MibScalar
gponTrapOltPortId = _GponTrapOltPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 6, 4),
    _GponTrapOltPortId_Type()
)
gponTrapOltPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTrapOltPortId.setStatus("current")


class _GponTrapOnuId_Type(Integer32):
    """Custom type gponTrapOnuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
        ValueRangeConstraint(65535, 65535),
    )


_GponTrapOnuId_Type.__name__ = "Integer32"
_GponTrapOnuId_Object = MibScalar
gponTrapOnuId = _GponTrapOnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 6, 5),
    _GponTrapOnuId_Type()
)
gponTrapOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTrapOnuId.setStatus("current")
_GponTrapOnuSn_Type = DisplayString
_GponTrapOnuSn_Object = MibScalar
gponTrapOnuSn = _GponTrapOnuSn_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 6, 6),
    _GponTrapOnuSn_Type()
)
gponTrapOnuSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTrapOnuSn.setStatus("current")
_GponTrapOnuPassword_Type = DisplayString
_GponTrapOnuPassword_Object = MibScalar
gponTrapOnuPassword = _GponTrapOnuPassword_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 6, 7),
    _GponTrapOnuPassword_Type()
)
gponTrapOnuPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTrapOnuPassword.setStatus("current")
_GponTrapRogueOnuSn_Type = DisplayString
_GponTrapRogueOnuSn_Object = MibScalar
gponTrapRogueOnuSn = _GponTrapRogueOnuSn_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 6, 8),
    _GponTrapRogueOnuSn_Type()
)
gponTrapRogueOnuSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTrapRogueOnuSn.setStatus("current")
_GponManagementObjects_ObjectIdentity = ObjectIdentity
gponManagementObjects = _GponManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 8)
)
_GponManagementAddrTable_Object = MibTable
gponManagementAddrTable = _GponManagementAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 8, 1)
)
if mibBuilder.loadTexts:
    gponManagementAddrTable.setStatus("current")
_GponManagementAddrEntry_Object = MibTableRow
gponManagementAddrEntry = _GponManagementAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 8, 1, 1)
)
gponManagementAddrEntry.setIndexNames(
    (0, "CDATA-GPON-MIB2", "gponManagementAddrName"),
)
if mibBuilder.loadTexts:
    gponManagementAddrEntry.setStatus("current")


class _GponManagementAddrName_Type(OctetString):
    """Custom type gponManagementAddrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GponManagementAddrName_Type.__name__ = "OctetString"
_GponManagementAddrName_Object = MibTableColumn
gponManagementAddrName = _GponManagementAddrName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 8, 1, 1, 1),
    _GponManagementAddrName_Type()
)
gponManagementAddrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponManagementAddrName.setStatus("current")
_GponManagementAddrRowStatus_Type = RowStatus
_GponManagementAddrRowStatus_Object = MibTableColumn
gponManagementAddrRowStatus = _GponManagementAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 8, 1, 1, 2),
    _GponManagementAddrRowStatus_Type()
)
gponManagementAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponManagementAddrRowStatus.setStatus("current")


class _GponManagementAddrTAddress_Type(OctetString):
    """Custom type gponManagementAddrTAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_GponManagementAddrTAddress_Type.__name__ = "OctetString"
_GponManagementAddrTAddress_Object = MibTableColumn
gponManagementAddrTAddress = _GponManagementAddrTAddress_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 8, 1, 1, 3),
    _GponManagementAddrTAddress_Type()
)
gponManagementAddrTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponManagementAddrTAddress.setStatus("current")


class _GponManagementAddrCommunity_Type(OctetString):
    """Custom type gponManagementAddrCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GponManagementAddrCommunity_Type.__name__ = "OctetString"
_GponManagementAddrCommunity_Object = MibTableColumn
gponManagementAddrCommunity = _GponManagementAddrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 8, 1, 1, 4),
    _GponManagementAddrCommunity_Type()
)
gponManagementAddrCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponManagementAddrCommunity.setStatus("current")
_GponConformance_ObjectIdentity = ObjectIdentity
gponConformance = _GponConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64)
)
_GponCompliances_ObjectIdentity = ObjectIdentity
gponCompliances = _GponCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 1)
)
_GponGroups_ObjectIdentity = ObjectIdentity
gponGroups = _GponGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2)
)
_GponProfileGroups_ObjectIdentity = ObjectIdentity
gponProfileGroups = _GponProfileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 1)
)
_GponControlGroups_ObjectIdentity = ObjectIdentity
gponControlGroups = _GponControlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 2)
)
_GponTrapGroups_ObjectIdentity = ObjectIdentity
gponTrapGroups = _GponTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 4)
)

# Managed Objects groups

gponDbaProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 1, 1)
)
gponDbaProfileGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponDbaProfileFixRate"),
        ("CDATA-GPON-MIB2", "gponDbaProfileBindNum"),
        ("CDATA-GPON-MIB2", "gponDbaProfileName"),
        ("CDATA-GPON-MIB2", "gponDbaProfileRowStatus"),
        ("CDATA-GPON-MIB2", "gponDbaProfileMaxRate"),
        ("CDATA-GPON-MIB2", "gponDbaProfileType"),
        ("CDATA-GPON-MIB2", "gponDbaProfileAssureRate"))
)
if mibBuilder.loadTexts:
    gponDbaProfileGroup.setStatus("current")

gponLineProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 1, 2)
)
gponLineProfileGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponLineProfileRowStatus"),
        ("CDATA-GPON-MIB2", "gponLineProfileName"),
        ("CDATA-GPON-MIB2", "gponLineProfileMappingMode"),
        ("CDATA-GPON-MIB2", "gponLineProfileTcontNum"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemNum"),
        ("CDATA-GPON-MIB2", "gponLineProfileBindNum"),
        ("CDATA-GPON-MIB2", "gponLineProfileTcontId"),
        ("CDATA-GPON-MIB2", "gponLineProfileTcontRowStatus"),
        ("CDATA-GPON-MIB2", "gponLineProfileTcontDbaProfileId"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemId"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemRowStatus"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemTcontId"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemUpCar"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemDownCar"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemMapNum"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemMapId"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemMapRowStatus"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemMapPriority"),
        ("CDATA-GPON-MIB2", "gponLineProfileGemMapVlan"))
)
if mibBuilder.loadTexts:
    gponLineProfileGroup.setStatus("current")

gponSrvProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 1, 3)
)
gponSrvProfileGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponSrvProfileId"),
        ("CDATA-GPON-MIB2", "gponSrvProfileRowStatus"),
        ("CDATA-GPON-MIB2", "gponSrvProfileName"),
        ("CDATA-GPON-MIB2", "gponSrvProfileBindNum"),
        ("CDATA-GPON-MIB2", "gponSrvProfileMcMode"),
        ("CDATA-GPON-MIB2", "gponSrvProfileUpIgmpFwdMode"),
        ("CDATA-GPON-MIB2", "gponSrvProfileUpIgmpTCI"),
        ("CDATA-GPON-MIB2", "gponSrvProfileDnMcMode"),
        ("CDATA-GPON-MIB2", "gponSrvProfileDnMcTCI"),
        ("CDATA-GPON-MIB2", "gponSrvProfileEthNum"),
        ("CDATA-GPON-MIB2", "gponSrvProfilePotsNum"),
        ("CDATA-GPON-MIB2", "gponSrvProfilePortType"),
        ("CDATA-GPON-MIB2", "gponSrvProfilePortId"),
        ("CDATA-GPON-MIB2", "gponSrvProfilePortCvlan"),
        ("CDATA-GPON-MIB2", "gponSrvProfilePortVlanRowStatus"),
        ("CDATA-GPON-MIB2", "gponSrvProfilePortVlanMode"),
        ("CDATA-GPON-MIB2", "gponSrvProfilePortVlanSvlan"))
)
if mibBuilder.loadTexts:
    gponSrvProfileGroup.setStatus("current")

gponTrafficProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 1, 4)
)
gponTrafficProfileGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponTrafficProfileId"),
        ("CDATA-GPON-MIB2", "gponTrafficProfileRowStatus"),
        ("CDATA-GPON-MIB2", "gponTrafficProfileName"),
        ("CDATA-GPON-MIB2", "gponTrafficProfileBindNum"),
        ("CDATA-GPON-MIB2", "gponTrafficProfileCfgCir"),
        ("CDATA-GPON-MIB2", "gponTrafficProfileCfgPir"),
        ("CDATA-GPON-MIB2", "gponTrafficProfileCfgCbs"),
        ("CDATA-GPON-MIB2", "gponTrafficProfileCfgPbs"))
)
if mibBuilder.loadTexts:
    gponTrafficProfileGroup.setStatus("current")

gponSipAgentProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 1, 5)
)
gponSipAgentProfileGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponSipAgentProfileRowStatus"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileName"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileBindNum"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileProxyServerUri"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileRtpDscp"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileRtpMinPort"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileRtpMaxPort"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileSignalDscp"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileSignalPort"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileSignalTransferMode"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileRegistrationExpiration"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileRegistrationReregHeadStartTime"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileRegistrationServerUri"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileVoiceMailServerUri"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileVoiceMailSubscriptionExpiration"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileConfFactory"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileBridgedLineAgent"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileAuthRealm"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileBindPotsList"))
)
if mibBuilder.loadTexts:
    gponSipAgentProfileGroup.setStatus("current")

gponSipRightFlagProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 1, 6)
)
gponSipRightFlagProfileGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponSipRightFlagProfileId"),
        ("CDATA-GPON-MIB2", "gponSipRightFlagProfileRowStatus"),
        ("CDATA-GPON-MIB2", "gponSipRightFlagProfileName"),
        ("CDATA-GPON-MIB2", "gponSipRightFlagProfileBindNum"),
        ("CDATA-GPON-MIB2", "gponSipRightFlagProfileCallWaiting"),
        ("CDATA-GPON-MIB2", "gponSipRightFlagProfileCallProcess"),
        ("CDATA-GPON-MIB2", "gponSipRightFlagProfileCallPresentation"),
        ("CDATA-GPON-MIB2", "gponSipRightFlagProfileHotline"),
        ("CDATA-GPON-MIB2", "gponSipRightFlagProfileHotlineNum"),
        ("CDATA-GPON-MIB2", "gponSipRightFlagProfileBindPotsList"))
)
if mibBuilder.loadTexts:
    gponSipRightFlagProfileGroup.setStatus("current")

gponDigitMapProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 1, 7)
)
gponDigitMapProfileGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponDigitMapProfileId"),
        ("CDATA-GPON-MIB2", "gponDigitMapProfileRowStatus"),
        ("CDATA-GPON-MIB2", "gponDigitMapProfileName"),
        ("CDATA-GPON-MIB2", "gponDigitMapProfileBindNum"),
        ("CDATA-GPON-MIB2", "gponDigitMapProfileCriticalDialTime"),
        ("CDATA-GPON-MIB2", "gponDigitMapProfileDialPlanId"),
        ("CDATA-GPON-MIB2", "gponDigitMapProfileDialPlanRowStatus"),
        ("CDATA-GPON-MIB2", "gponDigitMapProfileDialPlanToken"),
        ("CDATA-GPON-MIB2", "gponDigitMapProfileBindPotsList"))
)
if mibBuilder.loadTexts:
    gponDigitMapProfileGroup.setStatus("current")

gponPotsProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 1, 8)
)
gponPotsProfileGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponPotsProfileId"),
        ("CDATA-GPON-MIB2", "gponPotsProfileRowStatus"),
        ("CDATA-GPON-MIB2", "gponPotsProfileName"),
        ("CDATA-GPON-MIB2", "gponPotsProfileBindNum"),
        ("CDATA-GPON-MIB2", "gponPotsProfileImpedance"),
        ("CDATA-GPON-MIB2", "gponPotsProfileSignallingCode"),
        ("CDATA-GPON-MIB2", "gponPotsProfileRxGain"),
        ("CDATA-GPON-MIB2", "gponPotsProfileTxGain"),
        ("CDATA-GPON-MIB2", "gponPotsProfileBindPotsList"))
)
if mibBuilder.loadTexts:
    gponPotsProfileGroup.setStatus("current")

gponControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 2, 1)
)
gponControlGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponOltPortAutoFindSwitch"),
        ("CDATA-GPON-MIB2", "gponOltPortSwitch"),
        ("CDATA-GPON-MIB2", "gponOltPortStatus"),
        ("CDATA-GPON-MIB2", "gponOltPortDdmTemperature"),
        ("CDATA-GPON-MIB2", "gponOltPortDdmVoltage"),
        ("CDATA-GPON-MIB2", "gponOltPortDdmTxBiasCurrent"),
        ("CDATA-GPON-MIB2", "gponOltPortDdmTxPower"),
        ("CDATA-GPON-MIB2", "gponOltPortDdmRxPower"),
        ("CDATA-GPON-MIB2", "gponOltTransceiverVendor"),
        ("CDATA-GPON-MIB2", "gponOltTransceiverProductName"),
        ("CDATA-GPON-MIB2", "gponOltTransceiverVersion"),
        ("CDATA-GPON-MIB2", "gponOltTransceiverSerialNumber"),
        ("CDATA-GPON-MIB2", "gponOnuId"),
        ("CDATA-GPON-MIB2", "gponOnuRowStatus"),
        ("CDATA-GPON-MIB2", "gponOnuAuthMode"),
        ("CDATA-GPON-MIB2", "gponOnuSn"),
        ("CDATA-GPON-MIB2", "gponOnuPassword"),
        ("CDATA-GPON-MIB2", "gponOnuLineProfileId"),
        ("CDATA-GPON-MIB2", "gponOnuServiceProfileId"),
        ("CDATA-GPON-MIB2", "gponOnuDescription"),
        ("CDATA-GPON-MIB2", "gponOnuRunState"),
        ("CDATA-GPON-MIB2", "gponOnuConfigState"),
        ("CDATA-GPON-MIB2", "gponOnuMatchState"),
        ("CDATA-GPON-MIB2", "gponOnuDistance"),
        ("CDATA-GPON-MIB2", "gponOnuPonPortNum"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortNum"),
        ("CDATA-GPON-MIB2", "gponOnuPotsPortNum"),
        ("CDATA-GPON-MIB2", "gponOnuGemPortNum"),
        ("CDATA-GPON-MIB2", "gponOnuTcontNum"),
        ("CDATA-GPON-MIB2", "gponOnuFlowControlType"),
        ("CDATA-GPON-MIB2", "gponOnuReset"),
        ("CDATA-GPON-MIB2", "gponOnuDeactive"),
        ("CDATA-GPON-MIB2", "gponOnuAutofindRowStatus"),
        ("CDATA-GPON-MIB2", "gponOnuAutofindSn"),
        ("CDATA-GPON-MIB2", "gponOnuAutofindPassword"),
        ("CDATA-GPON-MIB2", "gponOnuAutofindVendorId"),
        ("CDATA-GPON-MIB2", "gponOnuAutofindVersion"),
        ("CDATA-GPON-MIB2", "gponOnuAutofindEquipmentID"),
        ("CDATA-GPON-MIB2", "gponOnuAutofindSoftwareVersion"),
        ("CDATA-GPON-MIB2", "gponOnuAutofindTime"),
        ("CDATA-GPON-MIB2", "gponOnuOpticalVoltage"),
        ("CDATA-GPON-MIB2", "gponOnuOpticalTxPower"),
        ("CDATA-GPON-MIB2", "gponOnuOpticalRxPower"),
        ("CDATA-GPON-MIB2", "gponOnuOpticalLaserBiasCurrent"),
        ("CDATA-GPON-MIB2", "gponOnuOpticalTemperature"),
        ("CDATA-GPON-MIB2", "gponOnuMainSoftwareVersion"),
        ("CDATA-GPON-MIB2", "gponOnuStandbySoftwareVersion"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortId"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortNativeVlanId"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortNativeVlanPriority"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortInboundCarId"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortOutboundCarId"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortSpeedAndDuplex"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortFlowCtrl"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortOperationalState"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortSpeedAndDuplexInfo"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortState"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortMacAddressId"),
        ("CDATA-GPON-MIB2", "gponOnuEthPortMacAddress"),
        ("CDATA-GPON-MIB2", "gponOnuPotsPortId"),
        ("CDATA-GPON-MIB2", "gponOnuPotsPortOperationalState"),
        ("CDATA-GPON-MIB2", "gponOnuPotsPortCfgPotsProfileId"),
        ("CDATA-GPON-MIB2", "gponOnuIpCfgRowStatus"),
        ("CDATA-GPON-MIB2", "gponOnuIpCfgMode"),
        ("CDATA-GPON-MIB2", "gponOnuIpCfgVlanId"),
        ("CDATA-GPON-MIB2", "gponOnuIpCfgVlanPri"),
        ("CDATA-GPON-MIB2", "gponOnuIpCfgIp"),
        ("CDATA-GPON-MIB2", "gponOnuIpCfgMask"),
        ("CDATA-GPON-MIB2", "gponOnuIpCfgGateway"),
        ("CDATA-GPON-MIB2", "gponOnuIpCfgPriDns"),
        ("CDATA-GPON-MIB2", "gponOnuIpCfgSlaveDns"),
        ("CDATA-GPON-MIB2", "gponOnuIpCfgMacAddress"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserRowStatus"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserName"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserPassword"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserTelephoneNumber"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserAgentProfileId"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserDigitMapProfileId"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserSipRightFlagProfileId"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserState"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserHookState"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserCodec"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserServerStatus"),
        ("CDATA-GPON-MIB2", "gponOnuSipPstnUserSessionType"))
)
if mibBuilder.loadTexts:
    gponControlGroup.setStatus("current")

gponTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 4, 1)
)
gponTrapGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponTrapOltPortId"),
        ("CDATA-GPON-MIB2", "gponTrapOnuId"),
        ("CDATA-GPON-MIB2", "gponTrapOnuSn"))
)
if mibBuilder.loadTexts:
    gponTrapGroup.setStatus("current")


# Notification objects

gponAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4, 1, 1)
)
gponAlarmNotification.setObjects(
      *(("CDATA-GPON-MIB2", "gponTrapId"),
        ("CDATA-GPON-MIB2", "gponTrapState"),
        ("CDATA-GPON-MIB2", "gponTrapOltPortId"),
        ("CDATA-GPON-MIB2", "gponTrapOnuId"),
        ("CDATA-GPON-MIB2", "gponTrapOnuSn"),
        ("CDATA-GPON-MIB2", "gponTrapOnuPassword"),
        ("CDATA-GPON-MIB2", "gponTrapRogueOnuSn"),
        ("CDATA-GPON-MIB2", "gponTrapParameters"))
)
if mibBuilder.loadTexts:
    gponAlarmNotification.setStatus(
        "current"
    )


# Notifications groups

gponTrapTypeGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 2, 4, 2)
)
gponTrapTypeGroup.setObjects(
      *(("CDATA-GPON-MIB2", "gponTrapOltPortId"),
        ("CDATA-GPON-MIB2", "gponTrapOnuId"),
        ("CDATA-GPON-MIB2", "gponTrapOnuSn"))
)
if mibBuilder.loadTexts:
    gponTrapTypeGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

gponCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 64, 1, 1)
)
gponCompliance.setObjects(
      *(("CDATA-GPON-MIB2", "gponDbaProfileGroup"),
        ("CDATA-GPON-MIB2", "gponLineProfileGroup"),
        ("CDATA-GPON-MIB2", "gponSrvProfileGroup"),
        ("CDATA-GPON-MIB2", "gponTrafficProfileGroup"),
        ("CDATA-GPON-MIB2", "gponSipAgentProfileGroup"),
        ("CDATA-GPON-MIB2", "gponSipRightFlagProfileGroup"),
        ("CDATA-GPON-MIB2", "gponDigitMapProfileGroup"),
        ("CDATA-GPON-MIB2", "gponPotsProfileGroup"))
)
if mibBuilder.loadTexts:
    gponCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CDATA-GPON-MIB2",
    **{"GponDbaProfileId": GponDbaProfileId,
       "GponDbaProfileName": GponDbaProfileName,
       "GponLinePorfileId": GponLinePorfileId,
       "GponLinePorfileName": GponLinePorfileName,
       "GponLinePorfileTcontId": GponLinePorfileTcontId,
       "GponLinePorfileGemId": GponLinePorfileGemId,
       "GponLinePorfileGemMapId": GponLinePorfileGemMapId,
       "GponVlanPriority": GponVlanPriority,
       "GponSrvProfileId": GponSrvProfileId,
       "GponSrvProfileName": GponSrvProfileName,
       "GponVlanId": GponVlanId,
       "GponTrafficProfileId": GponTrafficProfileId,
       "GponTrafficProfileName": GponTrafficProfileName,
       "GponSipAgentProfileId": GponSipAgentProfileId,
       "GponSipAgentProfileName": GponSipAgentProfileName,
       "GponSipUri": GponSipUri,
       "GponSipRightFlagProfileId": GponSipRightFlagProfileId,
       "GponSipRightFlagProfileName": GponSipRightFlagProfileName,
       "GponDigitMapProfileId": GponDigitMapProfileId,
       "GponPotsProfileId": GponPotsProfileId,
       "GponDeviceId": GponDeviceId,
       "GponCardId": GponCardId,
       "GponOltPortId": GponOltPortId,
       "GponSwitch": GponSwitch,
       "GponOltAutoAuthRuleId": GponOltAutoAuthRuleId,
       "GponOnuId": GponOnuId,
       "GponOnuSn": GponOnuSn,
       "GponOnuPassword": GponOnuPassword,
       "GponOnuLoid": GponOnuLoid,
       "GponOnuLoidPassword": GponOnuLoidPassword,
       "GponOnuEthPortId": GponOnuEthPortId,
       "GponMac": GponMac,
       "GponOnuPotsPortId": GponOnuPotsPortId,
       "gponMIB": gponMIB,
       "gponObjects": gponObjects,
       "gponProfileObjects": gponProfileObjects,
       "gponDbaProfileObjects": gponDbaProfileObjects,
       "gponDbaProfileInfoTable": gponDbaProfileInfoTable,
       "gponDbaProfileInfoEntry": gponDbaProfileInfoEntry,
       "gponDbaProfileId": gponDbaProfileId,
       "gponDbaProfileRowStatus": gponDbaProfileRowStatus,
       "gponDbaProfileName": gponDbaProfileName,
       "gponDbaProfileBindNum": gponDbaProfileBindNum,
       "gponDbaProfileCfgTable": gponDbaProfileCfgTable,
       "gponDbaProfileCfgEntry": gponDbaProfileCfgEntry,
       "gponDbaProfileType": gponDbaProfileType,
       "gponDbaProfileFixRate": gponDbaProfileFixRate,
       "gponDbaProfileAssureRate": gponDbaProfileAssureRate,
       "gponDbaProfileMaxRate": gponDbaProfileMaxRate,
       "gponDbaProfileBindInfoTable": gponDbaProfileBindInfoTable,
       "gponDbaProfileBindInfoEntry": gponDbaProfileBindInfoEntry,
       "gponDbaProfileBindLineProfileTcontList": gponDbaProfileBindLineProfileTcontList,
       "gponLineProfileObjects": gponLineProfileObjects,
       "gponLineProfileInfoTable": gponLineProfileInfoTable,
       "gponLineProfileInfoEntry": gponLineProfileInfoEntry,
       "gponLineProfileId": gponLineProfileId,
       "gponLineProfileRowStatus": gponLineProfileRowStatus,
       "gponLineProfileName": gponLineProfileName,
       "gponLineProfileMappingMode": gponLineProfileMappingMode,
       "gponLineProfileTcontNum": gponLineProfileTcontNum,
       "gponLineProfileGemNum": gponLineProfileGemNum,
       "gponLineProfileBindNum": gponLineProfileBindNum,
       "gponLineProfileTcontTable": gponLineProfileTcontTable,
       "gponLineProfileTcontEntry": gponLineProfileTcontEntry,
       "gponLineProfileTcontId": gponLineProfileTcontId,
       "gponLineProfileTcontRowStatus": gponLineProfileTcontRowStatus,
       "gponLineProfileTcontDbaProfileId": gponLineProfileTcontDbaProfileId,
       "gponLineProfileGemTable": gponLineProfileGemTable,
       "gponLineProfileGemEntry": gponLineProfileGemEntry,
       "gponLineProfileGemId": gponLineProfileGemId,
       "gponLineProfileGemRowStatus": gponLineProfileGemRowStatus,
       "gponLineProfileGemTcontId": gponLineProfileGemTcontId,
       "gponLineProfileGemUpCar": gponLineProfileGemUpCar,
       "gponLineProfileGemDownCar": gponLineProfileGemDownCar,
       "gponLineProfileGemMapNum": gponLineProfileGemMapNum,
       "gponLineProfileGemMapTable": gponLineProfileGemMapTable,
       "gponLineProfileGemMapEntry": gponLineProfileGemMapEntry,
       "gponLineProfileGemMapId": gponLineProfileGemMapId,
       "gponLineProfileGemMapRowStatus": gponLineProfileGemMapRowStatus,
       "gponLineProfileGemMapVlan": gponLineProfileGemMapVlan,
       "gponLineProfileGemMapPriority": gponLineProfileGemMapPriority,
       "gponLineProfileBindInfoTable": gponLineProfileBindInfoTable,
       "gponLineProfileBindInfoEntry": gponLineProfileBindInfoEntry,
       "gponLineProfileBindOnuList": gponLineProfileBindOnuList,
       "gponSrvProfileObjects": gponSrvProfileObjects,
       "gponSrvProfileInfoTable": gponSrvProfileInfoTable,
       "gponSrvProfileInfoEntry": gponSrvProfileInfoEntry,
       "gponSrvProfileId": gponSrvProfileId,
       "gponSrvProfileRowStatus": gponSrvProfileRowStatus,
       "gponSrvProfileName": gponSrvProfileName,
       "gponSrvProfileBindNum": gponSrvProfileBindNum,
       "gponSrvProfileCfgTable": gponSrvProfileCfgTable,
       "gponSrvProfileCfgEntry": gponSrvProfileCfgEntry,
       "gponSrvProfileMcMode": gponSrvProfileMcMode,
       "gponSrvProfileUpIgmpFwdMode": gponSrvProfileUpIgmpFwdMode,
       "gponSrvProfileUpIgmpTCI": gponSrvProfileUpIgmpTCI,
       "gponSrvProfileDnMcMode": gponSrvProfileDnMcMode,
       "gponSrvProfileDnMcTCI": gponSrvProfileDnMcTCI,
       "gponSrvProfilePortNumTable": gponSrvProfilePortNumTable,
       "gponSrvProfilePortNumEntry": gponSrvProfilePortNumEntry,
       "gponSrvProfileEthNum": gponSrvProfileEthNum,
       "gponSrvProfilePotsNum": gponSrvProfilePotsNum,
       "gponSrvProfileCatvNum": gponSrvProfileCatvNum,
       "gponSrvProfilePortVlanCfgTable": gponSrvProfilePortVlanCfgTable,
       "gponSrvProfilePortVlanCfgEntry": gponSrvProfilePortVlanCfgEntry,
       "gponSrvProfilePortType": gponSrvProfilePortType,
       "gponSrvProfilePortId": gponSrvProfilePortId,
       "gponSrvProfilePortVlanEntryId": gponSrvProfilePortVlanEntryId,
       "gponSrvProfilePortVlanRowStatus": gponSrvProfilePortVlanRowStatus,
       "gponSrvProfilePortVlanMode": gponSrvProfilePortVlanMode,
       "gponSrvProfilePortVlanSvlan": gponSrvProfilePortVlanSvlan,
       "gponSrvProfilePortVlanSpri": gponSrvProfilePortVlanSpri,
       "gponSrvProfilePortCvlan": gponSrvProfilePortCvlan,
       "gponSrvProfilePortVlanCpri": gponSrvProfilePortVlanCpri,
       "gponSrvProfileBindInfoTable": gponSrvProfileBindInfoTable,
       "gponSrvProfileBindInfoEntry": gponSrvProfileBindInfoEntry,
       "gponSrvProfileBindOnuList": gponSrvProfileBindOnuList,
       "gponTrafficProfileObjects": gponTrafficProfileObjects,
       "gponTrafficProfileInfoTable": gponTrafficProfileInfoTable,
       "gponTrafficProfileInfoEntry": gponTrafficProfileInfoEntry,
       "gponTrafficProfileId": gponTrafficProfileId,
       "gponTrafficProfileRowStatus": gponTrafficProfileRowStatus,
       "gponTrafficProfileName": gponTrafficProfileName,
       "gponTrafficProfileBindNum": gponTrafficProfileBindNum,
       "gponTrafficProfileCfgTable": gponTrafficProfileCfgTable,
       "gponTrafficProfileCfgEntry": gponTrafficProfileCfgEntry,
       "gponTrafficProfileCfgCir": gponTrafficProfileCfgCir,
       "gponTrafficProfileCfgPir": gponTrafficProfileCfgPir,
       "gponTrafficProfileCfgCbs": gponTrafficProfileCfgCbs,
       "gponTrafficProfileCfgPbs": gponTrafficProfileCfgPbs,
       "gponTrafficProfileCfgPriority": gponTrafficProfileCfgPriority,
       "gponSipAgentProfileObjects": gponSipAgentProfileObjects,
       "gponSipAgentProfileInfoTable": gponSipAgentProfileInfoTable,
       "gponSipAgentProfileInfoEntry": gponSipAgentProfileInfoEntry,
       "gponSipAgentProfileId": gponSipAgentProfileId,
       "gponSipAgentProfileRowStatus": gponSipAgentProfileRowStatus,
       "gponSipAgentProfileName": gponSipAgentProfileName,
       "gponSipAgentProfileBindNum": gponSipAgentProfileBindNum,
       "gponSipAgentProfileCfgTable": gponSipAgentProfileCfgTable,
       "gponSipAgentProfileCfgEntry": gponSipAgentProfileCfgEntry,
       "gponSipAgentProfileProxyServerUri": gponSipAgentProfileProxyServerUri,
       "gponSipAgentProfileRtpDscp": gponSipAgentProfileRtpDscp,
       "gponSipAgentProfileRtpMinPort": gponSipAgentProfileRtpMinPort,
       "gponSipAgentProfileRtpMaxPort": gponSipAgentProfileRtpMaxPort,
       "gponSipAgentProfileSignalDscp": gponSipAgentProfileSignalDscp,
       "gponSipAgentProfileSignalPort": gponSipAgentProfileSignalPort,
       "gponSipAgentProfileSignalTransferMode": gponSipAgentProfileSignalTransferMode,
       "gponSipAgentProfileRegistrationExpiration": gponSipAgentProfileRegistrationExpiration,
       "gponSipAgentProfileRegistrationReregHeadStartTime": gponSipAgentProfileRegistrationReregHeadStartTime,
       "gponSipAgentProfileRegistrationServerUri": gponSipAgentProfileRegistrationServerUri,
       "gponSipAgentProfileVoiceMailServerUri": gponSipAgentProfileVoiceMailServerUri,
       "gponSipAgentProfileVoiceMailSubscriptionExpiration": gponSipAgentProfileVoiceMailSubscriptionExpiration,
       "gponSipAgentProfileConfFactory": gponSipAgentProfileConfFactory,
       "gponSipAgentProfileBridgedLineAgent": gponSipAgentProfileBridgedLineAgent,
       "gponSipAgentProfileAuthRealm": gponSipAgentProfileAuthRealm,
       "gponSipAgentProfileBindInfoTable": gponSipAgentProfileBindInfoTable,
       "gponSipAgentProfileBindInfoEntry": gponSipAgentProfileBindInfoEntry,
       "gponSipAgentProfileBindInfoOnuId": gponSipAgentProfileBindInfoOnuId,
       "gponSipAgentProfileBindPotsList": gponSipAgentProfileBindPotsList,
       "gponSipRightFlagProfileObjects": gponSipRightFlagProfileObjects,
       "gponSipRightFlagProfileInfoTable": gponSipRightFlagProfileInfoTable,
       "gponSipRightFlagProfileInfoEntry": gponSipRightFlagProfileInfoEntry,
       "gponSipRightFlagProfileId": gponSipRightFlagProfileId,
       "gponSipRightFlagProfileRowStatus": gponSipRightFlagProfileRowStatus,
       "gponSipRightFlagProfileName": gponSipRightFlagProfileName,
       "gponSipRightFlagProfileBindNum": gponSipRightFlagProfileBindNum,
       "gponSipRightFlagProfileCfgTable": gponSipRightFlagProfileCfgTable,
       "gponSipRightFlagProfileCfgEntry": gponSipRightFlagProfileCfgEntry,
       "gponSipRightFlagProfileCallWaiting": gponSipRightFlagProfileCallWaiting,
       "gponSipRightFlagProfileCallProcess": gponSipRightFlagProfileCallProcess,
       "gponSipRightFlagProfileCallPresentation": gponSipRightFlagProfileCallPresentation,
       "gponSipRightFlagProfileHotline": gponSipRightFlagProfileHotline,
       "gponSipRightFlagProfileHotlineNum": gponSipRightFlagProfileHotlineNum,
       "gponSipRightFlagProfileBindInfoTable": gponSipRightFlagProfileBindInfoTable,
       "gponSipRightFlagProfileBindInfoEntry": gponSipRightFlagProfileBindInfoEntry,
       "gponSipRightFlagProfileBindInfoOnuId": gponSipRightFlagProfileBindInfoOnuId,
       "gponSipRightFlagProfileBindPotsList": gponSipRightFlagProfileBindPotsList,
       "gponDigitMapProfileObjects": gponDigitMapProfileObjects,
       "gponDigitMapProfileInfoTable": gponDigitMapProfileInfoTable,
       "gponDigitMapProfileInfoEntry": gponDigitMapProfileInfoEntry,
       "gponDigitMapProfileId": gponDigitMapProfileId,
       "gponDigitMapProfileRowStatus": gponDigitMapProfileRowStatus,
       "gponDigitMapProfileName": gponDigitMapProfileName,
       "gponDigitMapProfileBindNum": gponDigitMapProfileBindNum,
       "gponDigitMapProfileCfgTable": gponDigitMapProfileCfgTable,
       "gponDigitMapProfileCfgEntry": gponDigitMapProfileCfgEntry,
       "gponDigitMapProfileCriticalDialTime": gponDigitMapProfileCriticalDialTime,
       "gponDigitMapProfileCfgPartialDialTime": gponDigitMapProfileCfgPartialDialTime,
       "gponDigitMapProfileCfgDigitmapFormat": gponDigitMapProfileCfgDigitmapFormat,
       "gponDigitMapProfileDialPlanTable": gponDigitMapProfileDialPlanTable,
       "gponDigitMapProfileDialPlanEntry": gponDigitMapProfileDialPlanEntry,
       "gponDigitMapProfileDialPlanId": gponDigitMapProfileDialPlanId,
       "gponDigitMapProfileDialPlanRowStatus": gponDigitMapProfileDialPlanRowStatus,
       "gponDigitMapProfileDialPlanToken": gponDigitMapProfileDialPlanToken,
       "gponDigitMapProfileBindInfoTable": gponDigitMapProfileBindInfoTable,
       "gponDigitMapProfileBindInfoEntry": gponDigitMapProfileBindInfoEntry,
       "gponDigitMapProfileBindInfoOnuId": gponDigitMapProfileBindInfoOnuId,
       "gponDigitMapProfileBindPotsList": gponDigitMapProfileBindPotsList,
       "gponPotsProfileObjects": gponPotsProfileObjects,
       "gponPotsProfileInfoTable": gponPotsProfileInfoTable,
       "gponPotsProfileInfoEntry": gponPotsProfileInfoEntry,
       "gponPotsProfileId": gponPotsProfileId,
       "gponPotsProfileRowStatus": gponPotsProfileRowStatus,
       "gponPotsProfileName": gponPotsProfileName,
       "gponPotsProfileBindNum": gponPotsProfileBindNum,
       "gponPotsProfileCfgTable": gponPotsProfileCfgTable,
       "gponPotsProfileCfgEntry": gponPotsProfileCfgEntry,
       "gponPotsProfileImpedance": gponPotsProfileImpedance,
       "gponPotsProfileSignallingCode": gponPotsProfileSignallingCode,
       "gponPotsProfileRxGain": gponPotsProfileRxGain,
       "gponPotsProfileTxGain": gponPotsProfileTxGain,
       "gponPotsProfileBindInfoTable": gponPotsProfileBindInfoTable,
       "gponPotsProfileBindInfoEntry": gponPotsProfileBindInfoEntry,
       "gponPotsProfileBindInfoOnuId": gponPotsProfileBindInfoOnuId,
       "gponPotsProfileBindPotsList": gponPotsProfileBindPotsList,
       "gponControlObjects": gponControlObjects,
       "gponOltObjects": gponOltObjects,
       "gponOltControlTable": gponOltControlTable,
       "gponOltControlEntry": gponOltControlEntry,
       "gponOltDeviceId": gponOltDeviceId,
       "gponOltCardId": gponOltCardId,
       "gponOltPortId": gponOltPortId,
       "gponOltPortAutoFindSwitch": gponOltPortAutoFindSwitch,
       "gponOltPortSwitch": gponOltPortSwitch,
       "gponOltPortStatus": gponOltPortStatus,
       "gponOltPortDdmInfoTable": gponOltPortDdmInfoTable,
       "gponOltPortDdmInfoEntry": gponOltPortDdmInfoEntry,
       "gponOltPortDdmTemperature": gponOltPortDdmTemperature,
       "gponOltPortDdmVoltage": gponOltPortDdmVoltage,
       "gponOltPortDdmTxBiasCurrent": gponOltPortDdmTxBiasCurrent,
       "gponOltPortDdmTxPower": gponOltPortDdmTxPower,
       "gponOltPortDdmRxPower": gponOltPortDdmRxPower,
       "gponOltTransceiverInfoTable": gponOltTransceiverInfoTable,
       "gponOltTransceiverInfoEntry": gponOltTransceiverInfoEntry,
       "gponOltTransceiverVendor": gponOltTransceiverVendor,
       "gponOltTransceiverProductName": gponOltTransceiverProductName,
       "gponOltTransceiverVersion": gponOltTransceiverVersion,
       "gponOltTransceiverSerialNumber": gponOltTransceiverSerialNumber,
       "gponOltAutoAuthTable": gponOltAutoAuthTable,
       "gponOltAutoAuthControlTable": gponOltAutoAuthControlTable,
       "gponOltAutoAuthControlEntry": gponOltAutoAuthControlEntry,
       "gponOltAutoAuthMode": gponOltAutoAuthMode,
       "gponOltAutoAuthSwitch": gponOltAutoAuthSwitch,
       "gponOltPortAutoAuthSwitchBitMap": gponOltPortAutoAuthSwitchBitMap,
       "gponOltAutoAuthRuleNumber": gponOltAutoAuthRuleNumber,
       "gponOltAutoAuthRuleTable": gponOltAutoAuthRuleTable,
       "gponOltAutoAuthRuleEntry": gponOltAutoAuthRuleEntry,
       "gponOltAutoAuthRuleId": gponOltAutoAuthRuleId,
       "gponOltAutoAuthRuleRowStatus": gponOltAutoAuthRuleRowStatus,
       "gponOltAutoAuthVendorId": gponOltAutoAuthVendorId,
       "gponOltAutoAuthEquipmentID": gponOltAutoAuthEquipmentID,
       "gponOltAutoAuthSoftwareVersion": gponOltAutoAuthSoftwareVersion,
       "gponOltAutoAuthLineProfileId": gponOltAutoAuthLineProfileId,
       "gponOltAutoAuthSrvProfileId": gponOltAutoAuthSrvProfileId,
       "gponOltAutoAuthOnuNumber": gponOltAutoAuthOnuNumber,
       "gponOnuObjects": gponOnuObjects,
       "gponOnuConfigTable": gponOnuConfigTable,
       "gponOnuConfigEntry": gponOnuConfigEntry,
       "gponOnuId": gponOnuId,
       "gponOnuRowStatus": gponOnuRowStatus,
       "gponOnuAuthMode": gponOnuAuthMode,
       "gponOnuSn": gponOnuSn,
       "gponOnuPassword": gponOnuPassword,
       "gponOnuLineProfileId": gponOnuLineProfileId,
       "gponOnuServiceProfileId": gponOnuServiceProfileId,
       "gponOnuDescription": gponOnuDescription,
       "gponOnuInfoTable": gponOnuInfoTable,
       "gponOnuInfoEntry": gponOnuInfoEntry,
       "gponOnuRunState": gponOnuRunState,
       "gponOnuConfigState": gponOnuConfigState,
       "gponOnuMatchState": gponOnuMatchState,
       "gponOnuDistance": gponOnuDistance,
       "gponOnuInfoDescription": gponOnuInfoDescription,
       "gponOnuInfoLastUpTime": gponOnuInfoLastUpTime,
       "gponOnuInfoLastDownTime": gponOnuInfoLastDownTime,
       "gponOnuCapabilityInfoTable": gponOnuCapabilityInfoTable,
       "gponOnuCapabilityInfoEntry": gponOnuCapabilityInfoEntry,
       "gponOnuType": gponOnuType,
       "gponOnuPonPortNum": gponOnuPonPortNum,
       "gponOnuEthPortNum": gponOnuEthPortNum,
       "gponOnuVeipPortNum": gponOnuVeipPortNum,
       "gponOnuPotsPortNum": gponOnuPotsPortNum,
       "gponOnuCatvPortNum": gponOnuCatvPortNum,
       "gponOnuGemPortNum": gponOnuGemPortNum,
       "gponOnuTcontNum": gponOnuTcontNum,
       "gponOnuFlowControlType": gponOnuFlowControlType,
       "gponOnuControlTable": gponOnuControlTable,
       "gponOnuControlEntry": gponOnuControlEntry,
       "gponOnuReset": gponOnuReset,
       "gponOnuDeactive": gponOnuDeactive,
       "gponOnuAutofindInfoTable": gponOnuAutofindInfoTable,
       "gponOnuAutofindInfoEntry": gponOnuAutofindInfoEntry,
       "gponOnuAutofindId": gponOnuAutofindId,
       "gponOnuAutofindRowStatus": gponOnuAutofindRowStatus,
       "gponOnuAutofindSn": gponOnuAutofindSn,
       "gponOnuAutofindPassword": gponOnuAutofindPassword,
       "gponOnuAutofindVendorId": gponOnuAutofindVendorId,
       "gponOnuAutofindVersion": gponOnuAutofindVersion,
       "gponOnuAutofindEquipmentID": gponOnuAutofindEquipmentID,
       "gponOnuAutofindSoftwareVersion": gponOnuAutofindSoftwareVersion,
       "gponOnuAutofindTime": gponOnuAutofindTime,
       "gponOnuOpticalInfoTable": gponOnuOpticalInfoTable,
       "gponOnuOpticalInfoEntry": gponOnuOpticalInfoEntry,
       "gponOnuOpticalVoltage": gponOnuOpticalVoltage,
       "gponOnuOpticalTxPower": gponOnuOpticalTxPower,
       "gponOnuOpticalRxPower": gponOnuOpticalRxPower,
       "gponOnuOpticalLaserBiasCurrent": gponOnuOpticalLaserBiasCurrent,
       "gponOnuOpticalTemperature": gponOnuOpticalTemperature,
       "gponOnuVersionTable": gponOnuVersionTable,
       "gponOnuVersionEntry": gponOnuVersionEntry,
       "gponOnuMainSoftwareVersion": gponOnuMainSoftwareVersion,
       "gponOnuStandbySoftwareVersion": gponOnuStandbySoftwareVersion,
       "gponOnuAuthenticationManagement": gponOnuAuthenticationManagement,
       "gponOnuAuthenticationConfirmTable": gponOnuAuthenticationConfirmTable,
       "gponOnuAuthenticationConfirmEntry": gponOnuAuthenticationConfirmEntry,
       "gponOnuAuthenticationConfirmDeviceId": gponOnuAuthenticationConfirmDeviceId,
       "gponOnuAuthenticationConfirmCardId": gponOnuAuthenticationConfirmCardId,
       "gponOnuAuthenticationConfirmPortId": gponOnuAuthenticationConfirmPortId,
       "gponOnuAuthenConfirmType": gponOnuAuthenConfirmType,
       "gponOnuAuthenConfirmSn": gponOnuAuthenConfirmSn,
       "gponOnuAuthenConfirmPassword": gponOnuAuthenConfirmPassword,
       "gponOnuAuthenConfirmLoid": gponOnuAuthenConfirmLoid,
       "gponOnuAuthenConfirmLoidPassword": gponOnuAuthenConfirmLoidPassword,
       "gponOnuAuthenConfirmLineProfileId": gponOnuAuthenConfirmLineProfileId,
       "gponOnuAuthenConfirmServiceProfileId": gponOnuAuthenConfirmServiceProfileId,
       "gponOnuAuthenConfirmTimeMode": gponOnuAuthenConfirmTimeMode,
       "gponOnuAuthenConfirmAgingDuration": gponOnuAuthenConfirmAgingDuration,
       "gponOnuAuthenticationConfirmRowStatus": gponOnuAuthenticationConfirmRowStatus,
       "gponOnuPolicyAuthTable": gponOnuPolicyAuthTable,
       "gponOnuPolicyAuthControlTable": gponOnuPolicyAuthControlTable,
       "gponOnuPolicyAuthControlEntry": gponOnuPolicyAuthControlEntry,
       "gponOnuPolicyAuthControlDeviceId": gponOnuPolicyAuthControlDeviceId,
       "gponOnuPolicyAuthSwitch": gponOnuPolicyAuthSwitch,
       "gponOnuPolicyAuthPortSwtichBitMap": gponOnuPolicyAuthPortSwtichBitMap,
       "gponOnuPolicyAuthMode": gponOnuPolicyAuthMode,
       "gponOnuPolicyAuthTargetMode": gponOnuPolicyAuthTargetMode,
       "gponOnuPolicyAuthTimeMode": gponOnuPolicyAuthTimeMode,
       "gponOnuPolicyAuthRuleTable": gponOnuPolicyAuthRuleTable,
       "gponOnuPolicyAuthRuleEntry": gponOnuPolicyAuthRuleEntry,
       "gponOnuPolicyAuthCardId": gponOnuPolicyAuthCardId,
       "gponOnuPolicyAuthRuleId": gponOnuPolicyAuthRuleId,
       "gponOnuPolicyAuthRuleMatchMode": gponOnuPolicyAuthRuleMatchMode,
       "gponOnuPolicyAuthRuleEquid": gponOnuPolicyAuthRuleEquid,
       "gponOnuPolicyAuthRuleVendorid": gponOnuPolicyAuthRuleVendorid,
       "gponOnuPolicyAuthRuleSoftwareVersion": gponOnuPolicyAuthRuleSoftwareVersion,
       "gponOnuPolicyAuthRuleLineProfileId": gponOnuPolicyAuthRuleLineProfileId,
       "gponOnuPolicyAuthRuleSrvProfileId": gponOnuPolicyAuthRuleSrvProfileId,
       "gponOnuPolicyAuthRuleRowStatus": gponOnuPolicyAuthRuleRowStatus,
       "gponOnuEthPortObjects": gponOnuEthPortObjects,
       "gponOnuEthPortCfgTable": gponOnuEthPortCfgTable,
       "gponOnuEthPortCfgEntry": gponOnuEthPortCfgEntry,
       "gponOnuEthPortId": gponOnuEthPortId,
       "gponOnuEthPortNativeVlanId": gponOnuEthPortNativeVlanId,
       "gponOnuEthPortNativeVlanPriority": gponOnuEthPortNativeVlanPriority,
       "gponOnuEthPortInboundCarId": gponOnuEthPortInboundCarId,
       "gponOnuEthPortOutboundCarId": gponOnuEthPortOutboundCarId,
       "gponOnuEthPortSpeedAndDuplex": gponOnuEthPortSpeedAndDuplex,
       "gponOnuEthPortFlowCtrl": gponOnuEthPortFlowCtrl,
       "gponOnuEthPortOperationalState": gponOnuEthPortOperationalState,
       "gponOnuEthPortInfoTable": gponOnuEthPortInfoTable,
       "gponOnuEthPortInfoEntry": gponOnuEthPortInfoEntry,
       "gponOnuEthPortSpeedAndDuplexInfo": gponOnuEthPortSpeedAndDuplexInfo,
       "gponOnuEthPortState": gponOnuEthPortState,
       "gponOnuEthPortMacAddressTable": gponOnuEthPortMacAddressTable,
       "gponOnuEthPortMacAddressEntry": gponOnuEthPortMacAddressEntry,
       "gponOnuEthPortMacAddressId": gponOnuEthPortMacAddressId,
       "gponOnuEthPortMacAddress": gponOnuEthPortMacAddress,
       "gponOnuPotsPortObjects": gponOnuPotsPortObjects,
       "gponOnuPotsPortCfgTable": gponOnuPotsPortCfgTable,
       "gponOnuPotsPortCfgEntry": gponOnuPotsPortCfgEntry,
       "gponOnuPotsPortId": gponOnuPotsPortId,
       "gponOnuPotsPortOperationalState": gponOnuPotsPortOperationalState,
       "gponOnuPotsPortCfgPotsProfileId": gponOnuPotsPortCfgPotsProfileId,
       "gponOnuIpCfgTable": gponOnuIpCfgTable,
       "gponOnuIpCfgEntry": gponOnuIpCfgEntry,
       "gponOnuIpHostId": gponOnuIpHostId,
       "gponOnuIpCfgRowStatus": gponOnuIpCfgRowStatus,
       "gponOnuIpCfgMode": gponOnuIpCfgMode,
       "gponOnuIpCfgVlanId": gponOnuIpCfgVlanId,
       "gponOnuIpCfgVlanPri": gponOnuIpCfgVlanPri,
       "gponOnuIpCfgIp": gponOnuIpCfgIp,
       "gponOnuIpCfgMask": gponOnuIpCfgMask,
       "gponOnuIpCfgGateway": gponOnuIpCfgGateway,
       "gponOnuIpCfgPriDns": gponOnuIpCfgPriDns,
       "gponOnuIpCfgSlaveDns": gponOnuIpCfgSlaveDns,
       "gponOnuIpCfgMacAddress": gponOnuIpCfgMacAddress,
       "gponOnuSipPstnUserTable": gponOnuSipPstnUserTable,
       "gponOnuSipPstnUserEntry": gponOnuSipPstnUserEntry,
       "gponOnuSipPstnUserId": gponOnuSipPstnUserId,
       "gponOnuSipPstnUserRowStatus": gponOnuSipPstnUserRowStatus,
       "gponOnuSipPstnUserName": gponOnuSipPstnUserName,
       "gponOnuSipPstnUserPassword": gponOnuSipPstnUserPassword,
       "gponOnuSipPstnUserTelephoneNumber": gponOnuSipPstnUserTelephoneNumber,
       "gponOnuSipPstnUserAgentProfileId": gponOnuSipPstnUserAgentProfileId,
       "gponOnuSipPstnUserDigitMapProfileId": gponOnuSipPstnUserDigitMapProfileId,
       "gponOnuSipPstnUserSipRightFlagProfileId": gponOnuSipPstnUserSipRightFlagProfileId,
       "gponOnuSipPstnUserInfoTable": gponOnuSipPstnUserInfoTable,
       "gponOnuSipPstnUserInfoEntry": gponOnuSipPstnUserInfoEntry,
       "gponOnuSipPstnUserState": gponOnuSipPstnUserState,
       "gponOnuSipPstnUserHookState": gponOnuSipPstnUserHookState,
       "gponOnuSipPstnUserCodec": gponOnuSipPstnUserCodec,
       "gponOnuSipPstnUserServerStatus": gponOnuSipPstnUserServerStatus,
       "gponOnuSipPstnUserSessionType": gponOnuSipPstnUserSessionType,
       "gponOnuCatvPortObjects": gponOnuCatvPortObjects,
       "gponOnuCatvPortCfgTable": gponOnuCatvPortCfgTable,
       "gponOnuCatvPortCfgEntry": gponOnuCatvPortCfgEntry,
       "gponOnuCatvPortId": gponOnuCatvPortId,
       "gponOnuCatvPortOperationalState": gponOnuCatvPortOperationalState,
       "gponAlarmObjects": gponAlarmObjects,
       "gponNotifications": gponNotifications,
       "gponAlarmNotification": gponAlarmNotification,
       "gponTrapObjects": gponTrapObjects,
       "gponTrapId": gponTrapId,
       "gponTrapState": gponTrapState,
       "gponTrapParameters": gponTrapParameters,
       "gponTrapOltPortId": gponTrapOltPortId,
       "gponTrapOnuId": gponTrapOnuId,
       "gponTrapOnuSn": gponTrapOnuSn,
       "gponTrapOnuPassword": gponTrapOnuPassword,
       "gponTrapRogueOnuSn": gponTrapRogueOnuSn,
       "gponManagementObjects": gponManagementObjects,
       "gponManagementAddrTable": gponManagementAddrTable,
       "gponManagementAddrEntry": gponManagementAddrEntry,
       "gponManagementAddrName": gponManagementAddrName,
       "gponManagementAddrRowStatus": gponManagementAddrRowStatus,
       "gponManagementAddrTAddress": gponManagementAddrTAddress,
       "gponManagementAddrCommunity": gponManagementAddrCommunity,
       "gponConformance": gponConformance,
       "gponCompliances": gponCompliances,
       "gponCompliance": gponCompliance,
       "gponGroups": gponGroups,
       "gponProfileGroups": gponProfileGroups,
       "gponDbaProfileGroup": gponDbaProfileGroup,
       "gponLineProfileGroup": gponLineProfileGroup,
       "gponSrvProfileGroup": gponSrvProfileGroup,
       "gponTrafficProfileGroup": gponTrafficProfileGroup,
       "gponSipAgentProfileGroup": gponSipAgentProfileGroup,
       "gponSipRightFlagProfileGroup": gponSipRightFlagProfileGroup,
       "gponDigitMapProfileGroup": gponDigitMapProfileGroup,
       "gponPotsProfileGroup": gponPotsProfileGroup,
       "gponControlGroups": gponControlGroups,
       "gponControlGroup": gponControlGroup,
       "gponTrapGroups": gponTrapGroups,
       "gponTrapGroup": gponTrapGroup,
       "gponTrapTypeGroup": gponTrapTypeGroup}
)
