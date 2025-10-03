# SNMP MIB module (TROPIC-OTUODU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-OTUODU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:40 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnOtuOduMIB,
 tnPortModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnOtuOduMIB",
    "tnPortModules")

(AluWdmFecMode,
 AluWdmOdukStatus,
 AluWdmPortOchOtuRate,
 AluWdmTtiStatus,
 TropicAdminStateType,
 TropicOperationalCapabilityType,
 TropicOperationalStateType,
 TropicStateQualifierType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmFecMode",
    "AluWdmOdukStatus",
    "AluWdmPortOchOtuRate",
    "AluWdmTtiStatus",
    "TropicAdminStateType",
    "TropicOperationalCapabilityType",
    "TropicOperationalStateType",
    "TropicStateQualifierType")


# MODULE-IDENTITY

tnOtuOduMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    tnOtuOduMibModule.setRevisions(
        ("2023-02-10 12:00",
         "2022-07-15 12:00",
         "2022-06-10 12:00",
         "2022-06-03 12:00",
         "2022-05-13 12:00",
         "2022-04-15 12:00",
         "2022-03-25 12:00",
         "2022-03-18 12:00",
         "2022-02-25 12:00",
         "2021-12-10 12:00",
         "2021-12-03 12:00",
         "2021-11-12 12:00",
         "2021-06-18 12:00",
         "2021-05-14 12:00",
         "2021-02-26 12:00",
         "2021-01-15 12:00",
         "2020-12-11 12:00",
         "2020-07-10 12:00",
         "2020-05-08 12:00",
         "2020-03-20 12:00",
         "2020-02-21 12:00",
         "2019-11-01 12:00",
         "2019-10-25 12:00",
         "2019-08-30 12:00",
         "2019-06-07 12:00",
         "2019-05-31 12:00",
         "2019-04-26 12:00",
         "2019-04-12 12:00",
         "2019-04-05 12:00",
         "2019-03-08 12:00",
         "2019-02-15 12:00",
         "2019-02-08 12:00",
         "2019-01-11 12:00",
         "2018-12-28 12:00",
         "2018-02-23 12:00",
         "2017-07-07 12:00",
         "2017-02-24 12:00",
         "2017-01-20 12:00",
         "2016-11-16 12:00",
         "2016-03-25 12:00",
         "2016-03-02 12:00",
         "2015-07-17 12:00",
         "2015-05-15 12:00",
         "2014-11-13 12:00",
         "2014-10-31 12:00",
         "2014-02-26 12:00",
         "2013-04-16 12:00",
         "2013-03-14 12:00",
         "2012-12-05 12:00",
         "2012-10-22 12:00",
         "2012-09-28 12:00",
         "2012-09-24 12:00",
         "2012-08-22 12:00",
         "2012-04-10 12:00",
         "2011-07-22 12:00",
         "2011-04-25 12:00",
         "2011-03-30 12:00",
         "2011-03-04 12:00",
         "2011-02-23 12:00",
         "2010-11-24 12:00",
         "2010-11-22 12:00",
         "2010-11-14 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnOtuOduConf_ObjectIdentity = ObjectIdentity
tnOtuOduConf = _TnOtuOduConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1)
)
_TnOtuOduGroups_ObjectIdentity = ObjectIdentity
tnOtuOduGroups = _TnOtuOduGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 1)
)
_TnOtuOduCompliances_ObjectIdentity = ObjectIdentity
tnOtuOduCompliances = _TnOtuOduCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 2)
)
_TnOtuOduObjs_ObjectIdentity = ObjectIdentity
tnOtuOduObjs = _TnOtuOduObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2)
)
_TnOtuOduBasics_ObjectIdentity = ObjectIdentity
tnOtuOduBasics = _TnOtuOduBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1)
)
_TnOtukTable_Object = MibTable
tnOtukTable = _TnOtukTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnOtukTable.setStatus("current")
_TnOtukEntry_Object = MibTableRow
tnOtukEntry = _TnOtukEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1)
)
tnOtukEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnOtukEntry.setStatus("current")


class _TnOtukTtiStatus_Type(AluWdmTtiStatus):
    """Custom type tnOtukTtiStatus based on AluWdmTtiStatus"""
    defaultValue = 4


_TnOtukTtiStatus_Type.__name__ = "AluWdmTtiStatus"
_TnOtukTtiStatus_Object = MibTableColumn
tnOtukTtiStatus = _TnOtukTtiStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 1),
    _TnOtukTtiStatus_Type()
)
tnOtukTtiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukTtiStatus.setStatus("current")


class _TnOtukFecMode_Type(AluWdmFecMode):
    """Custom type tnOtukFecMode based on AluWdmFecMode"""
    defaultValue = 3


_TnOtukFecMode_Type.__name__ = "AluWdmFecMode"
_TnOtukFecMode_Object = MibTableColumn
tnOtukFecMode = _TnOtukFecMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 2),
    _TnOtukFecMode_Type()
)
tnOtukFecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukFecMode.setStatus("current")


class _TnOtukRate_Type(AluWdmPortOchOtuRate):
    """Custom type tnOtukRate based on AluWdmPortOchOtuRate"""
    defaultValue = 1


_TnOtukRate_Type.__name__ = "AluWdmPortOchOtuRate"
_TnOtukRate_Object = MibTableColumn
tnOtukRate = _TnOtukRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 3),
    _TnOtukRate_Type()
)
tnOtukRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukRate.setStatus("current")


class _TnOtukIncRes_Type(OctetString):
    """Custom type tnOtukIncRes based on OctetString"""
    defaultValue = OctetString("")


_TnOtukIncRes_Type.__name__ = "OctetString"
_TnOtukIncRes_Object = MibTableColumn
tnOtukIncRes = _TnOtukIncRes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 4),
    _TnOtukIncRes_Type()
)
tnOtukIncRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukIncRes.setStatus("current")


class _TnOtukAdminStatus_Type(AluWdmOdukStatus):
    """Custom type tnOtukAdminStatus based on AluWdmOdukStatus"""
    defaultValue = 2


_TnOtukAdminStatus_Type.__name__ = "AluWdmOdukStatus"
_TnOtukAdminStatus_Object = MibTableColumn
tnOtukAdminStatus = _TnOtukAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 5),
    _TnOtukAdminStatus_Type()
)
tnOtukAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukAdminStatus.setStatus("current")


class _TnOtukStateAINS_Type(TruthValue):
    """Custom type tnOtukStateAINS based on TruthValue"""
    defaultValue = 2


_TnOtukStateAINS_Type.__name__ = "TruthValue"
_TnOtukStateAINS_Object = MibTableColumn
tnOtukStateAINS = _TnOtukStateAINS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 6),
    _TnOtukStateAINS_Type()
)
tnOtukStateAINS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukStateAINS.setStatus("current")


class _TnOtukOperStatus_Type(AluWdmOdukStatus):
    """Custom type tnOtukOperStatus based on AluWdmOdukStatus"""
    defaultValue = 2


_TnOtukOperStatus_Type.__name__ = "AluWdmOdukStatus"
_TnOtukOperStatus_Object = MibTableColumn
tnOtukOperStatus = _TnOtukOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 7),
    _TnOtukOperStatus_Type()
)
tnOtukOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukOperStatus.setStatus("current")
_TnOtukStateQualifier_Type = TropicStateQualifierType
_TnOtukStateQualifier_Object = MibTableColumn
tnOtukStateQualifier = _TnOtukStateQualifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 8),
    _TnOtukStateQualifier_Type()
)
tnOtukStateQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukStateQualifier.setStatus("current")


class _TnOtukOperationalCapability_Type(TropicOperationalCapabilityType):
    """Custom type tnOtukOperationalCapability based on TropicOperationalCapabilityType"""
    defaultValue = 1


_TnOtukOperationalCapability_Type.__name__ = "TropicOperationalCapabilityType"
_TnOtukOperationalCapability_Object = MibTableColumn
tnOtukOperationalCapability = _TnOtukOperationalCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 9),
    _TnOtukOperationalCapability_Type()
)
tnOtukOperationalCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukOperationalCapability.setStatus("current")
_TnOtukAINSDebounceTime_Type = Integer32
_TnOtukAINSDebounceTime_Object = MibTableColumn
tnOtukAINSDebounceTime = _TnOtukAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 10),
    _TnOtukAINSDebounceTime_Type()
)
tnOtukAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukAINSDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    tnOtukAINSDebounceTime.setUnits("Seconds")
_TnOtukUsingSysAINSDebounceTime_Type = TruthValue
_TnOtukUsingSysAINSDebounceTime_Object = MibTableColumn
tnOtukUsingSysAINSDebounceTime = _TnOtukUsingSysAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 11),
    _TnOtukUsingSysAINSDebounceTime_Type()
)
tnOtukUsingSysAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukUsingSysAINSDebounceTime.setStatus("current")


class _TnOtukAINSDebounceTimeRemaining_Type(Unsigned32):
    """Custom type tnOtukAINSDebounceTimeRemaining based on Unsigned32"""
    defaultValue = 0


_TnOtukAINSDebounceTimeRemaining_Type.__name__ = "Unsigned32"
_TnOtukAINSDebounceTimeRemaining_Object = MibTableColumn
tnOtukAINSDebounceTimeRemaining = _TnOtukAINSDebounceTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 12),
    _TnOtukAINSDebounceTimeRemaining_Type()
)
tnOtukAINSDebounceTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukAINSDebounceTimeRemaining.setStatus("current")
_TnOtukPreFec_Type = Counter64
_TnOtukPreFec_Object = MibTableColumn
tnOtukPreFec = _TnOtukPreFec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 14),
    _TnOtukPreFec_Type()
)
tnOtukPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukPreFec.setStatus("current")
_TnOtukPostFec_Type = Counter64
_TnOtukPostFec_Object = MibTableColumn
tnOtukPostFec = _TnOtukPostFec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 15),
    _TnOtukPostFec_Type()
)
tnOtukPostFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukPostFec.setStatus("current")


class _TnOtukAsymInterworking_Type(TruthValue):
    """Custom type tnOtukAsymInterworking based on TruthValue"""
    defaultValue = 2


_TnOtukAsymInterworking_Type.__name__ = "TruthValue"
_TnOtukAsymInterworking_Object = MibTableColumn
tnOtukAsymInterworking = _TnOtukAsymInterworking_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 17),
    _TnOtukAsymInterworking_Type()
)
tnOtukAsymInterworking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukAsymInterworking.setStatus("current")
_TnOtukDegThr_Type = Unsigned32
_TnOtukDegThr_Object = MibTableColumn
tnOtukDegThr = _TnOtukDegThr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 18),
    _TnOtukDegThr_Type()
)
tnOtukDegThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukDegThr.setStatus("current")
_TnOtukDegM_Type = Unsigned32
_TnOtukDegM_Object = MibTableColumn
tnOtukDegM = _TnOtukDegM_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 19),
    _TnOtukDegM_Type()
)
tnOtukDegM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukDegM.setStatus("current")


class _TnOtukDapiAccepted_Type(OctetString):
    """Custom type tnOtukDapiAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOtukDapiAccepted_Type.__name__ = "OctetString"
_TnOtukDapiAccepted_Object = MibTableColumn
tnOtukDapiAccepted = _TnOtukDapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 20),
    _TnOtukDapiAccepted_Type()
)
tnOtukDapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukDapiAccepted.setStatus("current")


class _TnOtukDapiExpected_Type(OctetString):
    """Custom type tnOtukDapiExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOtukDapiExpected_Type.__name__ = "OctetString"
_TnOtukDapiExpected_Object = MibTableColumn
tnOtukDapiExpected = _TnOtukDapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 21),
    _TnOtukDapiExpected_Type()
)
tnOtukDapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukDapiExpected.setStatus("current")


class _TnOtukDapiTransmitted_Type(OctetString):
    """Custom type tnOtukDapiTransmitted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOtukDapiTransmitted_Type.__name__ = "OctetString"
_TnOtukDapiTransmitted_Object = MibTableColumn
tnOtukDapiTransmitted = _TnOtukDapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 22),
    _TnOtukDapiTransmitted_Type()
)
tnOtukDapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukDapiTransmitted.setStatus("current")


class _TnOtukOsAccepted_Type(OctetString):
    """Custom type tnOtukOsAccepted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnOtukOsAccepted_Type.__name__ = "OctetString"
_TnOtukOsAccepted_Object = MibTableColumn
tnOtukOsAccepted = _TnOtukOsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 23),
    _TnOtukOsAccepted_Type()
)
tnOtukOsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtukOsAccepted.setStatus("current")


class _TnOtukOsTransmitted_Type(OctetString):
    """Custom type tnOtukOsTransmitted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnOtukOsTransmitted_Type.__name__ = "OctetString"
_TnOtukOsTransmitted_Object = MibTableColumn
tnOtukOsTransmitted = _TnOtukOsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 24),
    _TnOtukOsTransmitted_Type()
)
tnOtukOsTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukOsTransmitted.setStatus("current")
_TnOtuAlmProfName_Type = OctetString
_TnOtuAlmProfName_Object = MibTableColumn
tnOtuAlmProfName = _TnOtuAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 25),
    _TnOtuAlmProfName_Type()
)
tnOtuAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtuAlmProfName.setStatus("current")


class _TnOtuServerPort_Type(Integer32):
    """Custom type tnOtuServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              11,
              12,
              13,
              14,
              21,
              22,
              31,
              32,
              33,
              34,
              35,
              41,
              42,
              43,
              44,
              51,
              52,
              61,
              62,
              63,
              64,
              65,
              71,
              72,
              81,
              82)
        )
    )
    namedValues = NamedValues(
        *(("unassigned", 0),
          ("spL1Ch1", 11),
          ("spL1Ch2", 12),
          ("spL1Ch3", 13),
          ("spL1Ch4", 14),
          ("spL2Ch1", 21),
          ("spL2Ch2", 22),
          ("spL1L2Ch1", 31),
          ("spL1L2Ch2", 32),
          ("spL1L2Ch3", 33),
          ("spL1L2Ch4", 34),
          ("spL1L2Ch5", 35),
          ("spL3Ch1", 41),
          ("spL3Ch2", 42),
          ("spL3Ch3", 43),
          ("spL3Ch4", 44),
          ("spL4Ch1", 51),
          ("spL4Ch2", 52),
          ("spL3L4Ch1", 61),
          ("spL3L4Ch2", 62),
          ("spL3L4Ch3", 63),
          ("spL3L4Ch4", 64),
          ("spL3L4Ch5", 65),
          ("spL5Ch1", 71),
          ("spL5Ch2", 72),
          ("spL6Ch1", 81),
          ("spL6Ch2", 82))
    )


_TnOtuServerPort_Type.__name__ = "Integer32"
_TnOtuServerPort_Object = MibTableColumn
tnOtuServerPort = _TnOtuServerPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 26),
    _TnOtuServerPort_Type()
)
tnOtuServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtuServerPort.setStatus("current")


class _TnOtukMgracd_Type(Integer32):
    """Custom type tnOtukMgracd based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("cp", 2),
          ("mgnpln", 3),
          ("cpmgnpln", 4))
    )


_TnOtukMgracd_Type.__name__ = "Integer32"
_TnOtukMgracd_Object = MibTableColumn
tnOtukMgracd = _TnOtukMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 27),
    _TnOtukMgracd_Type()
)
tnOtukMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukMgracd.setStatus("current")


class _TnOtukType_Type(Integer32):
    """Custom type tnOtukType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("proprietary", 2))
    )


_TnOtukType_Type.__name__ = "Integer32"
_TnOtukType_Object = MibTableColumn
tnOtukType = _TnOtukType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 28),
    _TnOtukType_Type()
)
tnOtukType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtukType.setStatus("current")


class _TnOtuOtsigId_Type(Integer32):
    """Custom type tnOtuOtsigId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnOtuOtsigId_Type.__name__ = "Integer32"
_TnOtuOtsigId_Object = MibTableColumn
tnOtuOtsigId = _TnOtuOtsigId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 29),
    _TnOtuOtsigId_Type()
)
tnOtuOtsigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtuOtsigId.setStatus("current")


class _TnOtuChanPoolIfIndex_Type(OctetString):
    """Custom type tnOtuChanPoolIfIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TnOtuChanPoolIfIndex_Type.__name__ = "OctetString"
_TnOtuChanPoolIfIndex_Object = MibTableColumn
tnOtuChanPoolIfIndex = _TnOtuChanPoolIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 30),
    _TnOtuChanPoolIfIndex_Type()
)
tnOtuChanPoolIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtuChanPoolIfIndex.setStatus("current")


class _TnOtuFacilityDescriptorName_Type(SnmpAdminString):
    """Custom type tnOtuFacilityDescriptorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnOtuFacilityDescriptorName_Type.__name__ = "SnmpAdminString"
_TnOtuFacilityDescriptorName_Object = MibTableColumn
tnOtuFacilityDescriptorName = _TnOtuFacilityDescriptorName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 31),
    _TnOtuFacilityDescriptorName_Type()
)
tnOtuFacilityDescriptorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtuFacilityDescriptorName.setStatus("current")


class _TnOtuFacilityDescriptorDesc_Type(SnmpAdminString):
    """Custom type tnOtuFacilityDescriptorDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnOtuFacilityDescriptorDesc_Type.__name__ = "SnmpAdminString"
_TnOtuFacilityDescriptorDesc_Object = MibTableColumn
tnOtuFacilityDescriptorDesc = _TnOtuFacilityDescriptorDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 32),
    _TnOtuFacilityDescriptorDesc_Type()
)
tnOtuFacilityDescriptorDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtuFacilityDescriptorDesc.setStatus("current")


class _TnOtuFacilityDescriptorCirId_Type(SnmpAdminString):
    """Custom type tnOtuFacilityDescriptorCirId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnOtuFacilityDescriptorCirId_Type.__name__ = "SnmpAdminString"
_TnOtuFacilityDescriptorCirId_Object = MibTableColumn
tnOtuFacilityDescriptorCirId = _TnOtuFacilityDescriptorCirId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 33),
    _TnOtuFacilityDescriptorCirId_Type()
)
tnOtuFacilityDescriptorCirId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtuFacilityDescriptorCirId.setStatus("current")


class _TnOtuFacilityDescriptorConnPtId_Type(SnmpAdminString):
    """Custom type tnOtuFacilityDescriptorConnPtId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnOtuFacilityDescriptorConnPtId_Type.__name__ = "SnmpAdminString"
_TnOtuFacilityDescriptorConnPtId_Object = MibTableColumn
tnOtuFacilityDescriptorConnPtId = _TnOtuFacilityDescriptorConnPtId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 34),
    _TnOtuFacilityDescriptorConnPtId_Type()
)
tnOtuFacilityDescriptorConnPtId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtuFacilityDescriptorConnPtId.setStatus("current")


class _TnOtuFacilityDescCustLifeCycleState_Type(SnmpAdminString):
    """Custom type tnOtuFacilityDescCustLifeCycleState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnOtuFacilityDescCustLifeCycleState_Type.__name__ = "SnmpAdminString"
_TnOtuFacilityDescCustLifeCycleState_Object = MibTableColumn
tnOtuFacilityDescCustLifeCycleState = _TnOtuFacilityDescCustLifeCycleState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 35),
    _TnOtuFacilityDescCustLifeCycleState_Type()
)
tnOtuFacilityDescCustLifeCycleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtuFacilityDescCustLifeCycleState.setStatus("current")


class _TnOtuFacilityDescAdminState_Type(Integer32):
    """Custom type tnOtuFacilityDescAdminState based on Integer32"""
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
        *(("down", 1),
          ("mt", 2),
          ("unassigned", 3),
          ("up", 4),
          ("invalid", 5))
    )


_TnOtuFacilityDescAdminState_Type.__name__ = "Integer32"
_TnOtuFacilityDescAdminState_Object = MibTableColumn
tnOtuFacilityDescAdminState = _TnOtuFacilityDescAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 1, 1, 36),
    _TnOtuFacilityDescAdminState_Type()
)
tnOtuFacilityDescAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtuFacilityDescAdminState.setStatus("current")
_TnOtuApaTable_Object = MibTable
tnOtuApaTable = _TnOtuApaTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 11)
)
if mibBuilder.loadTexts:
    tnOtuApaTable.setStatus("current")
_TnOtuApaEntry_Object = MibTableRow
tnOtuApaEntry = _TnOtuApaEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 11, 1)
)
tnOtuApaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-OTUODU-MIB", "tnOtuApaInterval"),
)
if mibBuilder.loadTexts:
    tnOtuApaEntry.setStatus("current")


class _TnOtuApaInterval_Type(Integer32):
    """Custom type tnOtuApaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TnOtuApaInterval_Type.__name__ = "Integer32"
_TnOtuApaInterval_Object = MibTableColumn
tnOtuApaInterval = _TnOtuApaInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 11, 1, 1),
    _TnOtuApaInterval_Type()
)
tnOtuApaInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOtuApaInterval.setStatus("current")
_TnOtuApaPreFecBer_Type = Counter64
_TnOtuApaPreFecBer_Object = MibTableColumn
tnOtuApaPreFecBer = _TnOtuApaPreFecBer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 11, 1, 2),
    _TnOtuApaPreFecBer_Type()
)
tnOtuApaPreFecBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtuApaPreFecBer.setStatus("current")
_TnOtuApaFecUncorrCnt_Type = Counter64
_TnOtuApaFecUncorrCnt_Object = MibTableColumn
tnOtuApaFecUncorrCnt = _TnOtuApaFecUncorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 11, 1, 3),
    _TnOtuApaFecUncorrCnt_Type()
)
tnOtuApaFecUncorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtuApaFecUncorrCnt.setStatus("current")
_TnOtsigTable_Object = MibTable
tnOtsigTable = _TnOtsigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12)
)
if mibBuilder.loadTexts:
    tnOtsigTable.setStatus("current")
_TnOtsigEntry_Object = MibTableRow
tnOtsigEntry = _TnOtsigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1)
)
tnOtsigEntry.setIndexNames(
    (0, "TROPIC-OTUODU-MIB", "tnOtsigIndex"),
)
if mibBuilder.loadTexts:
    tnOtsigEntry.setStatus("current")
_TnOtsigIndex_Type = Integer32
_TnOtsigIndex_Object = MibTableColumn
tnOtsigIndex = _TnOtsigIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 1),
    _TnOtsigIndex_Type()
)
tnOtsigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOtsigIndex.setStatus("current")


class _TnOtsigCommand_Type(Integer32):
    """Custom type tnOtsigCommand based on Integer32"""
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
        *(("noCmd", 1),
          ("create", 2),
          ("delete", 3),
          ("update", 4))
    )


_TnOtsigCommand_Type.__name__ = "Integer32"
_TnOtsigCommand_Object = MibTableColumn
tnOtsigCommand = _TnOtsigCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 2),
    _TnOtsigCommand_Type()
)
tnOtsigCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigCommand.setStatus("current")


class _TnOtsigOtuStruct_Type(SnmpAdminString):
    """Custom type tnOtsigOtuStruct based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 192),
    )


_TnOtsigOtuStruct_Type.__name__ = "SnmpAdminString"
_TnOtsigOtuStruct_Object = MibTableColumn
tnOtsigOtuStruct = _TnOtsigOtuStruct_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 3),
    _TnOtsigOtuStruct_Type()
)
tnOtsigOtuStruct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigOtuStruct.setStatus("current")


class _TnOtsigTransmissionMode_Type(Integer32):
    """Custom type tnOtsigTransmissionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("addDrop", 1),
          ("dropOnly", 2),
          ("addOnly", 3),
          ("thru", 4),
          ("dropContinue", 5),
          ("crossRegen", 6),
          ("regenGcc0LoopThrough", 7))
    )


_TnOtsigTransmissionMode_Type.__name__ = "Integer32"
_TnOtsigTransmissionMode_Object = MibTableColumn
tnOtsigTransmissionMode = _TnOtsigTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 4),
    _TnOtsigTransmissionMode_Type()
)
tnOtsigTransmissionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigTransmissionMode.setStatus("current")


class _TnOtsigRegenResponse_Type(Integer32):
    """Custom type tnOtsigRegenResponse based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("laserOn", 1),
          ("laserOff", 2))
    )


_TnOtsigRegenResponse_Type.__name__ = "Integer32"
_TnOtsigRegenResponse_Object = MibTableColumn
tnOtsigRegenResponse = _TnOtsigRegenResponse_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 5),
    _TnOtsigRegenResponse_Type()
)
tnOtsigRegenResponse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigRegenResponse.setStatus("current")


class _TnOtsigOTSilist_Type(SnmpAdminString):
    """Custom type tnOtsigOTSilist based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnOtsigOTSilist_Type.__name__ = "SnmpAdminString"
_TnOtsigOTSilist_Object = MibTableColumn
tnOtsigOTSilist = _TnOtsigOTSilist_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 6),
    _TnOtsigOTSilist_Type()
)
tnOtsigOTSilist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigOTSilist.setStatus("current")


class _TnOtsigLLEB_Type(TruthValue):
    """Custom type tnOtsigLLEB based on TruthValue"""
    defaultValue = 2


_TnOtsigLLEB_Type.__name__ = "TruthValue"
_TnOtsigLLEB_Object = MibTableColumn
tnOtsigLLEB = _TnOtsigLLEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 7),
    _TnOtsigLLEB_Type()
)
tnOtsigLLEB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigLLEB.setStatus("current")


class _TnOtsigDLEB_Type(TruthValue):
    """Custom type tnOtsigDLEB based on TruthValue"""
    defaultValue = 2


_TnOtsigDLEB_Type.__name__ = "TruthValue"
_TnOtsigDLEB_Object = MibTableColumn
tnOtsigDLEB = _TnOtsigDLEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 8),
    _TnOtsigDLEB_Type()
)
tnOtsigDLEB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigDLEB.setStatus("current")


class _TnOtsigTSEB_Type(TruthValue):
    """Custom type tnOtsigTSEB based on TruthValue"""
    defaultValue = 2


_TnOtsigTSEB_Type.__name__ = "TruthValue"
_TnOtsigTSEB_Object = MibTableColumn
tnOtsigTSEB = _TnOtsigTSEB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 9),
    _TnOtsigTSEB_Type()
)
tnOtsigTSEB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigTSEB.setStatus("current")
_TnOtsigBaudrate_Type = Integer32
_TnOtsigBaudrate_Object = MibTableColumn
tnOtsigBaudrate = _TnOtsigBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 10),
    _TnOtsigBaudrate_Type()
)
tnOtsigBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigBaudrate.setStatus("current")


class _TnOtsigEncoding_Type(Integer32):
    """Custom type tnOtsigEncoding based on Integer32"""
    defaultValue = 9996

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
              9996,
              9997,
              9998,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 0),
          ("pdpsk", 1),
          ("dpsk", 2),
          ("bpsk", 3),
          ("qpsk", 4),
          ("qpskEnhOsnr", 5),
          ("nrzCFP1", 6),
          ("icohpmqpsk", 7),
          ("duobinary", 8),
          ("qpskhperf2", 9),
          ("qam16", 10),
          ("qam8", 11),
          ("spqpsk", 12),
          ("qam64", 13),
          ("cohpm16qam250G", 14),
          ("cohpmsqam16", 15),
          ("cohpmsqam64", 16),
          ("qam32", 17),
          ("optimization", 9996),
          ("unassigned", 9997),
          ("alien", 9998),
          ("unknown", 9999))
    )


_TnOtsigEncoding_Type.__name__ = "Integer32"
_TnOtsigEncoding_Object = MibTableColumn
tnOtsigEncoding = _TnOtsigEncoding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 11),
    _TnOtsigEncoding_Type()
)
tnOtsigEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigEncoding.setStatus("current")


class _TnOtsigPhaseEncode_Type(Integer32):
    """Custom type tnOtsigPhaseEncode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("differential", 2))
    )


_TnOtsigPhaseEncode_Type.__name__ = "Integer32"
_TnOtsigPhaseEncode_Object = MibTableColumn
tnOtsigPhaseEncode = _TnOtsigPhaseEncode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 12),
    _TnOtsigPhaseEncode_Type()
)
tnOtsigPhaseEncode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigPhaseEncode.setStatus("current")


class _TnOtsigPolarizationTrack_Type(Integer32):
    """Custom type tnOtsigPolarizationTrack based on Integer32"""
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
        *(("normal", 1),
          ("fast", 2),
          ("devDefault", 3))
    )


_TnOtsigPolarizationTrack_Type.__name__ = "Integer32"
_TnOtsigPolarizationTrack_Object = MibTableColumn
tnOtsigPolarizationTrack = _TnOtsigPolarizationTrack_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 13),
    _TnOtsigPolarizationTrack_Type()
)
tnOtsigPolarizationTrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigPolarizationTrack.setStatus("current")


class _TnOtsigTxShape_Type(Integer32):
    """Custom type tnOtsigTxShape based on Integer32"""
    defaultValue = 1

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
        *(("single", 1),
          ("super", 2),
          ("alien", 3),
          ("superRRC01", 4),
          ("superChannel0-05", 5),
          ("superChannel0-07", 6),
          ("superChannel0-15", 7),
          ("superChannel0-25", 8),
          ("superChannel0-3", 9))
    )


_TnOtsigTxShape_Type.__name__ = "Integer32"
_TnOtsigTxShape_Object = MibTableColumn
tnOtsigTxShape = _TnOtsigTxShape_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 14),
    _TnOtsigTxShape_Type()
)
tnOtsigTxShape.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigTxShape.setStatus("current")


class _TnOtsigFecMode_Type(Integer32):
    """Custom type tnOtsigFecMode based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("noFec", 1),
          ("g709Fec", 2),
          ("enhancedFec", 3),
          ("uFec", 4),
          ("enhancedFec2", 5),
          ("aFec", 6),
          ("eSDFec", 10),
          ("hpFec", 11),
          ("usdFec", 12),
          ("bjFec", 13),
          ("scFec", 14),
          ("sdFecAcc", 15),
          ("eSDFecG2", 16),
          ("eSDFecExt", 17),
          ("ePuncturedSDFecG2", 18),
          ("sdFecCE", 19),
          ("sdFecV", 20),
          ("eOFec", 21),
          ("eSDFec6", 22))
    )


_TnOtsigFecMode_Type.__name__ = "Integer32"
_TnOtsigFecMode_Object = MibTableColumn
tnOtsigFecMode = _TnOtsigFecMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 15),
    _TnOtsigFecMode_Type()
)
tnOtsigFecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigFecMode.setStatus("current")


class _TnOtsigNonLinearComp_Type(TruthValue):
    """Custom type tnOtsigNonLinearComp based on TruthValue"""
    defaultValue = 2


_TnOtsigNonLinearComp_Type.__name__ = "TruthValue"
_TnOtsigNonLinearComp_Object = MibTableColumn
tnOtsigNonLinearComp = _TnOtsigNonLinearComp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 16),
    _TnOtsigNonLinearComp_Type()
)
tnOtsigNonLinearComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigNonLinearComp.setStatus("current")


class _TnOtsigCdPreComp_Type(Integer32):
    """Custom type tnOtsigCdPreComp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_TnOtsigCdPreComp_Type.__name__ = "Integer32"
_TnOtsigCdPreComp_Object = MibTableColumn
tnOtsigCdPreComp = _TnOtsigCdPreComp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 17),
    _TnOtsigCdPreComp_Type()
)
tnOtsigCdPreComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigCdPreComp.setStatus("current")


class _TnOtsigDescription_Type(SnmpAdminString):
    """Custom type tnOtsigDescription based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnOtsigDescription_Type.__name__ = "SnmpAdminString"
_TnOtsigDescription_Object = MibTableColumn
tnOtsigDescription = _TnOtsigDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 18),
    _TnOtsigDescription_Type()
)
tnOtsigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigDescription.setStatus("current")


class _TnOtsigPayloadRate_Type(Integer32):
    """Custom type tnOtsigPayloadRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TnOtsigPayloadRate_Type.__name__ = "Integer32"
_TnOtsigPayloadRate_Object = MibTableColumn
tnOtsigPayloadRate = _TnOtsigPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 19),
    _TnOtsigPayloadRate_Type()
)
tnOtsigPayloadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigPayloadRate.setStatus("current")


class _TnOtsigIOPMode_Type(Integer32):
    """Custom type tnOtsigIOPMode based on Integer32"""
    defaultValue = 9999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("flex", 1),
          ("legacy", 2),
          ("otucn", 3),
          ("otutcn", 4),
          ("otu4", 5),
          ("flexO", 6),
          ("unknown", 9999))
    )


_TnOtsigIOPMode_Type.__name__ = "Integer32"
_TnOtsigIOPMode_Object = MibTableColumn
tnOtsigIOPMode = _TnOtsigIOPMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 20),
    _TnOtsigIOPMode_Type()
)
tnOtsigIOPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigIOPMode.setStatus("current")


class _TnOtsigCapacity_Type(Integer32):
    """Custom type tnOtsigCapacity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_TnOtsigCapacity_Type.__name__ = "Integer32"
_TnOtsigCapacity_Object = MibTableColumn
tnOtsigCapacity = _TnOtsigCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 21),
    _TnOtsigCapacity_Type()
)
tnOtsigCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigCapacity.setStatus("current")


class _TnOtsigProfileId_Type(Integer32):
    """Custom type tnOtsigProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3999),
    )


_TnOtsigProfileId_Type.__name__ = "Integer32"
_TnOtsigProfileId_Object = MibTableColumn
tnOtsigProfileId = _TnOtsigProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 22),
    _TnOtsigProfileId_Type()
)
tnOtsigProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigProfileId.setStatus("current")


class _TnOtsigMgracd_Type(Integer32):
    """Custom type tnOtsigMgracd based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("cp", 2),
          ("mgnpln", 3),
          ("cpmgnpln", 4))
    )


_TnOtsigMgracd_Type.__name__ = "Integer32"
_TnOtsigMgracd_Object = MibTableColumn
tnOtsigMgracd = _TnOtsigMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 23),
    _TnOtsigMgracd_Type()
)
tnOtsigMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigMgracd.setStatus("current")


class _TnOtsigFacilityDescriptorName_Type(SnmpAdminString):
    """Custom type tnOtsigFacilityDescriptorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnOtsigFacilityDescriptorName_Type.__name__ = "SnmpAdminString"
_TnOtsigFacilityDescriptorName_Object = MibTableColumn
tnOtsigFacilityDescriptorName = _TnOtsigFacilityDescriptorName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 24),
    _TnOtsigFacilityDescriptorName_Type()
)
tnOtsigFacilityDescriptorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigFacilityDescriptorName.setStatus("current")


class _TnOtsigFacilityDescriptorDesc_Type(SnmpAdminString):
    """Custom type tnOtsigFacilityDescriptorDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnOtsigFacilityDescriptorDesc_Type.__name__ = "SnmpAdminString"
_TnOtsigFacilityDescriptorDesc_Object = MibTableColumn
tnOtsigFacilityDescriptorDesc = _TnOtsigFacilityDescriptorDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 25),
    _TnOtsigFacilityDescriptorDesc_Type()
)
tnOtsigFacilityDescriptorDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigFacilityDescriptorDesc.setStatus("current")


class _TnOtsigFacilityDescriptorCirId_Type(SnmpAdminString):
    """Custom type tnOtsigFacilityDescriptorCirId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnOtsigFacilityDescriptorCirId_Type.__name__ = "SnmpAdminString"
_TnOtsigFacilityDescriptorCirId_Object = MibTableColumn
tnOtsigFacilityDescriptorCirId = _TnOtsigFacilityDescriptorCirId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 26),
    _TnOtsigFacilityDescriptorCirId_Type()
)
tnOtsigFacilityDescriptorCirId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigFacilityDescriptorCirId.setStatus("current")


class _TnOtsigFacilityDescriptorConnPtId_Type(SnmpAdminString):
    """Custom type tnOtsigFacilityDescriptorConnPtId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnOtsigFacilityDescriptorConnPtId_Type.__name__ = "SnmpAdminString"
_TnOtsigFacilityDescriptorConnPtId_Object = MibTableColumn
tnOtsigFacilityDescriptorConnPtId = _TnOtsigFacilityDescriptorConnPtId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 27),
    _TnOtsigFacilityDescriptorConnPtId_Type()
)
tnOtsigFacilityDescriptorConnPtId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigFacilityDescriptorConnPtId.setStatus("current")


class _TnOtsigFacilityDescCustLifeCycleState_Type(SnmpAdminString):
    """Custom type tnOtsigFacilityDescCustLifeCycleState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnOtsigFacilityDescCustLifeCycleState_Type.__name__ = "SnmpAdminString"
_TnOtsigFacilityDescCustLifeCycleState_Object = MibTableColumn
tnOtsigFacilityDescCustLifeCycleState = _TnOtsigFacilityDescCustLifeCycleState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 28),
    _TnOtsigFacilityDescCustLifeCycleState_Type()
)
tnOtsigFacilityDescCustLifeCycleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigFacilityDescCustLifeCycleState.setStatus("current")


class _TnOtsigFacilityDescAdminState_Type(Integer32):
    """Custom type tnOtsigFacilityDescAdminState based on Integer32"""
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
        *(("down", 1),
          ("mt", 2),
          ("unassigned", 3),
          ("up", 4),
          ("invalid", 5))
    )


_TnOtsigFacilityDescAdminState_Type.__name__ = "Integer32"
_TnOtsigFacilityDescAdminState_Object = MibTableColumn
tnOtsigFacilityDescAdminState = _TnOtsigFacilityDescAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 29),
    _TnOtsigFacilityDescAdminState_Type()
)
tnOtsigFacilityDescAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigFacilityDescAdminState.setStatus("current")


class _TnOtsigGroupIdentification_Type(Integer32):
    """Custom type tnOtsigGroupIdentification based on Integer32"""
    defaultValue = 1


_TnOtsigGroupIdentification_Type.__name__ = "Integer32"
_TnOtsigGroupIdentification_Object = MibTableColumn
tnOtsigGroupIdentification = _TnOtsigGroupIdentification_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 30),
    _TnOtsigGroupIdentification_Type()
)
tnOtsigGroupIdentification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigGroupIdentification.setStatus("current")


class _TnOtsigInterfaceIdentification_Type(SnmpAdminString):
    """Custom type tnOtsigInterfaceIdentification based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_TnOtsigInterfaceIdentification_Type.__name__ = "SnmpAdminString"
_TnOtsigInterfaceIdentification_Object = MibTableColumn
tnOtsigInterfaceIdentification = _TnOtsigInterfaceIdentification_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 31),
    _TnOtsigInterfaceIdentification_Type()
)
tnOtsigInterfaceIdentification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigInterfaceIdentification.setStatus("current")


class _TnOtsigAdminState_Type(TropicAdminStateType):
    """Custom type tnOtsigAdminState based on TropicAdminStateType"""
    defaultValue = 1


_TnOtsigAdminState_Type.__name__ = "TropicAdminStateType"
_TnOtsigAdminState_Object = MibTableColumn
tnOtsigAdminState = _TnOtsigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 32),
    _TnOtsigAdminState_Type()
)
tnOtsigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigAdminState.setStatus("current")


class _TnOtsigStateAINS_Type(TruthValue):
    """Custom type tnOtsigStateAINS based on TruthValue"""
    defaultValue = 2


_TnOtsigStateAINS_Type.__name__ = "TruthValue"
_TnOtsigStateAINS_Object = MibTableColumn
tnOtsigStateAINS = _TnOtsigStateAINS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 33),
    _TnOtsigStateAINS_Type()
)
tnOtsigStateAINS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigStateAINS.setStatus("current")
_TnOtsigStateAINSTimerStart_Type = Unsigned32
_TnOtsigStateAINSTimerStart_Object = MibTableColumn
tnOtsigStateAINSTimerStart = _TnOtsigStateAINSTimerStart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 34),
    _TnOtsigStateAINSTimerStart_Type()
)
tnOtsigStateAINSTimerStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigStateAINSTimerStart.setStatus("current")
_TnOtsigStateAINSDebounce_Type = Integer32
_TnOtsigStateAINSDebounce_Object = MibTableColumn
tnOtsigStateAINSDebounce = _TnOtsigStateAINSDebounce_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 35),
    _TnOtsigStateAINSDebounce_Type()
)
tnOtsigStateAINSDebounce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigStateAINSDebounce.setStatus("current")


class _TnOtsigStateQualifier_Type(TropicStateQualifierType):
    """Custom type tnOtsigStateQualifier based on TropicStateQualifierType"""
    defaultBinValue = "0000001"


_TnOtsigStateQualifier_Type.__name__ = "TropicStateQualifierType"
_TnOtsigStateQualifier_Object = MibTableColumn
tnOtsigStateQualifier = _TnOtsigStateQualifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 36),
    _TnOtsigStateQualifier_Type()
)
tnOtsigStateQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigStateQualifier.setStatus("current")


class _TnOtsigOperationalCapability_Type(TropicOperationalCapabilityType):
    """Custom type tnOtsigOperationalCapability based on TropicOperationalCapabilityType"""
    defaultValue = 1


_TnOtsigOperationalCapability_Type.__name__ = "TropicOperationalCapabilityType"
_TnOtsigOperationalCapability_Object = MibTableColumn
tnOtsigOperationalCapability = _TnOtsigOperationalCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 37),
    _TnOtsigOperationalCapability_Type()
)
tnOtsigOperationalCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigOperationalCapability.setStatus("current")


class _TnOtsigOperationalState_Type(TropicOperationalStateType):
    """Custom type tnOtsigOperationalState based on TropicOperationalStateType"""
    defaultValue = 2


_TnOtsigOperationalState_Type.__name__ = "TropicOperationalStateType"
_TnOtsigOperationalState_Object = MibTableColumn
tnOtsigOperationalState = _TnOtsigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 38),
    _TnOtsigOperationalState_Type()
)
tnOtsigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigOperationalState.setStatus("current")
_TnOtsigUsingSysAINSDebounceTime_Type = TruthValue
_TnOtsigUsingSysAINSDebounceTime_Object = MibTableColumn
tnOtsigUsingSysAINSDebounceTime = _TnOtsigUsingSysAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 39),
    _TnOtsigUsingSysAINSDebounceTime_Type()
)
tnOtsigUsingSysAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigUsingSysAINSDebounceTime.setStatus("current")
_TnOtsigIncFlexOFrameGid_Type = OctetString
_TnOtsigIncFlexOFrameGid_Object = MibTableColumn
tnOtsigIncFlexOFrameGid = _TnOtsigIncFlexOFrameGid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 40),
    _TnOtsigIncFlexOFrameGid_Type()
)
tnOtsigIncFlexOFrameGid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigIncFlexOFrameGid.setStatus("current")
_TnOtsigIncFlexOFrameIID_Type = OctetString
_TnOtsigIncFlexOFrameIID_Object = MibTableColumn
tnOtsigIncFlexOFrameIID = _TnOtsigIncFlexOFrameIID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 41),
    _TnOtsigIncFlexOFrameIID_Type()
)
tnOtsigIncFlexOFrameIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigIncFlexOFrameIID.setStatus("current")


class _TnOtsigIncFlexOFrameIIDMap1_Type(SnmpAdminString):
    """Custom type tnOtsigIncFlexOFrameIIDMap1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnOtsigIncFlexOFrameIIDMap1_Type.__name__ = "SnmpAdminString"
_TnOtsigIncFlexOFrameIIDMap1_Object = MibTableColumn
tnOtsigIncFlexOFrameIIDMap1 = _TnOtsigIncFlexOFrameIIDMap1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 42),
    _TnOtsigIncFlexOFrameIIDMap1_Type()
)
tnOtsigIncFlexOFrameIIDMap1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigIncFlexOFrameIIDMap1.setStatus("current")


class _TnOtsigIncFlexOFrameIIDMap2_Type(SnmpAdminString):
    """Custom type tnOtsigIncFlexOFrameIIDMap2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnOtsigIncFlexOFrameIIDMap2_Type.__name__ = "SnmpAdminString"
_TnOtsigIncFlexOFrameIIDMap2_Object = MibTableColumn
tnOtsigIncFlexOFrameIIDMap2 = _TnOtsigIncFlexOFrameIIDMap2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 43),
    _TnOtsigIncFlexOFrameIIDMap2_Type()
)
tnOtsigIncFlexOFrameIIDMap2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigIncFlexOFrameIIDMap2.setStatus("current")


class _TnOtsigIncFlexOFrameIIDMap3_Type(SnmpAdminString):
    """Custom type tnOtsigIncFlexOFrameIIDMap3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnOtsigIncFlexOFrameIIDMap3_Type.__name__ = "SnmpAdminString"
_TnOtsigIncFlexOFrameIIDMap3_Object = MibTableColumn
tnOtsigIncFlexOFrameIIDMap3 = _TnOtsigIncFlexOFrameIIDMap3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 44),
    _TnOtsigIncFlexOFrameIIDMap3_Type()
)
tnOtsigIncFlexOFrameIIDMap3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigIncFlexOFrameIIDMap3.setStatus("current")


class _TnOtsigIncFlexOFrameIIDMap4_Type(SnmpAdminString):
    """Custom type tnOtsigIncFlexOFrameIIDMap4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnOtsigIncFlexOFrameIIDMap4_Type.__name__ = "SnmpAdminString"
_TnOtsigIncFlexOFrameIIDMap4_Object = MibTableColumn
tnOtsigIncFlexOFrameIIDMap4 = _TnOtsigIncFlexOFrameIIDMap4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 45),
    _TnOtsigIncFlexOFrameIIDMap4_Type()
)
tnOtsigIncFlexOFrameIIDMap4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigIncFlexOFrameIIDMap4.setStatus("current")
_TnOtsigAlmProfName_Type = OctetString
_TnOtsigAlmProfName_Object = MibTableColumn
tnOtsigAlmProfName = _TnOtsigAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 46),
    _TnOtsigAlmProfName_Type()
)
tnOtsigAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigAlmProfName.setStatus("current")
_TnOtsigReferenceProfileId_Type = Integer32
_TnOtsigReferenceProfileId_Object = MibTableColumn
tnOtsigReferenceProfileId = _TnOtsigReferenceProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 12, 1, 47),
    _TnOtsigReferenceProfileId_Type()
)
tnOtsigReferenceProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigReferenceProfileId.setStatus("current")
_TnOtsigProfileTable_Object = MibTable
tnOtsigProfileTable = _TnOtsigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 13)
)
if mibBuilder.loadTexts:
    tnOtsigProfileTable.setStatus("current")
_TnOtsigProfileEntry_Object = MibTableRow
tnOtsigProfileEntry = _TnOtsigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 13, 1)
)
tnOtsigProfileEntry.setIndexNames(
    (0, "TROPIC-OTUODU-MIB", "tnOtsigProfileId"),
)
if mibBuilder.loadTexts:
    tnOtsigProfileEntry.setStatus("current")


class _TnOtsigProfile_Type(SnmpAdminString):
    """Custom type tnOtsigProfile based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_TnOtsigProfile_Type.__name__ = "SnmpAdminString"
_TnOtsigProfile_Object = MibTableColumn
tnOtsigProfile = _TnOtsigProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 13, 1, 1),
    _TnOtsigProfile_Type()
)
tnOtsigProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigProfile.setStatus("current")


class _TnOtsigProfileCardType_Type(SnmpAdminString):
    """Custom type tnOtsigProfileCardType based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnOtsigProfileCardType_Type.__name__ = "SnmpAdminString"
_TnOtsigProfileCardType_Object = MibTableColumn
tnOtsigProfileCardType = _TnOtsigProfileCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 13, 1, 2),
    _TnOtsigProfileCardType_Type()
)
tnOtsigProfileCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigProfileCardType.setStatus("current")
_TnOtsigProfileExternalCategory_Type = TruthValue
_TnOtsigProfileExternalCategory_Object = MibTableColumn
tnOtsigProfileExternalCategory = _TnOtsigProfileExternalCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 13, 1, 3),
    _TnOtsigProfileExternalCategory_Type()
)
tnOtsigProfileExternalCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigProfileExternalCategory.setStatus("current")


class _TnOtsigProfileExternalCardType_Type(SnmpAdminString):
    """Custom type tnOtsigProfileExternalCardType based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnOtsigProfileExternalCardType_Type.__name__ = "SnmpAdminString"
_TnOtsigProfileExternalCardType_Object = MibTableColumn
tnOtsigProfileExternalCardType = _TnOtsigProfileExternalCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 13, 1, 4),
    _TnOtsigProfileExternalCardType_Type()
)
tnOtsigProfileExternalCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigProfileExternalCardType.setStatus("current")
_TnOtsigCustomProfileTable_Object = MibTable
tnOtsigCustomProfileTable = _TnOtsigCustomProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14)
)
if mibBuilder.loadTexts:
    tnOtsigCustomProfileTable.setStatus("current")
_TnOtsigCustomProfileEntry_Object = MibTableRow
tnOtsigCustomProfileEntry = _TnOtsigCustomProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1)
)
tnOtsigCustomProfileEntry.setIndexNames(
    (0, "TROPIC-OTUODU-MIB", "tnOtsigCustomProfile"),
)
if mibBuilder.loadTexts:
    tnOtsigCustomProfileEntry.setStatus("current")


class _TnOtsigCustomProfile_Type(Integer32):
    """Custom type tnOtsigCustomProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3999),
    )


_TnOtsigCustomProfile_Type.__name__ = "Integer32"
_TnOtsigCustomProfile_Object = MibTableColumn
tnOtsigCustomProfile = _TnOtsigCustomProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 1),
    _TnOtsigCustomProfile_Type()
)
tnOtsigCustomProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOtsigCustomProfile.setStatus("current")
_TnOtsigRefSysProfileId_Type = Integer32
_TnOtsigRefSysProfileId_Object = MibTableColumn
tnOtsigRefSysProfileId = _TnOtsigRefSysProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 2),
    _TnOtsigRefSysProfileId_Type()
)
tnOtsigRefSysProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigRefSysProfileId.setStatus("current")
_TnOtsigCustomProfileRowStatus_Type = RowStatus
_TnOtsigCustomProfileRowStatus_Object = MibTableColumn
tnOtsigCustomProfileRowStatus = _TnOtsigCustomProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 3),
    _TnOtsigCustomProfileRowStatus_Type()
)
tnOtsigCustomProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigCustomProfileRowStatus.setStatus("current")
_TnOtsigCustomProfileBaudRate_Type = Integer32
_TnOtsigCustomProfileBaudRate_Object = MibTableColumn
tnOtsigCustomProfileBaudRate = _TnOtsigCustomProfileBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 4),
    _TnOtsigCustomProfileBaudRate_Type()
)
tnOtsigCustomProfileBaudRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigCustomProfileBaudRate.setStatus("current")


class _TnOtsigCustomProfileIOPMode_Type(Integer32):
    """Custom type tnOtsigCustomProfileIOPMode based on Integer32"""
    defaultValue = 9999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("flex", 1),
          ("legacy", 2),
          ("otucn", 3),
          ("otutcn", 4),
          ("otu4", 5),
          ("flexO", 6),
          ("unknown", 9999))
    )


_TnOtsigCustomProfileIOPMode_Type.__name__ = "Integer32"
_TnOtsigCustomProfileIOPMode_Object = MibTableColumn
tnOtsigCustomProfileIOPMode = _TnOtsigCustomProfileIOPMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 5),
    _TnOtsigCustomProfileIOPMode_Type()
)
tnOtsigCustomProfileIOPMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigCustomProfileIOPMode.setStatus("current")


class _TnOtsigCustomProfileEncoding_Type(Integer32):
    """Custom type tnOtsigCustomProfileEncoding based on Integer32"""
    defaultValue = 9996

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
              9996,
              9997,
              9998,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 0),
          ("pdpsk", 1),
          ("dpsk", 2),
          ("bpsk", 3),
          ("qpsk", 4),
          ("qpskEnhOsnr", 5),
          ("nrzCFP1", 6),
          ("icohpmqpsk", 7),
          ("duobinary", 8),
          ("qpskhperf2", 9),
          ("qam16", 10),
          ("qam8", 11),
          ("spqpsk", 12),
          ("qam64", 13),
          ("cohpm16qam250G", 14),
          ("cohpmsqam16", 15),
          ("cohpmsqam64", 16),
          ("qam32", 17),
          ("optimization", 9996),
          ("unassigned", 9997),
          ("alien", 9998),
          ("unknown", 9999))
    )


_TnOtsigCustomProfileEncoding_Type.__name__ = "Integer32"
_TnOtsigCustomProfileEncoding_Object = MibTableColumn
tnOtsigCustomProfileEncoding = _TnOtsigCustomProfileEncoding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 6),
    _TnOtsigCustomProfileEncoding_Type()
)
tnOtsigCustomProfileEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigCustomProfileEncoding.setStatus("current")


class _TnOtsigCustomProfileFecMode_Type(Integer32):
    """Custom type tnOtsigCustomProfileFecMode based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
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
        *(("noFec", 1),
          ("g709Fec", 2),
          ("enhancedFec", 3),
          ("uFec", 4),
          ("enhancedFec2", 5),
          ("aFec", 6),
          ("eSDFec", 10),
          ("hpFec", 11),
          ("usdFec", 12),
          ("bjFec", 13),
          ("scFec", 14),
          ("sdFecAcc", 15),
          ("eSDFecG2", 16),
          ("eSDFecExt", 17),
          ("ePuncturedSDFecG2", 18),
          ("sdFecCE", 19),
          ("sdFecV", 20),
          ("eOFec", 21))
    )


_TnOtsigCustomProfileFecMode_Type.__name__ = "Integer32"
_TnOtsigCustomProfileFecMode_Object = MibTableColumn
tnOtsigCustomProfileFecMode = _TnOtsigCustomProfileFecMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 7),
    _TnOtsigCustomProfileFecMode_Type()
)
tnOtsigCustomProfileFecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigCustomProfileFecMode.setStatus("current")


class _TnOtsigCustomProfilePhaseEnc_Type(Integer32):
    """Custom type tnOtsigCustomProfilePhaseEnc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("differential", 2))
    )


_TnOtsigCustomProfilePhaseEnc_Type.__name__ = "Integer32"
_TnOtsigCustomProfilePhaseEnc_Object = MibTableColumn
tnOtsigCustomProfilePhaseEnc = _TnOtsigCustomProfilePhaseEnc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 8),
    _TnOtsigCustomProfilePhaseEnc_Type()
)
tnOtsigCustomProfilePhaseEnc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigCustomProfilePhaseEnc.setStatus("current")


class _TnOtsigCustomDescription_Type(SnmpAdminString):
    """Custom type tnOtsigCustomDescription based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnOtsigCustomDescription_Type.__name__ = "SnmpAdminString"
_TnOtsigCustomDescription_Object = MibTableColumn
tnOtsigCustomDescription = _TnOtsigCustomDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 9),
    _TnOtsigCustomDescription_Type()
)
tnOtsigCustomDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigCustomDescription.setStatus("current")


class _TnOtsigCustomPayloadRate_Type(Integer32):
    """Custom type tnOtsigCustomPayloadRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TnOtsigCustomPayloadRate_Type.__name__ = "Integer32"
_TnOtsigCustomPayloadRate_Object = MibTableColumn
tnOtsigCustomPayloadRate = _TnOtsigCustomPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 10),
    _TnOtsigCustomPayloadRate_Type()
)
tnOtsigCustomPayloadRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigCustomPayloadRate.setStatus("current")


class _TnOtsigCustomTxShape_Type(Integer32):
    """Custom type tnOtsigCustomTxShape based on Integer32"""
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
        *(("single", 1),
          ("super", 2),
          ("alien", 3),
          ("superRRC01", 4),
          ("superChannel0-05", 5),
          ("superChannel0-07", 6),
          ("superChannel0-15", 7),
          ("superChannel0-25", 8),
          ("superChannel0-3", 9))
    )


_TnOtsigCustomTxShape_Type.__name__ = "Integer32"
_TnOtsigCustomTxShape_Object = MibTableColumn
tnOtsigCustomTxShape = _TnOtsigCustomTxShape_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 11),
    _TnOtsigCustomTxShape_Type()
)
tnOtsigCustomTxShape.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOtsigCustomTxShape.setStatus("current")


class _TnOtsigCustomProfileCategory_Type(Integer32):
    """Custom type tnOtsigCustomProfileCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("user", 1),
          ("demo", 2))
    )


_TnOtsigCustomProfileCategory_Type.__name__ = "Integer32"
_TnOtsigCustomProfileCategory_Object = MibTableColumn
tnOtsigCustomProfileCategory = _TnOtsigCustomProfileCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 12),
    _TnOtsigCustomProfileCategory_Type()
)
tnOtsigCustomProfileCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigCustomProfileCategory.setStatus("current")


class _TnOtsigCustomProfileCardType_Type(SnmpAdminString):
    """Custom type tnOtsigCustomProfileCardType based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnOtsigCustomProfileCardType_Type.__name__ = "SnmpAdminString"
_TnOtsigCustomProfileCardType_Object = MibTableColumn
tnOtsigCustomProfileCardType = _TnOtsigCustomProfileCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 2, 1, 14, 1, 13),
    _TnOtsigCustomProfileCardType_Type()
)
tnOtsigCustomProfileCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOtsigCustomProfileCardType.setStatus("current")

# Managed Objects groups

tnOtukGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 1, 1)
)
tnOtukGroup.setObjects(
      *(("TROPIC-OTUODU-MIB", "tnOtukTtiStatus"),
        ("TROPIC-OTUODU-MIB", "tnOtukFecMode"),
        ("TROPIC-OTUODU-MIB", "tnOtukRate"),
        ("TROPIC-OTUODU-MIB", "tnOtukIncRes"),
        ("TROPIC-OTUODU-MIB", "tnOtukAdminStatus"),
        ("TROPIC-OTUODU-MIB", "tnOtukStateAINS"),
        ("TROPIC-OTUODU-MIB", "tnOtukOperStatus"),
        ("TROPIC-OTUODU-MIB", "tnOtukStateQualifier"),
        ("TROPIC-OTUODU-MIB", "tnOtukOperationalCapability"),
        ("TROPIC-OTUODU-MIB", "tnOtukAINSDebounceTime"),
        ("TROPIC-OTUODU-MIB", "tnOtukUsingSysAINSDebounceTime"),
        ("TROPIC-OTUODU-MIB", "tnOtukAINSDebounceTimeRemaining"),
        ("TROPIC-OTUODU-MIB", "tnOtukPreFec"),
        ("TROPIC-OTUODU-MIB", "tnOtukPostFec"),
        ("TROPIC-OTUODU-MIB", "tnOtukAsymInterworking"),
        ("TROPIC-OTUODU-MIB", "tnOtukDegThr"),
        ("TROPIC-OTUODU-MIB", "tnOtukDegM"),
        ("TROPIC-OTUODU-MIB", "tnOtukDapiAccepted"),
        ("TROPIC-OTUODU-MIB", "tnOtukDapiExpected"),
        ("TROPIC-OTUODU-MIB", "tnOtukDapiTransmitted"),
        ("TROPIC-OTUODU-MIB", "tnOtukOsAccepted"),
        ("TROPIC-OTUODU-MIB", "tnOtukOsTransmitted"),
        ("TROPIC-OTUODU-MIB", "tnOtuAlmProfName"),
        ("TROPIC-OTUODU-MIB", "tnOtuServerPort"),
        ("TROPIC-OTUODU-MIB", "tnOtukMgracd"),
        ("TROPIC-OTUODU-MIB", "tnOtukType"),
        ("TROPIC-OTUODU-MIB", "tnOtuOtsigId"),
        ("TROPIC-OTUODU-MIB", "tnOtuChanPoolIfIndex"),
        ("TROPIC-OTUODU-MIB", "tnOtuFacilityDescriptorName"),
        ("TROPIC-OTUODU-MIB", "tnOtuFacilityDescriptorDesc"),
        ("TROPIC-OTUODU-MIB", "tnOtuFacilityDescriptorCirId"),
        ("TROPIC-OTUODU-MIB", "tnOtuFacilityDescriptorConnPtId"),
        ("TROPIC-OTUODU-MIB", "tnOtuFacilityDescCustLifeCycleState"),
        ("TROPIC-OTUODU-MIB", "tnOtuFacilityDescAdminState"))
)
if mibBuilder.loadTexts:
    tnOtukGroup.setStatus("current")

tnOtuApaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 1, 11)
)
tnOtuApaGroup.setObjects(
      *(("TROPIC-OTUODU-MIB", "tnOtuApaPreFecBer"),
        ("TROPIC-OTUODU-MIB", "tnOtuApaFecUncorrCnt"))
)
if mibBuilder.loadTexts:
    tnOtuApaGroup.setStatus("current")

tnOtsigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 1, 12)
)
tnOtsigGroup.setObjects(
      *(("TROPIC-OTUODU-MIB", "tnOtsigCommand"),
        ("TROPIC-OTUODU-MIB", "tnOtsigOtuStruct"),
        ("TROPIC-OTUODU-MIB", "tnOtsigTransmissionMode"),
        ("TROPIC-OTUODU-MIB", "tnOtsigRegenResponse"),
        ("TROPIC-OTUODU-MIB", "tnOtsigOTSilist"),
        ("TROPIC-OTUODU-MIB", "tnOtsigLLEB"),
        ("TROPIC-OTUODU-MIB", "tnOtsigDLEB"),
        ("TROPIC-OTUODU-MIB", "tnOtsigTSEB"),
        ("TROPIC-OTUODU-MIB", "tnOtsigBaudrate"),
        ("TROPIC-OTUODU-MIB", "tnOtsigEncoding"),
        ("TROPIC-OTUODU-MIB", "tnOtsigPhaseEncode"),
        ("TROPIC-OTUODU-MIB", "tnOtsigPolarizationTrack"),
        ("TROPIC-OTUODU-MIB", "tnOtsigTxShape"),
        ("TROPIC-OTUODU-MIB", "tnOtsigFecMode"),
        ("TROPIC-OTUODU-MIB", "tnOtsigNonLinearComp"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCdPreComp"),
        ("TROPIC-OTUODU-MIB", "tnOtsigDescription"),
        ("TROPIC-OTUODU-MIB", "tnOtsigPayloadRate"),
        ("TROPIC-OTUODU-MIB", "tnOtsigIOPMode"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCapacity"),
        ("TROPIC-OTUODU-MIB", "tnOtsigProfileId"),
        ("TROPIC-OTUODU-MIB", "tnOtsigMgracd"),
        ("TROPIC-OTUODU-MIB", "tnOtsigFacilityDescriptorName"),
        ("TROPIC-OTUODU-MIB", "tnOtsigFacilityDescriptorDesc"),
        ("TROPIC-OTUODU-MIB", "tnOtsigFacilityDescriptorCirId"),
        ("TROPIC-OTUODU-MIB", "tnOtsigFacilityDescriptorConnPtId"),
        ("TROPIC-OTUODU-MIB", "tnOtsigFacilityDescCustLifeCycleState"),
        ("TROPIC-OTUODU-MIB", "tnOtsigFacilityDescAdminState"),
        ("TROPIC-OTUODU-MIB", "tnOtsigGroupIdentification"),
        ("TROPIC-OTUODU-MIB", "tnOtsigInterfaceIdentification"),
        ("TROPIC-OTUODU-MIB", "tnOtsigAdminState"),
        ("TROPIC-OTUODU-MIB", "tnOtsigStateAINS"),
        ("TROPIC-OTUODU-MIB", "tnOtsigStateAINSTimerStart"),
        ("TROPIC-OTUODU-MIB", "tnOtsigStateAINSDebounce"),
        ("TROPIC-OTUODU-MIB", "tnOtsigStateQualifier"),
        ("TROPIC-OTUODU-MIB", "tnOtsigOperationalCapability"),
        ("TROPIC-OTUODU-MIB", "tnOtsigOperationalState"),
        ("TROPIC-OTUODU-MIB", "tnOtsigUsingSysAINSDebounceTime"),
        ("TROPIC-OTUODU-MIB", "tnOtsigIncFlexOFrameGid"),
        ("TROPIC-OTUODU-MIB", "tnOtsigIncFlexOFrameIID"),
        ("TROPIC-OTUODU-MIB", "tnOtsigIncFlexOFrameIIDMap1"),
        ("TROPIC-OTUODU-MIB", "tnOtsigIncFlexOFrameIIDMap2"),
        ("TROPIC-OTUODU-MIB", "tnOtsigIncFlexOFrameIIDMap3"),
        ("TROPIC-OTUODU-MIB", "tnOtsigIncFlexOFrameIIDMap4"),
        ("TROPIC-OTUODU-MIB", "tnOtsigAlmProfName"),
        ("TROPIC-OTUODU-MIB", "tnOtsigReferenceProfileId"))
)
if mibBuilder.loadTexts:
    tnOtsigGroup.setStatus("current")

tnOtsigProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 1, 13)
)
tnOtsigProfileGroup.setObjects(
      *(("TROPIC-OTUODU-MIB", "tnOtsigProfile"),
        ("TROPIC-OTUODU-MIB", "tnOtsigProfileCardType"),
        ("TROPIC-OTUODU-MIB", "tnOtsigProfileExternalCategory"),
        ("TROPIC-OTUODU-MIB", "tnOtsigProfileExternalCardType"))
)
if mibBuilder.loadTexts:
    tnOtsigProfileGroup.setStatus("current")

tnOtsigCustomProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 1, 14)
)
tnOtsigCustomProfileGroup.setObjects(
      *(("TROPIC-OTUODU-MIB", "tnOtsigRefSysProfileId"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomProfileRowStatus"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomProfileCategory"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomProfileBaudRate"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomProfileIOPMode"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomProfileEncoding"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomProfileFecMode"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomProfilePhaseEnc"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomDescription"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomPayloadRate"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomTxShape"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomProfileCardType"))
)
if mibBuilder.loadTexts:
    tnOtsigCustomProfileGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnOdukCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7, 1, 2, 1)
)
tnOdukCompliance.setObjects(
      *(("TROPIC-OTUODU-MIB", "tnOtukGroup"),
        ("TROPIC-OTUODU-MIB", "tnOtuApaGroup"),
        ("TROPIC-OTUODU-MIB", "tnOtsigGroup"),
        ("TROPIC-OTUODU-MIB", "tnOtsigProfileGroup"),
        ("TROPIC-OTUODU-MIB", "tnOtsigCustomProfileGroup"))
)
if mibBuilder.loadTexts:
    tnOdukCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-OTUODU-MIB",
    **{"tnOtuOduMibModule": tnOtuOduMibModule,
       "tnOtuOduConf": tnOtuOduConf,
       "tnOtuOduGroups": tnOtuOduGroups,
       "tnOtukGroup": tnOtukGroup,
       "tnOtuApaGroup": tnOtuApaGroup,
       "tnOtsigGroup": tnOtsigGroup,
       "tnOtsigProfileGroup": tnOtsigProfileGroup,
       "tnOtsigCustomProfileGroup": tnOtsigCustomProfileGroup,
       "tnOtuOduCompliances": tnOtuOduCompliances,
       "tnOdukCompliance": tnOdukCompliance,
       "tnOtuOduObjs": tnOtuOduObjs,
       "tnOtuOduBasics": tnOtuOduBasics,
       "tnOtukTable": tnOtukTable,
       "tnOtukEntry": tnOtukEntry,
       "tnOtukTtiStatus": tnOtukTtiStatus,
       "tnOtukFecMode": tnOtukFecMode,
       "tnOtukRate": tnOtukRate,
       "tnOtukIncRes": tnOtukIncRes,
       "tnOtukAdminStatus": tnOtukAdminStatus,
       "tnOtukStateAINS": tnOtukStateAINS,
       "tnOtukOperStatus": tnOtukOperStatus,
       "tnOtukStateQualifier": tnOtukStateQualifier,
       "tnOtukOperationalCapability": tnOtukOperationalCapability,
       "tnOtukAINSDebounceTime": tnOtukAINSDebounceTime,
       "tnOtukUsingSysAINSDebounceTime": tnOtukUsingSysAINSDebounceTime,
       "tnOtukAINSDebounceTimeRemaining": tnOtukAINSDebounceTimeRemaining,
       "tnOtukPreFec": tnOtukPreFec,
       "tnOtukPostFec": tnOtukPostFec,
       "tnOtukAsymInterworking": tnOtukAsymInterworking,
       "tnOtukDegThr": tnOtukDegThr,
       "tnOtukDegM": tnOtukDegM,
       "tnOtukDapiAccepted": tnOtukDapiAccepted,
       "tnOtukDapiExpected": tnOtukDapiExpected,
       "tnOtukDapiTransmitted": tnOtukDapiTransmitted,
       "tnOtukOsAccepted": tnOtukOsAccepted,
       "tnOtukOsTransmitted": tnOtukOsTransmitted,
       "tnOtuAlmProfName": tnOtuAlmProfName,
       "tnOtuServerPort": tnOtuServerPort,
       "tnOtukMgracd": tnOtukMgracd,
       "tnOtukType": tnOtukType,
       "tnOtuOtsigId": tnOtuOtsigId,
       "tnOtuChanPoolIfIndex": tnOtuChanPoolIfIndex,
       "tnOtuFacilityDescriptorName": tnOtuFacilityDescriptorName,
       "tnOtuFacilityDescriptorDesc": tnOtuFacilityDescriptorDesc,
       "tnOtuFacilityDescriptorCirId": tnOtuFacilityDescriptorCirId,
       "tnOtuFacilityDescriptorConnPtId": tnOtuFacilityDescriptorConnPtId,
       "tnOtuFacilityDescCustLifeCycleState": tnOtuFacilityDescCustLifeCycleState,
       "tnOtuFacilityDescAdminState": tnOtuFacilityDescAdminState,
       "tnOtuApaTable": tnOtuApaTable,
       "tnOtuApaEntry": tnOtuApaEntry,
       "tnOtuApaInterval": tnOtuApaInterval,
       "tnOtuApaPreFecBer": tnOtuApaPreFecBer,
       "tnOtuApaFecUncorrCnt": tnOtuApaFecUncorrCnt,
       "tnOtsigTable": tnOtsigTable,
       "tnOtsigEntry": tnOtsigEntry,
       "tnOtsigIndex": tnOtsigIndex,
       "tnOtsigCommand": tnOtsigCommand,
       "tnOtsigOtuStruct": tnOtsigOtuStruct,
       "tnOtsigTransmissionMode": tnOtsigTransmissionMode,
       "tnOtsigRegenResponse": tnOtsigRegenResponse,
       "tnOtsigOTSilist": tnOtsigOTSilist,
       "tnOtsigLLEB": tnOtsigLLEB,
       "tnOtsigDLEB": tnOtsigDLEB,
       "tnOtsigTSEB": tnOtsigTSEB,
       "tnOtsigBaudrate": tnOtsigBaudrate,
       "tnOtsigEncoding": tnOtsigEncoding,
       "tnOtsigPhaseEncode": tnOtsigPhaseEncode,
       "tnOtsigPolarizationTrack": tnOtsigPolarizationTrack,
       "tnOtsigTxShape": tnOtsigTxShape,
       "tnOtsigFecMode": tnOtsigFecMode,
       "tnOtsigNonLinearComp": tnOtsigNonLinearComp,
       "tnOtsigCdPreComp": tnOtsigCdPreComp,
       "tnOtsigDescription": tnOtsigDescription,
       "tnOtsigPayloadRate": tnOtsigPayloadRate,
       "tnOtsigIOPMode": tnOtsigIOPMode,
       "tnOtsigCapacity": tnOtsigCapacity,
       "tnOtsigProfileId": tnOtsigProfileId,
       "tnOtsigMgracd": tnOtsigMgracd,
       "tnOtsigFacilityDescriptorName": tnOtsigFacilityDescriptorName,
       "tnOtsigFacilityDescriptorDesc": tnOtsigFacilityDescriptorDesc,
       "tnOtsigFacilityDescriptorCirId": tnOtsigFacilityDescriptorCirId,
       "tnOtsigFacilityDescriptorConnPtId": tnOtsigFacilityDescriptorConnPtId,
       "tnOtsigFacilityDescCustLifeCycleState": tnOtsigFacilityDescCustLifeCycleState,
       "tnOtsigFacilityDescAdminState": tnOtsigFacilityDescAdminState,
       "tnOtsigGroupIdentification": tnOtsigGroupIdentification,
       "tnOtsigInterfaceIdentification": tnOtsigInterfaceIdentification,
       "tnOtsigAdminState": tnOtsigAdminState,
       "tnOtsigStateAINS": tnOtsigStateAINS,
       "tnOtsigStateAINSTimerStart": tnOtsigStateAINSTimerStart,
       "tnOtsigStateAINSDebounce": tnOtsigStateAINSDebounce,
       "tnOtsigStateQualifier": tnOtsigStateQualifier,
       "tnOtsigOperationalCapability": tnOtsigOperationalCapability,
       "tnOtsigOperationalState": tnOtsigOperationalState,
       "tnOtsigUsingSysAINSDebounceTime": tnOtsigUsingSysAINSDebounceTime,
       "tnOtsigIncFlexOFrameGid": tnOtsigIncFlexOFrameGid,
       "tnOtsigIncFlexOFrameIID": tnOtsigIncFlexOFrameIID,
       "tnOtsigIncFlexOFrameIIDMap1": tnOtsigIncFlexOFrameIIDMap1,
       "tnOtsigIncFlexOFrameIIDMap2": tnOtsigIncFlexOFrameIIDMap2,
       "tnOtsigIncFlexOFrameIIDMap3": tnOtsigIncFlexOFrameIIDMap3,
       "tnOtsigIncFlexOFrameIIDMap4": tnOtsigIncFlexOFrameIIDMap4,
       "tnOtsigAlmProfName": tnOtsigAlmProfName,
       "tnOtsigReferenceProfileId": tnOtsigReferenceProfileId,
       "tnOtsigProfileTable": tnOtsigProfileTable,
       "tnOtsigProfileEntry": tnOtsigProfileEntry,
       "tnOtsigProfile": tnOtsigProfile,
       "tnOtsigProfileCardType": tnOtsigProfileCardType,
       "tnOtsigProfileExternalCategory": tnOtsigProfileExternalCategory,
       "tnOtsigProfileExternalCardType": tnOtsigProfileExternalCardType,
       "tnOtsigCustomProfileTable": tnOtsigCustomProfileTable,
       "tnOtsigCustomProfileEntry": tnOtsigCustomProfileEntry,
       "tnOtsigCustomProfile": tnOtsigCustomProfile,
       "tnOtsigRefSysProfileId": tnOtsigRefSysProfileId,
       "tnOtsigCustomProfileRowStatus": tnOtsigCustomProfileRowStatus,
       "tnOtsigCustomProfileBaudRate": tnOtsigCustomProfileBaudRate,
       "tnOtsigCustomProfileIOPMode": tnOtsigCustomProfileIOPMode,
       "tnOtsigCustomProfileEncoding": tnOtsigCustomProfileEncoding,
       "tnOtsigCustomProfileFecMode": tnOtsigCustomProfileFecMode,
       "tnOtsigCustomProfilePhaseEnc": tnOtsigCustomProfilePhaseEnc,
       "tnOtsigCustomDescription": tnOtsigCustomDescription,
       "tnOtsigCustomPayloadRate": tnOtsigCustomPayloadRate,
       "tnOtsigCustomTxShape": tnOtsigCustomTxShape,
       "tnOtsigCustomProfileCategory": tnOtsigCustomProfileCategory,
       "tnOtsigCustomProfileCardType": tnOtsigCustomProfileCardType}
)
