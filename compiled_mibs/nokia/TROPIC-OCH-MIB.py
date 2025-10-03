# SNMP MIB module (TROPIC-OCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-OCH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:33 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(tnOchMIB,
 tnPortModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnOchMIB",
    "tnPortModules")

(AluWdmDisabledEnabled,
 AluWdmOtuBitRate,
 AluWdmOtuEncoding,
 TnCommand) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmDisabledEnabled",
    "AluWdmOtuBitRate",
    "AluWdmOtuEncoding",
    "TnCommand")


# MODULE-IDENTITY

tnOchMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tnOchMibModule.setRevisions(
        ("2023-02-24 12:00",
         "2022-08-26 12:00",
         "2021-02-05 12:00",
         "2020-12-04 12:00",
         "2020-01-10 12:00",
         "2018-03-09 12:00",
         "2018-02-23 12:00",
         "2017-07-07 12:00",
         "2017-06-09 12:00",
         "2017-01-17 12:00",
         "2016-11-16 12:00",
         "2016-09-23 12:00",
         "2015-12-15 12:00",
         "2015-06-11 12:00",
         "2013-06-19 12:00",
         "2013-05-21 12:00",
         "2013-04-12 12:00",
         "2013-02-22 12:00",
         "2012-10-22 12:00",
         "2011-04-03 12:00",
         "2009-09-09 12:00",
         "2009-05-31 12:00",
         "2009-04-07 12:00",
         "2009-03-03 12:00",
         "2009-02-27 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicOchXcStateType(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )



class TropicOchXcStateQualifierType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("maskAlarmsZA", 0),
          ("maskAlarmsAZ", 1),
          ("unknownWaveKeyZA", 2),
          ("unknownWaveKeyAZ", 3),
          ("portDown", 4),
          ("manualOverride", 5),
          ("invalidTopology", 6),
          ("inProgress", 7),
          ("misMatchedKeysZA", 8),
          ("misMatchedKeysAZ", 9),
          ("fdiAZ", 10),
          ("fdiZA", 11))
    )


# MIB Managed Objects in the order of their OIDs

_TnOchConf_ObjectIdentity = ObjectIdentity
tnOchConf = _TnOchConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 1)
)
_TnOchGroups_ObjectIdentity = ObjectIdentity
tnOchGroups = _TnOchGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 1, 1)
)
_TnOchCompliances_ObjectIdentity = ObjectIdentity
tnOchCompliances = _TnOchCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 1, 2)
)
_TnOchObjs_ObjectIdentity = ObjectIdentity
tnOchObjs = _TnOchObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2)
)
_TnOchBasics_ObjectIdentity = ObjectIdentity
tnOchBasics = _TnOchBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1)
)
_TnOchTrailTable_Object = MibTable
tnOchTrailTable = _TnOchTrailTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnOchTrailTable.setStatus("current")
_TnOchTrailEntry_Object = MibTableRow
tnOchTrailEntry = _TnOchTrailEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1)
)
tnOchTrailEntry.setIndexNames(
    (0, "TROPIC-OCH-MIB", "tnOchTrailIpAddress"),
    (0, "TROPIC-OCH-MIB", "tnOchTrailifIndex"),
)
if mibBuilder.loadTexts:
    tnOchTrailEntry.setStatus("current")
_TnOchTrailIpAddress_Type = IpAddress
_TnOchTrailIpAddress_Object = MibTableColumn
tnOchTrailIpAddress = _TnOchTrailIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 1),
    _TnOchTrailIpAddress_Type()
)
tnOchTrailIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOchTrailIpAddress.setStatus("current")
_TnOchTrailifIndex_Type = InterfaceIndex
_TnOchTrailifIndex_Object = MibTableColumn
tnOchTrailifIndex = _TnOchTrailifIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 2),
    _TnOchTrailifIndex_Type()
)
tnOchTrailifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOchTrailifIndex.setStatus("current")


class _TnOchTrailName_Type(SnmpAdminString):
    """Custom type tnOchTrailName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 276),
    )


_TnOchTrailName_Type.__name__ = "SnmpAdminString"
_TnOchTrailName_Object = MibTableColumn
tnOchTrailName = _TnOchTrailName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 3),
    _TnOchTrailName_Type()
)
tnOchTrailName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailName.setStatus("current")
_TnOchTrailWaveKey1_Type = Unsigned32
_TnOchTrailWaveKey1_Object = MibTableColumn
tnOchTrailWaveKey1 = _TnOchTrailWaveKey1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 4),
    _TnOchTrailWaveKey1_Type()
)
tnOchTrailWaveKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailWaveKey1.setStatus("current")
_TnOchTrailWaveKey2_Type = Unsigned32
_TnOchTrailWaveKey2_Object = MibTableColumn
tnOchTrailWaveKey2 = _TnOchTrailWaveKey2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 5),
    _TnOchTrailWaveKey2_Type()
)
tnOchTrailWaveKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailWaveKey2.setStatus("current")
_TnOchTrailITUChannel_Type = Unsigned32
_TnOchTrailITUChannel_Object = MibTableColumn
tnOchTrailITUChannel = _TnOchTrailITUChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 6),
    _TnOchTrailITUChannel_Type()
)
tnOchTrailITUChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailITUChannel.setStatus("current")


class _TnOchTrailItuBitRate_Type(AluWdmOtuBitRate):
    """Custom type tnOchTrailItuBitRate based on AluWdmOtuBitRate"""
    defaultValue = 10000


_TnOchTrailItuBitRate_Type.__name__ = "AluWdmOtuBitRate"
_TnOchTrailItuBitRate_Object = MibTableColumn
tnOchTrailItuBitRate = _TnOchTrailItuBitRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 7),
    _TnOchTrailItuBitRate_Type()
)
tnOchTrailItuBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailItuBitRate.setStatus("current")


class _TnOchTrailItuEncoding_Type(AluWdmOtuEncoding):
    """Custom type tnOchTrailItuEncoding based on AluWdmOtuEncoding"""
    defaultValue = 10000


_TnOchTrailItuEncoding_Type.__name__ = "AluWdmOtuEncoding"
_TnOchTrailItuEncoding_Object = MibTableColumn
tnOchTrailItuEncoding = _TnOchTrailItuEncoding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 8),
    _TnOchTrailItuEncoding_Type()
)
tnOchTrailItuEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailItuEncoding.setStatus("current")


class _TnOchTrailItuSrcOTType_Type(Unsigned32):
    """Custom type tnOchTrailItuSrcOTType based on Unsigned32"""
    defaultValue = 2


_TnOchTrailItuSrcOTType_Type.__name__ = "Unsigned32"
_TnOchTrailItuSrcOTType_Object = MibTableColumn
tnOchTrailItuSrcOTType = _TnOchTrailItuSrcOTType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 9),
    _TnOchTrailItuSrcOTType_Type()
)
tnOchTrailItuSrcOTType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailItuSrcOTType.setStatus("current")


class _TnOchTrailEncoderDomain_Type(Integer32):
    """Custom type tnOchTrailEncoderDomain based on Integer32"""
    defaultValue = -1


_TnOchTrailEncoderDomain_Type.__name__ = "Integer32"
_TnOchTrailEncoderDomain_Object = MibTableColumn
tnOchTrailEncoderDomain = _TnOchTrailEncoderDomain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 10),
    _TnOchTrailEncoderDomain_Type()
)
tnOchTrailEncoderDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailEncoderDomain.setStatus("current")


class _TnOchTrailWaveKeyDupsUnlocked_Type(TruthValue):
    """Custom type tnOchTrailWaveKeyDupsUnlocked based on TruthValue"""
    defaultValue = 2


_TnOchTrailWaveKeyDupsUnlocked_Type.__name__ = "TruthValue"
_TnOchTrailWaveKeyDupsUnlocked_Object = MibTableColumn
tnOchTrailWaveKeyDupsUnlocked = _TnOchTrailWaveKeyDupsUnlocked_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 11),
    _TnOchTrailWaveKeyDupsUnlocked_Type()
)
tnOchTrailWaveKeyDupsUnlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailWaveKeyDupsUnlocked.setStatus("current")


class _TnOchTrailEncoderDomainProt_Type(Integer32):
    """Custom type tnOchTrailEncoderDomainProt based on Integer32"""
    defaultValue = -1


_TnOchTrailEncoderDomainProt_Type.__name__ = "Integer32"
_TnOchTrailEncoderDomainProt_Object = MibTableColumn
tnOchTrailEncoderDomainProt = _TnOchTrailEncoderDomainProt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 12),
    _TnOchTrailEncoderDomainProt_Type()
)
tnOchTrailEncoderDomainProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailEncoderDomainProt.setStatus("current")


class _TnOchTrailWaveKeyDupsUnlockedProt_Type(TruthValue):
    """Custom type tnOchTrailWaveKeyDupsUnlockedProt based on TruthValue"""
    defaultValue = 2


_TnOchTrailWaveKeyDupsUnlockedProt_Type.__name__ = "TruthValue"
_TnOchTrailWaveKeyDupsUnlockedProt_Object = MibTableColumn
tnOchTrailWaveKeyDupsUnlockedProt = _TnOchTrailWaveKeyDupsUnlockedProt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 13),
    _TnOchTrailWaveKeyDupsUnlockedProt_Type()
)
tnOchTrailWaveKeyDupsUnlockedProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailWaveKeyDupsUnlockedProt.setStatus("current")
_TnOchTrailItuSpectralWidth_Type = Unsigned32
_TnOchTrailItuSpectralWidth_Object = MibTableColumn
tnOchTrailItuSpectralWidth = _TnOchTrailItuSpectralWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 2, 1, 14),
    _TnOchTrailItuSpectralWidth_Type()
)
tnOchTrailItuSpectralWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchTrailItuSpectralWidth.setStatus("current")
if mibBuilder.loadTexts:
    tnOchTrailItuSpectralWidth.setUnits("MHz")
_TnOchXcItuTable_Object = MibTable
tnOchXcItuTable = _TnOchXcItuTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnOchXcItuTable.setStatus("current")
_TnOchXcItuEntry_Object = MibTableRow
tnOchXcItuEntry = _TnOchXcItuEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1)
)
tnOchXcItuEntry.setIndexNames(
    (0, "TROPIC-OCH-MIB", "tnOchXcItuSrcIfIndex"),
    (0, "TROPIC-OCH-MIB", "tnOchXcItuSrcChannel"),
    (0, "TROPIC-OCH-MIB", "tnOchXcItuDestIfIndex"),
    (0, "TROPIC-OCH-MIB", "tnOchXcItuDestChannel"),
)
if mibBuilder.loadTexts:
    tnOchXcItuEntry.setStatus("current")
_TnOchXcItuSrcIfIndex_Type = InterfaceIndex
_TnOchXcItuSrcIfIndex_Object = MibTableColumn
tnOchXcItuSrcIfIndex = _TnOchXcItuSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 1),
    _TnOchXcItuSrcIfIndex_Type()
)
tnOchXcItuSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOchXcItuSrcIfIndex.setStatus("current")
_TnOchXcItuSrcChannel_Type = Unsigned32
_TnOchXcItuSrcChannel_Object = MibTableColumn
tnOchXcItuSrcChannel = _TnOchXcItuSrcChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 2),
    _TnOchXcItuSrcChannel_Type()
)
tnOchXcItuSrcChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOchXcItuSrcChannel.setStatus("current")
_TnOchXcItuDestIfIndex_Type = InterfaceIndex
_TnOchXcItuDestIfIndex_Object = MibTableColumn
tnOchXcItuDestIfIndex = _TnOchXcItuDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 3),
    _TnOchXcItuDestIfIndex_Type()
)
tnOchXcItuDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOchXcItuDestIfIndex.setStatus("current")
_TnOchXcItuDestChannel_Type = Unsigned32
_TnOchXcItuDestChannel_Object = MibTableColumn
tnOchXcItuDestChannel = _TnOchXcItuDestChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 4),
    _TnOchXcItuDestChannel_Type()
)
tnOchXcItuDestChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOchXcItuDestChannel.setStatus("current")
_TnOchXcItuId_Type = Unsigned32
_TnOchXcItuId_Object = MibTableColumn
tnOchXcItuId = _TnOchXcItuId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 5),
    _TnOchXcItuId_Type()
)
tnOchXcItuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuId.setStatus("current")


class _TnOchXcItuName_Type(SnmpAdminString):
    """Custom type tnOchXcItuName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 276),
    )


_TnOchXcItuName_Type.__name__ = "SnmpAdminString"
_TnOchXcItuName_Object = MibTableColumn
tnOchXcItuName = _TnOchXcItuName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 6),
    _TnOchXcItuName_Type()
)
tnOchXcItuName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuName.setStatus("current")


class _TnOchXcItuBidirectional_Type(TruthValue):
    """Custom type tnOchXcItuBidirectional based on TruthValue"""
    defaultValue = 1


_TnOchXcItuBidirectional_Type.__name__ = "TruthValue"
_TnOchXcItuBidirectional_Object = MibTableColumn
tnOchXcItuBidirectional = _TnOchXcItuBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 7),
    _TnOchXcItuBidirectional_Type()
)
tnOchXcItuBidirectional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuBidirectional.setStatus("current")


class _TnOchXcItuEncodedWaveKey1AZ_Type(Unsigned32):
    """Custom type tnOchXcItuEncodedWaveKey1AZ based on Unsigned32"""
    defaultValue = 0


_TnOchXcItuEncodedWaveKey1AZ_Type.__name__ = "Unsigned32"
_TnOchXcItuEncodedWaveKey1AZ_Object = MibTableColumn
tnOchXcItuEncodedWaveKey1AZ = _TnOchXcItuEncodedWaveKey1AZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 8),
    _TnOchXcItuEncodedWaveKey1AZ_Type()
)
tnOchXcItuEncodedWaveKey1AZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuEncodedWaveKey1AZ.setStatus("current")


class _TnOchXcItuEncodedWaveKey2AZ_Type(Unsigned32):
    """Custom type tnOchXcItuEncodedWaveKey2AZ based on Unsigned32"""
    defaultValue = 0


_TnOchXcItuEncodedWaveKey2AZ_Type.__name__ = "Unsigned32"
_TnOchXcItuEncodedWaveKey2AZ_Object = MibTableColumn
tnOchXcItuEncodedWaveKey2AZ = _TnOchXcItuEncodedWaveKey2AZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 9),
    _TnOchXcItuEncodedWaveKey2AZ_Type()
)
tnOchXcItuEncodedWaveKey2AZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuEncodedWaveKey2AZ.setStatus("current")


class _TnOchXcItuEncodedWaveKey1ZA_Type(Unsigned32):
    """Custom type tnOchXcItuEncodedWaveKey1ZA based on Unsigned32"""
    defaultValue = 0


_TnOchXcItuEncodedWaveKey1ZA_Type.__name__ = "Unsigned32"
_TnOchXcItuEncodedWaveKey1ZA_Object = MibTableColumn
tnOchXcItuEncodedWaveKey1ZA = _TnOchXcItuEncodedWaveKey1ZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 10),
    _TnOchXcItuEncodedWaveKey1ZA_Type()
)
tnOchXcItuEncodedWaveKey1ZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuEncodedWaveKey1ZA.setStatus("current")


class _TnOchXcItuEncodedWaveKey2ZA_Type(Unsigned32):
    """Custom type tnOchXcItuEncodedWaveKey2ZA based on Unsigned32"""
    defaultValue = 0


_TnOchXcItuEncodedWaveKey2ZA_Type.__name__ = "Unsigned32"
_TnOchXcItuEncodedWaveKey2ZA_Object = MibTableColumn
tnOchXcItuEncodedWaveKey2ZA = _TnOchXcItuEncodedWaveKey2ZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 11),
    _TnOchXcItuEncodedWaveKey2ZA_Type()
)
tnOchXcItuEncodedWaveKey2ZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuEncodedWaveKey2ZA.setStatus("current")


class _TnOchXcItuAutoWaveKeySelect_Type(Integer32):
    """Custom type tnOchXcItuAutoWaveKeySelect based on Integer32"""
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
        *(("auto", 1),
          ("manual", 2),
          ("unkey", 3),
          ("unkeyAuto", 4),
          ("unkeyManual", 5),
          ("manualDnd", 6),
          ("unkeyManualDnd", 7))
    )


_TnOchXcItuAutoWaveKeySelect_Type.__name__ = "Integer32"
_TnOchXcItuAutoWaveKeySelect_Object = MibTableColumn
tnOchXcItuAutoWaveKeySelect = _TnOchXcItuAutoWaveKeySelect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 12),
    _TnOchXcItuAutoWaveKeySelect_Type()
)
tnOchXcItuAutoWaveKeySelect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuAutoWaveKeySelect.setStatus("current")


class _TnOchXcItuAdminState_Type(TropicOchXcStateType):
    """Custom type tnOchXcItuAdminState based on TropicOchXcStateType"""
    defaultValue = 2


_TnOchXcItuAdminState_Type.__name__ = "TropicOchXcStateType"
_TnOchXcItuAdminState_Object = MibTableColumn
tnOchXcItuAdminState = _TnOchXcItuAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 13),
    _TnOchXcItuAdminState_Type()
)
tnOchXcItuAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuAdminState.setStatus("current")
_TnOchXcItuOperState_Type = TropicOchXcStateType
_TnOchXcItuOperState_Object = MibTableColumn
tnOchXcItuOperState = _TnOchXcItuOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 14),
    _TnOchXcItuOperState_Type()
)
tnOchXcItuOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuOperState.setStatus("current")
_TnOchXcItuStateQualifier_Type = TropicOchXcStateQualifierType
_TnOchXcItuStateQualifier_Object = MibTableColumn
tnOchXcItuStateQualifier = _TnOchXcItuStateQualifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 15),
    _TnOchXcItuStateQualifier_Type()
)
tnOchXcItuStateQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuStateQualifier.setStatus("current")


class _TnOchXcItuProtectionState_Type(Integer32):
    """Custom type tnOchXcItuProtectionState based on Integer32"""
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
          ("working", 2),
          ("protection", 3),
          ("dropContinue", 4))
    )


_TnOchXcItuProtectionState_Type.__name__ = "Integer32"
_TnOchXcItuProtectionState_Object = MibTableColumn
tnOchXcItuProtectionState = _TnOchXcItuProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 16),
    _TnOchXcItuProtectionState_Type()
)
tnOchXcItuProtectionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuProtectionState.setStatus("current")


class _TnOchXcItuForceDeletion_Type(TruthValue):
    """Custom type tnOchXcItuForceDeletion based on TruthValue"""
    defaultValue = 2


_TnOchXcItuForceDeletion_Type.__name__ = "TruthValue"
_TnOchXcItuForceDeletion_Object = MibTableColumn
tnOchXcItuForceDeletion = _TnOchXcItuForceDeletion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 17),
    _TnOchXcItuForceDeletion_Type()
)
tnOchXcItuForceDeletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuForceDeletion.setStatus("current")
_TnOchXcItuRowStatus_Type = RowStatus
_TnOchXcItuRowStatus_Object = MibTableColumn
tnOchXcItuRowStatus = _TnOchXcItuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 18),
    _TnOchXcItuRowStatus_Type()
)
tnOchXcItuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuRowStatus.setStatus("current")


class _TnOchXcItuAcceptPowers_Type(Integer32):
    """Custom type tnOchXcItuAcceptPowers based on Integer32"""
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
        *(("noCmd", 1),
          ("azIngress", 2),
          ("azEgress", 3),
          ("zaIngress", 4),
          ("zaEgress", 5),
          ("azBoth", 6),
          ("zaBoth", 7))
    )


_TnOchXcItuAcceptPowers_Type.__name__ = "Integer32"
_TnOchXcItuAcceptPowers_Object = MibTableColumn
tnOchXcItuAcceptPowers = _TnOchXcItuAcceptPowers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 19),
    _TnOchXcItuAcceptPowers_Type()
)
tnOchXcItuAcceptPowers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuAcceptPowers.setStatus("current")
_TnOchXcItuOperCapability_Type = AluWdmDisabledEnabled
_TnOchXcItuOperCapability_Object = MibTableColumn
tnOchXcItuOperCapability = _TnOchXcItuOperCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 20),
    _TnOchXcItuOperCapability_Type()
)
tnOchXcItuOperCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuOperCapability.setStatus("current")


class _TnOchXcItuType_Type(Integer32):
    """Custom type tnOchXcItuType based on Integer32"""
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
          ("drop", 2),
          ("thru", 3),
          ("addDrop", 4),
          ("continue", 5))
    )


_TnOchXcItuType_Type.__name__ = "Integer32"
_TnOchXcItuType_Object = MibTableColumn
tnOchXcItuType = _TnOchXcItuType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 21),
    _TnOchXcItuType_Type()
)
tnOchXcItuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuType.setStatus("current")


class _TnOchXcItuPowerMgmtType_Type(Integer32):
    """Custom type tnOchXcItuPowerMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2),
          ("hybrid", 3))
    )


_TnOchXcItuPowerMgmtType_Type.__name__ = "Integer32"
_TnOchXcItuPowerMgmtType_Object = MibTableColumn
tnOchXcItuPowerMgmtType = _TnOchXcItuPowerMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 22),
    _TnOchXcItuPowerMgmtType_Type()
)
tnOchXcItuPowerMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuPowerMgmtType.setStatus("current")


class _TnOchXcItuTopology_Type(OctetString):
    """Custom type tnOchXcItuTopology based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_TnOchXcItuTopology_Type.__name__ = "OctetString"
_TnOchXcItuTopology_Object = MibTableColumn
tnOchXcItuTopology = _TnOchXcItuTopology_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 23),
    _TnOchXcItuTopology_Type()
)
tnOchXcItuTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuTopology.setStatus("current")


class _TnOchXcItuTopologyZA_Type(OctetString):
    """Custom type tnOchXcItuTopologyZA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_TnOchXcItuTopologyZA_Type.__name__ = "OctetString"
_TnOchXcItuTopologyZA_Object = MibTableColumn
tnOchXcItuTopologyZA = _TnOchXcItuTopologyZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 24),
    _TnOchXcItuTopologyZA_Type()
)
tnOchXcItuTopologyZA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuTopologyZA.setStatus("current")


class _TnOchXcItuBitRateAZ_Type(AluWdmOtuBitRate):
    """Custom type tnOchXcItuBitRateAZ based on AluWdmOtuBitRate"""
    defaultValue = 9998


_TnOchXcItuBitRateAZ_Type.__name__ = "AluWdmOtuBitRate"
_TnOchXcItuBitRateAZ_Object = MibTableColumn
tnOchXcItuBitRateAZ = _TnOchXcItuBitRateAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 25),
    _TnOchXcItuBitRateAZ_Type()
)
tnOchXcItuBitRateAZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuBitRateAZ.setStatus("current")


class _TnOchXcItuBitRateZA_Type(AluWdmOtuBitRate):
    """Custom type tnOchXcItuBitRateZA based on AluWdmOtuBitRate"""
    defaultValue = 9998


_TnOchXcItuBitRateZA_Type.__name__ = "AluWdmOtuBitRate"
_TnOchXcItuBitRateZA_Object = MibTableColumn
tnOchXcItuBitRateZA = _TnOchXcItuBitRateZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 26),
    _TnOchXcItuBitRateZA_Type()
)
tnOchXcItuBitRateZA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuBitRateZA.setStatus("current")


class _TnOchXcItuEncodingAZ_Type(AluWdmOtuEncoding):
    """Custom type tnOchXcItuEncodingAZ based on AluWdmOtuEncoding"""
    defaultValue = 9998


_TnOchXcItuEncodingAZ_Type.__name__ = "AluWdmOtuEncoding"
_TnOchXcItuEncodingAZ_Object = MibTableColumn
tnOchXcItuEncodingAZ = _TnOchXcItuEncodingAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 27),
    _TnOchXcItuEncodingAZ_Type()
)
tnOchXcItuEncodingAZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuEncodingAZ.setStatus("current")


class _TnOchXcItuEncodingZA_Type(AluWdmOtuEncoding):
    """Custom type tnOchXcItuEncodingZA based on AluWdmOtuEncoding"""
    defaultValue = 9998


_TnOchXcItuEncodingZA_Type.__name__ = "AluWdmOtuEncoding"
_TnOchXcItuEncodingZA_Object = MibTableColumn
tnOchXcItuEncodingZA = _TnOchXcItuEncodingZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 28),
    _TnOchXcItuEncodingZA_Type()
)
tnOchXcItuEncodingZA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuEncodingZA.setStatus("current")


class _TnOchXcItuUserBitRateAZ_Type(AluWdmOtuBitRate):
    """Custom type tnOchXcItuUserBitRateAZ based on AluWdmOtuBitRate"""
    defaultValue = 9998


_TnOchXcItuUserBitRateAZ_Type.__name__ = "AluWdmOtuBitRate"
_TnOchXcItuUserBitRateAZ_Object = MibTableColumn
tnOchXcItuUserBitRateAZ = _TnOchXcItuUserBitRateAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 29),
    _TnOchXcItuUserBitRateAZ_Type()
)
tnOchXcItuUserBitRateAZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuUserBitRateAZ.setStatus("current")


class _TnOchXcItuUserBitRateZA_Type(AluWdmOtuBitRate):
    """Custom type tnOchXcItuUserBitRateZA based on AluWdmOtuBitRate"""
    defaultValue = 9998


_TnOchXcItuUserBitRateZA_Type.__name__ = "AluWdmOtuBitRate"
_TnOchXcItuUserBitRateZA_Object = MibTableColumn
tnOchXcItuUserBitRateZA = _TnOchXcItuUserBitRateZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 30),
    _TnOchXcItuUserBitRateZA_Type()
)
tnOchXcItuUserBitRateZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuUserBitRateZA.setStatus("current")


class _TnOchXcItuUserEncodingAZ_Type(AluWdmOtuEncoding):
    """Custom type tnOchXcItuUserEncodingAZ based on AluWdmOtuEncoding"""
    defaultValue = 9998


_TnOchXcItuUserEncodingAZ_Type.__name__ = "AluWdmOtuEncoding"
_TnOchXcItuUserEncodingAZ_Object = MibTableColumn
tnOchXcItuUserEncodingAZ = _TnOchXcItuUserEncodingAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 31),
    _TnOchXcItuUserEncodingAZ_Type()
)
tnOchXcItuUserEncodingAZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuUserEncodingAZ.setStatus("current")


class _TnOchXcItuUserEncodingZA_Type(AluWdmOtuEncoding):
    """Custom type tnOchXcItuUserEncodingZA based on AluWdmOtuEncoding"""
    defaultValue = 9998


_TnOchXcItuUserEncodingZA_Type.__name__ = "AluWdmOtuEncoding"
_TnOchXcItuUserEncodingZA_Object = MibTableColumn
tnOchXcItuUserEncodingZA = _TnOchXcItuUserEncodingZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 32),
    _TnOchXcItuUserEncodingZA_Type()
)
tnOchXcItuUserEncodingZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuUserEncodingZA.setStatus("current")


class _TnOchXcItuWaveKeySelectPreference_Type(Integer32):
    """Custom type tnOchXcItuWaveKeySelectPreference based on Integer32"""
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
        *(("notApplicable", 1),
          ("none", 2),
          ("dupsOk", 3),
          ("forceNoDups", 4))
    )


_TnOchXcItuWaveKeySelectPreference_Type.__name__ = "Integer32"
_TnOchXcItuWaveKeySelectPreference_Object = MibTableColumn
tnOchXcItuWaveKeySelectPreference = _TnOchXcItuWaveKeySelectPreference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 33),
    _TnOchXcItuWaveKeySelectPreference_Type()
)
tnOchXcItuWaveKeySelectPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuWaveKeySelectPreference.setStatus("current")


class _TnOchXcItuEncoderDomainAZ_Type(Integer32):
    """Custom type tnOchXcItuEncoderDomainAZ based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 19),
    )


_TnOchXcItuEncoderDomainAZ_Type.__name__ = "Integer32"
_TnOchXcItuEncoderDomainAZ_Object = MibTableColumn
tnOchXcItuEncoderDomainAZ = _TnOchXcItuEncoderDomainAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 34),
    _TnOchXcItuEncoderDomainAZ_Type()
)
tnOchXcItuEncoderDomainAZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuEncoderDomainAZ.setStatus("current")


class _TnOchXcItuEncoderDomainZA_Type(Integer32):
    """Custom type tnOchXcItuEncoderDomainZA based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 19),
    )


_TnOchXcItuEncoderDomainZA_Type.__name__ = "Integer32"
_TnOchXcItuEncoderDomainZA_Object = MibTableColumn
tnOchXcItuEncoderDomainZA = _TnOchXcItuEncoderDomainZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 35),
    _TnOchXcItuEncoderDomainZA_Type()
)
tnOchXcItuEncoderDomainZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuEncoderDomainZA.setStatus("current")


class _TnOchXcItuWaveKeyDupsUnlockedAZ_Type(Integer32):
    """Custom type tnOchXcItuWaveKeyDupsUnlockedAZ based on Integer32"""
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
        *(("notReceived", 1),
          ("true", 2),
          ("false", 3))
    )


_TnOchXcItuWaveKeyDupsUnlockedAZ_Type.__name__ = "Integer32"
_TnOchXcItuWaveKeyDupsUnlockedAZ_Object = MibTableColumn
tnOchXcItuWaveKeyDupsUnlockedAZ = _TnOchXcItuWaveKeyDupsUnlockedAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 36),
    _TnOchXcItuWaveKeyDupsUnlockedAZ_Type()
)
tnOchXcItuWaveKeyDupsUnlockedAZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuWaveKeyDupsUnlockedAZ.setStatus("current")


class _TnOchXcItuWaveKeyDupsUnlockedZA_Type(Integer32):
    """Custom type tnOchXcItuWaveKeyDupsUnlockedZA based on Integer32"""
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
        *(("notReceived", 1),
          ("true", 2),
          ("false", 3))
    )


_TnOchXcItuWaveKeyDupsUnlockedZA_Type.__name__ = "Integer32"
_TnOchXcItuWaveKeyDupsUnlockedZA_Object = MibTableColumn
tnOchXcItuWaveKeyDupsUnlockedZA = _TnOchXcItuWaveKeyDupsUnlockedZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 37),
    _TnOchXcItuWaveKeyDupsUnlockedZA_Type()
)
tnOchXcItuWaveKeyDupsUnlockedZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuWaveKeyDupsUnlockedZA.setStatus("current")


class _TnOchXcItuRekeyWithDuplicatesAllowed_Type(TnCommand):
    """Custom type tnOchXcItuRekeyWithDuplicatesAllowed based on TnCommand"""
    defaultValue = 1


_TnOchXcItuRekeyWithDuplicatesAllowed_Type.__name__ = "TnCommand"
_TnOchXcItuRekeyWithDuplicatesAllowed_Object = MibTableColumn
tnOchXcItuRekeyWithDuplicatesAllowed = _TnOchXcItuRekeyWithDuplicatesAllowed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 38),
    _TnOchXcItuRekeyWithDuplicatesAllowed_Type()
)
tnOchXcItuRekeyWithDuplicatesAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuRekeyWithDuplicatesAllowed.setStatus("current")


class _TnOchXcItuEncoderDomainProtectAZ_Type(Integer32):
    """Custom type tnOchXcItuEncoderDomainProtectAZ based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 19),
    )


_TnOchXcItuEncoderDomainProtectAZ_Type.__name__ = "Integer32"
_TnOchXcItuEncoderDomainProtectAZ_Object = MibTableColumn
tnOchXcItuEncoderDomainProtectAZ = _TnOchXcItuEncoderDomainProtectAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 39),
    _TnOchXcItuEncoderDomainProtectAZ_Type()
)
tnOchXcItuEncoderDomainProtectAZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuEncoderDomainProtectAZ.setStatus("current")


class _TnOchXcItuEncoderDomainProtectZA_Type(Integer32):
    """Custom type tnOchXcItuEncoderDomainProtectZA based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 19),
    )


_TnOchXcItuEncoderDomainProtectZA_Type.__name__ = "Integer32"
_TnOchXcItuEncoderDomainProtectZA_Object = MibTableColumn
tnOchXcItuEncoderDomainProtectZA = _TnOchXcItuEncoderDomainProtectZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 40),
    _TnOchXcItuEncoderDomainProtectZA_Type()
)
tnOchXcItuEncoderDomainProtectZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuEncoderDomainProtectZA.setStatus("current")


class _TnOchXcItuWaveKeyDupsUnlockedProtectAZ_Type(Integer32):
    """Custom type tnOchXcItuWaveKeyDupsUnlockedProtectAZ based on Integer32"""
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
        *(("notReceived", 1),
          ("true", 2),
          ("false", 3))
    )


_TnOchXcItuWaveKeyDupsUnlockedProtectAZ_Type.__name__ = "Integer32"
_TnOchXcItuWaveKeyDupsUnlockedProtectAZ_Object = MibTableColumn
tnOchXcItuWaveKeyDupsUnlockedProtectAZ = _TnOchXcItuWaveKeyDupsUnlockedProtectAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 41),
    _TnOchXcItuWaveKeyDupsUnlockedProtectAZ_Type()
)
tnOchXcItuWaveKeyDupsUnlockedProtectAZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuWaveKeyDupsUnlockedProtectAZ.setStatus("current")


class _TnOchXcItuWaveKeyDupsUnlockedProtectZA_Type(Integer32):
    """Custom type tnOchXcItuWaveKeyDupsUnlockedProtectZA based on Integer32"""
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
        *(("notReceived", 1),
          ("true", 2),
          ("false", 3))
    )


_TnOchXcItuWaveKeyDupsUnlockedProtectZA_Type.__name__ = "Integer32"
_TnOchXcItuWaveKeyDupsUnlockedProtectZA_Object = MibTableColumn
tnOchXcItuWaveKeyDupsUnlockedProtectZA = _TnOchXcItuWaveKeyDupsUnlockedProtectZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 42),
    _TnOchXcItuWaveKeyDupsUnlockedProtectZA_Type()
)
tnOchXcItuWaveKeyDupsUnlockedProtectZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuWaveKeyDupsUnlockedProtectZA.setStatus("current")


class _TnOchXcItuSpectralWidth_Type(Unsigned32):
    """Custom type tnOchXcItuSpectralWidth based on Unsigned32"""
    defaultValue = 50000


_TnOchXcItuSpectralWidth_Type.__name__ = "Unsigned32"
_TnOchXcItuSpectralWidth_Object = MibTableColumn
tnOchXcItuSpectralWidth = _TnOchXcItuSpectralWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 43),
    _TnOchXcItuSpectralWidth_Type()
)
tnOchXcItuSpectralWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuSpectralWidth.setStatus("current")
if mibBuilder.loadTexts:
    tnOchXcItuSpectralWidth.setUnits("MHz")


class _TnOchXcItuAseControlMode_Type(Integer32):
    """Custom type tnOchXcItuAseControlMode based on Integer32"""
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
        *(("aseDisabled", 1),
          ("aseEnabled", 2),
          ("autoAseOnFailure", 3),
          ("autoAseFailureAndRestore", 4))
    )


_TnOchXcItuAseControlMode_Type.__name__ = "Integer32"
_TnOchXcItuAseControlMode_Object = MibTableColumn
tnOchXcItuAseControlMode = _TnOchXcItuAseControlMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 44),
    _TnOchXcItuAseControlMode_Type()
)
tnOchXcItuAseControlMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuAseControlMode.setStatus("current")
_TnOchXcItuRxBlkByLOSAtoZ_Type = TruthValue
_TnOchXcItuRxBlkByLOSAtoZ_Object = MibTableColumn
tnOchXcItuRxBlkByLOSAtoZ = _TnOchXcItuRxBlkByLOSAtoZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 45),
    _TnOchXcItuRxBlkByLOSAtoZ_Type()
)
tnOchXcItuRxBlkByLOSAtoZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuRxBlkByLOSAtoZ.setStatus("current")
_TnOchXcItuAseFilledAtoZ_Type = TruthValue
_TnOchXcItuAseFilledAtoZ_Object = MibTableColumn
tnOchXcItuAseFilledAtoZ = _TnOchXcItuAseFilledAtoZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 46),
    _TnOchXcItuAseFilledAtoZ_Type()
)
tnOchXcItuAseFilledAtoZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuAseFilledAtoZ.setStatus("current")
_TnOchXcItuRxBlkByLOSZtoA_Type = TruthValue
_TnOchXcItuRxBlkByLOSZtoA_Object = MibTableColumn
tnOchXcItuRxBlkByLOSZtoA = _TnOchXcItuRxBlkByLOSZtoA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 47),
    _TnOchXcItuRxBlkByLOSZtoA_Type()
)
tnOchXcItuRxBlkByLOSZtoA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuRxBlkByLOSZtoA.setStatus("current")
_TnOchXcItuAseFilledZtoA_Type = TruthValue
_TnOchXcItuAseFilledZtoA_Object = MibTableColumn
tnOchXcItuAseFilledZtoA = _TnOchXcItuAseFilledZtoA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 48),
    _TnOchXcItuAseFilledZtoA_Type()
)
tnOchXcItuAseFilledZtoA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuAseFilledZtoA.setStatus("current")


class _TnOchXcItuAseGuardBandMHz_Type(Integer32):
    """Custom type tnOchXcItuAseGuardBandMHz based on Integer32"""
    defaultValue = 6250


_TnOchXcItuAseGuardBandMHz_Type.__name__ = "Integer32"
_TnOchXcItuAseGuardBandMHz_Object = MibTableColumn
tnOchXcItuAseGuardBandMHz = _TnOchXcItuAseGuardBandMHz_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 49),
    _TnOchXcItuAseGuardBandMHz_Type()
)
tnOchXcItuAseGuardBandMHz.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuAseGuardBandMHz.setStatus("current")


class _TnOchXcItuPurpose_Type(Integer32):
    """Custom type tnOchXcItuPurpose based on Integer32"""
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
        *(("payload", 1),
          ("alien", 2),
          ("blocked", 3),
          ("aseFill", 4))
    )


_TnOchXcItuPurpose_Type.__name__ = "Integer32"
_TnOchXcItuPurpose_Object = MibTableColumn
tnOchXcItuPurpose = _TnOchXcItuPurpose_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 50),
    _TnOchXcItuPurpose_Type()
)
tnOchXcItuPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchXcItuPurpose.setStatus("current")
_TnOchXcItuAsonId_Type = Counter64
_TnOchXcItuAsonId_Object = MibTableColumn
tnOchXcItuAsonId = _TnOchXcItuAsonId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 3, 1, 51),
    _TnOchXcItuAsonId_Type()
)
tnOchXcItuAsonId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuAsonId.setStatus("current")
_TnOchXcItuIdTable_Object = MibTable
tnOchXcItuIdTable = _TnOchXcItuIdTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnOchXcItuIdTable.setStatus("current")
_TnOchXcItuIdEntry_Object = MibTableRow
tnOchXcItuIdEntry = _TnOchXcItuIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 4, 1)
)
tnOchXcItuIdEntry.setIndexNames(
    (0, "TROPIC-OCH-MIB", "tnOchXcItuId"),
)
if mibBuilder.loadTexts:
    tnOchXcItuIdEntry.setStatus("current")
_TnOchXcItuIdSrcIfIndex_Type = InterfaceIndex
_TnOchXcItuIdSrcIfIndex_Object = MibTableColumn
tnOchXcItuIdSrcIfIndex = _TnOchXcItuIdSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 4, 1, 1),
    _TnOchXcItuIdSrcIfIndex_Type()
)
tnOchXcItuIdSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuIdSrcIfIndex.setStatus("current")
_TnOchXcItuIdSrcChannel_Type = Unsigned32
_TnOchXcItuIdSrcChannel_Object = MibTableColumn
tnOchXcItuIdSrcChannel = _TnOchXcItuIdSrcChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 4, 1, 2),
    _TnOchXcItuIdSrcChannel_Type()
)
tnOchXcItuIdSrcChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuIdSrcChannel.setStatus("current")
_TnOchXcItuIdDestIfIndex_Type = InterfaceIndex
_TnOchXcItuIdDestIfIndex_Object = MibTableColumn
tnOchXcItuIdDestIfIndex = _TnOchXcItuIdDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 4, 1, 3),
    _TnOchXcItuIdDestIfIndex_Type()
)
tnOchXcItuIdDestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuIdDestIfIndex.setStatus("current")
_TnOchXcItuIdDestChannel_Type = Unsigned32
_TnOchXcItuIdDestChannel_Object = MibTableColumn
tnOchXcItuIdDestChannel = _TnOchXcItuIdDestChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 4, 1, 4),
    _TnOchXcItuIdDestChannel_Type()
)
tnOchXcItuIdDestChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchXcItuIdDestChannel.setStatus("current")
_TnOchGroupXcItuTable_Object = MibTable
tnOchGroupXcItuTable = _TnOchGroupXcItuTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnOchGroupXcItuTable.setStatus("current")
_TnOchGroupXcItuEntry_Object = MibTableRow
tnOchGroupXcItuEntry = _TnOchGroupXcItuEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1)
)
tnOchGroupXcItuEntry.setIndexNames(
    (0, "TROPIC-OCH-MIB", "tnOchGroupXcItuSrcIfIndex"),
    (0, "TROPIC-OCH-MIB", "tnOchGroupXcItuSrcChannel1"),
    (0, "TROPIC-OCH-MIB", "tnOchGroupXcItuDestIfIndex"),
    (0, "TROPIC-OCH-MIB", "tnOchGroupXcItuDestChannel1"),
)
if mibBuilder.loadTexts:
    tnOchGroupXcItuEntry.setStatus("current")
_TnOchGroupXcItuSrcIfIndex_Type = InterfaceIndex
_TnOchGroupXcItuSrcIfIndex_Object = MibTableColumn
tnOchGroupXcItuSrcIfIndex = _TnOchGroupXcItuSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 1),
    _TnOchGroupXcItuSrcIfIndex_Type()
)
tnOchGroupXcItuSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOchGroupXcItuSrcIfIndex.setStatus("current")
_TnOchGroupXcItuSrcChannel1_Type = Unsigned32
_TnOchGroupXcItuSrcChannel1_Object = MibTableColumn
tnOchGroupXcItuSrcChannel1 = _TnOchGroupXcItuSrcChannel1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 2),
    _TnOchGroupXcItuSrcChannel1_Type()
)
tnOchGroupXcItuSrcChannel1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOchGroupXcItuSrcChannel1.setStatus("current")
_TnOchGroupXcItuDestIfIndex_Type = InterfaceIndex
_TnOchGroupXcItuDestIfIndex_Object = MibTableColumn
tnOchGroupXcItuDestIfIndex = _TnOchGroupXcItuDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 3),
    _TnOchGroupXcItuDestIfIndex_Type()
)
tnOchGroupXcItuDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOchGroupXcItuDestIfIndex.setStatus("current")
_TnOchGroupXcItuDestChannel1_Type = Unsigned32
_TnOchGroupXcItuDestChannel1_Object = MibTableColumn
tnOchGroupXcItuDestChannel1 = _TnOchGroupXcItuDestChannel1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 4),
    _TnOchGroupXcItuDestChannel1_Type()
)
tnOchGroupXcItuDestChannel1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOchGroupXcItuDestChannel1.setStatus("current")
_TnOchGroupXcItuSrcChannel2_Type = Unsigned32
_TnOchGroupXcItuSrcChannel2_Object = MibTableColumn
tnOchGroupXcItuSrcChannel2 = _TnOchGroupXcItuSrcChannel2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 5),
    _TnOchGroupXcItuSrcChannel2_Type()
)
tnOchGroupXcItuSrcChannel2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuSrcChannel2.setStatus("current")
_TnOchGroupXcItuDestChannel2_Type = Unsigned32
_TnOchGroupXcItuDestChannel2_Object = MibTableColumn
tnOchGroupXcItuDestChannel2 = _TnOchGroupXcItuDestChannel2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 6),
    _TnOchGroupXcItuDestChannel2_Type()
)
tnOchGroupXcItuDestChannel2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuDestChannel2.setStatus("current")
_TnOchGroupXcItuSrcChannel3_Type = Unsigned32
_TnOchGroupXcItuSrcChannel3_Object = MibTableColumn
tnOchGroupXcItuSrcChannel3 = _TnOchGroupXcItuSrcChannel3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 7),
    _TnOchGroupXcItuSrcChannel3_Type()
)
tnOchGroupXcItuSrcChannel3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuSrcChannel3.setStatus("current")
_TnOchGroupXcItuDestChannel3_Type = Unsigned32
_TnOchGroupXcItuDestChannel3_Object = MibTableColumn
tnOchGroupXcItuDestChannel3 = _TnOchGroupXcItuDestChannel3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 8),
    _TnOchGroupXcItuDestChannel3_Type()
)
tnOchGroupXcItuDestChannel3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuDestChannel3.setStatus("current")
_TnOchGroupXcItuSrcChannel4_Type = Unsigned32
_TnOchGroupXcItuSrcChannel4_Object = MibTableColumn
tnOchGroupXcItuSrcChannel4 = _TnOchGroupXcItuSrcChannel4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 9),
    _TnOchGroupXcItuSrcChannel4_Type()
)
tnOchGroupXcItuSrcChannel4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuSrcChannel4.setStatus("current")
_TnOchGroupXcItuDestChannel4_Type = Unsigned32
_TnOchGroupXcItuDestChannel4_Object = MibTableColumn
tnOchGroupXcItuDestChannel4 = _TnOchGroupXcItuDestChannel4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 10),
    _TnOchGroupXcItuDestChannel4_Type()
)
tnOchGroupXcItuDestChannel4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuDestChannel4.setStatus("current")
_TnOchGroupXcItuGroupId_Type = Unsigned32
_TnOchGroupXcItuGroupId_Object = MibTableColumn
tnOchGroupXcItuGroupId = _TnOchGroupXcItuGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 11),
    _TnOchGroupXcItuGroupId_Type()
)
tnOchGroupXcItuGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuGroupId.setStatus("current")
_TnOchGroupXcItuId1_Type = Unsigned32
_TnOchGroupXcItuId1_Object = MibTableColumn
tnOchGroupXcItuId1 = _TnOchGroupXcItuId1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 12),
    _TnOchGroupXcItuId1_Type()
)
tnOchGroupXcItuId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuId1.setStatus("current")
_TnOchGroupXcItuId2_Type = Unsigned32
_TnOchGroupXcItuId2_Object = MibTableColumn
tnOchGroupXcItuId2 = _TnOchGroupXcItuId2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 13),
    _TnOchGroupXcItuId2_Type()
)
tnOchGroupXcItuId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuId2.setStatus("current")
_TnOchGroupXcItuId3_Type = Unsigned32
_TnOchGroupXcItuId3_Object = MibTableColumn
tnOchGroupXcItuId3 = _TnOchGroupXcItuId3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 14),
    _TnOchGroupXcItuId3_Type()
)
tnOchGroupXcItuId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuId3.setStatus("current")
_TnOchGroupXcItuId4_Type = Unsigned32
_TnOchGroupXcItuId4_Object = MibTableColumn
tnOchGroupXcItuId4 = _TnOchGroupXcItuId4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 15),
    _TnOchGroupXcItuId4_Type()
)
tnOchGroupXcItuId4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuId4.setStatus("current")


class _TnOchGroupXcItuName_Type(SnmpAdminString):
    """Custom type tnOchGroupXcItuName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 276),
    )


_TnOchGroupXcItuName_Type.__name__ = "SnmpAdminString"
_TnOchGroupXcItuName_Object = MibTableColumn
tnOchGroupXcItuName = _TnOchGroupXcItuName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 16),
    _TnOchGroupXcItuName_Type()
)
tnOchGroupXcItuName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuName.setStatus("current")


class _TnOchGroupXcItuBidirectional_Type(TruthValue):
    """Custom type tnOchGroupXcItuBidirectional based on TruthValue"""
    defaultValue = 1


_TnOchGroupXcItuBidirectional_Type.__name__ = "TruthValue"
_TnOchGroupXcItuBidirectional_Object = MibTableColumn
tnOchGroupXcItuBidirectional = _TnOchGroupXcItuBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 17),
    _TnOchGroupXcItuBidirectional_Type()
)
tnOchGroupXcItuBidirectional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuBidirectional.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey1AZ_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey1AZ based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey1AZ_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey1AZ_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey1AZ = _TnOchGroupXcItuEncodedWaveKey1AZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 18),
    _TnOchGroupXcItuEncodedWaveKey1AZ_Type()
)
tnOchGroupXcItuEncodedWaveKey1AZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey1AZ.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey2AZ_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey2AZ based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey2AZ_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey2AZ_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey2AZ = _TnOchGroupXcItuEncodedWaveKey2AZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 19),
    _TnOchGroupXcItuEncodedWaveKey2AZ_Type()
)
tnOchGroupXcItuEncodedWaveKey2AZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey2AZ.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey3AZ_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey3AZ based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey3AZ_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey3AZ_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey3AZ = _TnOchGroupXcItuEncodedWaveKey3AZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 20),
    _TnOchGroupXcItuEncodedWaveKey3AZ_Type()
)
tnOchGroupXcItuEncodedWaveKey3AZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey3AZ.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey4AZ_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey4AZ based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey4AZ_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey4AZ_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey4AZ = _TnOchGroupXcItuEncodedWaveKey4AZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 21),
    _TnOchGroupXcItuEncodedWaveKey4AZ_Type()
)
tnOchGroupXcItuEncodedWaveKey4AZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey4AZ.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey5AZ_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey5AZ based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey5AZ_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey5AZ_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey5AZ = _TnOchGroupXcItuEncodedWaveKey5AZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 22),
    _TnOchGroupXcItuEncodedWaveKey5AZ_Type()
)
tnOchGroupXcItuEncodedWaveKey5AZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey5AZ.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey6AZ_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey6AZ based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey6AZ_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey6AZ_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey6AZ = _TnOchGroupXcItuEncodedWaveKey6AZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 23),
    _TnOchGroupXcItuEncodedWaveKey6AZ_Type()
)
tnOchGroupXcItuEncodedWaveKey6AZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey6AZ.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey7AZ_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey7AZ based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey7AZ_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey7AZ_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey7AZ = _TnOchGroupXcItuEncodedWaveKey7AZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 24),
    _TnOchGroupXcItuEncodedWaveKey7AZ_Type()
)
tnOchGroupXcItuEncodedWaveKey7AZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey7AZ.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey8AZ_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey8AZ based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey8AZ_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey8AZ_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey8AZ = _TnOchGroupXcItuEncodedWaveKey8AZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 25),
    _TnOchGroupXcItuEncodedWaveKey8AZ_Type()
)
tnOchGroupXcItuEncodedWaveKey8AZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey8AZ.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey1ZA_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey1ZA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey1ZA_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey1ZA_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey1ZA = _TnOchGroupXcItuEncodedWaveKey1ZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 26),
    _TnOchGroupXcItuEncodedWaveKey1ZA_Type()
)
tnOchGroupXcItuEncodedWaveKey1ZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey1ZA.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey2ZA_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey2ZA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey2ZA_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey2ZA_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey2ZA = _TnOchGroupXcItuEncodedWaveKey2ZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 27),
    _TnOchGroupXcItuEncodedWaveKey2ZA_Type()
)
tnOchGroupXcItuEncodedWaveKey2ZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey2ZA.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey3ZA_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey3ZA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey3ZA_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey3ZA_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey3ZA = _TnOchGroupXcItuEncodedWaveKey3ZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 28),
    _TnOchGroupXcItuEncodedWaveKey3ZA_Type()
)
tnOchGroupXcItuEncodedWaveKey3ZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey3ZA.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey4ZA_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey4ZA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey4ZA_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey4ZA_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey4ZA = _TnOchGroupXcItuEncodedWaveKey4ZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 29),
    _TnOchGroupXcItuEncodedWaveKey4ZA_Type()
)
tnOchGroupXcItuEncodedWaveKey4ZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey4ZA.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey5ZA_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey5ZA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey5ZA_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey5ZA_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey5ZA = _TnOchGroupXcItuEncodedWaveKey5ZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 30),
    _TnOchGroupXcItuEncodedWaveKey5ZA_Type()
)
tnOchGroupXcItuEncodedWaveKey5ZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey5ZA.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey6ZA_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey6ZA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey6ZA_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey6ZA_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey6ZA = _TnOchGroupXcItuEncodedWaveKey6ZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 31),
    _TnOchGroupXcItuEncodedWaveKey6ZA_Type()
)
tnOchGroupXcItuEncodedWaveKey6ZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey6ZA.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey7ZA_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey7ZA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey7ZA_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey7ZA_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey7ZA = _TnOchGroupXcItuEncodedWaveKey7ZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 32),
    _TnOchGroupXcItuEncodedWaveKey7ZA_Type()
)
tnOchGroupXcItuEncodedWaveKey7ZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey7ZA.setStatus("current")


class _TnOchGroupXcItuEncodedWaveKey8ZA_Type(Unsigned32):
    """Custom type tnOchGroupXcItuEncodedWaveKey8ZA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TnOchGroupXcItuEncodedWaveKey8ZA_Type.__name__ = "Unsigned32"
_TnOchGroupXcItuEncodedWaveKey8ZA_Object = MibTableColumn
tnOchGroupXcItuEncodedWaveKey8ZA = _TnOchGroupXcItuEncodedWaveKey8ZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 33),
    _TnOchGroupXcItuEncodedWaveKey8ZA_Type()
)
tnOchGroupXcItuEncodedWaveKey8ZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodedWaveKey8ZA.setStatus("current")


class _TnOchGroupXcItuAutoWaveKeySelect_Type(Integer32):
    """Custom type tnOchGroupXcItuAutoWaveKeySelect based on Integer32"""
    defaultValue = 1

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
        *(("auto", 1),
          ("manual", 2),
          ("unkey", 3),
          ("unkeyAuto", 4),
          ("unkeyManual", 5))
    )


_TnOchGroupXcItuAutoWaveKeySelect_Type.__name__ = "Integer32"
_TnOchGroupXcItuAutoWaveKeySelect_Object = MibTableColumn
tnOchGroupXcItuAutoWaveKeySelect = _TnOchGroupXcItuAutoWaveKeySelect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 34),
    _TnOchGroupXcItuAutoWaveKeySelect_Type()
)
tnOchGroupXcItuAutoWaveKeySelect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuAutoWaveKeySelect.setStatus("current")


class _TnOchGroupXcItuAdminState_Type(TropicOchXcStateType):
    """Custom type tnOchGroupXcItuAdminState based on TropicOchXcStateType"""
    defaultValue = 2


_TnOchGroupXcItuAdminState_Type.__name__ = "TropicOchXcStateType"
_TnOchGroupXcItuAdminState_Object = MibTableColumn
tnOchGroupXcItuAdminState = _TnOchGroupXcItuAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 35),
    _TnOchGroupXcItuAdminState_Type()
)
tnOchGroupXcItuAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuAdminState.setStatus("current")


class _TnOchGroupXcItuProtectionState_Type(Integer32):
    """Custom type tnOchGroupXcItuProtectionState based on Integer32"""
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
          ("working", 2),
          ("protection", 3),
          ("dropContinue", 4))
    )


_TnOchGroupXcItuProtectionState_Type.__name__ = "Integer32"
_TnOchGroupXcItuProtectionState_Object = MibTableColumn
tnOchGroupXcItuProtectionState = _TnOchGroupXcItuProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 36),
    _TnOchGroupXcItuProtectionState_Type()
)
tnOchGroupXcItuProtectionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuProtectionState.setStatus("current")


class _TnOchGroupXcItuForceDeletion_Type(TruthValue):
    """Custom type tnOchGroupXcItuForceDeletion based on TruthValue"""
    defaultValue = 2


_TnOchGroupXcItuForceDeletion_Type.__name__ = "TruthValue"
_TnOchGroupXcItuForceDeletion_Object = MibTableColumn
tnOchGroupXcItuForceDeletion = _TnOchGroupXcItuForceDeletion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 37),
    _TnOchGroupXcItuForceDeletion_Type()
)
tnOchGroupXcItuForceDeletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuForceDeletion.setStatus("current")
_TnOchGroupXcItuRowStatus_Type = RowStatus
_TnOchGroupXcItuRowStatus_Object = MibTableColumn
tnOchGroupXcItuRowStatus = _TnOchGroupXcItuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 38),
    _TnOchGroupXcItuRowStatus_Type()
)
tnOchGroupXcItuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuRowStatus.setStatus("current")


class _TnOchGroupXcItuAcceptPowers_Type(Integer32):
    """Custom type tnOchGroupXcItuAcceptPowers based on Integer32"""
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
        *(("noCmd", 1),
          ("azBoth", 2),
          ("zaBoth", 3))
    )


_TnOchGroupXcItuAcceptPowers_Type.__name__ = "Integer32"
_TnOchGroupXcItuAcceptPowers_Object = MibTableColumn
tnOchGroupXcItuAcceptPowers = _TnOchGroupXcItuAcceptPowers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 39),
    _TnOchGroupXcItuAcceptPowers_Type()
)
tnOchGroupXcItuAcceptPowers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuAcceptPowers.setStatus("current")


class _TnOchGroupXcItuType_Type(Integer32):
    """Custom type tnOchGroupXcItuType based on Integer32"""
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
          ("drop", 2),
          ("thru", 3),
          ("addDrop", 4),
          ("continue", 5))
    )


_TnOchGroupXcItuType_Type.__name__ = "Integer32"
_TnOchGroupXcItuType_Object = MibTableColumn
tnOchGroupXcItuType = _TnOchGroupXcItuType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 40),
    _TnOchGroupXcItuType_Type()
)
tnOchGroupXcItuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuType.setStatus("current")


class _TnOchGroupXcItuPowerMgmtType_Type(Integer32):
    """Custom type tnOchGroupXcItuPowerMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2),
          ("hybrid", 3))
    )


_TnOchGroupXcItuPowerMgmtType_Type.__name__ = "Integer32"
_TnOchGroupXcItuPowerMgmtType_Object = MibTableColumn
tnOchGroupXcItuPowerMgmtType = _TnOchGroupXcItuPowerMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 41),
    _TnOchGroupXcItuPowerMgmtType_Type()
)
tnOchGroupXcItuPowerMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuPowerMgmtType.setStatus("current")


class _TnOchGroupXcItuUserBitRateAZ_Type(AluWdmOtuBitRate):
    """Custom type tnOchGroupXcItuUserBitRateAZ based on AluWdmOtuBitRate"""
    defaultValue = 9998


_TnOchGroupXcItuUserBitRateAZ_Type.__name__ = "AluWdmOtuBitRate"
_TnOchGroupXcItuUserBitRateAZ_Object = MibTableColumn
tnOchGroupXcItuUserBitRateAZ = _TnOchGroupXcItuUserBitRateAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 42),
    _TnOchGroupXcItuUserBitRateAZ_Type()
)
tnOchGroupXcItuUserBitRateAZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuUserBitRateAZ.setStatus("current")


class _TnOchGroupXcItuUserBitRateZA_Type(AluWdmOtuBitRate):
    """Custom type tnOchGroupXcItuUserBitRateZA based on AluWdmOtuBitRate"""
    defaultValue = 9998


_TnOchGroupXcItuUserBitRateZA_Type.__name__ = "AluWdmOtuBitRate"
_TnOchGroupXcItuUserBitRateZA_Object = MibTableColumn
tnOchGroupXcItuUserBitRateZA = _TnOchGroupXcItuUserBitRateZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 43),
    _TnOchGroupXcItuUserBitRateZA_Type()
)
tnOchGroupXcItuUserBitRateZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuUserBitRateZA.setStatus("current")


class _TnOchGroupXcItuUserEncodingAZ_Type(AluWdmOtuEncoding):
    """Custom type tnOchGroupXcItuUserEncodingAZ based on AluWdmOtuEncoding"""
    defaultValue = 9998


_TnOchGroupXcItuUserEncodingAZ_Type.__name__ = "AluWdmOtuEncoding"
_TnOchGroupXcItuUserEncodingAZ_Object = MibTableColumn
tnOchGroupXcItuUserEncodingAZ = _TnOchGroupXcItuUserEncodingAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 44),
    _TnOchGroupXcItuUserEncodingAZ_Type()
)
tnOchGroupXcItuUserEncodingAZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuUserEncodingAZ.setStatus("current")


class _TnOchGroupXcItuUserEncodingZA_Type(AluWdmOtuEncoding):
    """Custom type tnOchGroupXcItuUserEncodingZA based on AluWdmOtuEncoding"""
    defaultValue = 9998


_TnOchGroupXcItuUserEncodingZA_Type.__name__ = "AluWdmOtuEncoding"
_TnOchGroupXcItuUserEncodingZA_Object = MibTableColumn
tnOchGroupXcItuUserEncodingZA = _TnOchGroupXcItuUserEncodingZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 45),
    _TnOchGroupXcItuUserEncodingZA_Type()
)
tnOchGroupXcItuUserEncodingZA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOchGroupXcItuUserEncodingZA.setStatus("current")


class _TnOchGroupXcItuBitRateAZ_Type(AluWdmOtuBitRate):
    """Custom type tnOchGroupXcItuBitRateAZ based on AluWdmOtuBitRate"""
    defaultValue = 9998


_TnOchGroupXcItuBitRateAZ_Type.__name__ = "AluWdmOtuBitRate"
_TnOchGroupXcItuBitRateAZ_Object = MibTableColumn
tnOchGroupXcItuBitRateAZ = _TnOchGroupXcItuBitRateAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 46),
    _TnOchGroupXcItuBitRateAZ_Type()
)
tnOchGroupXcItuBitRateAZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuBitRateAZ.setStatus("current")


class _TnOchGroupXcItuBitRateZA_Type(AluWdmOtuBitRate):
    """Custom type tnOchGroupXcItuBitRateZA based on AluWdmOtuBitRate"""
    defaultValue = 9998


_TnOchGroupXcItuBitRateZA_Type.__name__ = "AluWdmOtuBitRate"
_TnOchGroupXcItuBitRateZA_Object = MibTableColumn
tnOchGroupXcItuBitRateZA = _TnOchGroupXcItuBitRateZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 47),
    _TnOchGroupXcItuBitRateZA_Type()
)
tnOchGroupXcItuBitRateZA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuBitRateZA.setStatus("current")


class _TnOchGroupXcItuEncodingAZ_Type(AluWdmOtuEncoding):
    """Custom type tnOchGroupXcItuEncodingAZ based on AluWdmOtuEncoding"""
    defaultValue = 9998


_TnOchGroupXcItuEncodingAZ_Type.__name__ = "AluWdmOtuEncoding"
_TnOchGroupXcItuEncodingAZ_Object = MibTableColumn
tnOchGroupXcItuEncodingAZ = _TnOchGroupXcItuEncodingAZ_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 48),
    _TnOchGroupXcItuEncodingAZ_Type()
)
tnOchGroupXcItuEncodingAZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodingAZ.setStatus("current")


class _TnOchGroupXcItuEncodingZA_Type(AluWdmOtuEncoding):
    """Custom type tnOchGroupXcItuEncodingZA based on AluWdmOtuEncoding"""
    defaultValue = 9998


_TnOchGroupXcItuEncodingZA_Type.__name__ = "AluWdmOtuEncoding"
_TnOchGroupXcItuEncodingZA_Object = MibTableColumn
tnOchGroupXcItuEncodingZA = _TnOchGroupXcItuEncodingZA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 49),
    _TnOchGroupXcItuEncodingZA_Type()
)
tnOchGroupXcItuEncodingZA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuEncodingZA.setStatus("current")


class _TnOchGroupXcItuPortIsInUseBySap_Type(TruthValue):
    """Custom type tnOchGroupXcItuPortIsInUseBySap based on TruthValue"""
    defaultValue = 2


_TnOchGroupXcItuPortIsInUseBySap_Type.__name__ = "TruthValue"
_TnOchGroupXcItuPortIsInUseBySap_Object = MibTableColumn
tnOchGroupXcItuPortIsInUseBySap = _TnOchGroupXcItuPortIsInUseBySap_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 5, 1, 50),
    _TnOchGroupXcItuPortIsInUseBySap_Type()
)
tnOchGroupXcItuPortIsInUseBySap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuPortIsInUseBySap.setStatus("current")
_TnOchGroupXcItuIdTable_Object = MibTable
tnOchGroupXcItuIdTable = _TnOchGroupXcItuIdTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnOchGroupXcItuIdTable.setStatus("current")
_TnOchGroupXcItuIdEntry_Object = MibTableRow
tnOchGroupXcItuIdEntry = _TnOchGroupXcItuIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 6, 1)
)
tnOchGroupXcItuIdEntry.setIndexNames(
    (0, "TROPIC-OCH-MIB", "tnOchGroupXcItuGroupId"),
)
if mibBuilder.loadTexts:
    tnOchGroupXcItuIdEntry.setStatus("current")
_TnOchGroupXcItuIdSrcIfIndex_Type = InterfaceIndex
_TnOchGroupXcItuIdSrcIfIndex_Object = MibTableColumn
tnOchGroupXcItuIdSrcIfIndex = _TnOchGroupXcItuIdSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 6, 1, 1),
    _TnOchGroupXcItuIdSrcIfIndex_Type()
)
tnOchGroupXcItuIdSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuIdSrcIfIndex.setStatus("current")
_TnOchGroupXcItuIdSrcChannel1_Type = Unsigned32
_TnOchGroupXcItuIdSrcChannel1_Object = MibTableColumn
tnOchGroupXcItuIdSrcChannel1 = _TnOchGroupXcItuIdSrcChannel1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 6, 1, 2),
    _TnOchGroupXcItuIdSrcChannel1_Type()
)
tnOchGroupXcItuIdSrcChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuIdSrcChannel1.setStatus("current")
_TnOchGroupXcItuIdDestIfIndex_Type = InterfaceIndex
_TnOchGroupXcItuIdDestIfIndex_Object = MibTableColumn
tnOchGroupXcItuIdDestIfIndex = _TnOchGroupXcItuIdDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 6, 1, 3),
    _TnOchGroupXcItuIdDestIfIndex_Type()
)
tnOchGroupXcItuIdDestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuIdDestIfIndex.setStatus("current")
_TnOchGroupXcItuIdDestChannel1_Type = Unsigned32
_TnOchGroupXcItuIdDestChannel1_Object = MibTableColumn
tnOchGroupXcItuIdDestChannel1 = _TnOchGroupXcItuIdDestChannel1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 2, 1, 6, 1, 4),
    _TnOchGroupXcItuIdDestChannel1_Type()
)
tnOchGroupXcItuIdDestChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOchGroupXcItuIdDestChannel1.setStatus("current")

# Managed Objects groups

tnOchTrailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 1, 1, 2)
)
tnOchTrailGroup.setObjects(
      *(("TROPIC-OCH-MIB", "tnOchTrailName"),
        ("TROPIC-OCH-MIB", "tnOchTrailWaveKey1"),
        ("TROPIC-OCH-MIB", "tnOchTrailWaveKey2"),
        ("TROPIC-OCH-MIB", "tnOchTrailITUChannel"),
        ("TROPIC-OCH-MIB", "tnOchTrailItuBitRate"),
        ("TROPIC-OCH-MIB", "tnOchTrailItuEncoding"),
        ("TROPIC-OCH-MIB", "tnOchTrailItuSrcOTType"),
        ("TROPIC-OCH-MIB", "tnOchTrailEncoderDomain"),
        ("TROPIC-OCH-MIB", "tnOchTrailWaveKeyDupsUnlocked"),
        ("TROPIC-OCH-MIB", "tnOchTrailEncoderDomainProt"),
        ("TROPIC-OCH-MIB", "tnOchTrailWaveKeyDupsUnlockedProt"),
        ("TROPIC-OCH-MIB", "tnOchTrailItuSpectralWidth"))
)
if mibBuilder.loadTexts:
    tnOchTrailGroup.setStatus("current")

tnOchXcItuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 1, 1, 3)
)
tnOchXcItuGroup.setObjects(
      *(("TROPIC-OCH-MIB", "tnOchXcItuId"),
        ("TROPIC-OCH-MIB", "tnOchXcItuName"),
        ("TROPIC-OCH-MIB", "tnOchXcItuBidirectional"),
        ("TROPIC-OCH-MIB", "tnOchXcItuEncodedWaveKey1AZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuEncodedWaveKey2AZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuEncodedWaveKey1ZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuEncodedWaveKey2ZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuAutoWaveKeySelect"),
        ("TROPIC-OCH-MIB", "tnOchXcItuAdminState"),
        ("TROPIC-OCH-MIB", "tnOchXcItuOperState"),
        ("TROPIC-OCH-MIB", "tnOchXcItuStateQualifier"),
        ("TROPIC-OCH-MIB", "tnOchXcItuProtectionState"),
        ("TROPIC-OCH-MIB", "tnOchXcItuForceDeletion"),
        ("TROPIC-OCH-MIB", "tnOchXcItuRowStatus"),
        ("TROPIC-OCH-MIB", "tnOchXcItuAcceptPowers"),
        ("TROPIC-OCH-MIB", "tnOchXcItuOperCapability"),
        ("TROPIC-OCH-MIB", "tnOchXcItuType"),
        ("TROPIC-OCH-MIB", "tnOchXcItuPowerMgmtType"),
        ("TROPIC-OCH-MIB", "tnOchXcItuTopology"),
        ("TROPIC-OCH-MIB", "tnOchXcItuTopologyZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuBitRateAZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuBitRateZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuEncodingAZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuEncodingZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuUserBitRateAZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuUserBitRateZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuUserEncodingAZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuUserEncodingZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuWaveKeySelectPreference"),
        ("TROPIC-OCH-MIB", "tnOchXcItuEncoderDomainAZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuEncoderDomainZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuWaveKeyDupsUnlockedAZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuWaveKeyDupsUnlockedZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuRekeyWithDuplicatesAllowed"),
        ("TROPIC-OCH-MIB", "tnOchXcItuEncoderDomainProtectAZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuEncoderDomainProtectZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuWaveKeyDupsUnlockedProtectAZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuWaveKeyDupsUnlockedProtectZA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuSpectralWidth"),
        ("TROPIC-OCH-MIB", "tnOchXcItuAseControlMode"),
        ("TROPIC-OCH-MIB", "tnOchXcItuRxBlkByLOSAtoZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuAseFilledAtoZ"),
        ("TROPIC-OCH-MIB", "tnOchXcItuRxBlkByLOSZtoA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuAseFilledZtoA"),
        ("TROPIC-OCH-MIB", "tnOchXcItuAseGuardBandMHz"),
        ("TROPIC-OCH-MIB", "tnOchXcItuPurpose"),
        ("TROPIC-OCH-MIB", "tnOchXcItuAsonId"))
)
if mibBuilder.loadTexts:
    tnOchXcItuGroup.setStatus("current")

tnOchXcItuIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 1, 1, 4)
)
tnOchXcItuIdGroup.setObjects(
      *(("TROPIC-OCH-MIB", "tnOchXcItuIdSrcIfIndex"),
        ("TROPIC-OCH-MIB", "tnOchXcItuIdSrcChannel"),
        ("TROPIC-OCH-MIB", "tnOchXcItuIdDestIfIndex"),
        ("TROPIC-OCH-MIB", "tnOchXcItuIdDestChannel"))
)
if mibBuilder.loadTexts:
    tnOchXcItuIdGroup.setStatus("current")

tnOchGroupXcItuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 1, 1, 5)
)
tnOchGroupXcItuGroup.setObjects(
      *(("TROPIC-OCH-MIB", "tnOchGroupXcItuSrcChannel2"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuDestChannel2"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuSrcChannel3"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuDestChannel3"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuSrcChannel4"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuDestChannel4"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuGroupId"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuId1"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuId2"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuId3"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuId4"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuName"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuBidirectional"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey1AZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey2AZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey3AZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey4AZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey5AZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey6AZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey7AZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey8AZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey1ZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey2ZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey3ZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey4ZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey5ZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey6ZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey7ZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodedWaveKey8ZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuAutoWaveKeySelect"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuAdminState"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuProtectionState"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuForceDeletion"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuRowStatus"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuAcceptPowers"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuType"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuPowerMgmtType"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuUserBitRateAZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuUserBitRateZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuUserEncodingAZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuUserEncodingZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuBitRateAZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuBitRateZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodingAZ"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuEncodingZA"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuPortIsInUseBySap"))
)
if mibBuilder.loadTexts:
    tnOchGroupXcItuGroup.setStatus("current")

tnOchGroupXcItuIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 1, 1, 6)
)
tnOchGroupXcItuIdGroup.setObjects(
      *(("TROPIC-OCH-MIB", "tnOchGroupXcItuIdSrcIfIndex"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuIdSrcChannel1"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuIdDestIfIndex"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuIdDestChannel1"))
)
if mibBuilder.loadTexts:
    tnOchGroupXcItuIdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnOchCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5, 1, 2, 1)
)
tnOchCompliance.setObjects(
      *(("TROPIC-OCH-MIB", "tnOchTrailGroup"),
        ("TROPIC-OCH-MIB", "tnOchXcItuGroup"),
        ("TROPIC-OCH-MIB", "tnOchXcItuIdGroup"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuGroup"),
        ("TROPIC-OCH-MIB", "tnOchGroupXcItuIdGroup"))
)
if mibBuilder.loadTexts:
    tnOchCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-OCH-MIB",
    **{"TropicOchXcStateType": TropicOchXcStateType,
       "TropicOchXcStateQualifierType": TropicOchXcStateQualifierType,
       "tnOchMibModule": tnOchMibModule,
       "tnOchConf": tnOchConf,
       "tnOchGroups": tnOchGroups,
       "tnOchTrailGroup": tnOchTrailGroup,
       "tnOchXcItuGroup": tnOchXcItuGroup,
       "tnOchXcItuIdGroup": tnOchXcItuIdGroup,
       "tnOchGroupXcItuGroup": tnOchGroupXcItuGroup,
       "tnOchGroupXcItuIdGroup": tnOchGroupXcItuIdGroup,
       "tnOchCompliances": tnOchCompliances,
       "tnOchCompliance": tnOchCompliance,
       "tnOchObjs": tnOchObjs,
       "tnOchBasics": tnOchBasics,
       "tnOchTrailTable": tnOchTrailTable,
       "tnOchTrailEntry": tnOchTrailEntry,
       "tnOchTrailIpAddress": tnOchTrailIpAddress,
       "tnOchTrailifIndex": tnOchTrailifIndex,
       "tnOchTrailName": tnOchTrailName,
       "tnOchTrailWaveKey1": tnOchTrailWaveKey1,
       "tnOchTrailWaveKey2": tnOchTrailWaveKey2,
       "tnOchTrailITUChannel": tnOchTrailITUChannel,
       "tnOchTrailItuBitRate": tnOchTrailItuBitRate,
       "tnOchTrailItuEncoding": tnOchTrailItuEncoding,
       "tnOchTrailItuSrcOTType": tnOchTrailItuSrcOTType,
       "tnOchTrailEncoderDomain": tnOchTrailEncoderDomain,
       "tnOchTrailWaveKeyDupsUnlocked": tnOchTrailWaveKeyDupsUnlocked,
       "tnOchTrailEncoderDomainProt": tnOchTrailEncoderDomainProt,
       "tnOchTrailWaveKeyDupsUnlockedProt": tnOchTrailWaveKeyDupsUnlockedProt,
       "tnOchTrailItuSpectralWidth": tnOchTrailItuSpectralWidth,
       "tnOchXcItuTable": tnOchXcItuTable,
       "tnOchXcItuEntry": tnOchXcItuEntry,
       "tnOchXcItuSrcIfIndex": tnOchXcItuSrcIfIndex,
       "tnOchXcItuSrcChannel": tnOchXcItuSrcChannel,
       "tnOchXcItuDestIfIndex": tnOchXcItuDestIfIndex,
       "tnOchXcItuDestChannel": tnOchXcItuDestChannel,
       "tnOchXcItuId": tnOchXcItuId,
       "tnOchXcItuName": tnOchXcItuName,
       "tnOchXcItuBidirectional": tnOchXcItuBidirectional,
       "tnOchXcItuEncodedWaveKey1AZ": tnOchXcItuEncodedWaveKey1AZ,
       "tnOchXcItuEncodedWaveKey2AZ": tnOchXcItuEncodedWaveKey2AZ,
       "tnOchXcItuEncodedWaveKey1ZA": tnOchXcItuEncodedWaveKey1ZA,
       "tnOchXcItuEncodedWaveKey2ZA": tnOchXcItuEncodedWaveKey2ZA,
       "tnOchXcItuAutoWaveKeySelect": tnOchXcItuAutoWaveKeySelect,
       "tnOchXcItuAdminState": tnOchXcItuAdminState,
       "tnOchXcItuOperState": tnOchXcItuOperState,
       "tnOchXcItuStateQualifier": tnOchXcItuStateQualifier,
       "tnOchXcItuProtectionState": tnOchXcItuProtectionState,
       "tnOchXcItuForceDeletion": tnOchXcItuForceDeletion,
       "tnOchXcItuRowStatus": tnOchXcItuRowStatus,
       "tnOchXcItuAcceptPowers": tnOchXcItuAcceptPowers,
       "tnOchXcItuOperCapability": tnOchXcItuOperCapability,
       "tnOchXcItuType": tnOchXcItuType,
       "tnOchXcItuPowerMgmtType": tnOchXcItuPowerMgmtType,
       "tnOchXcItuTopology": tnOchXcItuTopology,
       "tnOchXcItuTopologyZA": tnOchXcItuTopologyZA,
       "tnOchXcItuBitRateAZ": tnOchXcItuBitRateAZ,
       "tnOchXcItuBitRateZA": tnOchXcItuBitRateZA,
       "tnOchXcItuEncodingAZ": tnOchXcItuEncodingAZ,
       "tnOchXcItuEncodingZA": tnOchXcItuEncodingZA,
       "tnOchXcItuUserBitRateAZ": tnOchXcItuUserBitRateAZ,
       "tnOchXcItuUserBitRateZA": tnOchXcItuUserBitRateZA,
       "tnOchXcItuUserEncodingAZ": tnOchXcItuUserEncodingAZ,
       "tnOchXcItuUserEncodingZA": tnOchXcItuUserEncodingZA,
       "tnOchXcItuWaveKeySelectPreference": tnOchXcItuWaveKeySelectPreference,
       "tnOchXcItuEncoderDomainAZ": tnOchXcItuEncoderDomainAZ,
       "tnOchXcItuEncoderDomainZA": tnOchXcItuEncoderDomainZA,
       "tnOchXcItuWaveKeyDupsUnlockedAZ": tnOchXcItuWaveKeyDupsUnlockedAZ,
       "tnOchXcItuWaveKeyDupsUnlockedZA": tnOchXcItuWaveKeyDupsUnlockedZA,
       "tnOchXcItuRekeyWithDuplicatesAllowed": tnOchXcItuRekeyWithDuplicatesAllowed,
       "tnOchXcItuEncoderDomainProtectAZ": tnOchXcItuEncoderDomainProtectAZ,
       "tnOchXcItuEncoderDomainProtectZA": tnOchXcItuEncoderDomainProtectZA,
       "tnOchXcItuWaveKeyDupsUnlockedProtectAZ": tnOchXcItuWaveKeyDupsUnlockedProtectAZ,
       "tnOchXcItuWaveKeyDupsUnlockedProtectZA": tnOchXcItuWaveKeyDupsUnlockedProtectZA,
       "tnOchXcItuSpectralWidth": tnOchXcItuSpectralWidth,
       "tnOchXcItuAseControlMode": tnOchXcItuAseControlMode,
       "tnOchXcItuRxBlkByLOSAtoZ": tnOchXcItuRxBlkByLOSAtoZ,
       "tnOchXcItuAseFilledAtoZ": tnOchXcItuAseFilledAtoZ,
       "tnOchXcItuRxBlkByLOSZtoA": tnOchXcItuRxBlkByLOSZtoA,
       "tnOchXcItuAseFilledZtoA": tnOchXcItuAseFilledZtoA,
       "tnOchXcItuAseGuardBandMHz": tnOchXcItuAseGuardBandMHz,
       "tnOchXcItuPurpose": tnOchXcItuPurpose,
       "tnOchXcItuAsonId": tnOchXcItuAsonId,
       "tnOchXcItuIdTable": tnOchXcItuIdTable,
       "tnOchXcItuIdEntry": tnOchXcItuIdEntry,
       "tnOchXcItuIdSrcIfIndex": tnOchXcItuIdSrcIfIndex,
       "tnOchXcItuIdSrcChannel": tnOchXcItuIdSrcChannel,
       "tnOchXcItuIdDestIfIndex": tnOchXcItuIdDestIfIndex,
       "tnOchXcItuIdDestChannel": tnOchXcItuIdDestChannel,
       "tnOchGroupXcItuTable": tnOchGroupXcItuTable,
       "tnOchGroupXcItuEntry": tnOchGroupXcItuEntry,
       "tnOchGroupXcItuSrcIfIndex": tnOchGroupXcItuSrcIfIndex,
       "tnOchGroupXcItuSrcChannel1": tnOchGroupXcItuSrcChannel1,
       "tnOchGroupXcItuDestIfIndex": tnOchGroupXcItuDestIfIndex,
       "tnOchGroupXcItuDestChannel1": tnOchGroupXcItuDestChannel1,
       "tnOchGroupXcItuSrcChannel2": tnOchGroupXcItuSrcChannel2,
       "tnOchGroupXcItuDestChannel2": tnOchGroupXcItuDestChannel2,
       "tnOchGroupXcItuSrcChannel3": tnOchGroupXcItuSrcChannel3,
       "tnOchGroupXcItuDestChannel3": tnOchGroupXcItuDestChannel3,
       "tnOchGroupXcItuSrcChannel4": tnOchGroupXcItuSrcChannel4,
       "tnOchGroupXcItuDestChannel4": tnOchGroupXcItuDestChannel4,
       "tnOchGroupXcItuGroupId": tnOchGroupXcItuGroupId,
       "tnOchGroupXcItuId1": tnOchGroupXcItuId1,
       "tnOchGroupXcItuId2": tnOchGroupXcItuId2,
       "tnOchGroupXcItuId3": tnOchGroupXcItuId3,
       "tnOchGroupXcItuId4": tnOchGroupXcItuId4,
       "tnOchGroupXcItuName": tnOchGroupXcItuName,
       "tnOchGroupXcItuBidirectional": tnOchGroupXcItuBidirectional,
       "tnOchGroupXcItuEncodedWaveKey1AZ": tnOchGroupXcItuEncodedWaveKey1AZ,
       "tnOchGroupXcItuEncodedWaveKey2AZ": tnOchGroupXcItuEncodedWaveKey2AZ,
       "tnOchGroupXcItuEncodedWaveKey3AZ": tnOchGroupXcItuEncodedWaveKey3AZ,
       "tnOchGroupXcItuEncodedWaveKey4AZ": tnOchGroupXcItuEncodedWaveKey4AZ,
       "tnOchGroupXcItuEncodedWaveKey5AZ": tnOchGroupXcItuEncodedWaveKey5AZ,
       "tnOchGroupXcItuEncodedWaveKey6AZ": tnOchGroupXcItuEncodedWaveKey6AZ,
       "tnOchGroupXcItuEncodedWaveKey7AZ": tnOchGroupXcItuEncodedWaveKey7AZ,
       "tnOchGroupXcItuEncodedWaveKey8AZ": tnOchGroupXcItuEncodedWaveKey8AZ,
       "tnOchGroupXcItuEncodedWaveKey1ZA": tnOchGroupXcItuEncodedWaveKey1ZA,
       "tnOchGroupXcItuEncodedWaveKey2ZA": tnOchGroupXcItuEncodedWaveKey2ZA,
       "tnOchGroupXcItuEncodedWaveKey3ZA": tnOchGroupXcItuEncodedWaveKey3ZA,
       "tnOchGroupXcItuEncodedWaveKey4ZA": tnOchGroupXcItuEncodedWaveKey4ZA,
       "tnOchGroupXcItuEncodedWaveKey5ZA": tnOchGroupXcItuEncodedWaveKey5ZA,
       "tnOchGroupXcItuEncodedWaveKey6ZA": tnOchGroupXcItuEncodedWaveKey6ZA,
       "tnOchGroupXcItuEncodedWaveKey7ZA": tnOchGroupXcItuEncodedWaveKey7ZA,
       "tnOchGroupXcItuEncodedWaveKey8ZA": tnOchGroupXcItuEncodedWaveKey8ZA,
       "tnOchGroupXcItuAutoWaveKeySelect": tnOchGroupXcItuAutoWaveKeySelect,
       "tnOchGroupXcItuAdminState": tnOchGroupXcItuAdminState,
       "tnOchGroupXcItuProtectionState": tnOchGroupXcItuProtectionState,
       "tnOchGroupXcItuForceDeletion": tnOchGroupXcItuForceDeletion,
       "tnOchGroupXcItuRowStatus": tnOchGroupXcItuRowStatus,
       "tnOchGroupXcItuAcceptPowers": tnOchGroupXcItuAcceptPowers,
       "tnOchGroupXcItuType": tnOchGroupXcItuType,
       "tnOchGroupXcItuPowerMgmtType": tnOchGroupXcItuPowerMgmtType,
       "tnOchGroupXcItuUserBitRateAZ": tnOchGroupXcItuUserBitRateAZ,
       "tnOchGroupXcItuUserBitRateZA": tnOchGroupXcItuUserBitRateZA,
       "tnOchGroupXcItuUserEncodingAZ": tnOchGroupXcItuUserEncodingAZ,
       "tnOchGroupXcItuUserEncodingZA": tnOchGroupXcItuUserEncodingZA,
       "tnOchGroupXcItuBitRateAZ": tnOchGroupXcItuBitRateAZ,
       "tnOchGroupXcItuBitRateZA": tnOchGroupXcItuBitRateZA,
       "tnOchGroupXcItuEncodingAZ": tnOchGroupXcItuEncodingAZ,
       "tnOchGroupXcItuEncodingZA": tnOchGroupXcItuEncodingZA,
       "tnOchGroupXcItuPortIsInUseBySap": tnOchGroupXcItuPortIsInUseBySap,
       "tnOchGroupXcItuIdTable": tnOchGroupXcItuIdTable,
       "tnOchGroupXcItuIdEntry": tnOchGroupXcItuIdEntry,
       "tnOchGroupXcItuIdSrcIfIndex": tnOchGroupXcItuIdSrcIfIndex,
       "tnOchGroupXcItuIdSrcChannel1": tnOchGroupXcItuIdSrcChannel1,
       "tnOchGroupXcItuIdDestIfIndex": tnOchGroupXcItuIdDestIfIndex,
       "tnOchGroupXcItuIdDestChannel1": tnOchGroupXcItuIdDestChannel1}
)
