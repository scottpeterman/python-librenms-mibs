# SNMP MIB module (CDATA-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\CDATA-EPON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:47 2025
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

(eoc,
 epon,
 gpon,
 mediaConverter,
 switch) = mibBuilder.importSymbols(
    "CDATA-COMMON-SMI",
    "eoc",
    "epon",
    "gpon",
    "mediaConverter",
    "switch")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

eponMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EponProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class EponAlarmProfileThreshold(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )



class EponDbaProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



class EponDbaProfileName(TextualConvention, OctetString):
    status = "current"


class EponLinePorfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )



class EponLineProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class EponLineProfileLlId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class EponSrvProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )



class EponSrvProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class EponTrafficProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )



class EponTrafficProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class EponSwitch(TextualConvention, Integer32):
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



class EponVlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class EponVlanPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class EponOltPortId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class EponOnuId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class EponOnuEthPortId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class EponOnuCatvPortId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )



class EponMacAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



# MIB Managed Objects in the order of their OIDs

_EponObjects_ObjectIdentity = ObjectIdentity
eponObjects = _EponObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    eponObjects.setStatus("current")
_EponProfileObjects_ObjectIdentity = ObjectIdentity
eponProfileObjects = _EponProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eponProfileObjects.setStatus("current")
_EponDbaProfileObjects_ObjectIdentity = ObjectIdentity
eponDbaProfileObjects = _EponDbaProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eponDbaProfileObjects.setStatus("current")
_EponDbaProfileInfoTable_Object = MibTable
eponDbaProfileInfoTable = _EponDbaProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eponDbaProfileInfoTable.setStatus("current")
_EponDbaProfileInfoEntry_Object = MibTableRow
eponDbaProfileInfoEntry = _EponDbaProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1, 1, 1)
)
eponDbaProfileInfoEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponDbaProfileId"),
)
if mibBuilder.loadTexts:
    eponDbaProfileInfoEntry.setStatus("current")
_EponDbaProfileId_Type = EponDbaProfileId
_EponDbaProfileId_Object = MibTableColumn
eponDbaProfileId = _EponDbaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1, 1, 1, 1),
    _EponDbaProfileId_Type()
)
eponDbaProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponDbaProfileId.setStatus("current")


class _EponDbaProfileName_Type(EponDbaProfileName):
    """Custom type eponDbaProfileName based on EponDbaProfileName"""
    subtypeSpec = EponDbaProfileName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EponDbaProfileName_Type.__name__ = "EponDbaProfileName"
_EponDbaProfileName_Object = MibTableColumn
eponDbaProfileName = _EponDbaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1, 1, 1, 2),
    _EponDbaProfileName_Type()
)
eponDbaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponDbaProfileName.setStatus("current")


class _EponDbaProfileType_Type(Integer32):
    """Custom type eponDbaProfileType based on Integer32"""
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


_EponDbaProfileType_Type.__name__ = "Integer32"
_EponDbaProfileType_Object = MibTableColumn
eponDbaProfileType = _EponDbaProfileType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1, 1, 1, 3),
    _EponDbaProfileType_Type()
)
eponDbaProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponDbaProfileType.setStatus("current")


class _EponDbaProfileFixRate_Type(Integer32):
    """Custom type eponDbaProfileFixRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000000),
    )


_EponDbaProfileFixRate_Type.__name__ = "Integer32"
_EponDbaProfileFixRate_Object = MibTableColumn
eponDbaProfileFixRate = _EponDbaProfileFixRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1, 1, 1, 4),
    _EponDbaProfileFixRate_Type()
)
eponDbaProfileFixRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponDbaProfileFixRate.setStatus("current")
if mibBuilder.loadTexts:
    eponDbaProfileFixRate.setUnits("kbps")


class _EponDbaProfileAssureRate_Type(Integer32):
    """Custom type eponDbaProfileAssureRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000000),
    )


_EponDbaProfileAssureRate_Type.__name__ = "Integer32"
_EponDbaProfileAssureRate_Object = MibTableColumn
eponDbaProfileAssureRate = _EponDbaProfileAssureRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1, 1, 1, 5),
    _EponDbaProfileAssureRate_Type()
)
eponDbaProfileAssureRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponDbaProfileAssureRate.setStatus("current")
if mibBuilder.loadTexts:
    eponDbaProfileAssureRate.setUnits("kbps")


class _EponDbaProfileMaxRate_Type(Integer32):
    """Custom type eponDbaProfileMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 1000000),
    )


_EponDbaProfileMaxRate_Type.__name__ = "Integer32"
_EponDbaProfileMaxRate_Object = MibTableColumn
eponDbaProfileMaxRate = _EponDbaProfileMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1, 1, 1, 6),
    _EponDbaProfileMaxRate_Type()
)
eponDbaProfileMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponDbaProfileMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    eponDbaProfileMaxRate.setUnits("kbps")
_EponDbaProfileBindNum_Type = Integer32
_EponDbaProfileBindNum_Object = MibTableColumn
eponDbaProfileBindNum = _EponDbaProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1, 1, 1, 7),
    _EponDbaProfileBindNum_Type()
)
eponDbaProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponDbaProfileBindNum.setStatus("current")
_EponDbaProfileRowStatus_Type = RowStatus
_EponDbaProfileRowStatus_Object = MibTableColumn
eponDbaProfileRowStatus = _EponDbaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 1, 1, 1, 8),
    _EponDbaProfileRowStatus_Type()
)
eponDbaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponDbaProfileRowStatus.setStatus("current")
_EponLineProfileObjects_ObjectIdentity = ObjectIdentity
eponLineProfileObjects = _EponLineProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eponLineProfileObjects.setStatus("current")
_EponLineProfileInfoTable_Object = MibTable
eponLineProfileInfoTable = _EponLineProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eponLineProfileInfoTable.setStatus("current")
_EponLineProfileInfoEntry_Object = MibTableRow
eponLineProfileInfoEntry = _EponLineProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 1, 1)
)
eponLineProfileInfoEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponLineProfileId"),
)
if mibBuilder.loadTexts:
    eponLineProfileInfoEntry.setStatus("current")
_EponLineProfileId_Type = EponLinePorfileId
_EponLineProfileId_Object = MibTableColumn
eponLineProfileId = _EponLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 1, 1, 1),
    _EponLineProfileId_Type()
)
eponLineProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponLineProfileId.setStatus("current")
_EponLineProfileName_Type = EponLineProfileName
_EponLineProfileName_Object = MibTableColumn
eponLineProfileName = _EponLineProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 1, 1, 2),
    _EponLineProfileName_Type()
)
eponLineProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponLineProfileName.setStatus("current")
_EponLineProfileUpstreamFECMode_Type = EponSwitch
_EponLineProfileUpstreamFECMode_Object = MibTableColumn
eponLineProfileUpstreamFECMode = _EponLineProfileUpstreamFECMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 1, 1, 3),
    _EponLineProfileUpstreamFECMode_Type()
)
eponLineProfileUpstreamFECMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponLineProfileUpstreamFECMode.setStatus("current")
_EponLineProfileLlidNum_Type = Integer32
_EponLineProfileLlidNum_Object = MibTableColumn
eponLineProfileLlidNum = _EponLineProfileLlidNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 1, 1, 4),
    _EponLineProfileLlidNum_Type()
)
eponLineProfileLlidNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponLineProfileLlidNum.setStatus("current")
_EponLineProfileBindNum_Type = Integer32
_EponLineProfileBindNum_Object = MibTableColumn
eponLineProfileBindNum = _EponLineProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 1, 1, 7),
    _EponLineProfileBindNum_Type()
)
eponLineProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponLineProfileBindNum.setStatus("current")
_EponLineProfileRowStatus_Type = RowStatus
_EponLineProfileRowStatus_Object = MibTableColumn
eponLineProfileRowStatus = _EponLineProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 1, 1, 8),
    _EponLineProfileRowStatus_Type()
)
eponLineProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponLineProfileRowStatus.setStatus("current")
_EponLineProfileLlidTable_Object = MibTable
eponLineProfileLlidTable = _EponLineProfileLlidTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eponLineProfileLlidTable.setStatus("current")
_EponLineProfileLlidEntry_Object = MibTableRow
eponLineProfileLlidEntry = _EponLineProfileLlidEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 3, 1)
)
eponLineProfileLlidEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponLineProfileId"),
    (0, "CDATA-EPON-MIB", "eponLineProfileLlId"),
)
if mibBuilder.loadTexts:
    eponLineProfileLlidEntry.setStatus("current")
_EponLineProfileLlId_Type = EponLineProfileLlId
_EponLineProfileLlId_Object = MibTableColumn
eponLineProfileLlId = _EponLineProfileLlId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 3, 1, 2),
    _EponLineProfileLlId_Type()
)
eponLineProfileLlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponLineProfileLlId.setStatus("current")
_EponLineProfileLlidDbaProfileId_Type = EponDbaProfileId
_EponLineProfileLlidDbaProfileId_Object = MibTableColumn
eponLineProfileLlidDbaProfileId = _EponLineProfileLlidDbaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 3, 1, 3),
    _EponLineProfileLlidDbaProfileId_Type()
)
eponLineProfileLlidDbaProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponLineProfileLlidDbaProfileId.setStatus("current")


class _EponLineProfileLlidEncrypt_Type(Integer32):
    """Custom type eponLineProfileLlidEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("triple-churning", 1),
          ("off", 2))
    )


_EponLineProfileLlidEncrypt_Type.__name__ = "Integer32"
_EponLineProfileLlidEncrypt_Object = MibTableColumn
eponLineProfileLlidEncrypt = _EponLineProfileLlidEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 3, 1, 4),
    _EponLineProfileLlidEncrypt_Type()
)
eponLineProfileLlidEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponLineProfileLlidEncrypt.setStatus("current")
_EponLineProfileLlidOntCar_Type = EponTrafficProfileId
_EponLineProfileLlidOntCar_Object = MibTableColumn
eponLineProfileLlidOntCar = _EponLineProfileLlidOntCar_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 3, 1, 5),
    _EponLineProfileLlidOntCar_Type()
)
eponLineProfileLlidOntCar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponLineProfileLlidOntCar.setStatus("current")
_EponLineProfileLlidRowStatus_Type = RowStatus
_EponLineProfileLlidRowStatus_Object = MibTableColumn
eponLineProfileLlidRowStatus = _EponLineProfileLlidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 3, 1, 6),
    _EponLineProfileLlidRowStatus_Type()
)
eponLineProfileLlidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponLineProfileLlidRowStatus.setStatus("current")
_EponLineProfileDbaThresholdTable_Object = MibTable
eponLineProfileDbaThresholdTable = _EponLineProfileDbaThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    eponLineProfileDbaThresholdTable.setStatus("current")
_EponLineProfileDbaThresholdEntry_Object = MibTableRow
eponLineProfileDbaThresholdEntry = _EponLineProfileDbaThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 4, 1)
)
eponLineProfileDbaThresholdEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponLineProfileId"),
    (0, "CDATA-EPON-MIB", "eponLineProfileQueueSetId"),
    (0, "CDATA-EPON-MIB", "eponLineProfileQueueId"),
)
if mibBuilder.loadTexts:
    eponLineProfileDbaThresholdEntry.setStatus("current")


class _EponLineProfileQueueSetId_Type(Integer32):
    """Custom type eponLineProfileQueueSetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EponLineProfileQueueSetId_Type.__name__ = "Integer32"
_EponLineProfileQueueSetId_Object = MibTableColumn
eponLineProfileQueueSetId = _EponLineProfileQueueSetId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 4, 1, 1),
    _EponLineProfileQueueSetId_Type()
)
eponLineProfileQueueSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponLineProfileQueueSetId.setStatus("current")


class _EponLineProfileQueueId_Type(Integer32):
    """Custom type eponLineProfileQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EponLineProfileQueueId_Type.__name__ = "Integer32"
_EponLineProfileQueueId_Object = MibTableColumn
eponLineProfileQueueId = _EponLineProfileQueueId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 4, 1, 2),
    _EponLineProfileQueueId_Type()
)
eponLineProfileQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponLineProfileQueueId.setStatus("current")


class _EponLineProfileThreshold_Type(Integer32):
    """Custom type eponLineProfileThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EponLineProfileThreshold_Type.__name__ = "Integer32"
_EponLineProfileThreshold_Object = MibTableColumn
eponLineProfileThreshold = _EponLineProfileThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 4, 1, 3),
    _EponLineProfileThreshold_Type()
)
eponLineProfileThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponLineProfileThreshold.setStatus("current")
_EponLineProfileDbaThresholdRowStatus_Type = RowStatus
_EponLineProfileDbaThresholdRowStatus_Object = MibTableColumn
eponLineProfileDbaThresholdRowStatus = _EponLineProfileDbaThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 2, 4, 1, 4),
    _EponLineProfileDbaThresholdRowStatus_Type()
)
eponLineProfileDbaThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponLineProfileDbaThresholdRowStatus.setStatus("current")
_EponSrvProfileObjects_ObjectIdentity = ObjectIdentity
eponSrvProfileObjects = _EponSrvProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eponSrvProfileObjects.setStatus("current")
_EponSrvProfileInfoTable_Object = MibTable
eponSrvProfileInfoTable = _EponSrvProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eponSrvProfileInfoTable.setStatus("current")
_EponSrvProfileInfoEntry_Object = MibTableRow
eponSrvProfileInfoEntry = _EponSrvProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 1, 1)
)
eponSrvProfileInfoEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponSrvProfileId"),
)
if mibBuilder.loadTexts:
    eponSrvProfileInfoEntry.setStatus("current")
_EponSrvProfileId_Type = EponSrvProfileId
_EponSrvProfileId_Object = MibTableColumn
eponSrvProfileId = _EponSrvProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 1, 1, 1),
    _EponSrvProfileId_Type()
)
eponSrvProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponSrvProfileId.setStatus("current")
_EponSrvProfileName_Type = EponSrvProfileName
_EponSrvProfileName_Object = MibTableColumn
eponSrvProfileName = _EponSrvProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 1, 1, 2),
    _EponSrvProfileName_Type()
)
eponSrvProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfileName.setStatus("current")
_EponSrvProfileBindNum_Type = Integer32
_EponSrvProfileBindNum_Object = MibTableColumn
eponSrvProfileBindNum = _EponSrvProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 1, 1, 3),
    _EponSrvProfileBindNum_Type()
)
eponSrvProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponSrvProfileBindNum.setStatus("current")
_EponSrvProfileRowStatus_Type = RowStatus
_EponSrvProfileRowStatus_Object = MibTableColumn
eponSrvProfileRowStatus = _EponSrvProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 1, 1, 4),
    _EponSrvProfileRowStatus_Type()
)
eponSrvProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfileRowStatus.setStatus("current")
_EponSrvProfileCfgTable_Object = MibTable
eponSrvProfileCfgTable = _EponSrvProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eponSrvProfileCfgTable.setStatus("current")
_EponSrvProfileCfgEntry_Object = MibTableRow
eponSrvProfileCfgEntry = _EponSrvProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 2, 1)
)
eponSrvProfileCfgEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponSrvProfileId"),
)
if mibBuilder.loadTexts:
    eponSrvProfileCfgEntry.setStatus("current")
_EponSrvProfileMcFastLeave_Type = EponSwitch
_EponSrvProfileMcFastLeave_Object = MibTableColumn
eponSrvProfileMcFastLeave = _EponSrvProfileMcFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 2, 1, 1),
    _EponSrvProfileMcFastLeave_Type()
)
eponSrvProfileMcFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileMcFastLeave.setStatus("current")
_EponSrvProfileMacLearning_Type = EponSwitch
_EponSrvProfileMacLearning_Object = MibTableColumn
eponSrvProfileMacLearning = _EponSrvProfileMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 2, 1, 2),
    _EponSrvProfileMacLearning_Type()
)
eponSrvProfileMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileMacLearning.setStatus("current")
_EponSrvProfileMacAgeSeconds_Type = Integer32
_EponSrvProfileMacAgeSeconds_Object = MibTableColumn
eponSrvProfileMacAgeSeconds = _EponSrvProfileMacAgeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 2, 1, 3),
    _EponSrvProfileMacAgeSeconds_Type()
)
eponSrvProfileMacAgeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileMacAgeSeconds.setStatus("current")
_EponSrvProfileLoopbackDetectCheck_Type = EponSwitch
_EponSrvProfileLoopbackDetectCheck_Object = MibTableColumn
eponSrvProfileLoopbackDetectCheck = _EponSrvProfileLoopbackDetectCheck_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 2, 1, 4),
    _EponSrvProfileLoopbackDetectCheck_Type()
)
eponSrvProfileLoopbackDetectCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileLoopbackDetectCheck.setStatus("current")
_EponSrvProfilePortNumTable_Object = MibTable
eponSrvProfilePortNumTable = _EponSrvProfilePortNumTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eponSrvProfilePortNumTable.setStatus("current")
_EponSrvProfilePortNumEntry_Object = MibTableRow
eponSrvProfilePortNumEntry = _EponSrvProfilePortNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 3, 1)
)
eponSrvProfilePortNumEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponSrvProfileId"),
)
if mibBuilder.loadTexts:
    eponSrvProfilePortNumEntry.setStatus("current")
_EponSrvProfileEthNum_Type = Integer32
_EponSrvProfileEthNum_Object = MibTableColumn
eponSrvProfileEthNum = _EponSrvProfileEthNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 3, 1, 1),
    _EponSrvProfileEthNum_Type()
)
eponSrvProfileEthNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileEthNum.setStatus("current")
_EponSrvProfilePotsNum_Type = Integer32
_EponSrvProfilePotsNum_Object = MibTableColumn
eponSrvProfilePotsNum = _EponSrvProfilePotsNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 3, 1, 2),
    _EponSrvProfilePotsNum_Type()
)
eponSrvProfilePotsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfilePotsNum.setStatus("current")
_EponSrvProfileCatvNum_Type = Integer32
_EponSrvProfileCatvNum_Object = MibTableColumn
eponSrvProfileCatvNum = _EponSrvProfileCatvNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 3, 1, 3),
    _EponSrvProfileCatvNum_Type()
)
eponSrvProfileCatvNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileCatvNum.setStatus("current")
_EponSrvProfileEthPortCfgTable_Object = MibTable
eponSrvProfileEthPortCfgTable = _EponSrvProfileEthPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    eponSrvProfileEthPortCfgTable.setStatus("current")
_EponSrvProfileEthPortCfgEntry_Object = MibTableRow
eponSrvProfileEthPortCfgEntry = _EponSrvProfileEthPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 4, 1)
)
eponSrvProfileEthPortCfgEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponSrvProfileId"),
    (0, "CDATA-EPON-MIB", "eponSrvProfilePortId"),
)
if mibBuilder.loadTexts:
    eponSrvProfileEthPortCfgEntry.setStatus("current")
_EponSrvProfileEthPortMacLimited_Type = Integer32
_EponSrvProfileEthPortMacLimited_Object = MibTableColumn
eponSrvProfileEthPortMacLimited = _EponSrvProfileEthPortMacLimited_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 4, 1, 1),
    _EponSrvProfileEthPortMacLimited_Type()
)
eponSrvProfileEthPortMacLimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileEthPortMacLimited.setStatus("current")
_EponSrvProfileEthPortMtu_Type = Integer32
_EponSrvProfileEthPortMtu_Object = MibTableColumn
eponSrvProfileEthPortMtu = _EponSrvProfileEthPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 4, 1, 2),
    _EponSrvProfileEthPortMtu_Type()
)
eponSrvProfileEthPortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileEthPortMtu.setStatus("current")
_EponSrvProfileEthPortFlowCtrl_Type = EponSwitch
_EponSrvProfileEthPortFlowCtrl_Object = MibTableColumn
eponSrvProfileEthPortFlowCtrl = _EponSrvProfileEthPortFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 4, 1, 3),
    _EponSrvProfileEthPortFlowCtrl_Type()
)
eponSrvProfileEthPortFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileEthPortFlowCtrl.setStatus("current")
_EponSrvProfileEthPortInTrafficProfileId_Type = EponTrafficProfileId
_EponSrvProfileEthPortInTrafficProfileId_Object = MibTableColumn
eponSrvProfileEthPortInTrafficProfileId = _EponSrvProfileEthPortInTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 4, 1, 4),
    _EponSrvProfileEthPortInTrafficProfileId_Type()
)
eponSrvProfileEthPortInTrafficProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileEthPortInTrafficProfileId.setStatus("current")
_EponSrvProfileEthPortOutTrafficProfileId_Type = EponTrafficProfileId
_EponSrvProfileEthPortOutTrafficProfileId_Object = MibTableColumn
eponSrvProfileEthPortOutTrafficProfileId = _EponSrvProfileEthPortOutTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 4, 1, 5),
    _EponSrvProfileEthPortOutTrafficProfileId_Type()
)
eponSrvProfileEthPortOutTrafficProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileEthPortOutTrafficProfileId.setStatus("current")
_EponSrvProfileEthPortNativeVlanId_Type = EponVlanId
_EponSrvProfileEthPortNativeVlanId_Object = MibTableColumn
eponSrvProfileEthPortNativeVlanId = _EponSrvProfileEthPortNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 4, 1, 6),
    _EponSrvProfileEthPortNativeVlanId_Type()
)
eponSrvProfileEthPortNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileEthPortNativeVlanId.setStatus("current")
_EponSrvProfileEthPortNativeVlanPriority_Type = EponVlanPriority
_EponSrvProfileEthPortNativeVlanPriority_Object = MibTableColumn
eponSrvProfileEthPortNativeVlanPriority = _EponSrvProfileEthPortNativeVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 4, 1, 7),
    _EponSrvProfileEthPortNativeVlanPriority_Type()
)
eponSrvProfileEthPortNativeVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSrvProfileEthPortNativeVlanPriority.setStatus("current")
_EponSrvProfilePortVlanCfgTable_Object = MibTable
eponSrvProfilePortVlanCfgTable = _EponSrvProfilePortVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    eponSrvProfilePortVlanCfgTable.setStatus("current")
_EponSrvProfilePortVlanCfgEntry_Object = MibTableRow
eponSrvProfilePortVlanCfgEntry = _EponSrvProfilePortVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6, 1)
)
eponSrvProfilePortVlanCfgEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponSrvProfileId"),
    (0, "CDATA-EPON-MIB", "eponSrvProfilePortType"),
    (0, "CDATA-EPON-MIB", "eponSrvProfilePortId"),
    (0, "CDATA-EPON-MIB", "eponSrvProfilePortVlanEntryId"),
)
if mibBuilder.loadTexts:
    eponSrvProfilePortVlanCfgEntry.setStatus("current")


class _EponSrvProfilePortType_Type(Integer32):
    """Custom type eponSrvProfilePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eth", 1)
    )


_EponSrvProfilePortType_Type.__name__ = "Integer32"
_EponSrvProfilePortType_Object = MibTableColumn
eponSrvProfilePortType = _EponSrvProfilePortType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6, 1, 1),
    _EponSrvProfilePortType_Type()
)
eponSrvProfilePortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponSrvProfilePortType.setStatus("current")


class _EponSrvProfilePortId_Type(Integer32):
    """Custom type eponSrvProfilePortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_EponSrvProfilePortId_Type.__name__ = "Integer32"
_EponSrvProfilePortId_Object = MibTableColumn
eponSrvProfilePortId = _EponSrvProfilePortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6, 1, 2),
    _EponSrvProfilePortId_Type()
)
eponSrvProfilePortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponSrvProfilePortId.setStatus("current")


class _EponSrvProfilePortVlanEntryId_Type(Integer32):
    """Custom type eponSrvProfilePortVlanEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_EponSrvProfilePortVlanEntryId_Type.__name__ = "Integer32"
_EponSrvProfilePortVlanEntryId_Object = MibTableColumn
eponSrvProfilePortVlanEntryId = _EponSrvProfilePortVlanEntryId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6, 1, 3),
    _EponSrvProfilePortVlanEntryId_Type()
)
eponSrvProfilePortVlanEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponSrvProfilePortVlanEntryId.setStatus("current")


class _EponSrvProfilePortVlanMode_Type(Integer32):
    """Custom type eponSrvProfilePortVlanMode based on Integer32"""
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


_EponSrvProfilePortVlanMode_Type.__name__ = "Integer32"
_EponSrvProfilePortVlanMode_Object = MibTableColumn
eponSrvProfilePortVlanMode = _EponSrvProfilePortVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6, 1, 4),
    _EponSrvProfilePortVlanMode_Type()
)
eponSrvProfilePortVlanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortVlanMode.setStatus("current")
_EponSrvProfilePortVlanSvlan_Type = EponVlanId
_EponSrvProfilePortVlanSvlan_Object = MibTableColumn
eponSrvProfilePortVlanSvlan = _EponSrvProfilePortVlanSvlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6, 1, 5),
    _EponSrvProfilePortVlanSvlan_Type()
)
eponSrvProfilePortVlanSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortVlanSvlan.setStatus("current")
_EponSrvProfilePortVlanSpri_Type = Integer32
_EponSrvProfilePortVlanSpri_Object = MibTableColumn
eponSrvProfilePortVlanSpri = _EponSrvProfilePortVlanSpri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6, 1, 6),
    _EponSrvProfilePortVlanSpri_Type()
)
eponSrvProfilePortVlanSpri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortVlanSpri.setStatus("current")
_EponSrvProfilePortVlanCvlan_Type = EponVlanId
_EponSrvProfilePortVlanCvlan_Object = MibTableColumn
eponSrvProfilePortVlanCvlan = _EponSrvProfilePortVlanCvlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6, 1, 7),
    _EponSrvProfilePortVlanCvlan_Type()
)
eponSrvProfilePortVlanCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortVlanCvlan.setStatus("current")
_EponSrvProfilePortVlanCpri_Type = Integer32
_EponSrvProfilePortVlanCpri_Object = MibTableColumn
eponSrvProfilePortVlanCpri = _EponSrvProfilePortVlanCpri_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6, 1, 8),
    _EponSrvProfilePortVlanCpri_Type()
)
eponSrvProfilePortVlanCpri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortVlanCpri.setStatus("current")
_EponSrvProfilePortVlanRowStatus_Type = RowStatus
_EponSrvProfilePortVlanRowStatus_Object = MibTableColumn
eponSrvProfilePortVlanRowStatus = _EponSrvProfilePortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 6, 1, 9),
    _EponSrvProfilePortVlanRowStatus_Type()
)
eponSrvProfilePortVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortVlanRowStatus.setStatus("current")
_EponSrvProfilePortMcCfgTable_Object = MibTable
eponSrvProfilePortMcCfgTable = _EponSrvProfilePortMcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    eponSrvProfilePortMcCfgTable.setStatus("current")
_EponSrvProfilePortMcCfgEntry_Object = MibTableRow
eponSrvProfilePortMcCfgEntry = _EponSrvProfilePortMcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 8, 1)
)
eponSrvProfilePortMcCfgEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponSrvProfileId"),
    (0, "CDATA-EPON-MIB", "eponSrvProfilePortType"),
    (0, "CDATA-EPON-MIB", "eponSrvProfilePortId"),
    (0, "CDATA-EPON-MIB", "eponSrvProfilePortMcEntryId"),
)
if mibBuilder.loadTexts:
    eponSrvProfilePortMcCfgEntry.setStatus("current")


class _EponSrvProfilePortMcEntryId_Type(Integer32):
    """Custom type eponSrvProfilePortMcEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EponSrvProfilePortMcEntryId_Type.__name__ = "Integer32"
_EponSrvProfilePortMcEntryId_Object = MibTableColumn
eponSrvProfilePortMcEntryId = _EponSrvProfilePortMcEntryId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 8, 1, 1),
    _EponSrvProfilePortMcEntryId_Type()
)
eponSrvProfilePortMcEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponSrvProfilePortMcEntryId.setStatus("current")


class _EponSrvProfilePortMcMaxGroupNum_Type(Integer32):
    """Custom type eponSrvProfilePortMcMaxGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EponSrvProfilePortMcMaxGroupNum_Type.__name__ = "Integer32"
_EponSrvProfilePortMcMaxGroupNum_Object = MibTableColumn
eponSrvProfilePortMcMaxGroupNum = _EponSrvProfilePortMcMaxGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 8, 1, 2),
    _EponSrvProfilePortMcMaxGroupNum_Type()
)
eponSrvProfilePortMcMaxGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortMcMaxGroupNum.setStatus("current")


class _EponSrvProfilePortMcTagStripMode_Type(Integer32):
    """Custom type eponSrvProfilePortMcTagStripMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("untag", 1),
          ("tag", 2),
          ("translation", 3))
    )


_EponSrvProfilePortMcTagStripMode_Type.__name__ = "Integer32"
_EponSrvProfilePortMcTagStripMode_Object = MibTableColumn
eponSrvProfilePortMcTagStripMode = _EponSrvProfilePortMcTagStripMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 8, 1, 3),
    _EponSrvProfilePortMcTagStripMode_Type()
)
eponSrvProfilePortMcTagStripMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortMcTagStripMode.setStatus("current")
_EponSrvProfilePortMcTagStripSvlan_Type = EponVlanId
_EponSrvProfilePortMcTagStripSvlan_Object = MibTableColumn
eponSrvProfilePortMcTagStripSvlan = _EponSrvProfilePortMcTagStripSvlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 8, 1, 4),
    _EponSrvProfilePortMcTagStripSvlan_Type()
)
eponSrvProfilePortMcTagStripSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortMcTagStripSvlan.setStatus("current")
_EponSrvProfilePortMcTagStripCvlan_Type = EponVlanId
_EponSrvProfilePortMcTagStripCvlan_Object = MibTableColumn
eponSrvProfilePortMcTagStripCvlan = _EponSrvProfilePortMcTagStripCvlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 8, 1, 5),
    _EponSrvProfilePortMcTagStripCvlan_Type()
)
eponSrvProfilePortMcTagStripCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortMcTagStripCvlan.setStatus("current")
_EponSrvProfilePortMcRowStatus_Type = RowStatus
_EponSrvProfilePortMcRowStatus_Object = MibTableColumn
eponSrvProfilePortMcRowStatus = _EponSrvProfilePortMcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 8, 1, 6),
    _EponSrvProfilePortMcRowStatus_Type()
)
eponSrvProfilePortMcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortMcRowStatus.setStatus("current")
_EponSrvProfilePortMcVlanCfgTable_Object = MibTable
eponSrvProfilePortMcVlanCfgTable = _EponSrvProfilePortMcVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    eponSrvProfilePortMcVlanCfgTable.setStatus("current")
_EponSrvProfilePortMcVlanCfgEntry_Object = MibTableRow
eponSrvProfilePortMcVlanCfgEntry = _EponSrvProfilePortMcVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 9, 1)
)
eponSrvProfilePortMcVlanCfgEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponSrvProfileId"),
    (0, "CDATA-EPON-MIB", "eponSrvProfilePortType"),
    (0, "CDATA-EPON-MIB", "eponSrvProfilePortId"),
    (0, "CDATA-EPON-MIB", "eponSrvProfilePortMcVlanEntryId"),
)
if mibBuilder.loadTexts:
    eponSrvProfilePortMcVlanCfgEntry.setStatus("current")


class _EponSrvProfilePortMcVlanEntryId_Type(Integer32):
    """Custom type eponSrvProfilePortMcVlanEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EponSrvProfilePortMcVlanEntryId_Type.__name__ = "Integer32"
_EponSrvProfilePortMcVlanEntryId_Object = MibTableColumn
eponSrvProfilePortMcVlanEntryId = _EponSrvProfilePortMcVlanEntryId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 9, 1, 1),
    _EponSrvProfilePortMcVlanEntryId_Type()
)
eponSrvProfilePortMcVlanEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponSrvProfilePortMcVlanEntryId.setStatus("current")
_EponSrvProfilePortMcVlan_Type = EponVlanId
_EponSrvProfilePortMcVlan_Object = MibTableColumn
eponSrvProfilePortMcVlan = _EponSrvProfilePortMcVlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 9, 1, 2),
    _EponSrvProfilePortMcVlan_Type()
)
eponSrvProfilePortMcVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortMcVlan.setStatus("current")
_EponSrvProfilePortMcVlanRowStatus_Type = RowStatus
_EponSrvProfilePortMcVlanRowStatus_Object = MibTableColumn
eponSrvProfilePortMcVlanRowStatus = _EponSrvProfilePortMcVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 3, 9, 1, 3),
    _EponSrvProfilePortMcVlanRowStatus_Type()
)
eponSrvProfilePortMcVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSrvProfilePortMcVlanRowStatus.setStatus("current")
_EponTrafficProfileObjects_ObjectIdentity = ObjectIdentity
eponTrafficProfileObjects = _EponTrafficProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    eponTrafficProfileObjects.setStatus("current")
_EponTrafficProfileInfoTable_Object = MibTable
eponTrafficProfileInfoTable = _EponTrafficProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eponTrafficProfileInfoTable.setStatus("current")
_EponTrafficProfileInfoEntry_Object = MibTableRow
eponTrafficProfileInfoEntry = _EponTrafficProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1, 1)
)
eponTrafficProfileInfoEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponTrafficProfileId"),
)
if mibBuilder.loadTexts:
    eponTrafficProfileInfoEntry.setStatus("current")
_EponTrafficProfileId_Type = EponTrafficProfileId
_EponTrafficProfileId_Object = MibTableColumn
eponTrafficProfileId = _EponTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1, 1, 1),
    _EponTrafficProfileId_Type()
)
eponTrafficProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponTrafficProfileId.setStatus("current")
_EponTrafficProfileName_Type = EponTrafficProfileName
_EponTrafficProfileName_Object = MibTableColumn
eponTrafficProfileName = _EponTrafficProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1, 1, 2),
    _EponTrafficProfileName_Type()
)
eponTrafficProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponTrafficProfileName.setStatus("current")


class _EponTrafficProfileCfgCir_Type(Integer32):
    """Custom type eponTrafficProfileCfgCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 10240000),
    )


_EponTrafficProfileCfgCir_Type.__name__ = "Integer32"
_EponTrafficProfileCfgCir_Object = MibTableColumn
eponTrafficProfileCfgCir = _EponTrafficProfileCfgCir_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1, 1, 3),
    _EponTrafficProfileCfgCir_Type()
)
eponTrafficProfileCfgCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponTrafficProfileCfgCir.setStatus("current")


class _EponTrafficProfileCfgPir_Type(Integer32):
    """Custom type eponTrafficProfileCfgPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 10240000),
    )


_EponTrafficProfileCfgPir_Type.__name__ = "Integer32"
_EponTrafficProfileCfgPir_Object = MibTableColumn
eponTrafficProfileCfgPir = _EponTrafficProfileCfgPir_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1, 1, 4),
    _EponTrafficProfileCfgPir_Type()
)
eponTrafficProfileCfgPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponTrafficProfileCfgPir.setStatus("current")


class _EponTrafficProfileCfgCbs_Type(Integer32):
    """Custom type eponTrafficProfileCfgCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 10240000),
    )


_EponTrafficProfileCfgCbs_Type.__name__ = "Integer32"
_EponTrafficProfileCfgCbs_Object = MibTableColumn
eponTrafficProfileCfgCbs = _EponTrafficProfileCfgCbs_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1, 1, 5),
    _EponTrafficProfileCfgCbs_Type()
)
eponTrafficProfileCfgCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponTrafficProfileCfgCbs.setStatus("current")


class _EponTrafficProfileCfgPbs_Type(Integer32):
    """Custom type eponTrafficProfileCfgPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 10240000),
    )


_EponTrafficProfileCfgPbs_Type.__name__ = "Integer32"
_EponTrafficProfileCfgPbs_Object = MibTableColumn
eponTrafficProfileCfgPbs = _EponTrafficProfileCfgPbs_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1, 1, 6),
    _EponTrafficProfileCfgPbs_Type()
)
eponTrafficProfileCfgPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponTrafficProfileCfgPbs.setStatus("current")
_EponTrafficProfileCfgPriority_Type = Integer32
_EponTrafficProfileCfgPriority_Object = MibTableColumn
eponTrafficProfileCfgPriority = _EponTrafficProfileCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1, 1, 7),
    _EponTrafficProfileCfgPriority_Type()
)
eponTrafficProfileCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponTrafficProfileCfgPriority.setStatus("current")
_EponTrafficProfileBindNum_Type = Integer32
_EponTrafficProfileBindNum_Object = MibTableColumn
eponTrafficProfileBindNum = _EponTrafficProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1, 1, 8),
    _EponTrafficProfileBindNum_Type()
)
eponTrafficProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponTrafficProfileBindNum.setStatus("current")
_EponTrafficProfileRowStatus_Type = RowStatus
_EponTrafficProfileRowStatus_Object = MibTableColumn
eponTrafficProfileRowStatus = _EponTrafficProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 4, 1, 1, 9),
    _EponTrafficProfileRowStatus_Type()
)
eponTrafficProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponTrafficProfileRowStatus.setStatus("current")
_EponAlarmProfileObjects_ObjectIdentity = ObjectIdentity
eponAlarmProfileObjects = _EponAlarmProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    eponAlarmProfileObjects.setStatus("current")
_EponAlarmProfileInfoTable_Object = MibTable
eponAlarmProfileInfoTable = _EponAlarmProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    eponAlarmProfileInfoTable.setStatus("current")
_EponAlarmProfileInfoEntry_Object = MibTableRow
eponAlarmProfileInfoEntry = _EponAlarmProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 5, 1, 1)
)
eponAlarmProfileInfoEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponAlarmProfileId"),
    (0, "CDATA-EPON-MIB", "eponAlarmProfileTypeId"),
)
if mibBuilder.loadTexts:
    eponAlarmProfileInfoEntry.setStatus("current")


class _EponAlarmProfileId_Type(Integer32):
    """Custom type eponAlarmProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_EponAlarmProfileId_Type.__name__ = "Integer32"
_EponAlarmProfileId_Object = MibTableColumn
eponAlarmProfileId = _EponAlarmProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 5, 1, 1, 1),
    _EponAlarmProfileId_Type()
)
eponAlarmProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponAlarmProfileId.setStatus("current")


class _EponAlarmProfileTypeId_Type(Integer32):
    """Custom type eponAlarmProfileTypeId based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("rx-dropevents-alarm", 1),
          ("tx-dropevents-alarm", 2),
          ("rx-crcerrors-alarm", 3),
          ("tx-crcerrors-alarm", 4),
          ("rx-undersizes-alarm", 5),
          ("tx-undersizes-alarm", 6),
          ("rx-oversizes-alarm", 7),
          ("tx-oversizes-alarm", 8),
          ("rx-fragments-alarm", 9),
          ("tx-fragments-alarm", 10),
          ("rx-jabbers-alarm", 11),
          ("tx-jabbers-alarm", 12),
          ("rx-discards-alarm", 13),
          ("tx-discards-alarm", 14),
          ("rx-errors-alarm", 15),
          ("tx-errors-alarm", 16),
          ("rx-dropevents-warning", 17),
          ("tx-dropevents-warning", 18),
          ("rx-crcerrors-warning", 19),
          ("tx-crcerrors-warning", 20),
          ("rx-undersizes-warning", 21),
          ("tx-undersizes-warning", 22),
          ("rx-oversizes-warning", 23),
          ("tx-oversizes-warning", 24),
          ("rx-fragments-warning", 25),
          ("tx-fragments-warning", 26),
          ("rx-jabbers-warning", 27),
          ("tx-jabbers-warning", 28),
          ("rx-discards-warning", 29),
          ("tx-discards-warning", 30),
          ("rx-errors-warning", 31),
          ("tx-errors-warning", 32))
    )


_EponAlarmProfileTypeId_Type.__name__ = "Integer32"
_EponAlarmProfileTypeId_Object = MibTableColumn
eponAlarmProfileTypeId = _EponAlarmProfileTypeId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 5, 1, 1, 2),
    _EponAlarmProfileTypeId_Type()
)
eponAlarmProfileTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponAlarmProfileTypeId.setStatus("current")
_EponAlarmProfileName_Type = EponProfileName
_EponAlarmProfileName_Object = MibTableColumn
eponAlarmProfileName = _EponAlarmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 5, 1, 1, 3),
    _EponAlarmProfileName_Type()
)
eponAlarmProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponAlarmProfileName.setStatus("current")
_EponAlarmProfileThreshold_Type = EponAlarmProfileThreshold
_EponAlarmProfileThreshold_Object = MibTableColumn
eponAlarmProfileThreshold = _EponAlarmProfileThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 5, 1, 1, 5),
    _EponAlarmProfileThreshold_Type()
)
eponAlarmProfileThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponAlarmProfileThreshold.setStatus("current")
_EponAlarmProfileRestoreThreshold_Type = EponAlarmProfileThreshold
_EponAlarmProfileRestoreThreshold_Object = MibTableColumn
eponAlarmProfileRestoreThreshold = _EponAlarmProfileRestoreThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 5, 1, 1, 6),
    _EponAlarmProfileRestoreThreshold_Type()
)
eponAlarmProfileRestoreThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponAlarmProfileRestoreThreshold.setStatus("current")
_EponAlarmProfileRowStatus_Type = RowStatus
_EponAlarmProfileRowStatus_Object = MibTableColumn
eponAlarmProfileRowStatus = _EponAlarmProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 5, 1, 1, 7),
    _EponAlarmProfileRowStatus_Type()
)
eponAlarmProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponAlarmProfileRowStatus.setStatus("current")
_EponOpticalAlarmProfileObjects_ObjectIdentity = ObjectIdentity
eponOpticalAlarmProfileObjects = _EponOpticalAlarmProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    eponOpticalAlarmProfileObjects.setStatus("current")
_EponOpticalAlarmProfileInfoTable_Object = MibTable
eponOpticalAlarmProfileInfoTable = _EponOpticalAlarmProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    eponOpticalAlarmProfileInfoTable.setStatus("current")
_EponOpticalAlarmProfileInfoEntry_Object = MibTableRow
eponOpticalAlarmProfileInfoEntry = _EponOpticalAlarmProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 6, 1, 1)
)
eponOpticalAlarmProfileInfoEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponOpticalAlarmProfileId"),
    (0, "CDATA-EPON-MIB", "eponOpticalAlarmProfileTypeId"),
)
if mibBuilder.loadTexts:
    eponOpticalAlarmProfileInfoEntry.setStatus("current")


class _EponOpticalAlarmProfileId_Type(Integer32):
    """Custom type eponOpticalAlarmProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_EponOpticalAlarmProfileId_Type.__name__ = "Integer32"
_EponOpticalAlarmProfileId_Object = MibTableColumn
eponOpticalAlarmProfileId = _EponOpticalAlarmProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 6, 1, 1, 1),
    _EponOpticalAlarmProfileId_Type()
)
eponOpticalAlarmProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOpticalAlarmProfileId.setStatus("current")


class _EponOpticalAlarmProfileTypeId_Type(Integer32):
    """Custom type eponOpticalAlarmProfileTypeId based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("rx-power-high-alarm", 1),
          ("rx-power-low-alarm", 2),
          ("tx-power-high-alarm", 3),
          ("tx-power-low-alarm", 4),
          ("bias-high-alarm", 5),
          ("bias-low-alarm", 6),
          ("voltage-high-alarm", 7),
          ("voltage-low-alarm", 8),
          ("temperature-high-alarm", 9),
          ("temperature-low-alarm", 10),
          ("rx-power-high-warning", 11),
          ("rx-power-low-warning", 12),
          ("tx-power-high-warning", 13),
          ("tx-power-low-warning", 14),
          ("bias-high-warning", 15),
          ("bias-low-warning", 16),
          ("voltage-high-warning", 17),
          ("voltage-low-warning", 18),
          ("temperature-high-warning", 19),
          ("temperature-low-warning", 20))
    )


_EponOpticalAlarmProfileTypeId_Type.__name__ = "Integer32"
_EponOpticalAlarmProfileTypeId_Object = MibTableColumn
eponOpticalAlarmProfileTypeId = _EponOpticalAlarmProfileTypeId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 6, 1, 1, 2),
    _EponOpticalAlarmProfileTypeId_Type()
)
eponOpticalAlarmProfileTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOpticalAlarmProfileTypeId.setStatus("current")
_EponOpticalAlarmProfileName_Type = EponProfileName
_EponOpticalAlarmProfileName_Object = MibTableColumn
eponOpticalAlarmProfileName = _EponOpticalAlarmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 6, 1, 1, 3),
    _EponOpticalAlarmProfileName_Type()
)
eponOpticalAlarmProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOpticalAlarmProfileName.setStatus("current")
_EponOpticalAlarmProfileUpperThreshold_Type = OctetString
_EponOpticalAlarmProfileUpperThreshold_Object = MibTableColumn
eponOpticalAlarmProfileUpperThreshold = _EponOpticalAlarmProfileUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 6, 1, 1, 5),
    _EponOpticalAlarmProfileUpperThreshold_Type()
)
eponOpticalAlarmProfileUpperThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOpticalAlarmProfileUpperThreshold.setStatus("current")
_EponOpticalAlarmProfileLowerThreshold_Type = OctetString
_EponOpticalAlarmProfileLowerThreshold_Object = MibTableColumn
eponOpticalAlarmProfileLowerThreshold = _EponOpticalAlarmProfileLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 6, 1, 1, 6),
    _EponOpticalAlarmProfileLowerThreshold_Type()
)
eponOpticalAlarmProfileLowerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOpticalAlarmProfileLowerThreshold.setStatus("current")
_EponOpticalAlarmProfileRowStatus_Type = RowStatus
_EponOpticalAlarmProfileRowStatus_Object = MibTableColumn
eponOpticalAlarmProfileRowStatus = _EponOpticalAlarmProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 6, 1, 1, 7),
    _EponOpticalAlarmProfileRowStatus_Type()
)
eponOpticalAlarmProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOpticalAlarmProfileRowStatus.setStatus("current")
_EponSlaProfileObjects_ObjectIdentity = ObjectIdentity
eponSlaProfileObjects = _EponSlaProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    eponSlaProfileObjects.setStatus("current")
_EponSlaProfileInfoTable_Object = MibTable
eponSlaProfileInfoTable = _EponSlaProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    eponSlaProfileInfoTable.setStatus("current")
_EponSlaProfileInfoEntry_Object = MibTableRow
eponSlaProfileInfoEntry = _EponSlaProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 1, 1)
)
eponSlaProfileInfoEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponSlaProfileId"),
)
if mibBuilder.loadTexts:
    eponSlaProfileInfoEntry.setStatus("current")


class _EponSlaProfileId_Type(Integer32):
    """Custom type eponSlaProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_EponSlaProfileId_Type.__name__ = "Integer32"
_EponSlaProfileId_Object = MibTableColumn
eponSlaProfileId = _EponSlaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 1, 1, 1),
    _EponSlaProfileId_Type()
)
eponSlaProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponSlaProfileId.setStatus("current")
_EponSlaProfileName_Type = EponProfileName
_EponSlaProfileName_Object = MibTableColumn
eponSlaProfileName = _EponSlaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 1, 1, 2),
    _EponSlaProfileName_Type()
)
eponSlaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSlaProfileName.setStatus("current")


class _EponSlaProfileCycleLength_Type(Unsigned32):
    """Custom type eponSlaProfileCycleLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 16777215),
    )


_EponSlaProfileCycleLength_Type.__name__ = "Unsigned32"
_EponSlaProfileCycleLength_Object = MibTableColumn
eponSlaProfileCycleLength = _EponSlaProfileCycleLength_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 1, 1, 3),
    _EponSlaProfileCycleLength_Type()
)
eponSlaProfileCycleLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSlaProfileCycleLength.setStatus("current")


class _EponSlaProfileServicesNumber_Type(Unsigned32):
    """Custom type eponSlaProfileServicesNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EponSlaProfileServicesNumber_Type.__name__ = "Unsigned32"
_EponSlaProfileServicesNumber_Object = MibTableColumn
eponSlaProfileServicesNumber = _EponSlaProfileServicesNumber_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 1, 1, 4),
    _EponSlaProfileServicesNumber_Type()
)
eponSlaProfileServicesNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSlaProfileServicesNumber.setStatus("current")
_EponSlaProfileRowStatus_Type = RowStatus
_EponSlaProfileRowStatus_Object = MibTableColumn
eponSlaProfileRowStatus = _EponSlaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 1, 1, 5),
    _EponSlaProfileRowStatus_Type()
)
eponSlaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponSlaProfileRowStatus.setStatus("current")
_EponSlaProfileServiceTable_Object = MibTable
eponSlaProfileServiceTable = _EponSlaProfileServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    eponSlaProfileServiceTable.setStatus("current")
_EponSlaProfileServiceEntry_Object = MibTableRow
eponSlaProfileServiceEntry = _EponSlaProfileServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 2, 1)
)
eponSlaProfileServiceEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponSlaProfileId"),
    (0, "CDATA-EPON-MIB", "eponSlaProfileServiceId"),
)
if mibBuilder.loadTexts:
    eponSlaProfileServiceEntry.setStatus("current")


class _EponSlaProfileServiceId_Type(Integer32):
    """Custom type eponSlaProfileServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EponSlaProfileServiceId_Type.__name__ = "Integer32"
_EponSlaProfileServiceId_Object = MibTableColumn
eponSlaProfileServiceId = _EponSlaProfileServiceId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 2, 1, 1),
    _EponSlaProfileServiceId_Type()
)
eponSlaProfileServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponSlaProfileServiceId.setStatus("current")


class _EponSlaProfileServiceFixPacketSize_Type(Integer32):
    """Custom type eponSlaProfileServiceFixPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2000),
    )


_EponSlaProfileServiceFixPacketSize_Type.__name__ = "Integer32"
_EponSlaProfileServiceFixPacketSize_Object = MibTableColumn
eponSlaProfileServiceFixPacketSize = _EponSlaProfileServiceFixPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 2, 1, 2),
    _EponSlaProfileServiceFixPacketSize_Type()
)
eponSlaProfileServiceFixPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSlaProfileServiceFixPacketSize.setStatus("current")


class _EponSlaProfileServiceFixBandwidth_Type(Integer32):
    """Custom type eponSlaProfileServiceFixBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999936),
    )


_EponSlaProfileServiceFixBandwidth_Type.__name__ = "Integer32"
_EponSlaProfileServiceFixBandwidth_Object = MibTableColumn
eponSlaProfileServiceFixBandwidth = _EponSlaProfileServiceFixBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 2, 1, 3),
    _EponSlaProfileServiceFixBandwidth_Type()
)
eponSlaProfileServiceFixBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSlaProfileServiceFixBandwidth.setStatus("current")


class _EponSlaProfileServiceGuaranteBandwidth_Type(Integer32):
    """Custom type eponSlaProfileServiceGuaranteBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999936),
    )


_EponSlaProfileServiceGuaranteBandwidth_Type.__name__ = "Integer32"
_EponSlaProfileServiceGuaranteBandwidth_Object = MibTableColumn
eponSlaProfileServiceGuaranteBandwidth = _EponSlaProfileServiceGuaranteBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 2, 1, 4),
    _EponSlaProfileServiceGuaranteBandwidth_Type()
)
eponSlaProfileServiceGuaranteBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSlaProfileServiceGuaranteBandwidth.setStatus("current")


class _EponSlaProfileServiceBestEffortBandwidth_Type(Integer32):
    """Custom type eponSlaProfileServiceBestEffortBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999936),
    )


_EponSlaProfileServiceBestEffortBandwidth_Type.__name__ = "Integer32"
_EponSlaProfileServiceBestEffortBandwidth_Object = MibTableColumn
eponSlaProfileServiceBestEffortBandwidth = _EponSlaProfileServiceBestEffortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 2, 1, 5),
    _EponSlaProfileServiceBestEffortBandwidth_Type()
)
eponSlaProfileServiceBestEffortBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSlaProfileServiceBestEffortBandwidth.setStatus("current")


class _EponSlaProfileServiceWrrWeight_Type(Integer32):
    """Custom type eponSlaProfileServiceWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EponSlaProfileServiceWrrWeight_Type.__name__ = "Integer32"
_EponSlaProfileServiceWrrWeight_Object = MibTableColumn
eponSlaProfileServiceWrrWeight = _EponSlaProfileServiceWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1, 7, 2, 1, 6),
    _EponSlaProfileServiceWrrWeight_Type()
)
eponSlaProfileServiceWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponSlaProfileServiceWrrWeight.setStatus("current")
_EponControlObjects_ObjectIdentity = ObjectIdentity
eponControlObjects = _EponControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eponControlObjects.setStatus("current")
_EponOnuObjects_ObjectIdentity = ObjectIdentity
eponOnuObjects = _EponOnuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eponOnuObjects.setStatus("current")
_EponOnuAuthenticationManagement_ObjectIdentity = ObjectIdentity
eponOnuAuthenticationManagement = _EponOnuAuthenticationManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eponOnuAuthenticationManagement.setStatus("current")
_EponOnuAuthenticationModeTable_Object = MibTable
eponOnuAuthenticationModeTable = _EponOnuAuthenticationModeTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eponOnuAuthenticationModeTable.setStatus("current")
_EponOnuAuthenticationModeEntry_Object = MibTableRow
eponOnuAuthenticationModeEntry = _EponOnuAuthenticationModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 1, 1)
)
eponOnuAuthenticationModeEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponOnuAuthenticationModeDeviceId"),
    (0, "CDATA-EPON-MIB", "eponOnuAuthenticationModeSlotId"),
    (0, "CDATA-EPON-MIB", "eponOnuAuthenticationModePortId"),
)
if mibBuilder.loadTexts:
    eponOnuAuthenticationModeEntry.setStatus("current")
_EponOnuAuthenticationModeDeviceId_Type = Integer32
_EponOnuAuthenticationModeDeviceId_Object = MibTableColumn
eponOnuAuthenticationModeDeviceId = _EponOnuAuthenticationModeDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 1, 1, 1),
    _EponOnuAuthenticationModeDeviceId_Type()
)
eponOnuAuthenticationModeDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuAuthenticationModeDeviceId.setStatus("current")
_EponOnuAuthenticationModeSlotId_Type = Integer32
_EponOnuAuthenticationModeSlotId_Object = MibTableColumn
eponOnuAuthenticationModeSlotId = _EponOnuAuthenticationModeSlotId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 1, 1, 2),
    _EponOnuAuthenticationModeSlotId_Type()
)
eponOnuAuthenticationModeSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuAuthenticationModeSlotId.setStatus("current")
_EponOnuAuthenticationModePortId_Type = Integer32
_EponOnuAuthenticationModePortId_Object = MibTableColumn
eponOnuAuthenticationModePortId = _EponOnuAuthenticationModePortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 1, 1, 3),
    _EponOnuAuthenticationModePortId_Type()
)
eponOnuAuthenticationModePortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuAuthenticationModePortId.setStatus("current")
_EponOnuAuthenticationModeAdaptive_Type = EponSwitch
_EponOnuAuthenticationModeAdaptive_Object = MibTableColumn
eponOnuAuthenticationModeAdaptive = _EponOnuAuthenticationModeAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 1, 1, 4),
    _EponOnuAuthenticationModeAdaptive_Type()
)
eponOnuAuthenticationModeAdaptive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuAuthenticationModeAdaptive.setStatus("current")
_EponOnuAuthenticationConfigTable_Object = MibTable
eponOnuAuthenticationConfigTable = _EponOnuAuthenticationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eponOnuAuthenticationConfigTable.setStatus("current")
_EponOnuAuthenticationConfigEntry_Object = MibTableRow
eponOnuAuthenticationConfigEntry = _EponOnuAuthenticationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 2, 1)
)
eponOnuAuthenticationConfigEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponOnuAuthenOnuId"),
)
if mibBuilder.loadTexts:
    eponOnuAuthenticationConfigEntry.setStatus("current")
_EponOnuAuthenOnuId_Type = Unsigned32
_EponOnuAuthenOnuId_Object = MibTableColumn
eponOnuAuthenOnuId = _EponOnuAuthenOnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 2, 1, 1),
    _EponOnuAuthenOnuId_Type()
)
eponOnuAuthenOnuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuAuthenOnuId.setStatus("current")
_EponOnuAuthenMacAddress_Type = EponMacAddress
_EponOnuAuthenMacAddress_Object = MibTableColumn
eponOnuAuthenMacAddress = _EponOnuAuthenMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 2, 1, 2),
    _EponOnuAuthenMacAddress_Type()
)
eponOnuAuthenMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenMacAddress.setStatus("current")
_EponOnuAuthenLineProfileId_Type = EponLinePorfileId
_EponOnuAuthenLineProfileId_Object = MibTableColumn
eponOnuAuthenLineProfileId = _EponOnuAuthenLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 2, 1, 3),
    _EponOnuAuthenLineProfileId_Type()
)
eponOnuAuthenLineProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenLineProfileId.setStatus("current")
_EponOnuAuthenServiceProfileId_Type = EponSrvProfileId
_EponOnuAuthenServiceProfileId_Object = MibTableColumn
eponOnuAuthenServiceProfileId = _EponOnuAuthenServiceProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 2, 1, 4),
    _EponOnuAuthenServiceProfileId_Type()
)
eponOnuAuthenServiceProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenServiceProfileId.setStatus("current")


class _EponOnuAuthenTimeMode_Type(Integer32):
    """Custom type eponOnuAuthenTimeMode based on Integer32"""
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


_EponOnuAuthenTimeMode_Type.__name__ = "Integer32"
_EponOnuAuthenTimeMode_Object = MibTableColumn
eponOnuAuthenTimeMode = _EponOnuAuthenTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 2, 1, 5),
    _EponOnuAuthenTimeMode_Type()
)
eponOnuAuthenTimeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenTimeMode.setStatus("current")
_EponOnuAuthenExpireAt_Type = Integer32
_EponOnuAuthenExpireAt_Object = MibTableColumn
eponOnuAuthenExpireAt = _EponOnuAuthenExpireAt_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 2, 1, 6),
    _EponOnuAuthenExpireAt_Type()
)
eponOnuAuthenExpireAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuAuthenExpireAt.setStatus("current")
_EponOnuAuthenRowStatus_Type = RowStatus
_EponOnuAuthenRowStatus_Object = MibTableColumn
eponOnuAuthenRowStatus = _EponOnuAuthenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 2, 1, 7),
    _EponOnuAuthenRowStatus_Type()
)
eponOnuAuthenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenRowStatus.setStatus("current")
_EponOnuLoidAuthenticationConfigTable_Object = MibTable
eponOnuLoidAuthenticationConfigTable = _EponOnuLoidAuthenticationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eponOnuLoidAuthenticationConfigTable.setStatus("current")
_EponOnuLoidAuthenticationConfigEntry_Object = MibTableRow
eponOnuLoidAuthenticationConfigEntry = _EponOnuLoidAuthenticationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 3, 1)
)
eponOnuLoidAuthenticationConfigEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponOnuLoidAuthenOnuId"),
)
if mibBuilder.loadTexts:
    eponOnuLoidAuthenticationConfigEntry.setStatus("current")
_EponOnuLoidAuthenOnuId_Type = Unsigned32
_EponOnuLoidAuthenOnuId_Object = MibTableColumn
eponOnuLoidAuthenOnuId = _EponOnuLoidAuthenOnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 3, 1, 1),
    _EponOnuLoidAuthenOnuId_Type()
)
eponOnuLoidAuthenOnuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuLoidAuthenOnuId.setStatus("current")


class _EponOnuLoidAuthenLoid_Type(OctetString):
    """Custom type eponOnuLoidAuthenLoid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_EponOnuLoidAuthenLoid_Type.__name__ = "OctetString"
_EponOnuLoidAuthenLoid_Object = MibTableColumn
eponOnuLoidAuthenLoid = _EponOnuLoidAuthenLoid_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 3, 1, 2),
    _EponOnuLoidAuthenLoid_Type()
)
eponOnuLoidAuthenLoid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuLoidAuthenLoid.setStatus("current")


class _EponOnuLoidAuthenPassword_Type(OctetString):
    """Custom type eponOnuLoidAuthenPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_EponOnuLoidAuthenPassword_Type.__name__ = "OctetString"
_EponOnuLoidAuthenPassword_Object = MibTableColumn
eponOnuLoidAuthenPassword = _EponOnuLoidAuthenPassword_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 3, 1, 3),
    _EponOnuLoidAuthenPassword_Type()
)
eponOnuLoidAuthenPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuLoidAuthenPassword.setStatus("current")
_EponOnuLoidAuthenLineProfileId_Type = EponLinePorfileId
_EponOnuLoidAuthenLineProfileId_Object = MibTableColumn
eponOnuLoidAuthenLineProfileId = _EponOnuLoidAuthenLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 3, 1, 4),
    _EponOnuLoidAuthenLineProfileId_Type()
)
eponOnuLoidAuthenLineProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuLoidAuthenLineProfileId.setStatus("current")
_EponOnuLoidAuthenServiceProfileId_Type = EponSrvProfileId
_EponOnuLoidAuthenServiceProfileId_Object = MibTableColumn
eponOnuLoidAuthenServiceProfileId = _EponOnuLoidAuthenServiceProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 3, 1, 5),
    _EponOnuLoidAuthenServiceProfileId_Type()
)
eponOnuLoidAuthenServiceProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuLoidAuthenServiceProfileId.setStatus("current")


class _EponOnuLoidAuthenTimeMode_Type(Integer32):
    """Custom type eponOnuLoidAuthenTimeMode based on Integer32"""
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


_EponOnuLoidAuthenTimeMode_Type.__name__ = "Integer32"
_EponOnuLoidAuthenTimeMode_Object = MibTableColumn
eponOnuLoidAuthenTimeMode = _EponOnuLoidAuthenTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 3, 1, 6),
    _EponOnuLoidAuthenTimeMode_Type()
)
eponOnuLoidAuthenTimeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuLoidAuthenTimeMode.setStatus("current")
_EponOnuLoidAuthenExpireAt_Type = Integer32
_EponOnuLoidAuthenExpireAt_Object = MibTableColumn
eponOnuLoidAuthenExpireAt = _EponOnuLoidAuthenExpireAt_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 3, 1, 7),
    _EponOnuLoidAuthenExpireAt_Type()
)
eponOnuLoidAuthenExpireAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuLoidAuthenExpireAt.setStatus("current")
_EponOnuLoidAuthenRowStatus_Type = RowStatus
_EponOnuLoidAuthenRowStatus_Object = MibTableColumn
eponOnuLoidAuthenRowStatus = _EponOnuLoidAuthenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 3, 1, 8),
    _EponOnuLoidAuthenRowStatus_Type()
)
eponOnuLoidAuthenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuLoidAuthenRowStatus.setStatus("current")
_EponOnuAuthenticationConfirmTable_Object = MibTable
eponOnuAuthenticationConfirmTable = _EponOnuAuthenticationConfirmTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    eponOnuAuthenticationConfirmTable.setStatus("current")
_EponOnuAuthenticationConfirmEntry_Object = MibTableRow
eponOnuAuthenticationConfirmEntry = _EponOnuAuthenticationConfirmEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1)
)
eponOnuAuthenticationConfirmEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponOnuAuthenticationConfirmDeviceId"),
    (0, "CDATA-EPON-MIB", "eponOnuAuthenticationConfirmSlotId"),
    (0, "CDATA-EPON-MIB", "eponOnuAuthenticationConfirmPortId"),
)
if mibBuilder.loadTexts:
    eponOnuAuthenticationConfirmEntry.setStatus("current")
_EponOnuAuthenticationConfirmDeviceId_Type = Integer32
_EponOnuAuthenticationConfirmDeviceId_Object = MibTableColumn
eponOnuAuthenticationConfirmDeviceId = _EponOnuAuthenticationConfirmDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 1),
    _EponOnuAuthenticationConfirmDeviceId_Type()
)
eponOnuAuthenticationConfirmDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuAuthenticationConfirmDeviceId.setStatus("current")
_EponOnuAuthenticationConfirmSlotId_Type = Integer32
_EponOnuAuthenticationConfirmSlotId_Object = MibTableColumn
eponOnuAuthenticationConfirmSlotId = _EponOnuAuthenticationConfirmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 2),
    _EponOnuAuthenticationConfirmSlotId_Type()
)
eponOnuAuthenticationConfirmSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuAuthenticationConfirmSlotId.setStatus("current")
_EponOnuAuthenticationConfirmPortId_Type = Integer32
_EponOnuAuthenticationConfirmPortId_Object = MibTableColumn
eponOnuAuthenticationConfirmPortId = _EponOnuAuthenticationConfirmPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 3),
    _EponOnuAuthenticationConfirmPortId_Type()
)
eponOnuAuthenticationConfirmPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuAuthenticationConfirmPortId.setStatus("current")


class _EponOnuAuthenConfirmType_Type(Integer32):
    """Custom type eponOnuAuthenConfirmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("macAuth", 1),
          ("loidAuth", 2),
          ("loidPwdAuth", 3),
          ("macAuthAll", 4),
          ("loidAuthAll", 5),
          ("loidPwdAuthAll", 6))
    )


_EponOnuAuthenConfirmType_Type.__name__ = "Integer32"
_EponOnuAuthenConfirmType_Object = MibTableColumn
eponOnuAuthenConfirmType = _EponOnuAuthenConfirmType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 4),
    _EponOnuAuthenConfirmType_Type()
)
eponOnuAuthenConfirmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenConfirmType.setStatus("current")
_EponOnuAuthenConfirmMacAddress_Type = EponMacAddress
_EponOnuAuthenConfirmMacAddress_Object = MibTableColumn
eponOnuAuthenConfirmMacAddress = _EponOnuAuthenConfirmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 5),
    _EponOnuAuthenConfirmMacAddress_Type()
)
eponOnuAuthenConfirmMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenConfirmMacAddress.setStatus("current")


class _EponOnuAuthenConfirmLoid_Type(OctetString):
    """Custom type eponOnuAuthenConfirmLoid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_EponOnuAuthenConfirmLoid_Type.__name__ = "OctetString"
_EponOnuAuthenConfirmLoid_Object = MibTableColumn
eponOnuAuthenConfirmLoid = _EponOnuAuthenConfirmLoid_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 6),
    _EponOnuAuthenConfirmLoid_Type()
)
eponOnuAuthenConfirmLoid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenConfirmLoid.setStatus("current")


class _EponOnuAuthenConfirmLoidPassword_Type(OctetString):
    """Custom type eponOnuAuthenConfirmLoidPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_EponOnuAuthenConfirmLoidPassword_Type.__name__ = "OctetString"
_EponOnuAuthenConfirmLoidPassword_Object = MibTableColumn
eponOnuAuthenConfirmLoidPassword = _EponOnuAuthenConfirmLoidPassword_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 7),
    _EponOnuAuthenConfirmLoidPassword_Type()
)
eponOnuAuthenConfirmLoidPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenConfirmLoidPassword.setStatus("current")
_EponOnuAuthenConfirmLineProfileId_Type = EponLinePorfileId
_EponOnuAuthenConfirmLineProfileId_Object = MibTableColumn
eponOnuAuthenConfirmLineProfileId = _EponOnuAuthenConfirmLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 8),
    _EponOnuAuthenConfirmLineProfileId_Type()
)
eponOnuAuthenConfirmLineProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenConfirmLineProfileId.setStatus("current")
_EponOnuAuthenConfirmServiceProfileId_Type = EponSrvProfileId
_EponOnuAuthenConfirmServiceProfileId_Object = MibTableColumn
eponOnuAuthenConfirmServiceProfileId = _EponOnuAuthenConfirmServiceProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 9),
    _EponOnuAuthenConfirmServiceProfileId_Type()
)
eponOnuAuthenConfirmServiceProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenConfirmServiceProfileId.setStatus("current")


class _EponOnuAuthenConfirmTimeMode_Type(Integer32):
    """Custom type eponOnuAuthenConfirmTimeMode based on Integer32"""
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


_EponOnuAuthenConfirmTimeMode_Type.__name__ = "Integer32"
_EponOnuAuthenConfirmTimeMode_Object = MibTableColumn
eponOnuAuthenConfirmTimeMode = _EponOnuAuthenConfirmTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 10),
    _EponOnuAuthenConfirmTimeMode_Type()
)
eponOnuAuthenConfirmTimeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenConfirmTimeMode.setStatus("current")
_EponOnuAuthenConfirmAgingDuration_Type = Integer32
_EponOnuAuthenConfirmAgingDuration_Object = MibTableColumn
eponOnuAuthenConfirmAgingDuration = _EponOnuAuthenConfirmAgingDuration_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 11),
    _EponOnuAuthenConfirmAgingDuration_Type()
)
eponOnuAuthenConfirmAgingDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenConfirmAgingDuration.setStatus("current")
_EponOnuAuthenticationConfirmRowStatus_Type = RowStatus
_EponOnuAuthenticationConfirmRowStatus_Object = MibTableColumn
eponOnuAuthenticationConfirmRowStatus = _EponOnuAuthenticationConfirmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 4, 1, 12),
    _EponOnuAuthenticationConfirmRowStatus_Type()
)
eponOnuAuthenticationConfirmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuAuthenticationConfirmRowStatus.setStatus("current")
_EponOnuPolicyAuthTable_ObjectIdentity = ObjectIdentity
eponOnuPolicyAuthTable = _EponOnuPolicyAuthTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5)
)
_EponOnuPolicyAuthControlTable_Object = MibTable
eponOnuPolicyAuthControlTable = _EponOnuPolicyAuthControlTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    eponOnuPolicyAuthControlTable.setStatus("current")
_EponOnuPolicyAuthControlEntry_Object = MibTableRow
eponOnuPolicyAuthControlEntry = _EponOnuPolicyAuthControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 1, 1)
)
eponOnuPolicyAuthControlEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponOnuPolicyAuthControlDeviceId"),
)
if mibBuilder.loadTexts:
    eponOnuPolicyAuthControlEntry.setStatus("current")
_EponOnuPolicyAuthControlDeviceId_Type = Integer32
_EponOnuPolicyAuthControlDeviceId_Object = MibTableColumn
eponOnuPolicyAuthControlDeviceId = _EponOnuPolicyAuthControlDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 1, 1, 1),
    _EponOnuPolicyAuthControlDeviceId_Type()
)
eponOnuPolicyAuthControlDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthControlDeviceId.setStatus("current")
_EponOnuPolicyAuthSwitch_Type = EponSwitch
_EponOnuPolicyAuthSwitch_Object = MibTableColumn
eponOnuPolicyAuthSwitch = _EponOnuPolicyAuthSwitch_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 1, 1, 3),
    _EponOnuPolicyAuthSwitch_Type()
)
eponOnuPolicyAuthSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthSwitch.setStatus("current")


class _EponOnuPolicyAuthPortSwtichBitMap_Type(OctetString):
    """Custom type eponOnuPolicyAuthPortSwtichBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EponOnuPolicyAuthPortSwtichBitMap_Type.__name__ = "OctetString"
_EponOnuPolicyAuthPortSwtichBitMap_Object = MibTableColumn
eponOnuPolicyAuthPortSwtichBitMap = _EponOnuPolicyAuthPortSwtichBitMap_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 1, 1, 4),
    _EponOnuPolicyAuthPortSwtichBitMap_Type()
)
eponOnuPolicyAuthPortSwtichBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthPortSwtichBitMap.setStatus("current")


class _EponOnuPolicyAuthMode_Type(Integer32):
    """Custom type eponOnuPolicyAuthMode based on Integer32"""
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
          ("modelId", 2),
          ("vendorId", 3),
          ("modelIdAndSwver", 4))
    )


_EponOnuPolicyAuthMode_Type.__name__ = "Integer32"
_EponOnuPolicyAuthMode_Object = MibTableColumn
eponOnuPolicyAuthMode = _EponOnuPolicyAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 1, 1, 5),
    _EponOnuPolicyAuthMode_Type()
)
eponOnuPolicyAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthMode.setStatus("current")


class _EponOnuPolicyAuthTargetMode_Type(Integer32):
    """Custom type eponOnuPolicyAuthTargetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macAuth", 0),
          ("loidAuth", 1),
          ("loidPasswordAuth", 2))
    )


_EponOnuPolicyAuthTargetMode_Type.__name__ = "Integer32"
_EponOnuPolicyAuthTargetMode_Object = MibTableColumn
eponOnuPolicyAuthTargetMode = _EponOnuPolicyAuthTargetMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 1, 1, 6),
    _EponOnuPolicyAuthTargetMode_Type()
)
eponOnuPolicyAuthTargetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthTargetMode.setStatus("current")


class _EponOnuPolicyAuthTimeMode_Type(Integer32):
    """Custom type eponOnuPolicyAuthTimeMode based on Integer32"""
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


_EponOnuPolicyAuthTimeMode_Type.__name__ = "Integer32"
_EponOnuPolicyAuthTimeMode_Object = MibTableColumn
eponOnuPolicyAuthTimeMode = _EponOnuPolicyAuthTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 1, 1, 7),
    _EponOnuPolicyAuthTimeMode_Type()
)
eponOnuPolicyAuthTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthTimeMode.setStatus("current")
_EponOnuPolicyAuthRuleTable_Object = MibTable
eponOnuPolicyAuthRuleTable = _EponOnuPolicyAuthRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    eponOnuPolicyAuthRuleTable.setStatus("current")
_EponOnuPolicyAuthRuleEntry_Object = MibTableRow
eponOnuPolicyAuthRuleEntry = _EponOnuPolicyAuthRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 2, 1)
)
eponOnuPolicyAuthRuleEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponOnuPolicyAuthRuleId"),
)
if mibBuilder.loadTexts:
    eponOnuPolicyAuthRuleEntry.setStatus("current")
_EponOnuPolicyAuthRuleId_Type = Integer32
_EponOnuPolicyAuthRuleId_Object = MibTableColumn
eponOnuPolicyAuthRuleId = _EponOnuPolicyAuthRuleId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 2, 1, 1),
    _EponOnuPolicyAuthRuleId_Type()
)
eponOnuPolicyAuthRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthRuleId.setStatus("current")


class _EponOnuPolicyAuthRuleMatchMode_Type(Integer32):
    """Custom type eponOnuPolicyAuthRuleMatchMode based on Integer32"""
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
          ("modelId", 2),
          ("vendorId", 3),
          ("modelIdAndSwver", 4))
    )


_EponOnuPolicyAuthRuleMatchMode_Type.__name__ = "Integer32"
_EponOnuPolicyAuthRuleMatchMode_Object = MibTableColumn
eponOnuPolicyAuthRuleMatchMode = _EponOnuPolicyAuthRuleMatchMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 2, 1, 2),
    _EponOnuPolicyAuthRuleMatchMode_Type()
)
eponOnuPolicyAuthRuleMatchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthRuleMatchMode.setStatus("current")


class _EponOnuPolicyAuthRuleModelId_Type(OctetString):
    """Custom type eponOnuPolicyAuthRuleModelId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_EponOnuPolicyAuthRuleModelId_Type.__name__ = "OctetString"
_EponOnuPolicyAuthRuleModelId_Object = MibTableColumn
eponOnuPolicyAuthRuleModelId = _EponOnuPolicyAuthRuleModelId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 2, 1, 3),
    _EponOnuPolicyAuthRuleModelId_Type()
)
eponOnuPolicyAuthRuleModelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthRuleModelId.setStatus("current")


class _EponOnuPolicyAuthRuleVendorId_Type(OctetString):
    """Custom type eponOnuPolicyAuthRuleVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_EponOnuPolicyAuthRuleVendorId_Type.__name__ = "OctetString"
_EponOnuPolicyAuthRuleVendorId_Object = MibTableColumn
eponOnuPolicyAuthRuleVendorId = _EponOnuPolicyAuthRuleVendorId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 2, 1, 4),
    _EponOnuPolicyAuthRuleVendorId_Type()
)
eponOnuPolicyAuthRuleVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthRuleVendorId.setStatus("current")


class _EponOnuPolicyAuthRuleSoftwareVersion_Type(OctetString):
    """Custom type eponOnuPolicyAuthRuleSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EponOnuPolicyAuthRuleSoftwareVersion_Type.__name__ = "OctetString"
_EponOnuPolicyAuthRuleSoftwareVersion_Object = MibTableColumn
eponOnuPolicyAuthRuleSoftwareVersion = _EponOnuPolicyAuthRuleSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 2, 1, 5),
    _EponOnuPolicyAuthRuleSoftwareVersion_Type()
)
eponOnuPolicyAuthRuleSoftwareVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthRuleSoftwareVersion.setStatus("current")
_EponOnuPolicyAuthRuleLineProfileId_Type = EponLinePorfileId
_EponOnuPolicyAuthRuleLineProfileId_Object = MibTableColumn
eponOnuPolicyAuthRuleLineProfileId = _EponOnuPolicyAuthRuleLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 2, 1, 6),
    _EponOnuPolicyAuthRuleLineProfileId_Type()
)
eponOnuPolicyAuthRuleLineProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthRuleLineProfileId.setStatus("current")
_EponOnuPolicyAuthRuleSrvProfileId_Type = EponSrvProfileId
_EponOnuPolicyAuthRuleSrvProfileId_Object = MibTableColumn
eponOnuPolicyAuthRuleSrvProfileId = _EponOnuPolicyAuthRuleSrvProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 2, 1, 7),
    _EponOnuPolicyAuthRuleSrvProfileId_Type()
)
eponOnuPolicyAuthRuleSrvProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthRuleSrvProfileId.setStatus("current")
_EponOnuPolicyAuthRuleRowStatus_Type = RowStatus
_EponOnuPolicyAuthRuleRowStatus_Object = MibTableColumn
eponOnuPolicyAuthRuleRowStatus = _EponOnuPolicyAuthRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 1, 5, 2, 1, 8),
    _EponOnuPolicyAuthRuleRowStatus_Type()
)
eponOnuPolicyAuthRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuPolicyAuthRuleRowStatus.setStatus("current")
_EponOnuProfileConfigManagement_ObjectIdentity = ObjectIdentity
eponOnuProfileConfigManagement = _EponOnuProfileConfigManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    eponOnuProfileConfigManagement.setStatus("current")
_EponOnuProfileCfgTable_Object = MibTable
eponOnuProfileCfgTable = _EponOnuProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eponOnuProfileCfgTable.setStatus("current")
_EponOnuProfileCfgEntry_Object = MibTableRow
eponOnuProfileCfgEntry = _EponOnuProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 2, 1, 1)
)
eponOnuProfileCfgEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponOnuProfileCfgOnuId"),
)
if mibBuilder.loadTexts:
    eponOnuProfileCfgEntry.setStatus("current")
_EponOnuProfileCfgOnuId_Type = Integer32
_EponOnuProfileCfgOnuId_Object = MibTableColumn
eponOnuProfileCfgOnuId = _EponOnuProfileCfgOnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 2, 1, 1, 1),
    _EponOnuProfileCfgOnuId_Type()
)
eponOnuProfileCfgOnuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuProfileCfgOnuId.setStatus("current")


class _EponOnuAlarmProfileId_Type(Integer32):
    """Custom type eponOnuAlarmProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
        ValueRangeConstraint(65535, 65535),
    )


_EponOnuAlarmProfileId_Type.__name__ = "Integer32"
_EponOnuAlarmProfileId_Object = MibTableColumn
eponOnuAlarmProfileId = _EponOnuAlarmProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 2, 1, 1, 2),
    _EponOnuAlarmProfileId_Type()
)
eponOnuAlarmProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuAlarmProfileId.setStatus("current")


class _EponOnuOpticalAlarmProfileId_Type(Integer32):
    """Custom type eponOnuOpticalAlarmProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
        ValueRangeConstraint(65535, 65535),
    )


_EponOnuOpticalAlarmProfileId_Type.__name__ = "Integer32"
_EponOnuOpticalAlarmProfileId_Object = MibTableColumn
eponOnuOpticalAlarmProfileId = _EponOnuOpticalAlarmProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 2, 1, 1, 3),
    _EponOnuOpticalAlarmProfileId_Type()
)
eponOnuOpticalAlarmProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuOpticalAlarmProfileId.setStatus("current")


class _EponOnuSlaProfileId_Type(Integer32):
    """Custom type eponOnuSlaProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
        ValueRangeConstraint(65535, 65535),
    )


_EponOnuSlaProfileId_Type.__name__ = "Integer32"
_EponOnuSlaProfileId_Object = MibTableColumn
eponOnuSlaProfileId = _EponOnuSlaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 1, 2, 1, 1, 4),
    _EponOnuSlaProfileId_Type()
)
eponOnuSlaProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuSlaProfileId.setStatus("current")
_EponOnuPortObjects_ObjectIdentity = ObjectIdentity
eponOnuPortObjects = _EponOnuPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eponOnuPortObjects.setStatus("current")
_EponOnuPortConfigManagement_ObjectIdentity = ObjectIdentity
eponOnuPortConfigManagement = _EponOnuPortConfigManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    eponOnuPortConfigManagement.setStatus("current")
_EponOnuCatvPortCfgTable_Object = MibTable
eponOnuCatvPortCfgTable = _EponOnuCatvPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eponOnuCatvPortCfgTable.setStatus("current")
_EponOnuCatvPortCfgEntry_Object = MibTableRow
eponOnuCatvPortCfgEntry = _EponOnuCatvPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 2, 1, 1, 1)
)
eponOnuCatvPortCfgEntry.setIndexNames(
    (0, "CDATA-EPON-MIB", "eponOnuCatvPortCfgDeviceId"),
    (0, "CDATA-EPON-MIB", "eponOnuCatvPortCfgSlotId"),
    (0, "CDATA-EPON-MIB", "eponOnuCatvPortCfgPortId"),
)
if mibBuilder.loadTexts:
    eponOnuCatvPortCfgEntry.setStatus("current")
_EponOnuCatvPortCfgDeviceId_Type = Integer32
_EponOnuCatvPortCfgDeviceId_Object = MibTableColumn
eponOnuCatvPortCfgDeviceId = _EponOnuCatvPortCfgDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 2, 1, 1, 1, 1),
    _EponOnuCatvPortCfgDeviceId_Type()
)
eponOnuCatvPortCfgDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuCatvPortCfgDeviceId.setStatus("current")
_EponOnuCatvPortCfgSlotId_Type = Integer32
_EponOnuCatvPortCfgSlotId_Object = MibTableColumn
eponOnuCatvPortCfgSlotId = _EponOnuCatvPortCfgSlotId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 2, 1, 1, 1, 2),
    _EponOnuCatvPortCfgSlotId_Type()
)
eponOnuCatvPortCfgSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuCatvPortCfgSlotId.setStatus("current")
_EponOnuCatvPortCfgPortId_Type = Integer32
_EponOnuCatvPortCfgPortId_Object = MibTableColumn
eponOnuCatvPortCfgPortId = _EponOnuCatvPortCfgPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 2, 1, 1, 1, 3),
    _EponOnuCatvPortCfgPortId_Type()
)
eponOnuCatvPortCfgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuCatvPortCfgPortId.setStatus("current")
_EponOnuCatvPortOperationlState_Type = EponSwitch
_EponOnuCatvPortOperationlState_Object = MibTableColumn
eponOnuCatvPortOperationlState = _EponOnuCatvPortOperationlState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 2, 1, 1, 1, 4),
    _EponOnuCatvPortOperationlState_Type()
)
eponOnuCatvPortOperationlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuCatvPortOperationlState.setStatus("current")


class _EponOnuCatvPortRxPower_Type(OctetString):
    """Custom type eponOnuCatvPortRxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EponOnuCatvPortRxPower_Type.__name__ = "OctetString"
_EponOnuCatvPortRxPower_Object = MibTableColumn
eponOnuCatvPortRxPower = _EponOnuCatvPortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2, 2, 1, 1, 1, 5),
    _EponOnuCatvPortRxPower_Type()
)
eponOnuCatvPortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuCatvPortRxPower.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CDATA-EPON-MIB",
    **{"EponProfileName": EponProfileName,
       "EponAlarmProfileThreshold": EponAlarmProfileThreshold,
       "EponDbaProfileId": EponDbaProfileId,
       "EponDbaProfileName": EponDbaProfileName,
       "EponLinePorfileId": EponLinePorfileId,
       "EponLineProfileName": EponLineProfileName,
       "EponLineProfileLlId": EponLineProfileLlId,
       "EponSrvProfileId": EponSrvProfileId,
       "EponSrvProfileName": EponSrvProfileName,
       "EponTrafficProfileId": EponTrafficProfileId,
       "EponTrafficProfileName": EponTrafficProfileName,
       "EponSwitch": EponSwitch,
       "EponVlanId": EponVlanId,
       "EponVlanPriority": EponVlanPriority,
       "EponOltPortId": EponOltPortId,
       "EponOnuId": EponOnuId,
       "EponOnuEthPortId": EponOnuEthPortId,
       "EponOnuCatvPortId": EponOnuCatvPortId,
       "EponMacAddress": EponMacAddress,
       "eponMIB": eponMIB,
       "eponObjects": eponObjects,
       "eponProfileObjects": eponProfileObjects,
       "eponDbaProfileObjects": eponDbaProfileObjects,
       "eponDbaProfileInfoTable": eponDbaProfileInfoTable,
       "eponDbaProfileInfoEntry": eponDbaProfileInfoEntry,
       "eponDbaProfileId": eponDbaProfileId,
       "eponDbaProfileName": eponDbaProfileName,
       "eponDbaProfileType": eponDbaProfileType,
       "eponDbaProfileFixRate": eponDbaProfileFixRate,
       "eponDbaProfileAssureRate": eponDbaProfileAssureRate,
       "eponDbaProfileMaxRate": eponDbaProfileMaxRate,
       "eponDbaProfileBindNum": eponDbaProfileBindNum,
       "eponDbaProfileRowStatus": eponDbaProfileRowStatus,
       "eponLineProfileObjects": eponLineProfileObjects,
       "eponLineProfileInfoTable": eponLineProfileInfoTable,
       "eponLineProfileInfoEntry": eponLineProfileInfoEntry,
       "eponLineProfileId": eponLineProfileId,
       "eponLineProfileName": eponLineProfileName,
       "eponLineProfileUpstreamFECMode": eponLineProfileUpstreamFECMode,
       "eponLineProfileLlidNum": eponLineProfileLlidNum,
       "eponLineProfileBindNum": eponLineProfileBindNum,
       "eponLineProfileRowStatus": eponLineProfileRowStatus,
       "eponLineProfileLlidTable": eponLineProfileLlidTable,
       "eponLineProfileLlidEntry": eponLineProfileLlidEntry,
       "eponLineProfileLlId": eponLineProfileLlId,
       "eponLineProfileLlidDbaProfileId": eponLineProfileLlidDbaProfileId,
       "eponLineProfileLlidEncrypt": eponLineProfileLlidEncrypt,
       "eponLineProfileLlidOntCar": eponLineProfileLlidOntCar,
       "eponLineProfileLlidRowStatus": eponLineProfileLlidRowStatus,
       "eponLineProfileDbaThresholdTable": eponLineProfileDbaThresholdTable,
       "eponLineProfileDbaThresholdEntry": eponLineProfileDbaThresholdEntry,
       "eponLineProfileQueueSetId": eponLineProfileQueueSetId,
       "eponLineProfileQueueId": eponLineProfileQueueId,
       "eponLineProfileThreshold": eponLineProfileThreshold,
       "eponLineProfileDbaThresholdRowStatus": eponLineProfileDbaThresholdRowStatus,
       "eponSrvProfileObjects": eponSrvProfileObjects,
       "eponSrvProfileInfoTable": eponSrvProfileInfoTable,
       "eponSrvProfileInfoEntry": eponSrvProfileInfoEntry,
       "eponSrvProfileId": eponSrvProfileId,
       "eponSrvProfileName": eponSrvProfileName,
       "eponSrvProfileBindNum": eponSrvProfileBindNum,
       "eponSrvProfileRowStatus": eponSrvProfileRowStatus,
       "eponSrvProfileCfgTable": eponSrvProfileCfgTable,
       "eponSrvProfileCfgEntry": eponSrvProfileCfgEntry,
       "eponSrvProfileMcFastLeave": eponSrvProfileMcFastLeave,
       "eponSrvProfileMacLearning": eponSrvProfileMacLearning,
       "eponSrvProfileMacAgeSeconds": eponSrvProfileMacAgeSeconds,
       "eponSrvProfileLoopbackDetectCheck": eponSrvProfileLoopbackDetectCheck,
       "eponSrvProfilePortNumTable": eponSrvProfilePortNumTable,
       "eponSrvProfilePortNumEntry": eponSrvProfilePortNumEntry,
       "eponSrvProfileEthNum": eponSrvProfileEthNum,
       "eponSrvProfilePotsNum": eponSrvProfilePotsNum,
       "eponSrvProfileCatvNum": eponSrvProfileCatvNum,
       "eponSrvProfileEthPortCfgTable": eponSrvProfileEthPortCfgTable,
       "eponSrvProfileEthPortCfgEntry": eponSrvProfileEthPortCfgEntry,
       "eponSrvProfileEthPortMacLimited": eponSrvProfileEthPortMacLimited,
       "eponSrvProfileEthPortMtu": eponSrvProfileEthPortMtu,
       "eponSrvProfileEthPortFlowCtrl": eponSrvProfileEthPortFlowCtrl,
       "eponSrvProfileEthPortInTrafficProfileId": eponSrvProfileEthPortInTrafficProfileId,
       "eponSrvProfileEthPortOutTrafficProfileId": eponSrvProfileEthPortOutTrafficProfileId,
       "eponSrvProfileEthPortNativeVlanId": eponSrvProfileEthPortNativeVlanId,
       "eponSrvProfileEthPortNativeVlanPriority": eponSrvProfileEthPortNativeVlanPriority,
       "eponSrvProfilePortVlanCfgTable": eponSrvProfilePortVlanCfgTable,
       "eponSrvProfilePortVlanCfgEntry": eponSrvProfilePortVlanCfgEntry,
       "eponSrvProfilePortType": eponSrvProfilePortType,
       "eponSrvProfilePortId": eponSrvProfilePortId,
       "eponSrvProfilePortVlanEntryId": eponSrvProfilePortVlanEntryId,
       "eponSrvProfilePortVlanMode": eponSrvProfilePortVlanMode,
       "eponSrvProfilePortVlanSvlan": eponSrvProfilePortVlanSvlan,
       "eponSrvProfilePortVlanSpri": eponSrvProfilePortVlanSpri,
       "eponSrvProfilePortVlanCvlan": eponSrvProfilePortVlanCvlan,
       "eponSrvProfilePortVlanCpri": eponSrvProfilePortVlanCpri,
       "eponSrvProfilePortVlanRowStatus": eponSrvProfilePortVlanRowStatus,
       "eponSrvProfilePortMcCfgTable": eponSrvProfilePortMcCfgTable,
       "eponSrvProfilePortMcCfgEntry": eponSrvProfilePortMcCfgEntry,
       "eponSrvProfilePortMcEntryId": eponSrvProfilePortMcEntryId,
       "eponSrvProfilePortMcMaxGroupNum": eponSrvProfilePortMcMaxGroupNum,
       "eponSrvProfilePortMcTagStripMode": eponSrvProfilePortMcTagStripMode,
       "eponSrvProfilePortMcTagStripSvlan": eponSrvProfilePortMcTagStripSvlan,
       "eponSrvProfilePortMcTagStripCvlan": eponSrvProfilePortMcTagStripCvlan,
       "eponSrvProfilePortMcRowStatus": eponSrvProfilePortMcRowStatus,
       "eponSrvProfilePortMcVlanCfgTable": eponSrvProfilePortMcVlanCfgTable,
       "eponSrvProfilePortMcVlanCfgEntry": eponSrvProfilePortMcVlanCfgEntry,
       "eponSrvProfilePortMcVlanEntryId": eponSrvProfilePortMcVlanEntryId,
       "eponSrvProfilePortMcVlan": eponSrvProfilePortMcVlan,
       "eponSrvProfilePortMcVlanRowStatus": eponSrvProfilePortMcVlanRowStatus,
       "eponTrafficProfileObjects": eponTrafficProfileObjects,
       "eponTrafficProfileInfoTable": eponTrafficProfileInfoTable,
       "eponTrafficProfileInfoEntry": eponTrafficProfileInfoEntry,
       "eponTrafficProfileId": eponTrafficProfileId,
       "eponTrafficProfileName": eponTrafficProfileName,
       "eponTrafficProfileCfgCir": eponTrafficProfileCfgCir,
       "eponTrafficProfileCfgPir": eponTrafficProfileCfgPir,
       "eponTrafficProfileCfgCbs": eponTrafficProfileCfgCbs,
       "eponTrafficProfileCfgPbs": eponTrafficProfileCfgPbs,
       "eponTrafficProfileCfgPriority": eponTrafficProfileCfgPriority,
       "eponTrafficProfileBindNum": eponTrafficProfileBindNum,
       "eponTrafficProfileRowStatus": eponTrafficProfileRowStatus,
       "eponAlarmProfileObjects": eponAlarmProfileObjects,
       "eponAlarmProfileInfoTable": eponAlarmProfileInfoTable,
       "eponAlarmProfileInfoEntry": eponAlarmProfileInfoEntry,
       "eponAlarmProfileId": eponAlarmProfileId,
       "eponAlarmProfileTypeId": eponAlarmProfileTypeId,
       "eponAlarmProfileName": eponAlarmProfileName,
       "eponAlarmProfileThreshold": eponAlarmProfileThreshold,
       "eponAlarmProfileRestoreThreshold": eponAlarmProfileRestoreThreshold,
       "eponAlarmProfileRowStatus": eponAlarmProfileRowStatus,
       "eponOpticalAlarmProfileObjects": eponOpticalAlarmProfileObjects,
       "eponOpticalAlarmProfileInfoTable": eponOpticalAlarmProfileInfoTable,
       "eponOpticalAlarmProfileInfoEntry": eponOpticalAlarmProfileInfoEntry,
       "eponOpticalAlarmProfileId": eponOpticalAlarmProfileId,
       "eponOpticalAlarmProfileTypeId": eponOpticalAlarmProfileTypeId,
       "eponOpticalAlarmProfileName": eponOpticalAlarmProfileName,
       "eponOpticalAlarmProfileUpperThreshold": eponOpticalAlarmProfileUpperThreshold,
       "eponOpticalAlarmProfileLowerThreshold": eponOpticalAlarmProfileLowerThreshold,
       "eponOpticalAlarmProfileRowStatus": eponOpticalAlarmProfileRowStatus,
       "eponSlaProfileObjects": eponSlaProfileObjects,
       "eponSlaProfileInfoTable": eponSlaProfileInfoTable,
       "eponSlaProfileInfoEntry": eponSlaProfileInfoEntry,
       "eponSlaProfileId": eponSlaProfileId,
       "eponSlaProfileName": eponSlaProfileName,
       "eponSlaProfileCycleLength": eponSlaProfileCycleLength,
       "eponSlaProfileServicesNumber": eponSlaProfileServicesNumber,
       "eponSlaProfileRowStatus": eponSlaProfileRowStatus,
       "eponSlaProfileServiceTable": eponSlaProfileServiceTable,
       "eponSlaProfileServiceEntry": eponSlaProfileServiceEntry,
       "eponSlaProfileServiceId": eponSlaProfileServiceId,
       "eponSlaProfileServiceFixPacketSize": eponSlaProfileServiceFixPacketSize,
       "eponSlaProfileServiceFixBandwidth": eponSlaProfileServiceFixBandwidth,
       "eponSlaProfileServiceGuaranteBandwidth": eponSlaProfileServiceGuaranteBandwidth,
       "eponSlaProfileServiceBestEffortBandwidth": eponSlaProfileServiceBestEffortBandwidth,
       "eponSlaProfileServiceWrrWeight": eponSlaProfileServiceWrrWeight,
       "eponControlObjects": eponControlObjects,
       "eponOnuObjects": eponOnuObjects,
       "eponOnuAuthenticationManagement": eponOnuAuthenticationManagement,
       "eponOnuAuthenticationModeTable": eponOnuAuthenticationModeTable,
       "eponOnuAuthenticationModeEntry": eponOnuAuthenticationModeEntry,
       "eponOnuAuthenticationModeDeviceId": eponOnuAuthenticationModeDeviceId,
       "eponOnuAuthenticationModeSlotId": eponOnuAuthenticationModeSlotId,
       "eponOnuAuthenticationModePortId": eponOnuAuthenticationModePortId,
       "eponOnuAuthenticationModeAdaptive": eponOnuAuthenticationModeAdaptive,
       "eponOnuAuthenticationConfigTable": eponOnuAuthenticationConfigTable,
       "eponOnuAuthenticationConfigEntry": eponOnuAuthenticationConfigEntry,
       "eponOnuAuthenOnuId": eponOnuAuthenOnuId,
       "eponOnuAuthenMacAddress": eponOnuAuthenMacAddress,
       "eponOnuAuthenLineProfileId": eponOnuAuthenLineProfileId,
       "eponOnuAuthenServiceProfileId": eponOnuAuthenServiceProfileId,
       "eponOnuAuthenTimeMode": eponOnuAuthenTimeMode,
       "eponOnuAuthenExpireAt": eponOnuAuthenExpireAt,
       "eponOnuAuthenRowStatus": eponOnuAuthenRowStatus,
       "eponOnuLoidAuthenticationConfigTable": eponOnuLoidAuthenticationConfigTable,
       "eponOnuLoidAuthenticationConfigEntry": eponOnuLoidAuthenticationConfigEntry,
       "eponOnuLoidAuthenOnuId": eponOnuLoidAuthenOnuId,
       "eponOnuLoidAuthenLoid": eponOnuLoidAuthenLoid,
       "eponOnuLoidAuthenPassword": eponOnuLoidAuthenPassword,
       "eponOnuLoidAuthenLineProfileId": eponOnuLoidAuthenLineProfileId,
       "eponOnuLoidAuthenServiceProfileId": eponOnuLoidAuthenServiceProfileId,
       "eponOnuLoidAuthenTimeMode": eponOnuLoidAuthenTimeMode,
       "eponOnuLoidAuthenExpireAt": eponOnuLoidAuthenExpireAt,
       "eponOnuLoidAuthenRowStatus": eponOnuLoidAuthenRowStatus,
       "eponOnuAuthenticationConfirmTable": eponOnuAuthenticationConfirmTable,
       "eponOnuAuthenticationConfirmEntry": eponOnuAuthenticationConfirmEntry,
       "eponOnuAuthenticationConfirmDeviceId": eponOnuAuthenticationConfirmDeviceId,
       "eponOnuAuthenticationConfirmSlotId": eponOnuAuthenticationConfirmSlotId,
       "eponOnuAuthenticationConfirmPortId": eponOnuAuthenticationConfirmPortId,
       "eponOnuAuthenConfirmType": eponOnuAuthenConfirmType,
       "eponOnuAuthenConfirmMacAddress": eponOnuAuthenConfirmMacAddress,
       "eponOnuAuthenConfirmLoid": eponOnuAuthenConfirmLoid,
       "eponOnuAuthenConfirmLoidPassword": eponOnuAuthenConfirmLoidPassword,
       "eponOnuAuthenConfirmLineProfileId": eponOnuAuthenConfirmLineProfileId,
       "eponOnuAuthenConfirmServiceProfileId": eponOnuAuthenConfirmServiceProfileId,
       "eponOnuAuthenConfirmTimeMode": eponOnuAuthenConfirmTimeMode,
       "eponOnuAuthenConfirmAgingDuration": eponOnuAuthenConfirmAgingDuration,
       "eponOnuAuthenticationConfirmRowStatus": eponOnuAuthenticationConfirmRowStatus,
       "eponOnuPolicyAuthTable": eponOnuPolicyAuthTable,
       "eponOnuPolicyAuthControlTable": eponOnuPolicyAuthControlTable,
       "eponOnuPolicyAuthControlEntry": eponOnuPolicyAuthControlEntry,
       "eponOnuPolicyAuthControlDeviceId": eponOnuPolicyAuthControlDeviceId,
       "eponOnuPolicyAuthSwitch": eponOnuPolicyAuthSwitch,
       "eponOnuPolicyAuthPortSwtichBitMap": eponOnuPolicyAuthPortSwtichBitMap,
       "eponOnuPolicyAuthMode": eponOnuPolicyAuthMode,
       "eponOnuPolicyAuthTargetMode": eponOnuPolicyAuthTargetMode,
       "eponOnuPolicyAuthTimeMode": eponOnuPolicyAuthTimeMode,
       "eponOnuPolicyAuthRuleTable": eponOnuPolicyAuthRuleTable,
       "eponOnuPolicyAuthRuleEntry": eponOnuPolicyAuthRuleEntry,
       "eponOnuPolicyAuthRuleId": eponOnuPolicyAuthRuleId,
       "eponOnuPolicyAuthRuleMatchMode": eponOnuPolicyAuthRuleMatchMode,
       "eponOnuPolicyAuthRuleModelId": eponOnuPolicyAuthRuleModelId,
       "eponOnuPolicyAuthRuleVendorId": eponOnuPolicyAuthRuleVendorId,
       "eponOnuPolicyAuthRuleSoftwareVersion": eponOnuPolicyAuthRuleSoftwareVersion,
       "eponOnuPolicyAuthRuleLineProfileId": eponOnuPolicyAuthRuleLineProfileId,
       "eponOnuPolicyAuthRuleSrvProfileId": eponOnuPolicyAuthRuleSrvProfileId,
       "eponOnuPolicyAuthRuleRowStatus": eponOnuPolicyAuthRuleRowStatus,
       "eponOnuProfileConfigManagement": eponOnuProfileConfigManagement,
       "eponOnuProfileCfgTable": eponOnuProfileCfgTable,
       "eponOnuProfileCfgEntry": eponOnuProfileCfgEntry,
       "eponOnuProfileCfgOnuId": eponOnuProfileCfgOnuId,
       "eponOnuAlarmProfileId": eponOnuAlarmProfileId,
       "eponOnuOpticalAlarmProfileId": eponOnuOpticalAlarmProfileId,
       "eponOnuSlaProfileId": eponOnuSlaProfileId,
       "eponOnuPortObjects": eponOnuPortObjects,
       "eponOnuPortConfigManagement": eponOnuPortConfigManagement,
       "eponOnuCatvPortCfgTable": eponOnuCatvPortCfgTable,
       "eponOnuCatvPortCfgEntry": eponOnuCatvPortCfgEntry,
       "eponOnuCatvPortCfgDeviceId": eponOnuCatvPortCfgDeviceId,
       "eponOnuCatvPortCfgSlotId": eponOnuCatvPortCfgSlotId,
       "eponOnuCatvPortCfgPortId": eponOnuCatvPortCfgPortId,
       "eponOnuCatvPortOperationlState": eponOnuCatvPortOperationlState,
       "eponOnuCatvPortRxPower": eponOnuCatvPortRxPower}
)
