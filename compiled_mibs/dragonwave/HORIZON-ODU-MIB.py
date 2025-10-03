# SNMP MIB module (HORIZON-ODU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dragonwave\HORIZON-ODU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:32 2025
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

(horizon,) = mibBuilder.importSymbols(
    "HORIZON-MIB",
    "horizon")

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmp,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp")

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


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HorizonOdu_ObjectIdentity = ObjectIdentity
horizonOdu = _HorizonOdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2)
)
_HzOduSystem_ObjectIdentity = ObjectIdentity
hzOduSystem = _HzOduSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1)
)
_HzOduSysGeneral_ObjectIdentity = ObjectIdentity
hzOduSysGeneral = _HzOduSysGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 1)
)


class _HzOduResetSystem_Type(Integer32):
    """Custom type hzOduResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HzOduResetSystem_Type.__name__ = "Integer32"
_HzOduResetSystem_Object = MibScalar
hzOduResetSystem = _HzOduResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 1, 1),
    _HzOduResetSystem_Type()
)
hzOduResetSystem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzOduResetSystem.setStatus("mandatory")


class _HzOduSaveMIB_Type(Integer32):
    """Custom type hzOduSaveMIB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_HzOduSaveMIB_Type.__name__ = "Integer32"
_HzOduSaveMIB_Object = MibScalar
hzOduSaveMIB = _HzOduSaveMIB_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 1, 2),
    _HzOduSaveMIB_Type()
)
hzOduSaveMIB.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzOduSaveMIB.setStatus("mandatory")


class _HzOduOperStatus_Type(Integer32):
    """Custom type hzOduOperStatus based on Integer32"""
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
          ("testing", 3))
    )


_HzOduOperStatus_Type.__name__ = "Integer32"
_HzOduOperStatus_Object = MibScalar
hzOduOperStatus = _HzOduOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 1, 3),
    _HzOduOperStatus_Type()
)
hzOduOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduOperStatus.setStatus("mandatory")


class _HzOduAirInterfaceEncryption_Type(Integer32):
    """Custom type hzOduAirInterfaceEncryption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduAirInterfaceEncryption_Type.__name__ = "Integer32"
_HzOduAirInterfaceEncryption_Object = MibScalar
hzOduAirInterfaceEncryption = _HzOduAirInterfaceEncryption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 1, 4),
    _HzOduAirInterfaceEncryption_Type()
)
hzOduAirInterfaceEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduAirInterfaceEncryption.setStatus("mandatory")


class _HzOduSystemRedundancy_Type(Integer32):
    """Custom type hzOduSystemRedundancy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduSystemRedundancy_Type.__name__ = "Integer32"
_HzOduSystemRedundancy_Object = MibScalar
hzOduSystemRedundancy = _HzOduSystemRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 1, 5),
    _HzOduSystemRedundancy_Type()
)
hzOduSystemRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduSystemRedundancy.setStatus("mandatory")
_HzOduSysSpeed_ObjectIdentity = ObjectIdentity
hzOduSysSpeed = _HzOduSysSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 2)
)


class _HzOduSystemCurrentSpeed_Type(Integer32):
    """Custom type hzOduSystemCurrentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HzOduSystemCurrentSpeed_Type.__name__ = "Integer32"
_HzOduSystemCurrentSpeed_Object = MibScalar
hzOduSystemCurrentSpeed = _HzOduSystemCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 2, 1),
    _HzOduSystemCurrentSpeed_Type()
)
hzOduSystemCurrentSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduSystemCurrentSpeed.setStatus("mandatory")


class _HzOduSystemLicensedSpeed_Type(Integer32):
    """Custom type hzOduSystemLicensedSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HzOduSystemLicensedSpeed_Type.__name__ = "Integer32"
_HzOduSystemLicensedSpeed_Object = MibScalar
hzOduSystemLicensedSpeed = _HzOduSystemLicensedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 2, 2),
    _HzOduSystemLicensedSpeed_Type()
)
hzOduSystemLicensedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSystemLicensedSpeed.setStatus("mandatory")


class _HzOduSystemMode_Type(Integer32):
    """Custom type hzOduSystemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("cw-test", 1),
          ("hc50-67-qpsk", 5),
          ("hc50-110-16qam", 6),
          ("hc50-171-32qam", 7),
          ("hc50-215-64QAM", 8),
          ("hc50-271-128qam", 9),
          ("hc50-322-256qam", 10),
          ("hc50-371-256qam", 11),
          ("hc56-65-qpsk", 12),
          ("hc56-111-16qam", 13),
          ("hc56-216-32qam", 14),
          ("hc56-290-128qam", 15),
          ("hc56-385-256qam", 16),
          ("hc28-37-qpsk", 17),
          ("hc28-48-qpsk", 18),
          ("hc28-71-16qam", 19),
          ("hc28-100-32qam", 20),
          ("hc28-144-128qam", 21),
          ("hc28-190-256qam", 22),
          ("hc14-23-qpsk", 23),
          ("hc14-36-16qam", 24),
          ("hc14-47-32qam", 25),
          ("hc14-70-128qam", 26),
          ("hc14-95-256qam", 27),
          ("hc40-57-qpsk", 28),
          ("hc40-111-16qam", 29),
          ("hc30-107-32qam", 30),
          ("hc40-110-32qam", 31),
          ("hc40-142-32qam", 32),
          ("hc40-181-64qam", 33),
          ("hc30-165-128qam", 34),
          ("hc40-200-128qam", 35),
          ("hc40-212-128qam", 36),
          ("hc30-212-256qam", 37),
          ("hc40-277-256qam", 38),
          ("hc40-58-qpsk", 39),
          ("hc25-33-qpsk", 40),
          ("hc25-53-16qam", 41),
          ("hc25-80-32qam", 42),
          ("hc25-107-128qam", 43),
          ("hc25-174-256qam", 44),
          ("hc50-364-256qam", 45))
    )


_HzOduSystemMode_Type.__name__ = "Integer32"
_HzOduSystemMode_Object = MibScalar
hzOduSystemMode = _HzOduSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 2, 3),
    _HzOduSystemMode_Type()
)
hzOduSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSystemMode.setStatus("mandatory")
_HzOduUpgradeLicensedSpeed_Type = DisplayString
_HzOduUpgradeLicensedSpeed_Object = MibScalar
hzOduUpgradeLicensedSpeed = _HzOduUpgradeLicensedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 2, 4),
    _HzOduUpgradeLicensedSpeed_Type()
)
hzOduUpgradeLicensedSpeed.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzOduUpgradeLicensedSpeed.setStatus("mandatory")
_HzOduInventory_ObjectIdentity = ObjectIdentity
hzOduInventory = _HzOduInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3)
)
_HzOduHwInventory_ObjectIdentity = ObjectIdentity
hzOduHwInventory = _HzOduHwInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1)
)
_HzOduUnitSerialNo_Type = DisplayString
_HzOduUnitSerialNo_Object = MibScalar
hzOduUnitSerialNo = _HzOduUnitSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1, 1),
    _HzOduUnitSerialNo_Type()
)
hzOduUnitSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduUnitSerialNo.setStatus("mandatory")
_HzOduUnitAssemblylNo_Type = DisplayString
_HzOduUnitAssemblylNo_Object = MibScalar
hzOduUnitAssemblylNo = _HzOduUnitAssemblylNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1, 2),
    _HzOduUnitAssemblylNo_Type()
)
hzOduUnitAssemblylNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduUnitAssemblylNo.setStatus("mandatory")
_HzOduIfSerialNo_Type = DisplayString
_HzOduIfSerialNo_Object = MibScalar
hzOduIfSerialNo = _HzOduIfSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1, 3),
    _HzOduIfSerialNo_Type()
)
hzOduIfSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduIfSerialNo.setStatus("mandatory")
_HzOduIfAssemblylNo_Type = DisplayString
_HzOduIfAssemblylNo_Object = MibScalar
hzOduIfAssemblylNo = _HzOduIfAssemblylNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1, 4),
    _HzOduIfAssemblylNo_Type()
)
hzOduIfAssemblylNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduIfAssemblylNo.setStatus("mandatory")
_HzOduRfSerialNo_Type = DisplayString
_HzOduRfSerialNo_Object = MibScalar
hzOduRfSerialNo = _HzOduRfSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1, 5),
    _HzOduRfSerialNo_Type()
)
hzOduRfSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRfSerialNo.setStatus("mandatory")
_HzOduRfAssemblylNo_Type = DisplayString
_HzOduRfAssemblylNo_Object = MibScalar
hzOduRfAssemblylNo = _HzOduRfAssemblylNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1, 6),
    _HzOduRfAssemblylNo_Type()
)
hzOduRfAssemblylNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRfAssemblylNo.setStatus("mandatory")
_HzOduNccSerialNo_Type = DisplayString
_HzOduNccSerialNo_Object = MibScalar
hzOduNccSerialNo = _HzOduNccSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1, 7),
    _HzOduNccSerialNo_Type()
)
hzOduNccSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduNccSerialNo.setStatus("mandatory")
_HzOduNccAssemblylNo_Type = DisplayString
_HzOduNccAssemblylNo_Object = MibScalar
hzOduNccAssemblylNo = _HzOduNccAssemblylNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1, 8),
    _HzOduNccAssemblylNo_Type()
)
hzOduNccAssemblylNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduNccAssemblylNo.setStatus("mandatory")
_HzOduDiplexerSerialNo_Type = DisplayString
_HzOduDiplexerSerialNo_Object = MibScalar
hzOduDiplexerSerialNo = _HzOduDiplexerSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1, 9),
    _HzOduDiplexerSerialNo_Type()
)
hzOduDiplexerSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduDiplexerSerialNo.setStatus("mandatory")
_HzOduDiplexerAssemblylNo_Type = DisplayString
_HzOduDiplexerAssemblylNo_Object = MibScalar
hzOduDiplexerAssemblylNo = _HzOduDiplexerAssemblylNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 1, 10),
    _HzOduDiplexerAssemblylNo_Type()
)
hzOduDiplexerAssemblylNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduDiplexerAssemblylNo.setStatus("mandatory")
_HzOduSwInventory_ObjectIdentity = ObjectIdentity
hzOduSwInventory = _HzOduSwInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 2)
)
_HzOduSystemOmniVersionNo_Type = DisplayString
_HzOduSystemOmniVersionNo_Object = MibScalar
hzOduSystemOmniVersionNo = _HzOduSystemOmniVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 2, 1),
    _HzOduSystemOmniVersionNo_Type()
)
hzOduSystemOmniVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSystemOmniVersionNo.setStatus("mandatory")
_HzOduModemOmniVersionNo_Type = DisplayString
_HzOduModemOmniVersionNo_Object = MibScalar
hzOduModemOmniVersionNo = _HzOduModemOmniVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 2, 2),
    _HzOduModemOmniVersionNo_Type()
)
hzOduModemOmniVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModemOmniVersionNo.setStatus("mandatory")
_HzOduFrequencyFileVersionNo_Type = DisplayString
_HzOduFrequencyFileVersionNo_Object = MibScalar
hzOduFrequencyFileVersionNo = _HzOduFrequencyFileVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 2, 3),
    _HzOduFrequencyFileVersionNo_Type()
)
hzOduFrequencyFileVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduFrequencyFileVersionNo.setStatus("mandatory")
_HzOduMibVersionNo_Type = DisplayString
_HzOduMibVersionNo_Object = MibScalar
hzOduMibVersionNo = _HzOduMibVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 3, 2, 4),
    _HzOduMibVersionNo_Type()
)
hzOduMibVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduMibVersionNo.setStatus("mandatory")
_HzOduAtpc_ObjectIdentity = ObjectIdentity
hzOduAtpc = _HzOduAtpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 4)
)


class _HzOduAtpcEnable_Type(Integer32):
    """Custom type hzOduAtpcEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduAtpcEnable_Type.__name__ = "Integer32"
_HzOduAtpcEnable_Object = MibScalar
hzOduAtpcEnable = _HzOduAtpcEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 4, 1),
    _HzOduAtpcEnable_Type()
)
hzOduAtpcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduAtpcEnable.setStatus("mandatory")


class _HzOduAtpcCoordinatedPowerDbm_Type(Integer32):
    """Custom type hzOduAtpcCoordinatedPowerDbm based on Integer32"""
    defaultValue = 0


_HzOduAtpcCoordinatedPowerDbm_Type.__name__ = "Integer32"
_HzOduAtpcCoordinatedPowerDbm_Object = MibScalar
hzOduAtpcCoordinatedPowerDbm = _HzOduAtpcCoordinatedPowerDbm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 4, 2),
    _HzOduAtpcCoordinatedPowerDbm_Type()
)
hzOduAtpcCoordinatedPowerDbm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduAtpcCoordinatedPowerDbm.setStatus("mandatory")
_HzOduAam_ObjectIdentity = ObjectIdentity
hzOduAam = _HzOduAam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 5)
)


class _HzOduAamEnable_Type(Integer32):
    """Custom type hzOduAamEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduAamEnable_Type.__name__ = "Integer32"
_HzOduAamEnable_Object = MibScalar
hzOduAamEnable = _HzOduAamEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 5, 1),
    _HzOduAamEnable_Type()
)
hzOduAamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduAamEnable.setStatus("mandatory")
_HzOduPeerSysInfo_ObjectIdentity = ObjectIdentity
hzOduPeerSysInfo = _HzOduPeerSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 6)
)
_HzOduPeerMacAddress_Type = DisplayString
_HzOduPeerMacAddress_Object = MibScalar
hzOduPeerMacAddress = _HzOduPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 6, 1),
    _HzOduPeerMacAddress_Type()
)
hzOduPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPeerMacAddress.setStatus("mandatory")
_HzOduPeerIpAddress_Type = IpAddress
_HzOduPeerIpAddress_Object = MibScalar
hzOduPeerIpAddress = _HzOduPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 6, 2),
    _HzOduPeerIpAddress_Type()
)
hzOduPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPeerIpAddress.setStatus("mandatory")
_HzOduPeerSubnetMask_Type = IpAddress
_HzOduPeerSubnetMask_Object = MibScalar
hzOduPeerSubnetMask = _HzOduPeerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 6, 3),
    _HzOduPeerSubnetMask_Type()
)
hzOduPeerSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPeerSubnetMask.setStatus("mandatory")
_HzOduSysRedundancy_ObjectIdentity = ObjectIdentity
hzOduSysRedundancy = _HzOduSysRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 7)
)


class _HzOduSystemRedundancyMode_Type(Integer32):
    """Custom type hzOduSystemRedundancyMode based on Integer32"""
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
        *(("off", 1),
          ("primary-hsb-1wire", 2),
          ("secondary-hsb-1wire", 3),
          ("primary-hsb-2wire", 4),
          ("secondary-hsb-2wire", 5))
    )


_HzOduSystemRedundancyMode_Type.__name__ = "Integer32"
_HzOduSystemRedundancyMode_Object = MibScalar
hzOduSystemRedundancyMode = _HzOduSystemRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 7, 1),
    _HzOduSystemRedundancyMode_Type()
)
hzOduSystemRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduSystemRedundancyMode.setStatus("mandatory")


class _HzOduSystemRedundancyOverride_Type(Integer32):
    """Custom type hzOduSystemRedundancyOverride based on Integer32"""
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
        *(("primary", 1),
          ("secondary", 2),
          ("auto", 3),
          ("manual", 4))
    )


_HzOduSystemRedundancyOverride_Type.__name__ = "Integer32"
_HzOduSystemRedundancyOverride_Object = MibScalar
hzOduSystemRedundancyOverride = _HzOduSystemRedundancyOverride_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 7, 2),
    _HzOduSystemRedundancyOverride_Type()
)
hzOduSystemRedundancyOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduSystemRedundancyOverride.setStatus("mandatory")
_HzOduSystemRedundancyLinkStatus_Type = DisplayString
_HzOduSystemRedundancyLinkStatus_Object = MibScalar
hzOduSystemRedundancyLinkStatus = _HzOduSystemRedundancyLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 7, 3),
    _HzOduSystemRedundancyLinkStatus_Type()
)
hzOduSystemRedundancyLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSystemRedundancyLinkStatus.setStatus("mandatory")


class _HzOduSystemRedundancyStandbyEnetState_Type(Integer32):
    """Custom type hzOduSystemRedundancyStandbyEnetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("pulse", 3))
    )


_HzOduSystemRedundancyStandbyEnetState_Type.__name__ = "Integer32"
_HzOduSystemRedundancyStandbyEnetState_Object = MibScalar
hzOduSystemRedundancyStandbyEnetState = _HzOduSystemRedundancyStandbyEnetState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 7, 4),
    _HzOduSystemRedundancyStandbyEnetState_Type()
)
hzOduSystemRedundancyStandbyEnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduSystemRedundancyStandbyEnetState.setStatus("mandatory")


class _HzOduSystemRedundancyStateSwitch_Type(Integer32):
    """Custom type hzOduSystemRedundancyStateSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_HzOduSystemRedundancyStateSwitch_Type.__name__ = "Integer32"
_HzOduSystemRedundancyStateSwitch_Object = MibScalar
hzOduSystemRedundancyStateSwitch = _HzOduSystemRedundancyStateSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 1, 7, 5),
    _HzOduSystemRedundancyStateSwitch_Type()
)
hzOduSystemRedundancyStateSwitch.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzOduSystemRedundancyStateSwitch.setStatus("mandatory")
_HzOduAuthentication_ObjectIdentity = ObjectIdentity
hzOduAuthentication = _HzOduAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 2)
)


class _HzOduUniquePeerAuthenticationKey_Type(DisplayString):
    """Custom type hzOduUniquePeerAuthenticationKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_HzOduUniquePeerAuthenticationKey_Type.__name__ = "DisplayString"
_HzOduUniquePeerAuthenticationKey_Object = MibScalar
hzOduUniquePeerAuthenticationKey = _HzOduUniquePeerAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 2, 1),
    _HzOduUniquePeerAuthenticationKey_Type()
)
hzOduUniquePeerAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduUniquePeerAuthenticationKey.setStatus("mandatory")
_HzOduPeerDetectedSerialNumber_Type = DisplayString
_HzOduPeerDetectedSerialNumber_Object = MibScalar
hzOduPeerDetectedSerialNumber = _HzOduPeerDetectedSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 2, 2),
    _HzOduPeerDetectedSerialNumber_Type()
)
hzOduPeerDetectedSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPeerDetectedSerialNumber.setStatus("mandatory")


class _HzOduAuthenticationMode_Type(Integer32):
    """Custom type hzOduAuthenticationMode based on Integer32"""
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
        *(("none", 1),
          ("unique", 2),
          ("group", 3))
    )


_HzOduAuthenticationMode_Type.__name__ = "Integer32"
_HzOduAuthenticationMode_Object = MibScalar
hzOduAuthenticationMode = _HzOduAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 2, 3),
    _HzOduAuthenticationMode_Type()
)
hzOduAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduAuthenticationMode.setStatus("mandatory")


class _HzOduAuthenticationFailureAction_Type(Integer32):
    """Custom type hzOduAuthenticationFailureAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blockTraffic", 1),
          ("passTraffic", 2))
    )


_HzOduAuthenticationFailureAction_Type.__name__ = "Integer32"
_HzOduAuthenticationFailureAction_Object = MibScalar
hzOduAuthenticationFailureAction = _HzOduAuthenticationFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 2, 4),
    _HzOduAuthenticationFailureAction_Type()
)
hzOduAuthenticationFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduAuthenticationFailureAction.setStatus("mandatory")


class _HzOduPeerAuthenticationStatus_Type(Integer32):
    """Custom type hzOduPeerAuthenticationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAuthenticated", 1),
          ("authenticated", 2),
          ("explicitAuthenticationFailure", 3))
    )


_HzOduPeerAuthenticationStatus_Type.__name__ = "Integer32"
_HzOduPeerAuthenticationStatus_Object = MibScalar
hzOduPeerAuthenticationStatus = _HzOduPeerAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 2, 5),
    _HzOduPeerAuthenticationStatus_Type()
)
hzOduPeerAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPeerAuthenticationStatus.setStatus("mandatory")
_HzOduNetworkManagement_ObjectIdentity = ObjectIdentity
hzOduNetworkManagement = _HzOduNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3)
)
_HzOduMacAddress_Type = DisplayString
_HzOduMacAddress_Object = MibScalar
hzOduMacAddress = _HzOduMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3, 1),
    _HzOduMacAddress_Type()
)
hzOduMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduMacAddress.setStatus("mandatory")


class _HzOduNetworkManagementInterface_Type(Integer32):
    """Custom type hzOduNetworkManagementInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2),
          ("port2Extended", 3))
    )


_HzOduNetworkManagementInterface_Type.__name__ = "Integer32"
_HzOduNetworkManagementInterface_Object = MibScalar
hzOduNetworkManagementInterface = _HzOduNetworkManagementInterface_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3, 2),
    _HzOduNetworkManagementInterface_Type()
)
hzOduNetworkManagementInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduNetworkManagementInterface.setStatus("mandatory")
_HzOduIpAddress_Type = IpAddress
_HzOduIpAddress_Object = MibScalar
hzOduIpAddress = _HzOduIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3, 3),
    _HzOduIpAddress_Type()
)
hzOduIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduIpAddress.setStatus("mandatory")
_HzOduSubnetMask_Type = IpAddress
_HzOduSubnetMask_Object = MibScalar
hzOduSubnetMask = _HzOduSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3, 4),
    _HzOduSubnetMask_Type()
)
hzOduSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSubnetMask.setStatus("mandatory")
_HzOduDefaultGateway_Type = IpAddress
_HzOduDefaultGateway_Object = MibScalar
hzOduDefaultGateway = _HzOduDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3, 5),
    _HzOduDefaultGateway_Type()
)
hzOduDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduDefaultGateway.setStatus("mandatory")


class _HzOduTelnetAccessMode_Type(Integer32):
    """Custom type hzOduTelnetAccessMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduTelnetAccessMode_Type.__name__ = "Integer32"
_HzOduTelnetAccessMode_Object = MibScalar
hzOduTelnetAccessMode = _HzOduTelnetAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3, 6),
    _HzOduTelnetAccessMode_Type()
)
hzOduTelnetAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduTelnetAccessMode.setStatus("mandatory")


class _HzOduSshAccessMode_Type(Integer32):
    """Custom type hzOduSshAccessMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduSshAccessMode_Type.__name__ = "Integer32"
_HzOduSshAccessMode_Object = MibScalar
hzOduSshAccessMode = _HzOduSshAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3, 7),
    _HzOduSshAccessMode_Type()
)
hzOduSshAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduSshAccessMode.setStatus("mandatory")


class _HzOduVlanTagEnable_Type(Integer32):
    """Custom type hzOduVlanTagEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduVlanTagEnable_Type.__name__ = "Integer32"
_HzOduVlanTagEnable_Object = MibScalar
hzOduVlanTagEnable = _HzOduVlanTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3, 8),
    _HzOduVlanTagEnable_Type()
)
hzOduVlanTagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduVlanTagEnable.setStatus("mandatory")


class _HzOduVlanTagId_Type(Integer32):
    """Custom type hzOduVlanTagId based on Integer32"""
    defaultValue = 0


_HzOduVlanTagId_Type.__name__ = "Integer32"
_HzOduVlanTagId_Object = MibScalar
hzOduVlanTagId = _HzOduVlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3, 9),
    _HzOduVlanTagId_Type()
)
hzOduVlanTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduVlanTagId.setStatus("mandatory")


class _HzOduVlanTagPriority_Type(Integer32):
    """Custom type hzOduVlanTagPriority based on Integer32"""
    defaultValue = 0


_HzOduVlanTagPriority_Type.__name__ = "Integer32"
_HzOduVlanTagPriority_Object = MibScalar
hzOduVlanTagPriority = _HzOduVlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 3, 10),
    _HzOduVlanTagPriority_Type()
)
hzOduVlanTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduVlanTagPriority.setStatus("mandatory")
_HzOduNetworkInterface_ObjectIdentity = ObjectIdentity
hzOduNetworkInterface = _HzOduNetworkInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4)
)
_HzOduEnetPort1_ObjectIdentity = ObjectIdentity
hzOduEnetPort1 = _HzOduEnetPort1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1)
)
_HzOduEnetPort1Description_Type = DisplayString
_HzOduEnetPort1Description_Object = MibScalar
hzOduEnetPort1Description = _HzOduEnetPort1Description_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 1),
    _HzOduEnetPort1Description_Type()
)
hzOduEnetPort1Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1Description.setStatus("mandatory")
_HzOduEnetPort1Config_ObjectIdentity = ObjectIdentity
hzOduEnetPort1Config = _HzOduEnetPort1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2)
)


class _HzOduEnetPort1AutoNegotiation_Type(Integer32):
    """Custom type hzOduEnetPort1AutoNegotiation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HzOduEnetPort1AutoNegotiation_Type.__name__ = "Integer32"
_HzOduEnetPort1AutoNegotiation_Object = MibScalar
hzOduEnetPort1AutoNegotiation = _HzOduEnetPort1AutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2, 1),
    _HzOduEnetPort1AutoNegotiation_Type()
)
hzOduEnetPort1AutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1AutoNegotiation.setStatus("mandatory")


class _HzOduEnetPort1Speed_Type(Integer32):
    """Custom type hzOduEnetPort1Speed based on Integer32"""
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
        *(("x10M", 1),
          ("x100M", 2),
          ("x1000M", 3),
          ("auto", 4))
    )


_HzOduEnetPort1Speed_Type.__name__ = "Integer32"
_HzOduEnetPort1Speed_Object = MibScalar
hzOduEnetPort1Speed = _HzOduEnetPort1Speed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2, 2),
    _HzOduEnetPort1Speed_Type()
)
hzOduEnetPort1Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1Speed.setStatus("mandatory")


class _HzOduEnetPort1Duplex_Type(Integer32):
    """Custom type hzOduEnetPort1Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("auto", 3))
    )


_HzOduEnetPort1Duplex_Type.__name__ = "Integer32"
_HzOduEnetPort1Duplex_Object = MibScalar
hzOduEnetPort1Duplex = _HzOduEnetPort1Duplex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2, 3),
    _HzOduEnetPort1Duplex_Type()
)
hzOduEnetPort1Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1Duplex.setStatus("mandatory")


class _HzOduEnetPort1Media_Type(Integer32):
    """Custom type hzOduEnetPort1Media based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2),
          ("auto", 3))
    )


_HzOduEnetPort1Media_Type.__name__ = "Integer32"
_HzOduEnetPort1Media_Object = MibScalar
hzOduEnetPort1Media = _HzOduEnetPort1Media_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2, 4),
    _HzOduEnetPort1Media_Type()
)
hzOduEnetPort1Media.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1Media.setStatus("mandatory")


class _HzOduEnetPort1AdminState_Type(Integer32):
    """Custom type hzOduEnetPort1AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HzOduEnetPort1AdminState_Type.__name__ = "Integer32"
_HzOduEnetPort1AdminState_Object = MibScalar
hzOduEnetPort1AdminState = _HzOduEnetPort1AdminState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2, 5),
    _HzOduEnetPort1AdminState_Type()
)
hzOduEnetPort1AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1AdminState.setStatus("mandatory")


class _HzOduEnetPort1OpticalTransceiverState_Type(Integer32):
    """Custom type hzOduEnetPort1OpticalTransceiverState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HzOduEnetPort1OpticalTransceiverState_Type.__name__ = "Integer32"
_HzOduEnetPort1OpticalTransceiverState_Object = MibScalar
hzOduEnetPort1OpticalTransceiverState = _HzOduEnetPort1OpticalTransceiverState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2, 6),
    _HzOduEnetPort1OpticalTransceiverState_Type()
)
hzOduEnetPort1OpticalTransceiverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1OpticalTransceiverState.setStatus("mandatory")


class _HzOduEnetPort1PauseFrameEnable_Type(Integer32):
    """Custom type hzOduEnetPort1PauseFrameEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduEnetPort1PauseFrameEnable_Type.__name__ = "Integer32"
_HzOduEnetPort1PauseFrameEnable_Object = MibScalar
hzOduEnetPort1PauseFrameEnable = _HzOduEnetPort1PauseFrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2, 7),
    _HzOduEnetPort1PauseFrameEnable_Type()
)
hzOduEnetPort1PauseFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1PauseFrameEnable.setStatus("mandatory")


class _HzOduEnetPort1MaxFrameSize_Type(Integer32):
    """Custom type hzOduEnetPort1MaxFrameSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1600, 9600),
    )


_HzOduEnetPort1MaxFrameSize_Type.__name__ = "Integer32"
_HzOduEnetPort1MaxFrameSize_Object = MibScalar
hzOduEnetPort1MaxFrameSize = _HzOduEnetPort1MaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2, 8),
    _HzOduEnetPort1MaxFrameSize_Type()
)
hzOduEnetPort1MaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1MaxFrameSize.setStatus("mandatory")


class _HzOduEnetPort1DroppedEnetFramesThresholdParameters_Type(DisplayString):
    """Custom type hzOduEnetPort1DroppedEnetFramesThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduEnetPort1DroppedEnetFramesThresholdParameters_Type.__name__ = "DisplayString"
_HzOduEnetPort1DroppedEnetFramesThresholdParameters_Object = MibScalar
hzOduEnetPort1DroppedEnetFramesThresholdParameters = _HzOduEnetPort1DroppedEnetFramesThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2, 9),
    _HzOduEnetPort1DroppedEnetFramesThresholdParameters_Type()
)
hzOduEnetPort1DroppedEnetFramesThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1DroppedEnetFramesThresholdParameters.setStatus("mandatory")


class _HzOduEnetPort1BandwidthUtilizationThresholdParameters_Type(DisplayString):
    """Custom type hzOduEnetPort1BandwidthUtilizationThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduEnetPort1BandwidthUtilizationThresholdParameters_Type.__name__ = "DisplayString"
_HzOduEnetPort1BandwidthUtilizationThresholdParameters_Object = MibScalar
hzOduEnetPort1BandwidthUtilizationThresholdParameters = _HzOduEnetPort1BandwidthUtilizationThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 2, 10),
    _HzOduEnetPort1BandwidthUtilizationThresholdParameters_Type()
)
hzOduEnetPort1BandwidthUtilizationThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1BandwidthUtilizationThresholdParameters.setStatus("mandatory")
_HzOduEnetPort1Status_ObjectIdentity = ObjectIdentity
hzOduEnetPort1Status = _HzOduEnetPort1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 3)
)


class _HzOduEnetPort1LinkStatus_Type(Integer32):
    """Custom type hzOduEnetPort1LinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("invalid", 3))
    )


_HzOduEnetPort1LinkStatus_Type.__name__ = "Integer32"
_HzOduEnetPort1LinkStatus_Object = MibScalar
hzOduEnetPort1LinkStatus = _HzOduEnetPort1LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 3, 1),
    _HzOduEnetPort1LinkStatus_Type()
)
hzOduEnetPort1LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1LinkStatus.setStatus("mandatory")


class _HzOduEnetPort1AutoNegotiationStatus_Type(Integer32):
    """Custom type hzOduEnetPort1AutoNegotiationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("invalid", 3))
    )


_HzOduEnetPort1AutoNegotiationStatus_Type.__name__ = "Integer32"
_HzOduEnetPort1AutoNegotiationStatus_Object = MibScalar
hzOduEnetPort1AutoNegotiationStatus = _HzOduEnetPort1AutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 3, 2),
    _HzOduEnetPort1AutoNegotiationStatus_Type()
)
hzOduEnetPort1AutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1AutoNegotiationStatus.setStatus("mandatory")


class _HzOduEnetPort1SpeedStatus_Type(Integer32):
    """Custom type hzOduEnetPort1SpeedStatus based on Integer32"""
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
        *(("x10M", 1),
          ("x100M", 2),
          ("x1000M", 3),
          ("auto", 4),
          ("invalid", 5))
    )


_HzOduEnetPort1SpeedStatus_Type.__name__ = "Integer32"
_HzOduEnetPort1SpeedStatus_Object = MibScalar
hzOduEnetPort1SpeedStatus = _HzOduEnetPort1SpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 3, 3),
    _HzOduEnetPort1SpeedStatus_Type()
)
hzOduEnetPort1SpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1SpeedStatus.setStatus("mandatory")


class _HzOduEnetPort1DuplexStatus_Type(Integer32):
    """Custom type hzOduEnetPort1DuplexStatus based on Integer32"""
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
        *(("full", 1),
          ("half", 2),
          ("auto", 3),
          ("invalid", 4))
    )


_HzOduEnetPort1DuplexStatus_Type.__name__ = "Integer32"
_HzOduEnetPort1DuplexStatus_Object = MibScalar
hzOduEnetPort1DuplexStatus = _HzOduEnetPort1DuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 3, 4),
    _HzOduEnetPort1DuplexStatus_Type()
)
hzOduEnetPort1DuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1DuplexStatus.setStatus("mandatory")


class _HzOduEnetPort1MediaStatus_Type(Integer32):
    """Custom type hzOduEnetPort1MediaStatus based on Integer32"""
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
        *(("copper", 1),
          ("fiber", 2),
          ("auto", 3),
          ("invalid", 4))
    )


_HzOduEnetPort1MediaStatus_Type.__name__ = "Integer32"
_HzOduEnetPort1MediaStatus_Object = MibScalar
hzOduEnetPort1MediaStatus = _HzOduEnetPort1MediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 3, 5),
    _HzOduEnetPort1MediaStatus_Type()
)
hzOduEnetPort1MediaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1MediaStatus.setStatus("mandatory")
_HzOduEnetPort1Stats_ObjectIdentity = ObjectIdentity
hzOduEnetPort1Stats = _HzOduEnetPort1Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4)
)
_HzOduEnetPort1TxFrames_Type = Counter32
_HzOduEnetPort1TxFrames_Object = MibScalar
hzOduEnetPort1TxFrames = _HzOduEnetPort1TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 1),
    _HzOduEnetPort1TxFrames_Type()
)
hzOduEnetPort1TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1TxFrames.setStatus("mandatory")
_HzOduEnetPort1TxBytes_Type = Counter32
_HzOduEnetPort1TxBytes_Object = MibScalar
hzOduEnetPort1TxBytes = _HzOduEnetPort1TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 2),
    _HzOduEnetPort1TxBytes_Type()
)
hzOduEnetPort1TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1TxBytes.setStatus("mandatory")
_HzOduEnetPort1RxFrames_Type = Counter32
_HzOduEnetPort1RxFrames_Object = MibScalar
hzOduEnetPort1RxFrames = _HzOduEnetPort1RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 3),
    _HzOduEnetPort1RxFrames_Type()
)
hzOduEnetPort1RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1RxFrames.setStatus("mandatory")
_HzOduEnetPort1RxBytes_Type = Counter32
_HzOduEnetPort1RxBytes_Object = MibScalar
hzOduEnetPort1RxBytes = _HzOduEnetPort1RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 4),
    _HzOduEnetPort1RxBytes_Type()
)
hzOduEnetPort1RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1RxBytes.setStatus("mandatory")
_HzOduEnetPort1RxFramesInError_Type = Counter32
_HzOduEnetPort1RxFramesInError_Object = MibScalar
hzOduEnetPort1RxFramesInError = _HzOduEnetPort1RxFramesInError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 5),
    _HzOduEnetPort1RxFramesInError_Type()
)
hzOduEnetPort1RxFramesInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1RxFramesInError.setStatus("mandatory")
_HzOduEnetPort1RxFramesCRCError_Type = Counter32
_HzOduEnetPort1RxFramesCRCError_Object = MibScalar
hzOduEnetPort1RxFramesCRCError = _HzOduEnetPort1RxFramesCRCError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 6),
    _HzOduEnetPort1RxFramesCRCError_Type()
)
hzOduEnetPort1RxFramesCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1RxFramesCRCError.setStatus("mandatory")
_HzOduEnetPort1BWUtilization_Type = Integer32
_HzOduEnetPort1BWUtilization_Object = MibScalar
hzOduEnetPort1BWUtilization = _HzOduEnetPort1BWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 7),
    _HzOduEnetPort1BWUtilization_Type()
)
hzOduEnetPort1BWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1BWUtilization.setStatus("mandatory")
_HzOduEnetPort1IngressDataRate_Type = Integer32
_HzOduEnetPort1IngressDataRate_Object = MibScalar
hzOduEnetPort1IngressDataRate = _HzOduEnetPort1IngressDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 8),
    _HzOduEnetPort1IngressDataRate_Type()
)
hzOduEnetPort1IngressDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1IngressDataRate.setStatus("mandatory")
_HzOduEnetPort1EgressDataRate_Type = Integer32
_HzOduEnetPort1EgressDataRate_Object = MibScalar
hzOduEnetPort1EgressDataRate = _HzOduEnetPort1EgressDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 9),
    _HzOduEnetPort1EgressDataRate_Type()
)
hzOduEnetPort1EgressDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1EgressDataRate.setStatus("mandatory")
_HzOduEnetPort1FramesInQueue1_Type = Counter32
_HzOduEnetPort1FramesInQueue1_Object = MibScalar
hzOduEnetPort1FramesInQueue1 = _HzOduEnetPort1FramesInQueue1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 10),
    _HzOduEnetPort1FramesInQueue1_Type()
)
hzOduEnetPort1FramesInQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1FramesInQueue1.setStatus("mandatory")
_HzOduEnetPort1FramesInQueue2_Type = Counter32
_HzOduEnetPort1FramesInQueue2_Object = MibScalar
hzOduEnetPort1FramesInQueue2 = _HzOduEnetPort1FramesInQueue2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 11),
    _HzOduEnetPort1FramesInQueue2_Type()
)
hzOduEnetPort1FramesInQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1FramesInQueue2.setStatus("mandatory")
_HzOduEnetPort1FramesInQueue3_Type = Counter32
_HzOduEnetPort1FramesInQueue3_Object = MibScalar
hzOduEnetPort1FramesInQueue3 = _HzOduEnetPort1FramesInQueue3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 12),
    _HzOduEnetPort1FramesInQueue3_Type()
)
hzOduEnetPort1FramesInQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1FramesInQueue3.setStatus("mandatory")
_HzOduEnetPort1FramesInQueue4_Type = Counter32
_HzOduEnetPort1FramesInQueue4_Object = MibScalar
hzOduEnetPort1FramesInQueue4 = _HzOduEnetPort1FramesInQueue4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 13),
    _HzOduEnetPort1FramesInQueue4_Type()
)
hzOduEnetPort1FramesInQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1FramesInQueue4.setStatus("mandatory")
_HzOduEnetPort1FramesInQueue1Discarded_Type = Counter32
_HzOduEnetPort1FramesInQueue1Discarded_Object = MibScalar
hzOduEnetPort1FramesInQueue1Discarded = _HzOduEnetPort1FramesInQueue1Discarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 14),
    _HzOduEnetPort1FramesInQueue1Discarded_Type()
)
hzOduEnetPort1FramesInQueue1Discarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1FramesInQueue1Discarded.setStatus("mandatory")
_HzOduEnetPort1FramesInQueue2Discarded_Type = Counter32
_HzOduEnetPort1FramesInQueue2Discarded_Object = MibScalar
hzOduEnetPort1FramesInQueue2Discarded = _HzOduEnetPort1FramesInQueue2Discarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 15),
    _HzOduEnetPort1FramesInQueue2Discarded_Type()
)
hzOduEnetPort1FramesInQueue2Discarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1FramesInQueue2Discarded.setStatus("mandatory")
_HzOduEnetPort1FramesInQueue3Discarded_Type = Counter32
_HzOduEnetPort1FramesInQueue3Discarded_Object = MibScalar
hzOduEnetPort1FramesInQueue3Discarded = _HzOduEnetPort1FramesInQueue3Discarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 16),
    _HzOduEnetPort1FramesInQueue3Discarded_Type()
)
hzOduEnetPort1FramesInQueue3Discarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1FramesInQueue3Discarded.setStatus("mandatory")
_HzOduEnetPort1FramesInQueue4Discarded_Type = Counter32
_HzOduEnetPort1FramesInQueue4Discarded_Object = MibScalar
hzOduEnetPort1FramesInQueue4Discarded = _HzOduEnetPort1FramesInQueue4Discarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 1, 4, 17),
    _HzOduEnetPort1FramesInQueue4Discarded_Type()
)
hzOduEnetPort1FramesInQueue4Discarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1FramesInQueue4Discarded.setStatus("mandatory")
_HzOduEnetPort2_ObjectIdentity = ObjectIdentity
hzOduEnetPort2 = _HzOduEnetPort2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2)
)
_HzOduEnetPort2Description_Type = DisplayString
_HzOduEnetPort2Description_Object = MibScalar
hzOduEnetPort2Description = _HzOduEnetPort2Description_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 1),
    _HzOduEnetPort2Description_Type()
)
hzOduEnetPort2Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2Description.setStatus("mandatory")
_HzOduEnetPort2Config_ObjectIdentity = ObjectIdentity
hzOduEnetPort2Config = _HzOduEnetPort2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 2)
)


class _HzOduEnetPort2AutoNegotiation_Type(Integer32):
    """Custom type hzOduEnetPort2AutoNegotiation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HzOduEnetPort2AutoNegotiation_Type.__name__ = "Integer32"
_HzOduEnetPort2AutoNegotiation_Object = MibScalar
hzOduEnetPort2AutoNegotiation = _HzOduEnetPort2AutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 2, 1),
    _HzOduEnetPort2AutoNegotiation_Type()
)
hzOduEnetPort2AutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort2AutoNegotiation.setStatus("mandatory")


class _HzOduEnetPort2Speed_Type(Integer32):
    """Custom type hzOduEnetPort2Speed based on Integer32"""
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
        *(("x10M", 1),
          ("x100M", 2),
          ("x1000M", 3),
          ("auto", 4))
    )


_HzOduEnetPort2Speed_Type.__name__ = "Integer32"
_HzOduEnetPort2Speed_Object = MibScalar
hzOduEnetPort2Speed = _HzOduEnetPort2Speed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 2, 2),
    _HzOduEnetPort2Speed_Type()
)
hzOduEnetPort2Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort2Speed.setStatus("mandatory")


class _HzOduEnetPort2Duplex_Type(Integer32):
    """Custom type hzOduEnetPort2Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("auto", 3))
    )


_HzOduEnetPort2Duplex_Type.__name__ = "Integer32"
_HzOduEnetPort2Duplex_Object = MibScalar
hzOduEnetPort2Duplex = _HzOduEnetPort2Duplex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 2, 3),
    _HzOduEnetPort2Duplex_Type()
)
hzOduEnetPort2Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2Duplex.setStatus("mandatory")


class _HzOduEnetPort2AdminState_Type(Integer32):
    """Custom type hzOduEnetPort2AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HzOduEnetPort2AdminState_Type.__name__ = "Integer32"
_HzOduEnetPort2AdminState_Object = MibScalar
hzOduEnetPort2AdminState = _HzOduEnetPort2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 2, 4),
    _HzOduEnetPort2AdminState_Type()
)
hzOduEnetPort2AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2AdminState.setStatus("mandatory")
_HzOduEnetPort2Status_ObjectIdentity = ObjectIdentity
hzOduEnetPort2Status = _HzOduEnetPort2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 3)
)


class _HzOduEnetPort2LinkStatus_Type(Integer32):
    """Custom type hzOduEnetPort2LinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("invalid", 3))
    )


_HzOduEnetPort2LinkStatus_Type.__name__ = "Integer32"
_HzOduEnetPort2LinkStatus_Object = MibScalar
hzOduEnetPort2LinkStatus = _HzOduEnetPort2LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 3, 1),
    _HzOduEnetPort2LinkStatus_Type()
)
hzOduEnetPort2LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2LinkStatus.setStatus("mandatory")


class _HzOduEnetPort2AutoNegotiationStatus_Type(Integer32):
    """Custom type hzOduEnetPort2AutoNegotiationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("invalid", 3))
    )


_HzOduEnetPort2AutoNegotiationStatus_Type.__name__ = "Integer32"
_HzOduEnetPort2AutoNegotiationStatus_Object = MibScalar
hzOduEnetPort2AutoNegotiationStatus = _HzOduEnetPort2AutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 3, 2),
    _HzOduEnetPort2AutoNegotiationStatus_Type()
)
hzOduEnetPort2AutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2AutoNegotiationStatus.setStatus("mandatory")


class _HzOduEnetPort2SpeedStatus_Type(Integer32):
    """Custom type hzOduEnetPort2SpeedStatus based on Integer32"""
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
        *(("x10M", 1),
          ("x100M", 2),
          ("x1000M", 3),
          ("auto", 4),
          ("invalid", 5))
    )


_HzOduEnetPort2SpeedStatus_Type.__name__ = "Integer32"
_HzOduEnetPort2SpeedStatus_Object = MibScalar
hzOduEnetPort2SpeedStatus = _HzOduEnetPort2SpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 3, 3),
    _HzOduEnetPort2SpeedStatus_Type()
)
hzOduEnetPort2SpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2SpeedStatus.setStatus("mandatory")


class _HzOduEnetPort2DuplexStatus_Type(Integer32):
    """Custom type hzOduEnetPort2DuplexStatus based on Integer32"""
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
        *(("full", 1),
          ("half", 2),
          ("auto", 3),
          ("invalid", 4))
    )


_HzOduEnetPort2DuplexStatus_Type.__name__ = "Integer32"
_HzOduEnetPort2DuplexStatus_Object = MibScalar
hzOduEnetPort2DuplexStatus = _HzOduEnetPort2DuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 3, 4),
    _HzOduEnetPort2DuplexStatus_Type()
)
hzOduEnetPort2DuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2DuplexStatus.setStatus("mandatory")


class _HzOduEnetPort2MediaStatus_Type(Integer32):
    """Custom type hzOduEnetPort2MediaStatus based on Integer32"""
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
        *(("copper", 1),
          ("fiber", 2),
          ("auto", 3),
          ("invalid", 4))
    )


_HzOduEnetPort2MediaStatus_Type.__name__ = "Integer32"
_HzOduEnetPort2MediaStatus_Object = MibScalar
hzOduEnetPort2MediaStatus = _HzOduEnetPort2MediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 3, 5),
    _HzOduEnetPort2MediaStatus_Type()
)
hzOduEnetPort2MediaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2MediaStatus.setStatus("mandatory")
_HzOduEnetPort2Stats_ObjectIdentity = ObjectIdentity
hzOduEnetPort2Stats = _HzOduEnetPort2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 4)
)
_HzOduEnetPort2TxFrames_Type = Counter32
_HzOduEnetPort2TxFrames_Object = MibScalar
hzOduEnetPort2TxFrames = _HzOduEnetPort2TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 4, 1),
    _HzOduEnetPort2TxFrames_Type()
)
hzOduEnetPort2TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2TxFrames.setStatus("mandatory")
_HzOduEnetPort2TxBytes_Type = Counter32
_HzOduEnetPort2TxBytes_Object = MibScalar
hzOduEnetPort2TxBytes = _HzOduEnetPort2TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 4, 2),
    _HzOduEnetPort2TxBytes_Type()
)
hzOduEnetPort2TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2TxBytes.setStatus("mandatory")
_HzOduEnetPort2RxFrames_Type = Counter32
_HzOduEnetPort2RxFrames_Object = MibScalar
hzOduEnetPort2RxFrames = _HzOduEnetPort2RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 4, 3),
    _HzOduEnetPort2RxFrames_Type()
)
hzOduEnetPort2RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2RxFrames.setStatus("mandatory")
_HzOduEnetPort2RxBytes_Type = Counter32
_HzOduEnetPort2RxBytes_Object = MibScalar
hzOduEnetPort2RxBytes = _HzOduEnetPort2RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 4, 4),
    _HzOduEnetPort2RxBytes_Type()
)
hzOduEnetPort2RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2RxBytes.setStatus("mandatory")
_HzOduEnetPort2RxFramesInError_Type = Counter32
_HzOduEnetPort2RxFramesInError_Object = MibScalar
hzOduEnetPort2RxFramesInError = _HzOduEnetPort2RxFramesInError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 4, 5),
    _HzOduEnetPort2RxFramesInError_Type()
)
hzOduEnetPort2RxFramesInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2RxFramesInError.setStatus("mandatory")
_HzOduEnetPort2RxFramesCrcError_Type = Counter32
_HzOduEnetPort2RxFramesCrcError_Object = MibScalar
hzOduEnetPort2RxFramesCrcError = _HzOduEnetPort2RxFramesCrcError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 4, 2, 4, 6),
    _HzOduEnetPort2RxFramesCrcError_Type()
)
hzOduEnetPort2RxFramesCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2RxFramesCrcError.setStatus("mandatory")
_HzOduWirelessInterface_ObjectIdentity = ObjectIdentity
hzOduWirelessInterface = _HzOduWirelessInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5)
)
_HzOduWirelessPort1_ObjectIdentity = ObjectIdentity
hzOduWirelessPort1 = _HzOduWirelessPort1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1)
)
_HzOduWirelessPort1Description_Type = DisplayString
_HzOduWirelessPort1Description_Object = MibScalar
hzOduWirelessPort1Description = _HzOduWirelessPort1Description_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 1),
    _HzOduWirelessPort1Description_Type()
)
hzOduWirelessPort1Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduWirelessPort1Description.setStatus("mandatory")
_HzOduModem1_ObjectIdentity = ObjectIdentity
hzOduModem1 = _HzOduModem1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2)
)


class _HzOduModem1AdminStatus_Type(Integer32):
    """Custom type hzOduModem1AdminStatus based on Integer32"""
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
          ("testing", 3))
    )


_HzOduModem1AdminStatus_Type.__name__ = "Integer32"
_HzOduModem1AdminStatus_Object = MibScalar
hzOduModem1AdminStatus = _HzOduModem1AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 1),
    _HzOduModem1AdminStatus_Type()
)
hzOduModem1AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1AdminStatus.setStatus("mandatory")


class _HzOduModem1OperStatus_Type(Integer32):
    """Custom type hzOduModem1OperStatus based on Integer32"""
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
          ("testing", 3))
    )


_HzOduModem1OperStatus_Type.__name__ = "Integer32"
_HzOduModem1OperStatus_Object = MibScalar
hzOduModem1OperStatus = _HzOduModem1OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 2),
    _HzOduModem1OperStatus_Type()
)
hzOduModem1OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1OperStatus.setStatus("mandatory")


class _HzOduModem1Reset_Type(Integer32):
    """Custom type hzOduModem1Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HzOduModem1Reset_Type.__name__ = "Integer32"
_HzOduModem1Reset_Object = MibScalar
hzOduModem1Reset = _HzOduModem1Reset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 3),
    _HzOduModem1Reset_Type()
)
hzOduModem1Reset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzOduModem1Reset.setStatus("mandatory")
_HzOduModem1ChannelizedRSL_Type = Integer32
_HzOduModem1ChannelizedRSL_Object = MibScalar
hzOduModem1ChannelizedRSL = _HzOduModem1ChannelizedRSL_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 4),
    _HzOduModem1ChannelizedRSL_Type()
)
hzOduModem1ChannelizedRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1ChannelizedRSL.setStatus("mandatory")


class _HzOduModem1ModulationType_Type(Integer32):
    """Custom type hzOduModem1ModulationType based on Integer32"""
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
        *(("qpsk", 1),
          ("qam", 2),
          ("qam16", 3),
          ("qam32", 4),
          ("qam64", 5),
          ("qam128", 6),
          ("qam256", 7),
          ("x8psk", 8))
    )


_HzOduModem1ModulationType_Type.__name__ = "Integer32"
_HzOduModem1ModulationType_Object = MibScalar
hzOduModem1ModulationType = _HzOduModem1ModulationType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 5),
    _HzOduModem1ModulationType_Type()
)
hzOduModem1ModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1ModulationType.setStatus("mandatory")
_HzOduModem1CurrentRxSpeed_Type = Integer32
_HzOduModem1CurrentRxSpeed_Object = MibScalar
hzOduModem1CurrentRxSpeed = _HzOduModem1CurrentRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 6),
    _HzOduModem1CurrentRxSpeed_Type()
)
hzOduModem1CurrentRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1CurrentRxSpeed.setStatus("mandatory")
_HzOduModem1CurrentTxSpeed_Type = Integer32
_HzOduModem1CurrentTxSpeed_Object = MibScalar
hzOduModem1CurrentTxSpeed = _HzOduModem1CurrentTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 7),
    _HzOduModem1CurrentTxSpeed_Type()
)
hzOduModem1CurrentTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1CurrentTxSpeed.setStatus("mandatory")
_HzOduModem1SNR_Type = Integer32
_HzOduModem1SNR_Object = MibScalar
hzOduModem1SNR = _HzOduModem1SNR_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 8),
    _HzOduModem1SNR_Type()
)
hzOduModem1SNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1SNR.setStatus("mandatory")
_HzOduModem1EbToNoiseRatio_Type = Integer32
_HzOduModem1EbToNoiseRatio_Object = MibScalar
hzOduModem1EbToNoiseRatio = _HzOduModem1EbToNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 9),
    _HzOduModem1EbToNoiseRatio_Type()
)
hzOduModem1EbToNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1EbToNoiseRatio.setStatus("mandatory")
_HzOduModem1EqualizerStress_Type = Integer32
_HzOduModem1EqualizerStress_Object = MibScalar
hzOduModem1EqualizerStress = _HzOduModem1EqualizerStress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 10),
    _HzOduModem1EqualizerStress_Type()
)
hzOduModem1EqualizerStress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1EqualizerStress.setStatus("mandatory")


class _HzOduModem1SNRThresholdParameters_Type(DisplayString):
    """Custom type hzOduModem1SNRThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduModem1SNRThresholdParameters_Type.__name__ = "DisplayString"
_HzOduModem1SNRThresholdParameters_Object = MibScalar
hzOduModem1SNRThresholdParameters = _HzOduModem1SNRThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 11),
    _HzOduModem1SNRThresholdParameters_Type()
)
hzOduModem1SNRThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduModem1SNRThresholdParameters.setStatus("mandatory")


class _HzOduModem1ChannelizedRslBelowThresholdParameters_Type(DisplayString):
    """Custom type hzOduModem1ChannelizedRslBelowThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduModem1ChannelizedRslBelowThresholdParameters_Type.__name__ = "DisplayString"
_HzOduModem1ChannelizedRslBelowThresholdParameters_Object = MibScalar
hzOduModem1ChannelizedRslBelowThresholdParameters = _HzOduModem1ChannelizedRslBelowThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 12),
    _HzOduModem1ChannelizedRslBelowThresholdParameters_Type()
)
hzOduModem1ChannelizedRslBelowThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduModem1ChannelizedRslBelowThresholdParameters.setStatus("mandatory")
_HzOduModem1LastChange_Type = TimeTicks
_HzOduModem1LastChange_Object = MibScalar
hzOduModem1LastChange = _HzOduModem1LastChange_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 13),
    _HzOduModem1LastChange_Type()
)
hzOduModem1LastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1LastChange.setStatus("mandatory")
_HzOduModem1ChannelizedRSLUnsignedInt_Type = Integer32
_HzOduModem1ChannelizedRSLUnsignedInt_Object = MibScalar
hzOduModem1ChannelizedRSLUnsignedInt = _HzOduModem1ChannelizedRSLUnsignedInt_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 14),
    _HzOduModem1ChannelizedRSLUnsignedInt_Type()
)
hzOduModem1ChannelizedRSLUnsignedInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1ChannelizedRSLUnsignedInt.setStatus("mandatory")
_HzOduModem1Statistics_ObjectIdentity = ObjectIdentity
hzOduModem1Statistics = _HzOduModem1Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 15)
)
_HzOduModem1TxFrames_Type = Counter32
_HzOduModem1TxFrames_Object = MibScalar
hzOduModem1TxFrames = _HzOduModem1TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 15, 1),
    _HzOduModem1TxFrames_Type()
)
hzOduModem1TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1TxFrames.setStatus("mandatory")
_HzOduModem1RxFramesOK_Type = Counter32
_HzOduModem1RxFramesOK_Object = MibScalar
hzOduModem1RxFramesOK = _HzOduModem1RxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 15, 2),
    _HzOduModem1RxFramesOK_Type()
)
hzOduModem1RxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1RxFramesOK.setStatus("mandatory")
_HzOduModem1RxFramesError_Type = Counter32
_HzOduModem1RxFramesError_Object = MibScalar
hzOduModem1RxFramesError = _HzOduModem1RxFramesError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 15, 3),
    _HzOduModem1RxFramesError_Type()
)
hzOduModem1RxFramesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1RxFramesError.setStatus("mandatory")
_HzOduModem1RxFramesQueueDiscarded_Type = Counter32
_HzOduModem1RxFramesQueueDiscarded_Object = MibScalar
hzOduModem1RxFramesQueueDiscarded = _HzOduModem1RxFramesQueueDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 15, 4),
    _HzOduModem1RxFramesQueueDiscarded_Type()
)
hzOduModem1RxFramesQueueDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1RxFramesQueueDiscarded.setStatus("mandatory")
_HzOduModem1TxBlocks_Type = Counter32
_HzOduModem1TxBlocks_Object = MibScalar
hzOduModem1TxBlocks = _HzOduModem1TxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 15, 5),
    _HzOduModem1TxBlocks_Type()
)
hzOduModem1TxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1TxBlocks.setStatus("mandatory")
_HzOduModem1RxBlocksOK_Type = Counter32
_HzOduModem1RxBlocksOK_Object = MibScalar
hzOduModem1RxBlocksOK = _HzOduModem1RxBlocksOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 15, 6),
    _HzOduModem1RxBlocksOK_Type()
)
hzOduModem1RxBlocksOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1RxBlocksOK.setStatus("mandatory")
_HzOduModem1RxBlocksError_Type = Counter32
_HzOduModem1RxBlocksError_Object = MibScalar
hzOduModem1RxBlocksError = _HzOduModem1RxBlocksError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 2, 15, 7),
    _HzOduModem1RxBlocksError_Type()
)
hzOduModem1RxBlocksError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1RxBlocksError.setStatus("mandatory")
_HzOduRadio1_ObjectIdentity = ObjectIdentity
hzOduRadio1 = _HzOduRadio1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 3)
)


class _HzOduRadio1OperStatus_Type(Integer32):
    """Custom type hzOduRadio1OperStatus based on Integer32"""
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
          ("testing", 3))
    )


_HzOduRadio1OperStatus_Type.__name__ = "Integer32"
_HzOduRadio1OperStatus_Object = MibScalar
hzOduRadio1OperStatus = _HzOduRadio1OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 3, 1),
    _HzOduRadio1OperStatus_Type()
)
hzOduRadio1OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1OperStatus.setStatus("mandatory")


class _HzOduRadio1TransmitPowerDbm_Type(Integer32):
    """Custom type hzOduRadio1TransmitPowerDbm based on Integer32"""
    defaultValue = 0


_HzOduRadio1TransmitPowerDbm_Type.__name__ = "Integer32"
_HzOduRadio1TransmitPowerDbm_Object = MibScalar
hzOduRadio1TransmitPowerDbm = _HzOduRadio1TransmitPowerDbm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 3, 2),
    _HzOduRadio1TransmitPowerDbm_Type()
)
hzOduRadio1TransmitPowerDbm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRadio1TransmitPowerDbm.setStatus("mandatory")


class _HzOduRadio1ProgrammedAntennaDiameter_Type(Integer32):
    """Custom type hzOduRadio1ProgrammedAntennaDiameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("antenna12", 1),
          ("antenna24", 2),
          ("antenna36", 3))
    )


_HzOduRadio1ProgrammedAntennaDiameter_Type.__name__ = "Integer32"
_HzOduRadio1ProgrammedAntennaDiameter_Object = MibScalar
hzOduRadio1ProgrammedAntennaDiameter = _HzOduRadio1ProgrammedAntennaDiameter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 3, 3),
    _HzOduRadio1ProgrammedAntennaDiameter_Type()
)
hzOduRadio1ProgrammedAntennaDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRadio1ProgrammedAntennaDiameter.setStatus("mandatory")


class _HzOduRadio1PowerOption_Type(Integer32):
    """Custom type hzOduRadio1PowerOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("highPower", 2))
    )


_HzOduRadio1PowerOption_Type.__name__ = "Integer32"
_HzOduRadio1PowerOption_Object = MibScalar
hzOduRadio1PowerOption = _HzOduRadio1PowerOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 3, 4),
    _HzOduRadio1PowerOption_Type()
)
hzOduRadio1PowerOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1PowerOption.setStatus("mandatory")


class _HzOduRadio1TxState_Type(Integer32):
    """Custom type hzOduRadio1TxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduRadio1TxState_Type.__name__ = "Integer32"
_HzOduRadio1TxState_Object = MibScalar
hzOduRadio1TxState = _HzOduRadio1TxState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 3, 5),
    _HzOduRadio1TxState_Type()
)
hzOduRadio1TxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1TxState.setStatus("mandatory")
_HzOduRadio1Temperature_Type = Integer32
_HzOduRadio1Temperature_Object = MibScalar
hzOduRadio1Temperature = _HzOduRadio1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 5, 1, 3, 6),
    _HzOduRadio1Temperature_Type()
)
hzOduRadio1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1Temperature.setStatus("mandatory")
_HzOduFrequencies_ObjectIdentity = ObjectIdentity
hzOduFrequencies = _HzOduFrequencies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6)
)


class _HzOduRadioBand_Type(Integer32):
    """Custom type hzOduRadioBand based on Integer32"""
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
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91)
        )
    )
    namedValues = NamedValues(
        *(("freqNone", 1),
          ("fcc23-3-50", 2),
          ("etsi23-3-14", 3),
          ("fcc18-1-50", 4),
          ("ic18-1-50", 5),
          ("brazil18-1-27p5", 6),
          ("brazil18-1-55", 7),
          ("etsi23-3-28", 8),
          ("etsi23-3-56", 9),
          ("uk23-3-56", 10),
          ("itu23-3-14", 11),
          ("itu23-3-28", 12),
          ("itu23-3-56", 13),
          ("etsi18-2-13p75", 14),
          ("etsi18-2-27p5", 15),
          ("etsi18-2-55", 16),
          ("french18-2-13p75", 17),
          ("french18-2-27p5", 18),
          ("fcc23-2-50", 19),
          ("mex23-2-28", 20),
          ("itu23-2-28", 21),
          ("itu23-2-14", 22),
          ("etsi23-2-14", 23),
          ("etsi23-2-28", 24),
          ("etsi23-2-56", 25),
          ("uk23-2-56", 26),
          ("itu23-2-56", 27),
          ("fcc23-1-50", 28),
          ("mex23-1-28", 29),
          ("itu23-1-28", 30),
          ("itu23-1-14", 31),
          ("itu23-1-56", 32),
          ("etsi18-3-13p75", 33),
          ("etsi18-3-27p5", 34),
          ("etsi18-3-55", 35),
          ("france18-3-13p75", 36),
          ("france18-3-27p5", 37),
          ("france23-3-56", 38),
          ("france23-3-28", 39),
          ("france23-3-14", 40),
          ("france23-3-ext-28", 41),
          ("france23-2-14", 42),
          ("france23-2-28", 43),
          ("france23-2-56", 44),
          ("brazil23-2-14", 45),
          ("brazil23-2-28", 46),
          ("brazil23-2-56", 47),
          ("brazil18-1-13p75", 48),
          ("fcc-ic-18-1-40", 49),
          ("fcc11-1-40", 50),
          ("nz11-1-40", 51),
          ("fcc11-1-30a", 52),
          ("fcc11-1-30b", 53),
          ("ic11-1-30", 54),
          ("itu11-1-40", 55),
          ("fcc11-2-40", 56),
          ("nz11-2-40", 57),
          ("fcc11-2-30a", 58),
          ("fcc11-2-30b", 59),
          ("ic11-2-30", 60),
          ("itu11-2-40", 61),
          ("etsi11-1-40", 62),
          ("etsi11-2-40", 63),
          ("ul24-1-50", 64),
          ("mvdds12-1-50", 65),
          ("etsi13-1-14", 66),
          ("etsi13-1-28", 67),
          ("etsi13-2-14", 68),
          ("etsi13-2-28", 69),
          ("fcc28-1-50", 70),
          ("fcc28-1-25", 71),
          ("fcc28-2-50", 72),
          ("fcc28-2-25", 73),
          ("etsi28-3-56", 74),
          ("etsi28-3-28", 75),
          ("etsi28-3-14", 76),
          ("etsi28-4-56", 77),
          ("etsi28-4-28", 78),
          ("etsi28-4-14", 79),
          ("etsi15-4-7", 80),
          ("etsi15-4-14", 81),
          ("etsi15-4-28", 82),
          ("etsi15-4-56", 83),
          ("mex15-4-7", 84),
          ("mex15-4-14", 85),
          ("nz-aus15-4-7", 86),
          ("nz-aus15-4-14", 87),
          ("nz-aus15-4-28", 88),
          ("fcc23-1-40", 89),
          ("fcc23-2-40", 90),
          ("fcc23-3-40", 91))
    )


_HzOduRadioBand_Type.__name__ = "Integer32"
_HzOduRadioBand_Object = MibScalar
hzOduRadioBand = _HzOduRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 1),
    _HzOduRadioBand_Type()
)
hzOduRadioBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRadioBand.setStatus("mandatory")


class _HzOduFreqGroupSelected_Type(Integer32):
    """Custom type hzOduFreqGroupSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("txLow", 1),
          ("txHigh", 2))
    )


_HzOduFreqGroupSelected_Type.__name__ = "Integer32"
_HzOduFreqGroupSelected_Object = MibScalar
hzOduFreqGroupSelected = _HzOduFreqGroupSelected_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 2),
    _HzOduFreqGroupSelected_Type()
)
hzOduFreqGroupSelected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduFreqGroupSelected.setStatus("mandatory")
_HzOduTxHighFreqTable_Object = MibTable
hzOduTxHighFreqTable = _HzOduTxHighFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 3)
)
if mibBuilder.loadTexts:
    hzOduTxHighFreqTable.setStatus("mandatory")
_HzOduTxHighFreqEntry_Object = MibTableRow
hzOduTxHighFreqEntry = _HzOduTxHighFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 3, 1)
)
hzOduTxHighFreqEntry.setIndexNames(
    (0, "HORIZON-ODU-MIB", "hzOduTxHighFreqIndex"),
)
if mibBuilder.loadTexts:
    hzOduTxHighFreqEntry.setStatus("mandatory")
_HzOduTxHighFreqIndex_Type = Integer32
_HzOduTxHighFreqIndex_Object = MibTableColumn
hzOduTxHighFreqIndex = _HzOduTxHighFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 3, 1, 1),
    _HzOduTxHighFreqIndex_Type()
)
hzOduTxHighFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTxHighFreqIndex.setStatus("mandatory")
_HzOduTxHighFreqChannelIndex_Type = DisplayString
_HzOduTxHighFreqChannelIndex_Object = MibTableColumn
hzOduTxHighFreqChannelIndex = _HzOduTxHighFreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 3, 1, 2),
    _HzOduTxHighFreqChannelIndex_Type()
)
hzOduTxHighFreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTxHighFreqChannelIndex.setStatus("mandatory")
_HzOduTxHighFreqTransmitRfFrequency_Type = Integer32
_HzOduTxHighFreqTransmitRfFrequency_Object = MibTableColumn
hzOduTxHighFreqTransmitRfFrequency = _HzOduTxHighFreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 3, 1, 3),
    _HzOduTxHighFreqTransmitRfFrequency_Type()
)
hzOduTxHighFreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTxHighFreqTransmitRfFrequency.setStatus("mandatory")
_HzOduTxHighFreqReceiveRfFrequency_Type = Integer32
_HzOduTxHighFreqReceiveRfFrequency_Object = MibTableColumn
hzOduTxHighFreqReceiveRfFrequency = _HzOduTxHighFreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 3, 1, 4),
    _HzOduTxHighFreqReceiveRfFrequency_Type()
)
hzOduTxHighFreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTxHighFreqReceiveRfFrequency.setStatus("mandatory")


class _HzOduTxHighFreqProgrammed_Type(Integer32):
    """Custom type hzOduTxHighFreqProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzOduTxHighFreqProgrammed_Type.__name__ = "Integer32"
_HzOduTxHighFreqProgrammed_Object = MibTableColumn
hzOduTxHighFreqProgrammed = _HzOduTxHighFreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 3, 1, 5),
    _HzOduTxHighFreqProgrammed_Type()
)
hzOduTxHighFreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduTxHighFreqProgrammed.setStatus("mandatory")
_HzOduTxLowFreqTable_Object = MibTable
hzOduTxLowFreqTable = _HzOduTxLowFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 4)
)
if mibBuilder.loadTexts:
    hzOduTxLowFreqTable.setStatus("mandatory")
_HzOduTxLowFreqEntry_Object = MibTableRow
hzOduTxLowFreqEntry = _HzOduTxLowFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 4, 1)
)
hzOduTxLowFreqEntry.setIndexNames(
    (0, "HORIZON-ODU-MIB", "hzOduTxLowFreqIndex"),
)
if mibBuilder.loadTexts:
    hzOduTxLowFreqEntry.setStatus("mandatory")
_HzOduTxLowFreqIndex_Type = Integer32
_HzOduTxLowFreqIndex_Object = MibTableColumn
hzOduTxLowFreqIndex = _HzOduTxLowFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 4, 1, 1),
    _HzOduTxLowFreqIndex_Type()
)
hzOduTxLowFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTxLowFreqIndex.setStatus("mandatory")
_HzOduTxLowFreqChannelIndex_Type = DisplayString
_HzOduTxLowFreqChannelIndex_Object = MibTableColumn
hzOduTxLowFreqChannelIndex = _HzOduTxLowFreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 4, 1, 2),
    _HzOduTxLowFreqChannelIndex_Type()
)
hzOduTxLowFreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTxLowFreqChannelIndex.setStatus("mandatory")
_HzOduTxLowFreqTransmitRfFrequency_Type = Integer32
_HzOduTxLowFreqTransmitRfFrequency_Object = MibTableColumn
hzOduTxLowFreqTransmitRfFrequency = _HzOduTxLowFreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 4, 1, 3),
    _HzOduTxLowFreqTransmitRfFrequency_Type()
)
hzOduTxLowFreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTxLowFreqTransmitRfFrequency.setStatus("mandatory")
_HzOduTxLowFreqReceiveRfFrequency_Type = Integer32
_HzOduTxLowFreqReceiveRfFrequency_Object = MibTableColumn
hzOduTxLowFreqReceiveRfFrequency = _HzOduTxLowFreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 4, 1, 4),
    _HzOduTxLowFreqReceiveRfFrequency_Type()
)
hzOduTxLowFreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTxLowFreqReceiveRfFrequency.setStatus("mandatory")


class _HzOduTxLowFreqProgrammed_Type(Integer32):
    """Custom type hzOduTxLowFreqProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzOduTxLowFreqProgrammed_Type.__name__ = "Integer32"
_HzOduTxLowFreqProgrammed_Object = MibTableColumn
hzOduTxLowFreqProgrammed = _HzOduTxLowFreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 4, 1, 5),
    _HzOduTxLowFreqProgrammed_Type()
)
hzOduTxLowFreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduTxLowFreqProgrammed.setStatus("mandatory")
_HzOduProgrammedFrequency_ObjectIdentity = ObjectIdentity
hzOduProgrammedFrequency = _HzOduProgrammedFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 5)
)
_HzOduProgrammedFrequencyChannel_Type = DisplayString
_HzOduProgrammedFrequencyChannel_Object = MibScalar
hzOduProgrammedFrequencyChannel = _HzOduProgrammedFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 5, 1),
    _HzOduProgrammedFrequencyChannel_Type()
)
hzOduProgrammedFrequencyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduProgrammedFrequencyChannel.setStatus("mandatory")
_HzOduProgrammedFrequencyTxRf_Type = Integer32
_HzOduProgrammedFrequencyTxRf_Object = MibScalar
hzOduProgrammedFrequencyTxRf = _HzOduProgrammedFrequencyTxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 5, 2),
    _HzOduProgrammedFrequencyTxRf_Type()
)
hzOduProgrammedFrequencyTxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduProgrammedFrequencyTxRf.setStatus("mandatory")
_HzOduProgrammedFrequencyRxRf_Type = Integer32
_HzOduProgrammedFrequencyRxRf_Object = MibScalar
hzOduProgrammedFrequencyRxRf = _HzOduProgrammedFrequencyRxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 6, 5, 3),
    _HzOduProgrammedFrequencyRxRf_Type()
)
hzOduProgrammedFrequencyRxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduProgrammedFrequencyRxRf.setStatus("mandatory")
_HzOduCalendar_ObjectIdentity = ObjectIdentity
hzOduCalendar = _HzOduCalendar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 7)
)
_HzOduDate_Type = DisplayString
_HzOduDate_Object = MibScalar
hzOduDate = _HzOduDate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 7, 1),
    _HzOduDate_Type()
)
hzOduDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduDate.setStatus("mandatory")
_HzOduTime_Type = DisplayString
_HzOduTime_Object = MibScalar
hzOduTime = _HzOduTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 7, 2),
    _HzOduTime_Type()
)
hzOduTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTime.setStatus("mandatory")
_HzOduAlarms_ObjectIdentity = ObjectIdentity
hzOduAlarms = _HzOduAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8)
)


class _HzOduClearAlarmCounters_Type(Integer32):
    """Custom type hzOduClearAlarmCounters based on Integer32"""
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
        *(("nicCounters", 1),
          ("modemCounters", 2),
          ("radioCounters", 3),
          ("allCounters", 4),
          ("otherCounters", 5))
    )


_HzOduClearAlarmCounters_Type.__name__ = "Integer32"
_HzOduClearAlarmCounters_Object = MibScalar
hzOduClearAlarmCounters = _HzOduClearAlarmCounters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 1),
    _HzOduClearAlarmCounters_Type()
)
hzOduClearAlarmCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzOduClearAlarmCounters.setStatus("mandatory")
_HzOduSystemAlarms_ObjectIdentity = ObjectIdentity
hzOduSystemAlarms = _HzOduSystemAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2)
)


class _HzOduExplicitAuthenticationFailure_Type(Integer32):
    """Custom type hzOduExplicitAuthenticationFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduExplicitAuthenticationFailure_Type.__name__ = "Integer32"
_HzOduExplicitAuthenticationFailure_Object = MibScalar
hzOduExplicitAuthenticationFailure = _HzOduExplicitAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 1),
    _HzOduExplicitAuthenticationFailure_Type()
)
hzOduExplicitAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduExplicitAuthenticationFailure.setStatus("mandatory")
_HzOduExplicitAuthenticationFailureCount_Type = Counter32
_HzOduExplicitAuthenticationFailureCount_Object = MibScalar
hzOduExplicitAuthenticationFailureCount = _HzOduExplicitAuthenticationFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 2),
    _HzOduExplicitAuthenticationFailureCount_Type()
)
hzOduExplicitAuthenticationFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduExplicitAuthenticationFailureCount.setStatus("mandatory")


class _HzOduAamConfigMismatch_Type(Integer32):
    """Custom type hzOduAamConfigMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduAamConfigMismatch_Type.__name__ = "Integer32"
_HzOduAamConfigMismatch_Object = MibScalar
hzOduAamConfigMismatch = _HzOduAamConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 3),
    _HzOduAamConfigMismatch_Type()
)
hzOduAamConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduAamConfigMismatch.setStatus("mandatory")
_HzOduAamConfigMismatchCount_Type = Counter32
_HzOduAamConfigMismatchCount_Object = MibScalar
hzOduAamConfigMismatchCount = _HzOduAamConfigMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 4),
    _HzOduAamConfigMismatchCount_Type()
)
hzOduAamConfigMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduAamConfigMismatchCount.setStatus("mandatory")


class _HzOduAamActive_Type(Integer32):
    """Custom type hzOduAamActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduAamActive_Type.__name__ = "Integer32"
_HzOduAamActive_Object = MibScalar
hzOduAamActive = _HzOduAamActive_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 5),
    _HzOduAamActive_Type()
)
hzOduAamActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduAamActive.setStatus("mandatory")
_HzOduAamActiveCount_Type = Counter32
_HzOduAamActiveCount_Object = MibScalar
hzOduAamActiveCount = _HzOduAamActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 6),
    _HzOduAamActiveCount_Type()
)
hzOduAamActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduAamActiveCount.setStatus("mandatory")


class _HzOduAtpcConfigMismatch_Type(Integer32):
    """Custom type hzOduAtpcConfigMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduAtpcConfigMismatch_Type.__name__ = "Integer32"
_HzOduAtpcConfigMismatch_Object = MibScalar
hzOduAtpcConfigMismatch = _HzOduAtpcConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 7),
    _HzOduAtpcConfigMismatch_Type()
)
hzOduAtpcConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduAtpcConfigMismatch.setStatus("mandatory")
_HzOduAtpcConfigMismatchCount_Type = Counter32
_HzOduAtpcConfigMismatchCount_Object = MibScalar
hzOduAtpcConfigMismatchCount = _HzOduAtpcConfigMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 8),
    _HzOduAtpcConfigMismatchCount_Type()
)
hzOduAtpcConfigMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduAtpcConfigMismatchCount.setStatus("mandatory")


class _HzOduSntpServerUnavailableAlarm_Type(Integer32):
    """Custom type hzOduSntpServerUnavailableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduSntpServerUnavailableAlarm_Type.__name__ = "Integer32"
_HzOduSntpServerUnavailableAlarm_Object = MibScalar
hzOduSntpServerUnavailableAlarm = _HzOduSntpServerUnavailableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 9),
    _HzOduSntpServerUnavailableAlarm_Type()
)
hzOduSntpServerUnavailableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSntpServerUnavailableAlarm.setStatus("mandatory")
_HzOduSntpServerUnavailableAlarmCount_Type = Counter32
_HzOduSntpServerUnavailableAlarmCount_Object = MibScalar
hzOduSntpServerUnavailableAlarmCount = _HzOduSntpServerUnavailableAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 10),
    _HzOduSntpServerUnavailableAlarmCount_Type()
)
hzOduSntpServerUnavailableAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSntpServerUnavailableAlarmCount.setStatus("mandatory")


class _HzOduFrequencyFileInvalid_Type(Integer32):
    """Custom type hzOduFrequencyFileInvalid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduFrequencyFileInvalid_Type.__name__ = "Integer32"
_HzOduFrequencyFileInvalid_Object = MibScalar
hzOduFrequencyFileInvalid = _HzOduFrequencyFileInvalid_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 11),
    _HzOduFrequencyFileInvalid_Type()
)
hzOduFrequencyFileInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduFrequencyFileInvalid.setStatus("mandatory")
_HzOduFrequencyFileInvalidCount_Type = Counter32
_HzOduFrequencyFileInvalidCount_Object = MibScalar
hzOduFrequencyFileInvalidCount = _HzOduFrequencyFileInvalidCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 12),
    _HzOduFrequencyFileInvalidCount_Type()
)
hzOduFrequencyFileInvalidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduFrequencyFileInvalidCount.setStatus("mandatory")


class _HzOduAtpcAutoDisabled_Type(Integer32):
    """Custom type hzOduAtpcAutoDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduAtpcAutoDisabled_Type.__name__ = "Integer32"
_HzOduAtpcAutoDisabled_Object = MibScalar
hzOduAtpcAutoDisabled = _HzOduAtpcAutoDisabled_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 13),
    _HzOduAtpcAutoDisabled_Type()
)
hzOduAtpcAutoDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduAtpcAutoDisabled.setStatus("mandatory")
_HzOduAtpcAutoDisabledCount_Type = Counter32
_HzOduAtpcAutoDisabledCount_Object = MibScalar
hzOduAtpcAutoDisabledCount = _HzOduAtpcAutoDisabledCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 14),
    _HzOduAtpcAutoDisabledCount_Type()
)
hzOduAtpcAutoDisabledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduAtpcAutoDisabledCount.setStatus("mandatory")


class _HzOduPartnerRedundancyModeMismatch_Type(Integer32):
    """Custom type hzOduPartnerRedundancyModeMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduPartnerRedundancyModeMismatch_Type.__name__ = "Integer32"
_HzOduPartnerRedundancyModeMismatch_Object = MibScalar
hzOduPartnerRedundancyModeMismatch = _HzOduPartnerRedundancyModeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 15),
    _HzOduPartnerRedundancyModeMismatch_Type()
)
hzOduPartnerRedundancyModeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPartnerRedundancyModeMismatch.setStatus("mandatory")
_HzOduPartnerRedundancyModeMismatchCount_Type = Counter32
_HzOduPartnerRedundancyModeMismatchCount_Object = MibScalar
hzOduPartnerRedundancyModeMismatchCount = _HzOduPartnerRedundancyModeMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 16),
    _HzOduPartnerRedundancyModeMismatchCount_Type()
)
hzOduPartnerRedundancyModeMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPartnerRedundancyModeMismatchCount.setStatus("mandatory")


class _HzOduPartnerConfigurationMismatch_Type(Integer32):
    """Custom type hzOduPartnerConfigurationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduPartnerConfigurationMismatch_Type.__name__ = "Integer32"
_HzOduPartnerConfigurationMismatch_Object = MibScalar
hzOduPartnerConfigurationMismatch = _HzOduPartnerConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 17),
    _HzOduPartnerConfigurationMismatch_Type()
)
hzOduPartnerConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPartnerConfigurationMismatch.setStatus("mandatory")
_HzOduPartnerConfigurationMismatchCount_Type = Counter32
_HzOduPartnerConfigurationMismatchCount_Object = MibScalar
hzOduPartnerConfigurationMismatchCount = _HzOduPartnerConfigurationMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 18),
    _HzOduPartnerConfigurationMismatchCount_Type()
)
hzOduPartnerConfigurationMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPartnerConfigurationMismatchCount.setStatus("mandatory")


class _HzOduHsbActiveOnSecondary_Type(Integer32):
    """Custom type hzOduHsbActiveOnSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduHsbActiveOnSecondary_Type.__name__ = "Integer32"
_HzOduHsbActiveOnSecondary_Object = MibScalar
hzOduHsbActiveOnSecondary = _HzOduHsbActiveOnSecondary_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 19),
    _HzOduHsbActiveOnSecondary_Type()
)
hzOduHsbActiveOnSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduHsbActiveOnSecondary.setStatus("mandatory")
_HzOduHsbActiveOnSecondaryCount_Type = Counter32
_HzOduHsbActiveOnSecondaryCount_Object = MibScalar
hzOduHsbActiveOnSecondaryCount = _HzOduHsbActiveOnSecondaryCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 20),
    _HzOduHsbActiveOnSecondaryCount_Type()
)
hzOduHsbActiveOnSecondaryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduHsbActiveOnSecondaryCount.setStatus("mandatory")


class _HzOduHsbOverrideByUser_Type(Integer32):
    """Custom type hzOduHsbOverrideByUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduHsbOverrideByUser_Type.__name__ = "Integer32"
_HzOduHsbOverrideByUser_Object = MibScalar
hzOduHsbOverrideByUser = _HzOduHsbOverrideByUser_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 21),
    _HzOduHsbOverrideByUser_Type()
)
hzOduHsbOverrideByUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduHsbOverrideByUser.setStatus("mandatory")
_HzOduHsbOverrideByUserCount_Type = Counter32
_HzOduHsbOverrideByUserCount_Object = MibScalar
hzOduHsbOverrideByUserCount = _HzOduHsbOverrideByUserCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 22),
    _HzOduHsbOverrideByUserCount_Type()
)
hzOduHsbOverrideByUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduHsbOverrideByUserCount.setStatus("mandatory")


class _HzOduHsbCrossLinkActive_Type(Integer32):
    """Custom type hzOduHsbCrossLinkActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduHsbCrossLinkActive_Type.__name__ = "Integer32"
_HzOduHsbCrossLinkActive_Object = MibScalar
hzOduHsbCrossLinkActive = _HzOduHsbCrossLinkActive_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 23),
    _HzOduHsbCrossLinkActive_Type()
)
hzOduHsbCrossLinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduHsbCrossLinkActive.setStatus("mandatory")
_HzOduHsbCrossLinkActiveCount_Type = Counter32
_HzOduHsbCrossLinkActiveCount_Object = MibScalar
hzOduHsbCrossLinkActiveCount = _HzOduHsbCrossLinkActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 2, 24),
    _HzOduHsbCrossLinkActiveCount_Type()
)
hzOduHsbCrossLinkActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduHsbCrossLinkActiveCount.setStatus("mandatory")
_HzOduNetworkInterfaceAlarms_ObjectIdentity = ObjectIdentity
hzOduNetworkInterfaceAlarms = _HzOduNetworkInterfaceAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3)
)
_HzOduEnetPort1Alarms_ObjectIdentity = ObjectIdentity
hzOduEnetPort1Alarms = _HzOduEnetPort1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1)
)


class _HzOduEnetPort1DroppedEnetFramesThresholdExceeded_Type(Integer32):
    """Custom type hzOduEnetPort1DroppedEnetFramesThresholdExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduEnetPort1DroppedEnetFramesThresholdExceeded_Type.__name__ = "Integer32"
_HzOduEnetPort1DroppedEnetFramesThresholdExceeded_Object = MibScalar
hzOduEnetPort1DroppedEnetFramesThresholdExceeded = _HzOduEnetPort1DroppedEnetFramesThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1, 1),
    _HzOduEnetPort1DroppedEnetFramesThresholdExceeded_Type()
)
hzOduEnetPort1DroppedEnetFramesThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1DroppedEnetFramesThresholdExceeded.setStatus("mandatory")
_HzOduEnetPort1DroppedEnetFramesThresholdCount_Type = Counter32
_HzOduEnetPort1DroppedEnetFramesThresholdCount_Object = MibScalar
hzOduEnetPort1DroppedEnetFramesThresholdCount = _HzOduEnetPort1DroppedEnetFramesThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1, 2),
    _HzOduEnetPort1DroppedEnetFramesThresholdCount_Type()
)
hzOduEnetPort1DroppedEnetFramesThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1DroppedEnetFramesThresholdCount.setStatus("mandatory")


class _HzOduEnetPort1BandwidthUtilizationThresholdExceeded_Type(Integer32):
    """Custom type hzOduEnetPort1BandwidthUtilizationThresholdExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduEnetPort1BandwidthUtilizationThresholdExceeded_Type.__name__ = "Integer32"
_HzOduEnetPort1BandwidthUtilizationThresholdExceeded_Object = MibScalar
hzOduEnetPort1BandwidthUtilizationThresholdExceeded = _HzOduEnetPort1BandwidthUtilizationThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1, 3),
    _HzOduEnetPort1BandwidthUtilizationThresholdExceeded_Type()
)
hzOduEnetPort1BandwidthUtilizationThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1BandwidthUtilizationThresholdExceeded.setStatus("mandatory")
_HzOduEnetPort1BandwidthUtilizationThresholdCount_Type = Counter32
_HzOduEnetPort1BandwidthUtilizationThresholdCount_Object = MibScalar
hzOduEnetPort1BandwidthUtilizationThresholdCount = _HzOduEnetPort1BandwidthUtilizationThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1, 4),
    _HzOduEnetPort1BandwidthUtilizationThresholdCount_Type()
)
hzOduEnetPort1BandwidthUtilizationThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1BandwidthUtilizationThresholdCount.setStatus("mandatory")


class _HzOduEnetPort1RlsMismatch_Type(Integer32):
    """Custom type hzOduEnetPort1RlsMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduEnetPort1RlsMismatch_Type.__name__ = "Integer32"
_HzOduEnetPort1RlsMismatch_Object = MibScalar
hzOduEnetPort1RlsMismatch = _HzOduEnetPort1RlsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1, 5),
    _HzOduEnetPort1RlsMismatch_Type()
)
hzOduEnetPort1RlsMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1RlsMismatch.setStatus("mandatory")
_HzOduEnetPort1RlsMismatchCount_Type = Counter32
_HzOduEnetPort1RlsMismatchCount_Object = MibScalar
hzOduEnetPort1RlsMismatchCount = _HzOduEnetPort1RlsMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1, 6),
    _HzOduEnetPort1RlsMismatchCount_Type()
)
hzOduEnetPort1RlsMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1RlsMismatchCount.setStatus("mandatory")


class _HzOduEnetPort1RLSShutdownActivated_Type(Integer32):
    """Custom type hzOduEnetPort1RLSShutdownActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduEnetPort1RLSShutdownActivated_Type.__name__ = "Integer32"
_HzOduEnetPort1RLSShutdownActivated_Object = MibScalar
hzOduEnetPort1RLSShutdownActivated = _HzOduEnetPort1RLSShutdownActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1, 7),
    _HzOduEnetPort1RLSShutdownActivated_Type()
)
hzOduEnetPort1RLSShutdownActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1RLSShutdownActivated.setStatus("mandatory")
_HzOduEnetPort1RLSShutdownActivatedCount_Type = Counter32
_HzOduEnetPort1RLSShutdownActivatedCount_Object = MibScalar
hzOduEnetPort1RLSShutdownActivatedCount = _HzOduEnetPort1RLSShutdownActivatedCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1, 8),
    _HzOduEnetPort1RLSShutdownActivatedCount_Type()
)
hzOduEnetPort1RLSShutdownActivatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1RLSShutdownActivatedCount.setStatus("mandatory")


class _HzOduEnetPort1EthernetLinkDown_Type(Integer32):
    """Custom type hzOduEnetPort1EthernetLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduEnetPort1EthernetLinkDown_Type.__name__ = "Integer32"
_HzOduEnetPort1EthernetLinkDown_Object = MibScalar
hzOduEnetPort1EthernetLinkDown = _HzOduEnetPort1EthernetLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1, 9),
    _HzOduEnetPort1EthernetLinkDown_Type()
)
hzOduEnetPort1EthernetLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1EthernetLinkDown.setStatus("mandatory")
_HzOduEnetPort1EthernetLinkDownActivatedCount_Type = Counter32
_HzOduEnetPort1EthernetLinkDownActivatedCount_Object = MibScalar
hzOduEnetPort1EthernetLinkDownActivatedCount = _HzOduEnetPort1EthernetLinkDownActivatedCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 1, 10),
    _HzOduEnetPort1EthernetLinkDownActivatedCount_Type()
)
hzOduEnetPort1EthernetLinkDownActivatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort1EthernetLinkDownActivatedCount.setStatus("mandatory")
_HzOduEnetPort2Alarms_ObjectIdentity = ObjectIdentity
hzOduEnetPort2Alarms = _HzOduEnetPort2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 2)
)


class _HzOduEnetPort2EthernetLinkDown_Type(Integer32):
    """Custom type hzOduEnetPort2EthernetLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduEnetPort2EthernetLinkDown_Type.__name__ = "Integer32"
_HzOduEnetPort2EthernetLinkDown_Object = MibScalar
hzOduEnetPort2EthernetLinkDown = _HzOduEnetPort2EthernetLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 2, 1),
    _HzOduEnetPort2EthernetLinkDown_Type()
)
hzOduEnetPort2EthernetLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2EthernetLinkDown.setStatus("mandatory")
_HzOduEnetPort2EthernetLinkDownActivatedCount_Type = Counter32
_HzOduEnetPort2EthernetLinkDownActivatedCount_Object = MibScalar
hzOduEnetPort2EthernetLinkDownActivatedCount = _HzOduEnetPort2EthernetLinkDownActivatedCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 3, 2, 2),
    _HzOduEnetPort2EthernetLinkDownActivatedCount_Type()
)
hzOduEnetPort2EthernetLinkDownActivatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduEnetPort2EthernetLinkDownActivatedCount.setStatus("mandatory")
_HzOduWirelessInterfaceAlarms_ObjectIdentity = ObjectIdentity
hzOduWirelessInterfaceAlarms = _HzOduWirelessInterfaceAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4)
)
_HzOduModem1Alarms_ObjectIdentity = ObjectIdentity
hzOduModem1Alarms = _HzOduModem1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4)
)


class _HzOduModem1RxLossOfSignal_Type(Integer32):
    """Custom type hzOduModem1RxLossOfSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduModem1RxLossOfSignal_Type.__name__ = "Integer32"
_HzOduModem1RxLossOfSignal_Object = MibScalar
hzOduModem1RxLossOfSignal = _HzOduModem1RxLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 1),
    _HzOduModem1RxLossOfSignal_Type()
)
hzOduModem1RxLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1RxLossOfSignal.setStatus("mandatory")
_HzOduModem1RxLossOfSignalCount_Type = Counter32
_HzOduModem1RxLossOfSignalCount_Object = MibScalar
hzOduModem1RxLossOfSignalCount = _HzOduModem1RxLossOfSignalCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 2),
    _HzOduModem1RxLossOfSignalCount_Type()
)
hzOduModem1RxLossOfSignalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1RxLossOfSignalCount.setStatus("mandatory")


class _HzOduModem1TxLossOfSync_Type(Integer32):
    """Custom type hzOduModem1TxLossOfSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduModem1TxLossOfSync_Type.__name__ = "Integer32"
_HzOduModem1TxLossOfSync_Object = MibScalar
hzOduModem1TxLossOfSync = _HzOduModem1TxLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 3),
    _HzOduModem1TxLossOfSync_Type()
)
hzOduModem1TxLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1TxLossOfSync.setStatus("mandatory")
_HzOduModem1TxLossOfSyncCount_Type = Counter32
_HzOduModem1TxLossOfSyncCount_Object = MibScalar
hzOduModem1TxLossOfSyncCount = _HzOduModem1TxLossOfSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 4),
    _HzOduModem1TxLossOfSyncCount_Type()
)
hzOduModem1TxLossOfSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1TxLossOfSyncCount.setStatus("mandatory")


class _HzOduModem1SnrBelowThreshold_Type(Integer32):
    """Custom type hzOduModem1SnrBelowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduModem1SnrBelowThreshold_Type.__name__ = "Integer32"
_HzOduModem1SnrBelowThreshold_Object = MibScalar
hzOduModem1SnrBelowThreshold = _HzOduModem1SnrBelowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 5),
    _HzOduModem1SnrBelowThreshold_Type()
)
hzOduModem1SnrBelowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1SnrBelowThreshold.setStatus("mandatory")
_HzOduModem1SnrBelowThresholdCount_Type = Counter32
_HzOduModem1SnrBelowThresholdCount_Object = MibScalar
hzOduModem1SnrBelowThresholdCount = _HzOduModem1SnrBelowThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 6),
    _HzOduModem1SnrBelowThresholdCount_Type()
)
hzOduModem1SnrBelowThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1SnrBelowThresholdCount.setStatus("mandatory")


class _HzOduModem1EqualizerStressExceedThreshold_Type(Integer32):
    """Custom type hzOduModem1EqualizerStressExceedThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduModem1EqualizerStressExceedThreshold_Type.__name__ = "Integer32"
_HzOduModem1EqualizerStressExceedThreshold_Object = MibScalar
hzOduModem1EqualizerStressExceedThreshold = _HzOduModem1EqualizerStressExceedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 7),
    _HzOduModem1EqualizerStressExceedThreshold_Type()
)
hzOduModem1EqualizerStressExceedThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1EqualizerStressExceedThreshold.setStatus("mandatory")
_HzOduModem1EquilizerStressExceedThresholdCount_Type = Counter32
_HzOduModem1EquilizerStressExceedThresholdCount_Object = MibScalar
hzOduModem1EquilizerStressExceedThresholdCount = _HzOduModem1EquilizerStressExceedThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 8),
    _HzOduModem1EquilizerStressExceedThresholdCount_Type()
)
hzOduModem1EquilizerStressExceedThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1EquilizerStressExceedThresholdCount.setStatus("mandatory")


class _HzOduModem1HardwareFault_Type(Integer32):
    """Custom type hzOduModem1HardwareFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduModem1HardwareFault_Type.__name__ = "Integer32"
_HzOduModem1HardwareFault_Object = MibScalar
hzOduModem1HardwareFault = _HzOduModem1HardwareFault_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 9),
    _HzOduModem1HardwareFault_Type()
)
hzOduModem1HardwareFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1HardwareFault.setStatus("mandatory")
_HzOduModem1HardwareFaultCount_Type = Counter32
_HzOduModem1HardwareFaultCount_Object = MibScalar
hzOduModem1HardwareFaultCount = _HzOduModem1HardwareFaultCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 10),
    _HzOduModem1HardwareFaultCount_Type()
)
hzOduModem1HardwareFaultCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1HardwareFaultCount.setStatus("mandatory")


class _HzOduModem1ProgrammingError_Type(Integer32):
    """Custom type hzOduModem1ProgrammingError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduModem1ProgrammingError_Type.__name__ = "Integer32"
_HzOduModem1ProgrammingError_Object = MibScalar
hzOduModem1ProgrammingError = _HzOduModem1ProgrammingError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 11),
    _HzOduModem1ProgrammingError_Type()
)
hzOduModem1ProgrammingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1ProgrammingError.setStatus("mandatory")
_HzOduModem1ProgrammingErrorCount_Type = Counter32
_HzOduModem1ProgrammingErrorCount_Object = MibScalar
hzOduModem1ProgrammingErrorCount = _HzOduModem1ProgrammingErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 4, 12),
    _HzOduModem1ProgrammingErrorCount_Type()
)
hzOduModem1ProgrammingErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduModem1ProgrammingErrorCount.setStatus("mandatory")
_HzOduRadio1Alarms_ObjectIdentity = ObjectIdentity
hzOduRadio1Alarms = _HzOduRadio1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5)
)


class _HzOduRadio1SynthLostLock_Type(Integer32):
    """Custom type hzOduRadio1SynthLostLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduRadio1SynthLostLock_Type.__name__ = "Integer32"
_HzOduRadio1SynthLostLock_Object = MibScalar
hzOduRadio1SynthLostLock = _HzOduRadio1SynthLostLock_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5, 1),
    _HzOduRadio1SynthLostLock_Type()
)
hzOduRadio1SynthLostLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1SynthLostLock.setStatus("mandatory")
_HzOduRadio1SynthLostLockCount_Type = Counter32
_HzOduRadio1SynthLostLockCount_Object = MibScalar
hzOduRadio1SynthLostLockCount = _HzOduRadio1SynthLostLockCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5, 2),
    _HzOduRadio1SynthLostLockCount_Type()
)
hzOduRadio1SynthLostLockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1SynthLostLockCount.setStatus("mandatory")


class _HzOduRadio1TempCompCalTableNotAvail_Type(Integer32):
    """Custom type hzOduRadio1TempCompCalTableNotAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduRadio1TempCompCalTableNotAvail_Type.__name__ = "Integer32"
_HzOduRadio1TempCompCalTableNotAvail_Object = MibScalar
hzOduRadio1TempCompCalTableNotAvail = _HzOduRadio1TempCompCalTableNotAvail_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5, 3),
    _HzOduRadio1TempCompCalTableNotAvail_Type()
)
hzOduRadio1TempCompCalTableNotAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1TempCompCalTableNotAvail.setStatus("mandatory")
_HzOduRadio1TempCompCalTableNotAvailCount_Type = Counter32
_HzOduRadio1TempCompCalTableNotAvailCount_Object = MibScalar
hzOduRadio1TempCompCalTableNotAvailCount = _HzOduRadio1TempCompCalTableNotAvailCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5, 4),
    _HzOduRadio1TempCompCalTableNotAvailCount_Type()
)
hzOduRadio1TempCompCalTableNotAvailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1TempCompCalTableNotAvailCount.setStatus("mandatory")


class _HzOduRadio1TxDetectorPwrBelowThresh_Type(Integer32):
    """Custom type hzOduRadio1TxDetectorPwrBelowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduRadio1TxDetectorPwrBelowThresh_Type.__name__ = "Integer32"
_HzOduRadio1TxDetectorPwrBelowThresh_Object = MibScalar
hzOduRadio1TxDetectorPwrBelowThresh = _HzOduRadio1TxDetectorPwrBelowThresh_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5, 5),
    _HzOduRadio1TxDetectorPwrBelowThresh_Type()
)
hzOduRadio1TxDetectorPwrBelowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1TxDetectorPwrBelowThresh.setStatus("mandatory")
_HzOduRadio1TxDetectorPwrBelowThreshCount_Type = Counter32
_HzOduRadio1TxDetectorPwrBelowThreshCount_Object = MibScalar
hzOduRadio1TxDetectorPwrBelowThreshCount = _HzOduRadio1TxDetectorPwrBelowThreshCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5, 6),
    _HzOduRadio1TxDetectorPwrBelowThreshCount_Type()
)
hzOduRadio1TxDetectorPwrBelowThreshCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1TxDetectorPwrBelowThreshCount.setStatus("mandatory")


class _HzOduRadio1DrainCurrentOutOfLimit_Type(Integer32):
    """Custom type hzOduRadio1DrainCurrentOutOfLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduRadio1DrainCurrentOutOfLimit_Type.__name__ = "Integer32"
_HzOduRadio1DrainCurrentOutOfLimit_Object = MibScalar
hzOduRadio1DrainCurrentOutOfLimit = _HzOduRadio1DrainCurrentOutOfLimit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5, 7),
    _HzOduRadio1DrainCurrentOutOfLimit_Type()
)
hzOduRadio1DrainCurrentOutOfLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1DrainCurrentOutOfLimit.setStatus("mandatory")
_HzOduRadio1DrainCurrentOutOfLimitCount_Type = Counter32
_HzOduRadio1DrainCurrentOutOfLimitCount_Object = MibScalar
hzOduRadio1DrainCurrentOutOfLimitCount = _HzOduRadio1DrainCurrentOutOfLimitCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5, 8),
    _HzOduRadio1DrainCurrentOutOfLimitCount_Type()
)
hzOduRadio1DrainCurrentOutOfLimitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1DrainCurrentOutOfLimitCount.setStatus("mandatory")


class _HzOduRadio1TemperatureOutOfLimit_Type(Integer32):
    """Custom type hzOduRadio1TemperatureOutOfLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduRadio1TemperatureOutOfLimit_Type.__name__ = "Integer32"
_HzOduRadio1TemperatureOutOfLimit_Object = MibScalar
hzOduRadio1TemperatureOutOfLimit = _HzOduRadio1TemperatureOutOfLimit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5, 9),
    _HzOduRadio1TemperatureOutOfLimit_Type()
)
hzOduRadio1TemperatureOutOfLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1TemperatureOutOfLimit.setStatus("mandatory")
_HzOduRadio1TemperatureOutOfLimitCount_Type = Counter32
_HzOduRadio1TemperatureOutOfLimitCount_Object = MibScalar
hzOduRadio1TemperatureOutOfLimitCount = _HzOduRadio1TemperatureOutOfLimitCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 8, 4, 5, 10),
    _HzOduRadio1TemperatureOutOfLimitCount_Type()
)
hzOduRadio1TemperatureOutOfLimitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadio1TemperatureOutOfLimitCount.setStatus("mandatory")
_HzOduTraps_ObjectIdentity = ObjectIdentity
hzOduTraps = _HzOduTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9)
)
_HzOduSnmpTrapHostTable_Object = MibTable
hzOduSnmpTrapHostTable = _HzOduSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    hzOduSnmpTrapHostTable.setStatus("mandatory")
_HzOduSnmpTrapHostEntry_Object = MibTableRow
hzOduSnmpTrapHostEntry = _HzOduSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 1, 1)
)
hzOduSnmpTrapHostEntry.setIndexNames(
    (0, "HORIZON-ODU-MIB", "hzOduSnmpTrapHostIndex"),
)
if mibBuilder.loadTexts:
    hzOduSnmpTrapHostEntry.setStatus("mandatory")
_HzOduSnmpTrapHostIndex_Type = Integer32
_HzOduSnmpTrapHostIndex_Object = MibTableColumn
hzOduSnmpTrapHostIndex = _HzOduSnmpTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 1, 1, 1),
    _HzOduSnmpTrapHostIndex_Type()
)
hzOduSnmpTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpTrapHostIndex.setStatus("mandatory")


class _HzOduSnmpTrapHostMode_Type(Integer32):
    """Custom type hzOduSnmpTrapHostMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dns", 2))
    )


_HzOduSnmpTrapHostMode_Type.__name__ = "Integer32"
_HzOduSnmpTrapHostMode_Object = MibTableColumn
hzOduSnmpTrapHostMode = _HzOduSnmpTrapHostMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 1, 1, 2),
    _HzOduSnmpTrapHostMode_Type()
)
hzOduSnmpTrapHostMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpTrapHostMode.setStatus("mandatory")
_HzOduSnmpTrapHostIpAddress_Type = IpAddress
_HzOduSnmpTrapHostIpAddress_Object = MibTableColumn
hzOduSnmpTrapHostIpAddress = _HzOduSnmpTrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 1, 1, 3),
    _HzOduSnmpTrapHostIpAddress_Type()
)
hzOduSnmpTrapHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpTrapHostIpAddress.setStatus("mandatory")


class _HzOduSnmpTrapHostCommunityName_Type(DisplayString):
    """Custom type hzOduSnmpTrapHostCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduSnmpTrapHostCommunityName_Type.__name__ = "DisplayString"
_HzOduSnmpTrapHostCommunityName_Object = MibTableColumn
hzOduSnmpTrapHostCommunityName = _HzOduSnmpTrapHostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 1, 1, 4),
    _HzOduSnmpTrapHostCommunityName_Type()
)
hzOduSnmpTrapHostCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpTrapHostCommunityName.setStatus("mandatory")


class _HzOduSnmpTrapHostActivated_Type(Integer32):
    """Custom type hzOduSnmpTrapHostActivated based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzOduSnmpTrapHostActivated_Type.__name__ = "Integer32"
_HzOduSnmpTrapHostActivated_Object = MibTableColumn
hzOduSnmpTrapHostActivated = _HzOduSnmpTrapHostActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 1, 1, 5),
    _HzOduSnmpTrapHostActivated_Type()
)
hzOduSnmpTrapHostActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpTrapHostActivated.setStatus("mandatory")
_HzOduSnmpV3TrapHostsTable_Object = MibTable
hzOduSnmpV3TrapHostsTable = _HzOduSnmpV3TrapHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 2)
)
if mibBuilder.loadTexts:
    hzOduSnmpV3TrapHostsTable.setStatus("mandatory")
_HzOduSnmpV3TrapHostsEntry_Object = MibTableRow
hzOduSnmpV3TrapHostsEntry = _HzOduSnmpV3TrapHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 2, 1)
)
hzOduSnmpV3TrapHostsEntry.setIndexNames(
    (0, "HORIZON-ODU-MIB", "hzOduSnmpV3TrapHostsIndex"),
)
if mibBuilder.loadTexts:
    hzOduSnmpV3TrapHostsEntry.setStatus("mandatory")
_HzOduSnmpV3TrapHostsIndex_Type = Integer32
_HzOduSnmpV3TrapHostsIndex_Object = MibTableColumn
hzOduSnmpV3TrapHostsIndex = _HzOduSnmpV3TrapHostsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 2, 1, 1),
    _HzOduSnmpV3TrapHostsIndex_Type()
)
hzOduSnmpV3TrapHostsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpV3TrapHostsIndex.setStatus("mandatory")
_SnmpV3TrapHostIpAddress_Type = IpAddress
_SnmpV3TrapHostIpAddress_Object = MibTableColumn
snmpV3TrapHostIpAddress = _SnmpV3TrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 2, 1, 2),
    _SnmpV3TrapHostIpAddress_Type()
)
snmpV3TrapHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostIpAddress.setStatus("mandatory")


class _SnmpV3TrapHostUserName_Type(DisplayString):
    """Custom type snmpV3TrapHostUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SnmpV3TrapHostUserName_Type.__name__ = "DisplayString"
_SnmpV3TrapHostUserName_Object = MibTableColumn
snmpV3TrapHostUserName = _SnmpV3TrapHostUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 2, 1, 3),
    _SnmpV3TrapHostUserName_Type()
)
snmpV3TrapHostUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostUserName.setStatus("mandatory")


class _SnmpV3TrapHostAuthProtocol_Type(Integer32):
    """Custom type snmpV3TrapHostAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("md5", 2),
          ("sha", 3))
    )


_SnmpV3TrapHostAuthProtocol_Type.__name__ = "Integer32"
_SnmpV3TrapHostAuthProtocol_Object = MibTableColumn
snmpV3TrapHostAuthProtocol = _SnmpV3TrapHostAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 2, 1, 4),
    _SnmpV3TrapHostAuthProtocol_Type()
)
snmpV3TrapHostAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostAuthProtocol.setStatus("mandatory")


class _SnmpV3TrapHostAuthPassword_Type(DisplayString):
    """Custom type snmpV3TrapHostAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SnmpV3TrapHostAuthPassword_Type.__name__ = "DisplayString"
_SnmpV3TrapHostAuthPassword_Object = MibTableColumn
snmpV3TrapHostAuthPassword = _SnmpV3TrapHostAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 2, 1, 5),
    _SnmpV3TrapHostAuthPassword_Type()
)
snmpV3TrapHostAuthPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostAuthPassword.setStatus("mandatory")


class _SnmpV3TrapHostPrivProtocol_Type(Integer32):
    """Custom type snmpV3TrapHostPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPriv", 1),
          ("des", 2))
    )


_SnmpV3TrapHostPrivProtocol_Type.__name__ = "Integer32"
_SnmpV3TrapHostPrivProtocol_Object = MibTableColumn
snmpV3TrapHostPrivProtocol = _SnmpV3TrapHostPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 2, 1, 6),
    _SnmpV3TrapHostPrivProtocol_Type()
)
snmpV3TrapHostPrivProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostPrivProtocol.setStatus("mandatory")


class _SnmpV3TrapHostPrivPassword_Type(DisplayString):
    """Custom type snmpV3TrapHostPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SnmpV3TrapHostPrivPassword_Type.__name__ = "DisplayString"
_SnmpV3TrapHostPrivPassword_Object = MibTableColumn
snmpV3TrapHostPrivPassword = _SnmpV3TrapHostPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 2, 1, 7),
    _SnmpV3TrapHostPrivPassword_Type()
)
snmpV3TrapHostPrivPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostPrivPassword.setStatus("mandatory")


class _SnmpV3TrapHostActivated_Type(Integer32):
    """Custom type snmpV3TrapHostActivated based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_SnmpV3TrapHostActivated_Type.__name__ = "Integer32"
_SnmpV3TrapHostActivated_Object = MibTableColumn
snmpV3TrapHostActivated = _SnmpV3TrapHostActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 2, 1, 8),
    _SnmpV3TrapHostActivated_Type()
)
snmpV3TrapHostActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostActivated.setStatus("mandatory")


class _HzOduColdStartTrap_Type(Integer32):
    """Custom type hzOduColdStartTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduColdStartTrap_Type.__name__ = "Integer32"
_HzOduColdStartTrap_Object = MibScalar
hzOduColdStartTrap = _HzOduColdStartTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 3),
    _HzOduColdStartTrap_Type()
)
hzOduColdStartTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduColdStartTrap.setStatus("mandatory")


class _HzOduLinkDownTrap_Type(Integer32):
    """Custom type hzOduLinkDownTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduLinkDownTrap_Type.__name__ = "Integer32"
_HzOduLinkDownTrap_Object = MibScalar
hzOduLinkDownTrap = _HzOduLinkDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 4),
    _HzOduLinkDownTrap_Type()
)
hzOduLinkDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduLinkDownTrap.setStatus("mandatory")


class _HzOduLinkUpTrap_Type(Integer32):
    """Custom type hzOduLinkUpTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduLinkUpTrap_Type.__name__ = "Integer32"
_HzOduLinkUpTrap_Object = MibScalar
hzOduLinkUpTrap = _HzOduLinkUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 5),
    _HzOduLinkUpTrap_Type()
)
hzOduLinkUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduLinkUpTrap.setStatus("mandatory")


class _HzOduExplicitAuthenticationFailureTrap_Type(Integer32):
    """Custom type hzOduExplicitAuthenticationFailureTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduExplicitAuthenticationFailureTrap_Type.__name__ = "Integer32"
_HzOduExplicitAuthenticationFailureTrap_Object = MibScalar
hzOduExplicitAuthenticationFailureTrap = _HzOduExplicitAuthenticationFailureTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 6),
    _HzOduExplicitAuthenticationFailureTrap_Type()
)
hzOduExplicitAuthenticationFailureTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduExplicitAuthenticationFailureTrap.setStatus("mandatory")


class _HzOduAamConfigMismatchTrap_Type(Integer32):
    """Custom type hzOduAamConfigMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduAamConfigMismatchTrap_Type.__name__ = "Integer32"
_HzOduAamConfigMismatchTrap_Object = MibScalar
hzOduAamConfigMismatchTrap = _HzOduAamConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 7),
    _HzOduAamConfigMismatchTrap_Type()
)
hzOduAamConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduAamConfigMismatchTrap.setStatus("mandatory")


class _HzOduAamActiveTrap_Type(Integer32):
    """Custom type hzOduAamActiveTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduAamActiveTrap_Type.__name__ = "Integer32"
_HzOduAamActiveTrap_Object = MibScalar
hzOduAamActiveTrap = _HzOduAamActiveTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 8),
    _HzOduAamActiveTrap_Type()
)
hzOduAamActiveTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduAamActiveTrap.setStatus("mandatory")


class _HzOduAtpcConfigMismatchTrap_Type(Integer32):
    """Custom type hzOduAtpcConfigMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduAtpcConfigMismatchTrap_Type.__name__ = "Integer32"
_HzOduAtpcConfigMismatchTrap_Object = MibScalar
hzOduAtpcConfigMismatchTrap = _HzOduAtpcConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 9),
    _HzOduAtpcConfigMismatchTrap_Type()
)
hzOduAtpcConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduAtpcConfigMismatchTrap.setStatus("mandatory")


class _HzOduSntpServersUnreachableTrap_Type(Integer32):
    """Custom type hzOduSntpServersUnreachableTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduSntpServersUnreachableTrap_Type.__name__ = "Integer32"
_HzOduSntpServersUnreachableTrap_Object = MibScalar
hzOduSntpServersUnreachableTrap = _HzOduSntpServersUnreachableTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 10),
    _HzOduSntpServersUnreachableTrap_Type()
)
hzOduSntpServersUnreachableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduSntpServersUnreachableTrap.setStatus("mandatory")


class _HzOduFrequencyFileInvalidTrap_Type(Integer32):
    """Custom type hzOduFrequencyFileInvalidTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduFrequencyFileInvalidTrap_Type.__name__ = "Integer32"
_HzOduFrequencyFileInvalidTrap_Object = MibScalar
hzOduFrequencyFileInvalidTrap = _HzOduFrequencyFileInvalidTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 11),
    _HzOduFrequencyFileInvalidTrap_Type()
)
hzOduFrequencyFileInvalidTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduFrequencyFileInvalidTrap.setStatus("mandatory")


class _HzOduEnetPort1DroppedFramesThresholdExceedTrap_Type(Integer32):
    """Custom type hzOduEnetPort1DroppedFramesThresholdExceedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduEnetPort1DroppedFramesThresholdExceedTrap_Type.__name__ = "Integer32"
_HzOduEnetPort1DroppedFramesThresholdExceedTrap_Object = MibScalar
hzOduEnetPort1DroppedFramesThresholdExceedTrap = _HzOduEnetPort1DroppedFramesThresholdExceedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 12),
    _HzOduEnetPort1DroppedFramesThresholdExceedTrap_Type()
)
hzOduEnetPort1DroppedFramesThresholdExceedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1DroppedFramesThresholdExceedTrap.setStatus("mandatory")


class _HzOduEnetPort1BandwidthUtilizationThresholdExceedTrap_Type(Integer32):
    """Custom type hzOduEnetPort1BandwidthUtilizationThresholdExceedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduEnetPort1BandwidthUtilizationThresholdExceedTrap_Type.__name__ = "Integer32"
_HzOduEnetPort1BandwidthUtilizationThresholdExceedTrap_Object = MibScalar
hzOduEnetPort1BandwidthUtilizationThresholdExceedTrap = _HzOduEnetPort1BandwidthUtilizationThresholdExceedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 13),
    _HzOduEnetPort1BandwidthUtilizationThresholdExceedTrap_Type()
)
hzOduEnetPort1BandwidthUtilizationThresholdExceedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1BandwidthUtilizationThresholdExceedTrap.setStatus("mandatory")


class _HzOduEnetPort1RlsMismatchTrap_Type(Integer32):
    """Custom type hzOduEnetPort1RlsMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduEnetPort1RlsMismatchTrap_Type.__name__ = "Integer32"
_HzOduEnetPort1RlsMismatchTrap_Object = MibScalar
hzOduEnetPort1RlsMismatchTrap = _HzOduEnetPort1RlsMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 14),
    _HzOduEnetPort1RlsMismatchTrap_Type()
)
hzOduEnetPort1RlsMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1RlsMismatchTrap.setStatus("mandatory")


class _HzOduEnetPort1RLSShutdownActivatedTrap_Type(Integer32):
    """Custom type hzOduEnetPort1RLSShutdownActivatedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduEnetPort1RLSShutdownActivatedTrap_Type.__name__ = "Integer32"
_HzOduEnetPort1RLSShutdownActivatedTrap_Object = MibScalar
hzOduEnetPort1RLSShutdownActivatedTrap = _HzOduEnetPort1RLSShutdownActivatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 15),
    _HzOduEnetPort1RLSShutdownActivatedTrap_Type()
)
hzOduEnetPort1RLSShutdownActivatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEnetPort1RLSShutdownActivatedTrap.setStatus("mandatory")


class _HzOduModem1RxLossOfSignalLockTrap_Type(Integer32):
    """Custom type hzOduModem1RxLossOfSignalLockTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduModem1RxLossOfSignalLockTrap_Type.__name__ = "Integer32"
_HzOduModem1RxLossOfSignalLockTrap_Object = MibScalar
hzOduModem1RxLossOfSignalLockTrap = _HzOduModem1RxLossOfSignalLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 16),
    _HzOduModem1RxLossOfSignalLockTrap_Type()
)
hzOduModem1RxLossOfSignalLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduModem1RxLossOfSignalLockTrap.setStatus("mandatory")


class _HzOduModem1TxLossOfSyncTrap_Type(Integer32):
    """Custom type hzOduModem1TxLossOfSyncTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduModem1TxLossOfSyncTrap_Type.__name__ = "Integer32"
_HzOduModem1TxLossOfSyncTrap_Object = MibScalar
hzOduModem1TxLossOfSyncTrap = _HzOduModem1TxLossOfSyncTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 17),
    _HzOduModem1TxLossOfSyncTrap_Type()
)
hzOduModem1TxLossOfSyncTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduModem1TxLossOfSyncTrap.setStatus("mandatory")


class _HzOduModem1SnrBelowThresholdTrap_Type(Integer32):
    """Custom type hzOduModem1SnrBelowThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduModem1SnrBelowThresholdTrap_Type.__name__ = "Integer32"
_HzOduModem1SnrBelowThresholdTrap_Object = MibScalar
hzOduModem1SnrBelowThresholdTrap = _HzOduModem1SnrBelowThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 18),
    _HzOduModem1SnrBelowThresholdTrap_Type()
)
hzOduModem1SnrBelowThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduModem1SnrBelowThresholdTrap.setStatus("mandatory")


class _HzOduModem1EqualizerStressExceedThresholdTrap_Type(Integer32):
    """Custom type hzOduModem1EqualizerStressExceedThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduModem1EqualizerStressExceedThresholdTrap_Type.__name__ = "Integer32"
_HzOduModem1EqualizerStressExceedThresholdTrap_Object = MibScalar
hzOduModem1EqualizerStressExceedThresholdTrap = _HzOduModem1EqualizerStressExceedThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 19),
    _HzOduModem1EqualizerStressExceedThresholdTrap_Type()
)
hzOduModem1EqualizerStressExceedThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduModem1EqualizerStressExceedThresholdTrap.setStatus("mandatory")


class _HzOduModem1ChannelizedRslBelowThresholdTrap_Type(Integer32):
    """Custom type hzOduModem1ChannelizedRslBelowThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduModem1ChannelizedRslBelowThresholdTrap_Type.__name__ = "Integer32"
_HzOduModem1ChannelizedRslBelowThresholdTrap_Object = MibScalar
hzOduModem1ChannelizedRslBelowThresholdTrap = _HzOduModem1ChannelizedRslBelowThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 20),
    _HzOduModem1ChannelizedRslBelowThresholdTrap_Type()
)
hzOduModem1ChannelizedRslBelowThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduModem1ChannelizedRslBelowThresholdTrap.setStatus("mandatory")


class _HzOduModem1HardwareFaultTrap_Type(Integer32):
    """Custom type hzOduModem1HardwareFaultTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduModem1HardwareFaultTrap_Type.__name__ = "Integer32"
_HzOduModem1HardwareFaultTrap_Object = MibScalar
hzOduModem1HardwareFaultTrap = _HzOduModem1HardwareFaultTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 21),
    _HzOduModem1HardwareFaultTrap_Type()
)
hzOduModem1HardwareFaultTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduModem1HardwareFaultTrap.setStatus("mandatory")


class _HzOduModem1ProgrammingErrorTrap_Type(Integer32):
    """Custom type hzOduModem1ProgrammingErrorTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduModem1ProgrammingErrorTrap_Type.__name__ = "Integer32"
_HzOduModem1ProgrammingErrorTrap_Object = MibScalar
hzOduModem1ProgrammingErrorTrap = _HzOduModem1ProgrammingErrorTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 22),
    _HzOduModem1ProgrammingErrorTrap_Type()
)
hzOduModem1ProgrammingErrorTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduModem1ProgrammingErrorTrap.setStatus("mandatory")


class _HzOduRadio1SynthLostLockTrap_Type(Integer32):
    """Custom type hzOduRadio1SynthLostLockTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduRadio1SynthLostLockTrap_Type.__name__ = "Integer32"
_HzOduRadio1SynthLostLockTrap_Object = MibScalar
hzOduRadio1SynthLostLockTrap = _HzOduRadio1SynthLostLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 23),
    _HzOduRadio1SynthLostLockTrap_Type()
)
hzOduRadio1SynthLostLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRadio1SynthLostLockTrap.setStatus("mandatory")


class _HzOduRadio1TempCompCalTableNotAvailTrap_Type(Integer32):
    """Custom type hzOduRadio1TempCompCalTableNotAvailTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduRadio1TempCompCalTableNotAvailTrap_Type.__name__ = "Integer32"
_HzOduRadio1TempCompCalTableNotAvailTrap_Object = MibScalar
hzOduRadio1TempCompCalTableNotAvailTrap = _HzOduRadio1TempCompCalTableNotAvailTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 24),
    _HzOduRadio1TempCompCalTableNotAvailTrap_Type()
)
hzOduRadio1TempCompCalTableNotAvailTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRadio1TempCompCalTableNotAvailTrap.setStatus("mandatory")


class _HzOduRadio1TxDetectorPwrBelowThreshTrap_Type(Integer32):
    """Custom type hzOduRadio1TxDetectorPwrBelowThreshTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduRadio1TxDetectorPwrBelowThreshTrap_Type.__name__ = "Integer32"
_HzOduRadio1TxDetectorPwrBelowThreshTrap_Object = MibScalar
hzOduRadio1TxDetectorPwrBelowThreshTrap = _HzOduRadio1TxDetectorPwrBelowThreshTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 25),
    _HzOduRadio1TxDetectorPwrBelowThreshTrap_Type()
)
hzOduRadio1TxDetectorPwrBelowThreshTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRadio1TxDetectorPwrBelowThreshTrap.setStatus("mandatory")


class _HzOduRadio1DrainCurrentOutOfLimitTrap_Type(Integer32):
    """Custom type hzOduRadio1DrainCurrentOutOfLimitTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduRadio1DrainCurrentOutOfLimitTrap_Type.__name__ = "Integer32"
_HzOduRadio1DrainCurrentOutOfLimitTrap_Object = MibScalar
hzOduRadio1DrainCurrentOutOfLimitTrap = _HzOduRadio1DrainCurrentOutOfLimitTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 26),
    _HzOduRadio1DrainCurrentOutOfLimitTrap_Type()
)
hzOduRadio1DrainCurrentOutOfLimitTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRadio1DrainCurrentOutOfLimitTrap.setStatus("mandatory")


class _HzOduRadio1TemperatureOutOfLimitTrap_Type(Integer32):
    """Custom type hzOduRadio1TemperatureOutOfLimitTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduRadio1TemperatureOutOfLimitTrap_Type.__name__ = "Integer32"
_HzOduRadio1TemperatureOutOfLimitTrap_Object = MibScalar
hzOduRadio1TemperatureOutOfLimitTrap = _HzOduRadio1TemperatureOutOfLimitTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 27),
    _HzOduRadio1TemperatureOutOfLimitTrap_Type()
)
hzOduRadio1TemperatureOutOfLimitTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRadio1TemperatureOutOfLimitTrap.setStatus("mandatory")


class _HzOduTtyManagementSessionCommencedTrap_Type(Integer32):
    """Custom type hzOduTtyManagementSessionCommencedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduTtyManagementSessionCommencedTrap_Type.__name__ = "Integer32"
_HzOduTtyManagementSessionCommencedTrap_Object = MibScalar
hzOduTtyManagementSessionCommencedTrap = _HzOduTtyManagementSessionCommencedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 28),
    _HzOduTtyManagementSessionCommencedTrap_Type()
)
hzOduTtyManagementSessionCommencedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduTtyManagementSessionCommencedTrap.setStatus("mandatory")


class _HzOduTtyManagementSessionTerminatedTrap_Type(Integer32):
    """Custom type hzOduTtyManagementSessionTerminatedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduTtyManagementSessionTerminatedTrap_Type.__name__ = "Integer32"
_HzOduTtyManagementSessionTerminatedTrap_Object = MibScalar
hzOduTtyManagementSessionTerminatedTrap = _HzOduTtyManagementSessionTerminatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 29),
    _HzOduTtyManagementSessionTerminatedTrap_Type()
)
hzOduTtyManagementSessionTerminatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduTtyManagementSessionTerminatedTrap.setStatus("mandatory")


class _HzOduAtpcAutoDisabledTrap_Type(Integer32):
    """Custom type hzOduAtpcAutoDisabledTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduAtpcAutoDisabledTrap_Type.__name__ = "Integer32"
_HzOduAtpcAutoDisabledTrap_Object = MibScalar
hzOduAtpcAutoDisabledTrap = _HzOduAtpcAutoDisabledTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 30),
    _HzOduAtpcAutoDisabledTrap_Type()
)
hzOduAtpcAutoDisabledTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduAtpcAutoDisabledTrap.setStatus("mandatory")


class _HzOduPartnerRedundancyModeMismatchTrap_Type(Integer32):
    """Custom type hzOduPartnerRedundancyModeMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduPartnerRedundancyModeMismatchTrap_Type.__name__ = "Integer32"
_HzOduPartnerRedundancyModeMismatchTrap_Object = MibScalar
hzOduPartnerRedundancyModeMismatchTrap = _HzOduPartnerRedundancyModeMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 31),
    _HzOduPartnerRedundancyModeMismatchTrap_Type()
)
hzOduPartnerRedundancyModeMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPartnerRedundancyModeMismatchTrap.setStatus("mandatory")


class _HzOduPartnerConfigurationMismatchTrap_Type(Integer32):
    """Custom type hzOduPartnerConfigurationMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduPartnerConfigurationMismatchTrap_Type.__name__ = "Integer32"
_HzOduPartnerConfigurationMismatchTrap_Object = MibScalar
hzOduPartnerConfigurationMismatchTrap = _HzOduPartnerConfigurationMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 32),
    _HzOduPartnerConfigurationMismatchTrap_Type()
)
hzOduPartnerConfigurationMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPartnerConfigurationMismatchTrap.setStatus("mandatory")


class _HzOduHsbActiveOnSecondaryTrap_Type(Integer32):
    """Custom type hzOduHsbActiveOnSecondaryTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduHsbActiveOnSecondaryTrap_Type.__name__ = "Integer32"
_HzOduHsbActiveOnSecondaryTrap_Object = MibScalar
hzOduHsbActiveOnSecondaryTrap = _HzOduHsbActiveOnSecondaryTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 33),
    _HzOduHsbActiveOnSecondaryTrap_Type()
)
hzOduHsbActiveOnSecondaryTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHsbActiveOnSecondaryTrap.setStatus("mandatory")


class _HzOduHsbOverrideByUserTrap_Type(Integer32):
    """Custom type hzOduHsbOverrideByUserTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduHsbOverrideByUserTrap_Type.__name__ = "Integer32"
_HzOduHsbOverrideByUserTrap_Object = MibScalar
hzOduHsbOverrideByUserTrap = _HzOduHsbOverrideByUserTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 34),
    _HzOduHsbOverrideByUserTrap_Type()
)
hzOduHsbOverrideByUserTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHsbOverrideByUserTrap.setStatus("mandatory")


class _HzOduHsbCrossLinkTrap_Type(Integer32):
    """Custom type hzOduHsbCrossLinkTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduHsbCrossLinkTrap_Type.__name__ = "Integer32"
_HzOduHsbCrossLinkTrap_Object = MibScalar
hzOduHsbCrossLinkTrap = _HzOduHsbCrossLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 35),
    _HzOduHsbCrossLinkTrap_Type()
)
hzOduHsbCrossLinkTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHsbCrossLinkTrap.setStatus("mandatory")


class _HzOduHsbActiveOnPrimaryTrap_Type(Integer32):
    """Custom type hzOduHsbActiveOnPrimaryTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduHsbActiveOnPrimaryTrap_Type.__name__ = "Integer32"
_HzOduHsbActiveOnPrimaryTrap_Object = MibScalar
hzOduHsbActiveOnPrimaryTrap = _HzOduHsbActiveOnPrimaryTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 36),
    _HzOduHsbActiveOnPrimaryTrap_Type()
)
hzOduHsbActiveOnPrimaryTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHsbActiveOnPrimaryTrap.setStatus("mandatory")
_HzOduSnmp_ObjectIdentity = ObjectIdentity
hzOduSnmp = _HzOduSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10)
)


class _HzOduSnmpUserAccess_Type(Integer32):
    """Custom type hzOduSnmpUserAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("explicitManagers", 1),
          ("any", 2))
    )


_HzOduSnmpUserAccess_Type.__name__ = "Integer32"
_HzOduSnmpUserAccess_Object = MibScalar
hzOduSnmpUserAccess = _HzOduSnmpUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 1),
    _HzOduSnmpUserAccess_Type()
)
hzOduSnmpUserAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpUserAccess.setStatus("mandatory")


class _HzOduSnmpManagerAnyCommunityName_Type(DisplayString):
    """Custom type hzOduSnmpManagerAnyCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduSnmpManagerAnyCommunityName_Type.__name__ = "DisplayString"
_HzOduSnmpManagerAnyCommunityName_Object = MibScalar
hzOduSnmpManagerAnyCommunityName = _HzOduSnmpManagerAnyCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 2),
    _HzOduSnmpManagerAnyCommunityName_Type()
)
hzOduSnmpManagerAnyCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpManagerAnyCommunityName.setStatus("mandatory")


class _HzOduSnmpSetRequests_Type(Integer32):
    """Custom type hzOduSnmpSetRequests based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduSnmpSetRequests_Type.__name__ = "Integer32"
_HzOduSnmpSetRequests_Object = MibScalar
hzOduSnmpSetRequests = _HzOduSnmpSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 3),
    _HzOduSnmpSetRequests_Type()
)
hzOduSnmpSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpSetRequests.setStatus("mandatory")
_HzOduSnmpManagersTable_Object = MibTable
hzOduSnmpManagersTable = _HzOduSnmpManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 4)
)
if mibBuilder.loadTexts:
    hzOduSnmpManagersTable.setStatus("mandatory")
_HzOduSnmpManagersEntry_Object = MibTableRow
hzOduSnmpManagersEntry = _HzOduSnmpManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 4, 1)
)
hzOduSnmpManagersEntry.setIndexNames(
    (0, "HORIZON-ODU-MIB", "hzOduSnmpManagersIndex"),
)
if mibBuilder.loadTexts:
    hzOduSnmpManagersEntry.setStatus("mandatory")
_HzOduSnmpManagersIndex_Type = Integer32
_HzOduSnmpManagersIndex_Object = MibTableColumn
hzOduSnmpManagersIndex = _HzOduSnmpManagersIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 4, 1, 1),
    _HzOduSnmpManagersIndex_Type()
)
hzOduSnmpManagersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpManagersIndex.setStatus("mandatory")
_HzOduSnmpManagerIpAddress_Type = IpAddress
_HzOduSnmpManagerIpAddress_Object = MibTableColumn
hzOduSnmpManagerIpAddress = _HzOduSnmpManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 4, 1, 2),
    _HzOduSnmpManagerIpAddress_Type()
)
hzOduSnmpManagerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpManagerIpAddress.setStatus("mandatory")


class _HzOduSnmpManagerCommunityName_Type(DisplayString):
    """Custom type hzOduSnmpManagerCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduSnmpManagerCommunityName_Type.__name__ = "DisplayString"
_HzOduSnmpManagerCommunityName_Object = MibTableColumn
hzOduSnmpManagerCommunityName = _HzOduSnmpManagerCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 4, 1, 3),
    _HzOduSnmpManagerCommunityName_Type()
)
hzOduSnmpManagerCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpManagerCommunityName.setStatus("mandatory")


class _HzOduSnmpManagerActivated_Type(Integer32):
    """Custom type hzOduSnmpManagerActivated based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzOduSnmpManagerActivated_Type.__name__ = "Integer32"
_HzOduSnmpManagerActivated_Object = MibTableColumn
hzOduSnmpManagerActivated = _HzOduSnmpManagerActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 4, 1, 4),
    _HzOduSnmpManagerActivated_Type()
)
hzOduSnmpManagerActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpManagerActivated.setStatus("mandatory")
_HzOduSnmpV3ManagersTable_Object = MibTable
hzOduSnmpV3ManagersTable = _HzOduSnmpV3ManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 5)
)
if mibBuilder.loadTexts:
    hzOduSnmpV3ManagersTable.setStatus("mandatory")
_HzOduSnmpV3ManagersEntry_Object = MibTableRow
hzOduSnmpV3ManagersEntry = _HzOduSnmpV3ManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 5, 1)
)
hzOduSnmpV3ManagersEntry.setIndexNames(
    (0, "HORIZON-ODU-MIB", "hzOduSnmpV3ManagersIndex"),
)
if mibBuilder.loadTexts:
    hzOduSnmpV3ManagersEntry.setStatus("mandatory")
_HzOduSnmpV3ManagersIndex_Type = Integer32
_HzOduSnmpV3ManagersIndex_Object = MibTableColumn
hzOduSnmpV3ManagersIndex = _HzOduSnmpV3ManagersIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 5, 1, 1),
    _HzOduSnmpV3ManagersIndex_Type()
)
hzOduSnmpV3ManagersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpV3ManagersIndex.setStatus("mandatory")


class _HzOduSnmpV3ManagerUserName_Type(DisplayString):
    """Custom type hzOduSnmpV3ManagerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduSnmpV3ManagerUserName_Type.__name__ = "DisplayString"
_HzOduSnmpV3ManagerUserName_Object = MibTableColumn
hzOduSnmpV3ManagerUserName = _HzOduSnmpV3ManagerUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 5, 1, 2),
    _HzOduSnmpV3ManagerUserName_Type()
)
hzOduSnmpV3ManagerUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpV3ManagerUserName.setStatus("mandatory")


class _HzOduSnmpV3ManagerAuthProtocol_Type(Integer32):
    """Custom type hzOduSnmpV3ManagerAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("md5", 2),
          ("sha", 3))
    )


_HzOduSnmpV3ManagerAuthProtocol_Type.__name__ = "Integer32"
_HzOduSnmpV3ManagerAuthProtocol_Object = MibTableColumn
hzOduSnmpV3ManagerAuthProtocol = _HzOduSnmpV3ManagerAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 5, 1, 3),
    _HzOduSnmpV3ManagerAuthProtocol_Type()
)
hzOduSnmpV3ManagerAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpV3ManagerAuthProtocol.setStatus("mandatory")


class _HzOduSnmpV3ManagerAuthPassword_Type(DisplayString):
    """Custom type hzOduSnmpV3ManagerAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduSnmpV3ManagerAuthPassword_Type.__name__ = "DisplayString"
_HzOduSnmpV3ManagerAuthPassword_Object = MibTableColumn
hzOduSnmpV3ManagerAuthPassword = _HzOduSnmpV3ManagerAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 5, 1, 4),
    _HzOduSnmpV3ManagerAuthPassword_Type()
)
hzOduSnmpV3ManagerAuthPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpV3ManagerAuthPassword.setStatus("mandatory")


class _HzOduSnmpV3ManagerPrivProtocol_Type(Integer32):
    """Custom type hzOduSnmpV3ManagerPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPriv", 1),
          ("des", 2))
    )


_HzOduSnmpV3ManagerPrivProtocol_Type.__name__ = "Integer32"
_HzOduSnmpV3ManagerPrivProtocol_Object = MibTableColumn
hzOduSnmpV3ManagerPrivProtocol = _HzOduSnmpV3ManagerPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 5, 1, 5),
    _HzOduSnmpV3ManagerPrivProtocol_Type()
)
hzOduSnmpV3ManagerPrivProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpV3ManagerPrivProtocol.setStatus("mandatory")


class _HzOduSnmpV3ManagerPrivPassword_Type(DisplayString):
    """Custom type hzOduSnmpV3ManagerPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduSnmpV3ManagerPrivPassword_Type.__name__ = "DisplayString"
_HzOduSnmpV3ManagerPrivPassword_Object = MibTableColumn
hzOduSnmpV3ManagerPrivPassword = _HzOduSnmpV3ManagerPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 5, 1, 6),
    _HzOduSnmpV3ManagerPrivPassword_Type()
)
hzOduSnmpV3ManagerPrivPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpV3ManagerPrivPassword.setStatus("mandatory")


class _HzOduSnmpV3ManagerActivated_Type(Integer32):
    """Custom type hzOduSnmpV3ManagerActivated based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzOduSnmpV3ManagerActivated_Type.__name__ = "Integer32"
_HzOduSnmpV3ManagerActivated_Object = MibTableColumn
hzOduSnmpV3ManagerActivated = _HzOduSnmpV3ManagerActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 10, 5, 1, 7),
    _HzOduSnmpV3ManagerActivated_Type()
)
hzOduSnmpV3ManagerActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSnmpV3ManagerActivated.setStatus("mandatory")
_HzOduManagementSessions_ObjectIdentity = ObjectIdentity
hzOduManagementSessions = _HzOduManagementSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11)
)
_HzOduTtySessionUser1_ObjectIdentity = ObjectIdentity
hzOduTtySessionUser1 = _HzOduTtySessionUser1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 1)
)


class _HzOduTtySessionUser1Name_Type(DisplayString):
    """Custom type hzOduTtySessionUser1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzOduTtySessionUser1Name_Type.__name__ = "DisplayString"
_HzOduTtySessionUser1Name_Object = MibScalar
hzOduTtySessionUser1Name = _HzOduTtySessionUser1Name_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 1, 1),
    _HzOduTtySessionUser1Name_Type()
)
hzOduTtySessionUser1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser1Name.setStatus("mandatory")


class _HzOduTtySessionUser1ConnectionType_Type(Integer32):
    """Custom type hzOduTtySessionUser1ConnectionType based on Integer32"""
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
        *(("informationNotAvailable", 1),
          ("serialPort", 2),
          ("enetPort2", 3),
          ("enetPort1", 4))
    )


_HzOduTtySessionUser1ConnectionType_Type.__name__ = "Integer32"
_HzOduTtySessionUser1ConnectionType_Object = MibScalar
hzOduTtySessionUser1ConnectionType = _HzOduTtySessionUser1ConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 1, 2),
    _HzOduTtySessionUser1ConnectionType_Type()
)
hzOduTtySessionUser1ConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser1ConnectionType.setStatus("mandatory")


class _HzOduTtySessionUser1State_Type(Integer32):
    """Custom type hzOduTtySessionUser1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informationNotAvailable", 1),
          ("sessionTerminated", 2),
          ("sessionInProgress", 3))
    )


_HzOduTtySessionUser1State_Type.__name__ = "Integer32"
_HzOduTtySessionUser1State_Object = MibScalar
hzOduTtySessionUser1State = _HzOduTtySessionUser1State_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 1, 3),
    _HzOduTtySessionUser1State_Type()
)
hzOduTtySessionUser1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser1State.setStatus("mandatory")
_HzOduTtySessionUser2_ObjectIdentity = ObjectIdentity
hzOduTtySessionUser2 = _HzOduTtySessionUser2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 2)
)


class _HzOduTtySessionUser2Name_Type(DisplayString):
    """Custom type hzOduTtySessionUser2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzOduTtySessionUser2Name_Type.__name__ = "DisplayString"
_HzOduTtySessionUser2Name_Object = MibScalar
hzOduTtySessionUser2Name = _HzOduTtySessionUser2Name_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 2, 1),
    _HzOduTtySessionUser2Name_Type()
)
hzOduTtySessionUser2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser2Name.setStatus("mandatory")


class _HzOduTtySessionUser2ConnectionType_Type(Integer32):
    """Custom type hzOduTtySessionUser2ConnectionType based on Integer32"""
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
        *(("informationNotAvailable", 1),
          ("serialPort", 2),
          ("enetPort2", 3),
          ("enetPort1", 4))
    )


_HzOduTtySessionUser2ConnectionType_Type.__name__ = "Integer32"
_HzOduTtySessionUser2ConnectionType_Object = MibScalar
hzOduTtySessionUser2ConnectionType = _HzOduTtySessionUser2ConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 2, 2),
    _HzOduTtySessionUser2ConnectionType_Type()
)
hzOduTtySessionUser2ConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser2ConnectionType.setStatus("mandatory")


class _HzOduTtySessionUser2State_Type(Integer32):
    """Custom type hzOduTtySessionUser2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informationNotAvailable", 1),
          ("sessionTerminated", 2),
          ("sessionInProgress", 3))
    )


_HzOduTtySessionUser2State_Type.__name__ = "Integer32"
_HzOduTtySessionUser2State_Object = MibScalar
hzOduTtySessionUser2State = _HzOduTtySessionUser2State_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 2, 3),
    _HzOduTtySessionUser2State_Type()
)
hzOduTtySessionUser2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser2State.setStatus("mandatory")
_HzOduTtySessionUser3_ObjectIdentity = ObjectIdentity
hzOduTtySessionUser3 = _HzOduTtySessionUser3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 3)
)


class _HzOduTtySessionUser3Name_Type(DisplayString):
    """Custom type hzOduTtySessionUser3Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzOduTtySessionUser3Name_Type.__name__ = "DisplayString"
_HzOduTtySessionUser3Name_Object = MibScalar
hzOduTtySessionUser3Name = _HzOduTtySessionUser3Name_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 3, 1),
    _HzOduTtySessionUser3Name_Type()
)
hzOduTtySessionUser3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser3Name.setStatus("mandatory")


class _HzOduTtySessionUser3ConnectionType_Type(Integer32):
    """Custom type hzOduTtySessionUser3ConnectionType based on Integer32"""
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
        *(("informationNotAvailable", 1),
          ("serialPort", 2),
          ("enetPort2", 3),
          ("enetPort1", 4))
    )


_HzOduTtySessionUser3ConnectionType_Type.__name__ = "Integer32"
_HzOduTtySessionUser3ConnectionType_Object = MibScalar
hzOduTtySessionUser3ConnectionType = _HzOduTtySessionUser3ConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 3, 2),
    _HzOduTtySessionUser3ConnectionType_Type()
)
hzOduTtySessionUser3ConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser3ConnectionType.setStatus("mandatory")


class _HzOduTtySessionUser3State_Type(Integer32):
    """Custom type hzOduTtySessionUser3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informationNotAvailable", 1),
          ("sessionTerminated", 2),
          ("sessionInProgress", 3))
    )


_HzOduTtySessionUser3State_Type.__name__ = "Integer32"
_HzOduTtySessionUser3State_Object = MibScalar
hzOduTtySessionUser3State = _HzOduTtySessionUser3State_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 3, 3),
    _HzOduTtySessionUser3State_Type()
)
hzOduTtySessionUser3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser3State.setStatus("mandatory")
_HzOduTtySessionUser4_ObjectIdentity = ObjectIdentity
hzOduTtySessionUser4 = _HzOduTtySessionUser4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 4)
)


class _HzOduTtySessionUser4Name_Type(DisplayString):
    """Custom type hzOduTtySessionUser4Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzOduTtySessionUser4Name_Type.__name__ = "DisplayString"
_HzOduTtySessionUser4Name_Object = MibScalar
hzOduTtySessionUser4Name = _HzOduTtySessionUser4Name_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 4, 1),
    _HzOduTtySessionUser4Name_Type()
)
hzOduTtySessionUser4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser4Name.setStatus("mandatory")


class _HzOduTtySessionUser4ConnectionType_Type(Integer32):
    """Custom type hzOduTtySessionUser4ConnectionType based on Integer32"""
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
        *(("informationNotAvailable", 1),
          ("serialPort", 2),
          ("enetPort2", 3),
          ("enetPort1", 4))
    )


_HzOduTtySessionUser4ConnectionType_Type.__name__ = "Integer32"
_HzOduTtySessionUser4ConnectionType_Object = MibScalar
hzOduTtySessionUser4ConnectionType = _HzOduTtySessionUser4ConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 4, 2),
    _HzOduTtySessionUser4ConnectionType_Type()
)
hzOduTtySessionUser4ConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser4ConnectionType.setStatus("mandatory")


class _HzOduTtySessionUser4State_Type(Integer32):
    """Custom type hzOduTtySessionUser4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informationNotAvailable", 1),
          ("sessionTerminated", 2),
          ("sessionInProgress", 3))
    )


_HzOduTtySessionUser4State_Type.__name__ = "Integer32"
_HzOduTtySessionUser4State_Object = MibScalar
hzOduTtySessionUser4State = _HzOduTtySessionUser4State_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 4, 3),
    _HzOduTtySessionUser4State_Type()
)
hzOduTtySessionUser4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser4State.setStatus("mandatory")
_HzOduTtySessionUser5_ObjectIdentity = ObjectIdentity
hzOduTtySessionUser5 = _HzOduTtySessionUser5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 5)
)


class _HzOduTtySessionUser5Name_Type(DisplayString):
    """Custom type hzOduTtySessionUser5Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzOduTtySessionUser5Name_Type.__name__ = "DisplayString"
_HzOduTtySessionUser5Name_Object = MibScalar
hzOduTtySessionUser5Name = _HzOduTtySessionUser5Name_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 5, 1),
    _HzOduTtySessionUser5Name_Type()
)
hzOduTtySessionUser5Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser5Name.setStatus("mandatory")


class _HzOduTtySessionUser5ConnectionType_Type(Integer32):
    """Custom type hzOduTtySessionUser5ConnectionType based on Integer32"""
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
        *(("informationNotAvailable", 1),
          ("serialPort", 2),
          ("enetPort2", 3),
          ("enetPort1", 4))
    )


_HzOduTtySessionUser5ConnectionType_Type.__name__ = "Integer32"
_HzOduTtySessionUser5ConnectionType_Object = MibScalar
hzOduTtySessionUser5ConnectionType = _HzOduTtySessionUser5ConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 5, 2),
    _HzOduTtySessionUser5ConnectionType_Type()
)
hzOduTtySessionUser5ConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser5ConnectionType.setStatus("mandatory")


class _HzOduTtySessionUser5State_Type(Integer32):
    """Custom type hzOduTtySessionUser5State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informationNotAvailable", 1),
          ("sessionTerminated", 2),
          ("sessionInProgress", 3))
    )


_HzOduTtySessionUser5State_Type.__name__ = "Integer32"
_HzOduTtySessionUser5State_Object = MibScalar
hzOduTtySessionUser5State = _HzOduTtySessionUser5State_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 5, 3),
    _HzOduTtySessionUser5State_Type()
)
hzOduTtySessionUser5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser5State.setStatus("mandatory")
_HzOduTtySessionUser6_ObjectIdentity = ObjectIdentity
hzOduTtySessionUser6 = _HzOduTtySessionUser6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 6)
)


class _HzOduTtySessionUser6Name_Type(DisplayString):
    """Custom type hzOduTtySessionUser6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzOduTtySessionUser6Name_Type.__name__ = "DisplayString"
_HzOduTtySessionUser6Name_Object = MibScalar
hzOduTtySessionUser6Name = _HzOduTtySessionUser6Name_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 6, 1),
    _HzOduTtySessionUser6Name_Type()
)
hzOduTtySessionUser6Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser6Name.setStatus("mandatory")


class _HzOduTtySessionUser6ConnectionType_Type(Integer32):
    """Custom type hzOduTtySessionUser6ConnectionType based on Integer32"""
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
        *(("informationNotAvailable", 1),
          ("serialPort", 2),
          ("enetPort2", 3),
          ("enetPort1", 4))
    )


_HzOduTtySessionUser6ConnectionType_Type.__name__ = "Integer32"
_HzOduTtySessionUser6ConnectionType_Object = MibScalar
hzOduTtySessionUser6ConnectionType = _HzOduTtySessionUser6ConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 6, 2),
    _HzOduTtySessionUser6ConnectionType_Type()
)
hzOduTtySessionUser6ConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser6ConnectionType.setStatus("mandatory")


class _HzOduTtySessionUser6State_Type(Integer32):
    """Custom type hzOduTtySessionUser6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informationNotAvailable", 1),
          ("sessionTerminated", 2),
          ("sessionInProgress", 3))
    )


_HzOduTtySessionUser6State_Type.__name__ = "Integer32"
_HzOduTtySessionUser6State_Object = MibScalar
hzOduTtySessionUser6State = _HzOduTtySessionUser6State_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 6, 3),
    _HzOduTtySessionUser6State_Type()
)
hzOduTtySessionUser6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUser6State.setStatus("mandatory")
_HzOduSessionUserInformation_ObjectIdentity = ObjectIdentity
hzOduSessionUserInformation = _HzOduSessionUserInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 7)
)


class _HzOduTtySessionUserName_Type(DisplayString):
    """Custom type hzOduTtySessionUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzOduTtySessionUserName_Type.__name__ = "DisplayString"
_HzOduTtySessionUserName_Object = MibScalar
hzOduTtySessionUserName = _HzOduTtySessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 7, 1),
    _HzOduTtySessionUserName_Type()
)
hzOduTtySessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUserName.setStatus("mandatory")


class _HzOduTtySessionUserConnectionType_Type(Integer32):
    """Custom type hzOduTtySessionUserConnectionType based on Integer32"""
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
        *(("informationNotAvailable", 1),
          ("serialPort", 2),
          ("enetPort2", 3),
          ("enetPort1", 4))
    )


_HzOduTtySessionUserConnectionType_Type.__name__ = "Integer32"
_HzOduTtySessionUserConnectionType_Object = MibScalar
hzOduTtySessionUserConnectionType = _HzOduTtySessionUserConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 11, 7, 2),
    _HzOduTtySessionUserConnectionType_Type()
)
hzOduTtySessionUserConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduTtySessionUserConnectionType.setStatus("mandatory")
_HzOduHttp_ObjectIdentity = ObjectIdentity
hzOduHttp = _HzOduHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 12)
)


class _HzOduHttpEnable_Type(Integer32):
    """Custom type hzOduHttpEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduHttpEnable_Type.__name__ = "Integer32"
_HzOduHttpEnable_Object = MibScalar
hzOduHttpEnable = _HzOduHttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 12, 1),
    _HzOduHttpEnable_Type()
)
hzOduHttpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHttpEnable.setStatus("mandatory")
_HzOduHttpSecure_ObjectIdentity = ObjectIdentity
hzOduHttpSecure = _HzOduHttpSecure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 12, 2)
)


class _HzOduHttpSecureCertificateStatus_Type(DisplayString):
    """Custom type hzOduHttpSecureCertificateStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HzOduHttpSecureCertificateStatus_Type.__name__ = "DisplayString"
_HzOduHttpSecureCertificateStatus_Object = MibScalar
hzOduHttpSecureCertificateStatus = _HzOduHttpSecureCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 12, 2, 1),
    _HzOduHttpSecureCertificateStatus_Type()
)
hzOduHttpSecureCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduHttpSecureCertificateStatus.setStatus("mandatory")


class _HzOduHttpSecureAccessForAdminUsers_Type(Integer32):
    """Custom type hzOduHttpSecureAccessForAdminUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduHttpSecureAccessForAdminUsers_Type.__name__ = "Integer32"
_HzOduHttpSecureAccessForAdminUsers_Object = MibScalar
hzOduHttpSecureAccessForAdminUsers = _HzOduHttpSecureAccessForAdminUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 12, 2, 2),
    _HzOduHttpSecureAccessForAdminUsers_Type()
)
hzOduHttpSecureAccessForAdminUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHttpSecureAccessForAdminUsers.setStatus("mandatory")


class _HzOduHttpSecureAccessForNocUsers_Type(Integer32):
    """Custom type hzOduHttpSecureAccessForNocUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduHttpSecureAccessForNocUsers_Type.__name__ = "Integer32"
_HzOduHttpSecureAccessForNocUsers_Object = MibScalar
hzOduHttpSecureAccessForNocUsers = _HzOduHttpSecureAccessForNocUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 12, 2, 3),
    _HzOduHttpSecureAccessForNocUsers_Type()
)
hzOduHttpSecureAccessForNocUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHttpSecureAccessForNocUsers.setStatus("mandatory")


class _HzOduHttpSecureAccessForSuperUsers_Type(Integer32):
    """Custom type hzOduHttpSecureAccessForSuperUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduHttpSecureAccessForSuperUsers_Type.__name__ = "Integer32"
_HzOduHttpSecureAccessForSuperUsers_Object = MibScalar
hzOduHttpSecureAccessForSuperUsers = _HzOduHttpSecureAccessForSuperUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 12, 2, 4),
    _HzOduHttpSecureAccessForSuperUsers_Type()
)
hzOduHttpSecureAccessForSuperUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHttpSecureAccessForSuperUsers.setStatus("mandatory")
_HzOduQos_ObjectIdentity = ObjectIdentity
hzOduQos = _HzOduQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13)
)


class _HzOduQosEnable_Type(Integer32):
    """Custom type hzOduQosEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduQosEnable_Type.__name__ = "Integer32"
_HzOduQosEnable_Object = MibScalar
hzOduQosEnable = _HzOduQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13, 1),
    _HzOduQosEnable_Type()
)
hzOduQosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduQosEnable.setStatus("mandatory")


class _HzOduCosType_Type(Integer32):
    """Custom type hzOduCosType based on Integer32"""
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
        *(("cosVlan", 1),
          ("cosQinQiTag", 2),
          ("cosQinQoTag", 3),
          ("cosDscp", 4))
    )


_HzOduCosType_Type.__name__ = "Integer32"
_HzOduCosType_Object = MibScalar
hzOduCosType = _HzOduCosType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13, 2),
    _HzOduCosType_Type()
)
hzOduCosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduCosType.setStatus("mandatory")
_HzOduCoSQinQiTag_Type = DisplayString
_HzOduCoSQinQiTag_Object = MibScalar
hzOduCoSQinQiTag = _HzOduCoSQinQiTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13, 3),
    _HzOduCoSQinQiTag_Type()
)
hzOduCoSQinQiTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduCoSQinQiTag.setStatus("mandatory")
_HzOduCoSQinQoTag_Type = DisplayString
_HzOduCoSQinQoTag_Object = MibScalar
hzOduCoSQinQoTag = _HzOduCoSQinQoTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13, 4),
    _HzOduCoSQinQoTag_Type()
)
hzOduCoSQinQoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduCoSQinQoTag.setStatus("mandatory")


class _HzOduCosQueueMapping_Type(DisplayString):
    """Custom type hzOduCosQueueMapping based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 32),
    )


_HzOduCosQueueMapping_Type.__name__ = "DisplayString"
_HzOduCosQueueMapping_Object = MibScalar
hzOduCosQueueMapping = _HzOduCosQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13, 5),
    _HzOduCosQueueMapping_Type()
)
hzOduCosQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduCosQueueMapping.setStatus("mandatory")


class _HzOduCosExpediteQueue_Type(Integer32):
    """Custom type hzOduCosExpediteQueue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduCosExpediteQueue_Type.__name__ = "Integer32"
_HzOduCosExpediteQueue_Object = MibScalar
hzOduCosExpediteQueue = _HzOduCosExpediteQueue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13, 6),
    _HzOduCosExpediteQueue_Type()
)
hzOduCosExpediteQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduCosExpediteQueue.setStatus("mandatory")


class _HzOduCosQueueCIR_Type(DisplayString):
    """Custom type hzOduCosQueueCIR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzOduCosQueueCIR_Type.__name__ = "DisplayString"
_HzOduCosQueueCIR_Object = MibScalar
hzOduCosQueueCIR = _HzOduCosQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13, 7),
    _HzOduCosQueueCIR_Type()
)
hzOduCosQueueCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduCosQueueCIR.setStatus("mandatory")


class _HzOduCosQueueCBS_Type(DisplayString):
    """Custom type hzOduCosQueueCBS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzOduCosQueueCBS_Type.__name__ = "DisplayString"
_HzOduCosQueueCBS_Object = MibScalar
hzOduCosQueueCBS = _HzOduCosQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13, 8),
    _HzOduCosQueueCBS_Type()
)
hzOduCosQueueCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduCosQueueCBS.setStatus("mandatory")


class _HzOduCosDefaultValue_Type(Integer32):
    """Custom type hzOduCosDefaultValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HzOduCosDefaultValue_Type.__name__ = "Integer32"
_HzOduCosDefaultValue_Object = MibScalar
hzOduCosDefaultValue = _HzOduCosDefaultValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13, 9),
    _HzOduCosDefaultValue_Type()
)
hzOduCosDefaultValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduCosDefaultValue.setStatus("mandatory")


class _HzOduCutThroughProcessing_Type(Integer32):
    """Custom type hzOduCutThroughProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduCutThroughProcessing_Type.__name__ = "Integer32"
_HzOduCutThroughProcessing_Object = MibScalar
hzOduCutThroughProcessing = _HzOduCutThroughProcessing_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 13, 10),
    _HzOduCutThroughProcessing_Type()
)
hzOduCutThroughProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduCutThroughProcessing.setStatus("mandatory")
_HzOduRapidLinkShutdown_ObjectIdentity = ObjectIdentity
hzOduRapidLinkShutdown = _HzOduRapidLinkShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14)
)
_HzOduRapidLinkShutdownVer1_ObjectIdentity = ObjectIdentity
hzOduRapidLinkShutdownVer1 = _HzOduRapidLinkShutdownVer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 1)
)


class _HzOduRlsEnable_Type(Integer32):
    """Custom type hzOduRlsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduRlsEnable_Type.__name__ = "Integer32"
_HzOduRlsEnable_Object = MibScalar
hzOduRlsEnable = _HzOduRlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 1, 1),
    _HzOduRlsEnable_Type()
)
hzOduRlsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRlsEnable.setStatus("mandatory")


class _HzOduAutomaticLinkReestablish_Type(Integer32):
    """Custom type hzOduAutomaticLinkReestablish based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduAutomaticLinkReestablish_Type.__name__ = "Integer32"
_HzOduAutomaticLinkReestablish_Object = MibScalar
hzOduAutomaticLinkReestablish = _HzOduAutomaticLinkReestablish_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 1, 2),
    _HzOduAutomaticLinkReestablish_Type()
)
hzOduAutomaticLinkReestablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduAutomaticLinkReestablish.setStatus("mandatory")


class _HzOduManualLinkReestablish_Type(Integer32):
    """Custom type hzOduManualLinkReestablish based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduManualLinkReestablish_Type.__name__ = "Integer32"
_HzOduManualLinkReestablish_Object = MibScalar
hzOduManualLinkReestablish = _HzOduManualLinkReestablish_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 1, 3),
    _HzOduManualLinkReestablish_Type()
)
hzOduManualLinkReestablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduManualLinkReestablish.setStatus("mandatory")


class _HzOduHysterisisErredFramesPerMilliSecond_Type(Integer32):
    """Custom type hzOduHysterisisErredFramesPerMilliSecond based on Integer32"""
    defaultValue = 0


_HzOduHysterisisErredFramesPerMilliSecond_Type.__name__ = "Integer32"
_HzOduHysterisisErredFramesPerMilliSecond_Object = MibScalar
hzOduHysterisisErredFramesPerMilliSecond = _HzOduHysterisisErredFramesPerMilliSecond_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 1, 4),
    _HzOduHysterisisErredFramesPerMilliSecond_Type()
)
hzOduHysterisisErredFramesPerMilliSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHysterisisErredFramesPerMilliSecond.setStatus("mandatory")


class _HzOduHysterisisErredMilliSeconds_Type(Integer32):
    """Custom type hzOduHysterisisErredMilliSeconds based on Integer32"""
    defaultValue = 0


_HzOduHysterisisErredMilliSeconds_Type.__name__ = "Integer32"
_HzOduHysterisisErredMilliSeconds_Object = MibScalar
hzOduHysterisisErredMilliSeconds = _HzOduHysterisisErredMilliSeconds_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 1, 5),
    _HzOduHysterisisErredMilliSeconds_Type()
)
hzOduHysterisisErredMilliSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHysterisisErredMilliSeconds.setStatus("mandatory")


class _HzOduHysterisisUnerredFramesPerMilliSecond_Type(Integer32):
    """Custom type hzOduHysterisisUnerredFramesPerMilliSecond based on Integer32"""
    defaultValue = 0


_HzOduHysterisisUnerredFramesPerMilliSecond_Type.__name__ = "Integer32"
_HzOduHysterisisUnerredFramesPerMilliSecond_Object = MibScalar
hzOduHysterisisUnerredFramesPerMilliSecond = _HzOduHysterisisUnerredFramesPerMilliSecond_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 1, 6),
    _HzOduHysterisisUnerredFramesPerMilliSecond_Type()
)
hzOduHysterisisUnerredFramesPerMilliSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHysterisisUnerredFramesPerMilliSecond.setStatus("mandatory")


class _HzOduHysterisisUnerredMilliSeconds_Type(Integer32):
    """Custom type hzOduHysterisisUnerredMilliSeconds based on Integer32"""
    defaultValue = 0


_HzOduHysterisisUnerredMilliSeconds_Type.__name__ = "Integer32"
_HzOduHysterisisUnerredMilliSeconds_Object = MibScalar
hzOduHysterisisUnerredMilliSeconds = _HzOduHysterisisUnerredMilliSeconds_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 1, 7),
    _HzOduHysterisisUnerredMilliSeconds_Type()
)
hzOduHysterisisUnerredMilliSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduHysterisisUnerredMilliSeconds.setStatus("mandatory")


class _HzOduWriteRlsMonitorParametersToSystem_Type(Integer32):
    """Custom type hzOduWriteRlsMonitorParametersToSystem based on Integer32"""
    defaultValue = 0


_HzOduWriteRlsMonitorParametersToSystem_Type.__name__ = "Integer32"
_HzOduWriteRlsMonitorParametersToSystem_Object = MibScalar
hzOduWriteRlsMonitorParametersToSystem = _HzOduWriteRlsMonitorParametersToSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 1, 8),
    _HzOduWriteRlsMonitorParametersToSystem_Type()
)
hzOduWriteRlsMonitorParametersToSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduWriteRlsMonitorParametersToSystem.setStatus("mandatory")


class _HzOduRlsSampleTimeInMilliSeconds_Type(Integer32):
    """Custom type hzOduRlsSampleTimeInMilliSeconds based on Integer32"""
    defaultValue = 0


_HzOduRlsSampleTimeInMilliSeconds_Type.__name__ = "Integer32"
_HzOduRlsSampleTimeInMilliSeconds_Object = MibScalar
hzOduRlsSampleTimeInMilliSeconds = _HzOduRlsSampleTimeInMilliSeconds_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 1, 9),
    _HzOduRlsSampleTimeInMilliSeconds_Type()
)
hzOduRlsSampleTimeInMilliSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRlsSampleTimeInMilliSeconds.setStatus("mandatory")
_HzOduRapidLinkShutdownVer2_ObjectIdentity = ObjectIdentity
hzOduRapidLinkShutdownVer2 = _HzOduRapidLinkShutdownVer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2)
)


class _HzOduPrimaryRlsEnable_Type(Integer32):
    """Custom type hzOduPrimaryRlsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduPrimaryRlsEnable_Type.__name__ = "Integer32"
_HzOduPrimaryRlsEnable_Object = MibScalar
hzOduPrimaryRlsEnable = _HzOduPrimaryRlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 1),
    _HzOduPrimaryRlsEnable_Type()
)
hzOduPrimaryRlsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryRlsEnable.setStatus("mandatory")


class _HzOduPrimaryRlsHardFaultMonitor_Type(Integer32):
    """Custom type hzOduPrimaryRlsHardFaultMonitor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduPrimaryRlsHardFaultMonitor_Type.__name__ = "Integer32"
_HzOduPrimaryRlsHardFaultMonitor_Object = MibScalar
hzOduPrimaryRlsHardFaultMonitor = _HzOduPrimaryRlsHardFaultMonitor_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 2),
    _HzOduPrimaryRlsHardFaultMonitor_Type()
)
hzOduPrimaryRlsHardFaultMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryRlsHardFaultMonitor.setStatus("mandatory")


class _HzOduPrimaryAutomaticLinkReestablish_Type(Integer32):
    """Custom type hzOduPrimaryAutomaticLinkReestablish based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduPrimaryAutomaticLinkReestablish_Type.__name__ = "Integer32"
_HzOduPrimaryAutomaticLinkReestablish_Object = MibScalar
hzOduPrimaryAutomaticLinkReestablish = _HzOduPrimaryAutomaticLinkReestablish_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 3),
    _HzOduPrimaryAutomaticLinkReestablish_Type()
)
hzOduPrimaryAutomaticLinkReestablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryAutomaticLinkReestablish.setStatus("mandatory")


class _HzOduPrimaryManualLinkReestablish_Type(Integer32):
    """Custom type hzOduPrimaryManualLinkReestablish based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduPrimaryManualLinkReestablish_Type.__name__ = "Integer32"
_HzOduPrimaryManualLinkReestablish_Object = MibScalar
hzOduPrimaryManualLinkReestablish = _HzOduPrimaryManualLinkReestablish_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 4),
    _HzOduPrimaryManualLinkReestablish_Type()
)
hzOduPrimaryManualLinkReestablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryManualLinkReestablish.setStatus("mandatory")


class _HzOduWritePrimaryRlsMonitorParametersToSystem_Type(Integer32):
    """Custom type hzOduWritePrimaryRlsMonitorParametersToSystem based on Integer32"""
    defaultValue = 0


_HzOduWritePrimaryRlsMonitorParametersToSystem_Type.__name__ = "Integer32"
_HzOduWritePrimaryRlsMonitorParametersToSystem_Object = MibScalar
hzOduWritePrimaryRlsMonitorParametersToSystem = _HzOduWritePrimaryRlsMonitorParametersToSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 5),
    _HzOduWritePrimaryRlsMonitorParametersToSystem_Type()
)
hzOduWritePrimaryRlsMonitorParametersToSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduWritePrimaryRlsMonitorParametersToSystem.setStatus("mandatory")
_HzOduPrimarySoftFaultMonitor_ObjectIdentity = ObjectIdentity
hzOduPrimarySoftFaultMonitor = _HzOduPrimarySoftFaultMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 6)
)
_HzOduPrimaryEstablishErredFrameThreshold_Type = Integer32
_HzOduPrimaryEstablishErredFrameThreshold_Object = MibScalar
hzOduPrimaryEstablishErredFrameThreshold = _HzOduPrimaryEstablishErredFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 6, 1),
    _HzOduPrimaryEstablishErredFrameThreshold_Type()
)
hzOduPrimaryEstablishErredFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryEstablishErredFrameThreshold.setStatus("mandatory")
_HzOduPrimaryShutdownErredFrameThreshold_Type = Integer32
_HzOduPrimaryShutdownErredFrameThreshold_Object = MibScalar
hzOduPrimaryShutdownErredFrameThreshold = _HzOduPrimaryShutdownErredFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 6, 2),
    _HzOduPrimaryShutdownErredFrameThreshold_Type()
)
hzOduPrimaryShutdownErredFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryShutdownErredFrameThreshold.setStatus("mandatory")
_HzOduPrimaryEstablishNumberOfSamples_Type = Integer32
_HzOduPrimaryEstablishNumberOfSamples_Object = MibScalar
hzOduPrimaryEstablishNumberOfSamples = _HzOduPrimaryEstablishNumberOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 6, 3),
    _HzOduPrimaryEstablishNumberOfSamples_Type()
)
hzOduPrimaryEstablishNumberOfSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryEstablishNumberOfSamples.setStatus("mandatory")
_HzOduPrimaryShutdownNumberOfSamples_Type = Integer32
_HzOduPrimaryShutdownNumberOfSamples_Object = MibScalar
hzOduPrimaryShutdownNumberOfSamples = _HzOduPrimaryShutdownNumberOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 6, 4),
    _HzOduPrimaryShutdownNumberOfSamples_Type()
)
hzOduPrimaryShutdownNumberOfSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryShutdownNumberOfSamples.setStatus("mandatory")
_HzOduPrimaryEstablishSamplePeriod_Type = Integer32
_HzOduPrimaryEstablishSamplePeriod_Object = MibScalar
hzOduPrimaryEstablishSamplePeriod = _HzOduPrimaryEstablishSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 6, 5),
    _HzOduPrimaryEstablishSamplePeriod_Type()
)
hzOduPrimaryEstablishSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryEstablishSamplePeriod.setStatus("mandatory")
_HzOduPrimaryShutdownSamplePeriod_Type = Integer32
_HzOduPrimaryShutdownSamplePeriod_Object = MibScalar
hzOduPrimaryShutdownSamplePeriod = _HzOduPrimaryShutdownSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 6, 6),
    _HzOduPrimaryShutdownSamplePeriod_Type()
)
hzOduPrimaryShutdownSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryShutdownSamplePeriod.setStatus("mandatory")
_HzOduPrimaryQuickShutdownSamplePeriod_Type = Integer32
_HzOduPrimaryQuickShutdownSamplePeriod_Object = MibScalar
hzOduPrimaryQuickShutdownSamplePeriod = _HzOduPrimaryQuickShutdownSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 6, 7),
    _HzOduPrimaryQuickShutdownSamplePeriod_Type()
)
hzOduPrimaryQuickShutdownSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryQuickShutdownSamplePeriod.setStatus("mandatory")
_HzOduPrimaryHardFaultMonitor_ObjectIdentity = ObjectIdentity
hzOduPrimaryHardFaultMonitor = _HzOduPrimaryHardFaultMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 7)
)
_HzOduPrimaryFaultSamplePeriod_Type = Integer32
_HzOduPrimaryFaultSamplePeriod_Object = MibScalar
hzOduPrimaryFaultSamplePeriod = _HzOduPrimaryFaultSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 7, 1),
    _HzOduPrimaryFaultSamplePeriod_Type()
)
hzOduPrimaryFaultSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryFaultSamplePeriod.setStatus("mandatory")
_HzOduPrimaryFaultThreshold_Type = Integer32
_HzOduPrimaryFaultThreshold_Object = MibScalar
hzOduPrimaryFaultThreshold = _HzOduPrimaryFaultThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 7, 2),
    _HzOduPrimaryFaultThreshold_Type()
)
hzOduPrimaryFaultThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryFaultThreshold.setStatus("mandatory")
_HzOduPrimaryReceiveSignalLevelMonitor_ObjectIdentity = ObjectIdentity
hzOduPrimaryReceiveSignalLevelMonitor = _HzOduPrimaryReceiveSignalLevelMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 8)
)


class _HzOduPrimaryRlsMakeRslMonitorRslValue_Type(DisplayString):
    """Custom type hzOduPrimaryRlsMakeRslMonitorRslValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzOduPrimaryRlsMakeRslMonitorRslValue_Type.__name__ = "DisplayString"
_HzOduPrimaryRlsMakeRslMonitorRslValue_Object = MibScalar
hzOduPrimaryRlsMakeRslMonitorRslValue = _HzOduPrimaryRlsMakeRslMonitorRslValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 8, 1),
    _HzOduPrimaryRlsMakeRslMonitorRslValue_Type()
)
hzOduPrimaryRlsMakeRslMonitorRslValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryRlsMakeRslMonitorRslValue.setStatus("mandatory")
_HzOduPrimaryRlsMakeRslMonitorPeriod_Type = Integer32
_HzOduPrimaryRlsMakeRslMonitorPeriod_Object = MibScalar
hzOduPrimaryRlsMakeRslMonitorPeriod = _HzOduPrimaryRlsMakeRslMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 8, 2),
    _HzOduPrimaryRlsMakeRslMonitorPeriod_Type()
)
hzOduPrimaryRlsMakeRslMonitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPrimaryRlsMakeRslMonitorPeriod.setStatus("mandatory")
_HzOduPrimaryRlsStatus_ObjectIdentity = ObjectIdentity
hzOduPrimaryRlsStatus = _HzOduPrimaryRlsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9)
)
_HzOduPrimaryRlsOption_Type = DisplayString
_HzOduPrimaryRlsOption_Object = MibScalar
hzOduPrimaryRlsOption = _HzOduPrimaryRlsOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 1),
    _HzOduPrimaryRlsOption_Type()
)
hzOduPrimaryRlsOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryRlsOption.setStatus("mandatory")
_HzOduPrimaryRlsState_Type = DisplayString
_HzOduPrimaryRlsState_Object = MibScalar
hzOduPrimaryRlsState = _HzOduPrimaryRlsState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 2),
    _HzOduPrimaryRlsState_Type()
)
hzOduPrimaryRlsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryRlsState.setStatus("mandatory")
_HzOduPrimaryRlsMismatchState_Type = DisplayString
_HzOduPrimaryRlsMismatchState_Object = MibScalar
hzOduPrimaryRlsMismatchState = _HzOduPrimaryRlsMismatchState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 3),
    _HzOduPrimaryRlsMismatchState_Type()
)
hzOduPrimaryRlsMismatchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryRlsMismatchState.setStatus("mandatory")
_HzOduPrimaryDegradeMonitorState_Type = DisplayString
_HzOduPrimaryDegradeMonitorState_Object = MibScalar
hzOduPrimaryDegradeMonitorState = _HzOduPrimaryDegradeMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 4),
    _HzOduPrimaryDegradeMonitorState_Type()
)
hzOduPrimaryDegradeMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryDegradeMonitorState.setStatus("mandatory")
_HzOduPrimaryHardFaultMonitorState_Type = DisplayString
_HzOduPrimaryHardFaultMonitorState_Object = MibScalar
hzOduPrimaryHardFaultMonitorState = _HzOduPrimaryHardFaultMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 5),
    _HzOduPrimaryHardFaultMonitorState_Type()
)
hzOduPrimaryHardFaultMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryHardFaultMonitorState.setStatus("mandatory")
_HzOduPrimaryMakeRslThresholdState_Type = DisplayString
_HzOduPrimaryMakeRslThresholdState_Object = MibScalar
hzOduPrimaryMakeRslThresholdState = _HzOduPrimaryMakeRslThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 6),
    _HzOduPrimaryMakeRslThresholdState_Type()
)
hzOduPrimaryMakeRslThresholdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryMakeRslThresholdState.setStatus("mandatory")
_HzOduPrimaryPeerRslState_Type = DisplayString
_HzOduPrimaryPeerRslState_Object = MibScalar
hzOduPrimaryPeerRslState = _HzOduPrimaryPeerRslState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 7),
    _HzOduPrimaryPeerRslState_Type()
)
hzOduPrimaryPeerRslState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryPeerRslState.setStatus("mandatory")
_HzOduPrimaryRadioInterfaceState_Type = DisplayString
_HzOduPrimaryRadioInterfaceState_Object = MibScalar
hzOduPrimaryRadioInterfaceState = _HzOduPrimaryRadioInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 8),
    _HzOduPrimaryRadioInterfaceState_Type()
)
hzOduPrimaryRadioInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryRadioInterfaceState.setStatus("mandatory")
_HzOduPrimaryNetworkInterfaceState_Type = DisplayString
_HzOduPrimaryNetworkInterfaceState_Object = MibScalar
hzOduPrimaryNetworkInterfaceState = _HzOduPrimaryNetworkInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 9),
    _HzOduPrimaryNetworkInterfaceState_Type()
)
hzOduPrimaryNetworkInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryNetworkInterfaceState.setStatus("mandatory")
_HzOduPrimaryUserConfiguredEstablishFer_Type = DisplayString
_HzOduPrimaryUserConfiguredEstablishFer_Object = MibScalar
hzOduPrimaryUserConfiguredEstablishFer = _HzOduPrimaryUserConfiguredEstablishFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 10),
    _HzOduPrimaryUserConfiguredEstablishFer_Type()
)
hzOduPrimaryUserConfiguredEstablishFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryUserConfiguredEstablishFer.setStatus("mandatory")
_HzOduPrimaryMinimumAchievableEstablishFer_Type = DisplayString
_HzOduPrimaryMinimumAchievableEstablishFer_Object = MibScalar
hzOduPrimaryMinimumAchievableEstablishFer = _HzOduPrimaryMinimumAchievableEstablishFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 11),
    _HzOduPrimaryMinimumAchievableEstablishFer_Type()
)
hzOduPrimaryMinimumAchievableEstablishFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryMinimumAchievableEstablishFer.setStatus("mandatory")
_HzOduPrimaryUserConfiguredShutdownFer_Type = DisplayString
_HzOduPrimaryUserConfiguredShutdownFer_Object = MibScalar
hzOduPrimaryUserConfiguredShutdownFer = _HzOduPrimaryUserConfiguredShutdownFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 12),
    _HzOduPrimaryUserConfiguredShutdownFer_Type()
)
hzOduPrimaryUserConfiguredShutdownFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryUserConfiguredShutdownFer.setStatus("mandatory")
_HzOduPrimaryMinimumAchievableShutdownFer_Type = DisplayString
_HzOduPrimaryMinimumAchievableShutdownFer_Object = MibScalar
hzOduPrimaryMinimumAchievableShutdownFer = _HzOduPrimaryMinimumAchievableShutdownFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 13),
    _HzOduPrimaryMinimumAchievableShutdownFer_Type()
)
hzOduPrimaryMinimumAchievableShutdownFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryMinimumAchievableShutdownFer.setStatus("mandatory")
_HzOduPrimaryUserConfiguredEstablishMonitorTime_Type = Integer32
_HzOduPrimaryUserConfiguredEstablishMonitorTime_Object = MibScalar
hzOduPrimaryUserConfiguredEstablishMonitorTime = _HzOduPrimaryUserConfiguredEstablishMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 14),
    _HzOduPrimaryUserConfiguredEstablishMonitorTime_Type()
)
hzOduPrimaryUserConfiguredEstablishMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryUserConfiguredEstablishMonitorTime.setStatus("mandatory")
_HzOduPrimaryActualEstablishMonitorTime_Type = Integer32
_HzOduPrimaryActualEstablishMonitorTime_Object = MibScalar
hzOduPrimaryActualEstablishMonitorTime = _HzOduPrimaryActualEstablishMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 15),
    _HzOduPrimaryActualEstablishMonitorTime_Type()
)
hzOduPrimaryActualEstablishMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryActualEstablishMonitorTime.setStatus("mandatory")
_HzOduPrimaryUserConfiguredShutdownMonitorTime_Type = Integer32
_HzOduPrimaryUserConfiguredShutdownMonitorTime_Object = MibScalar
hzOduPrimaryUserConfiguredShutdownMonitorTime = _HzOduPrimaryUserConfiguredShutdownMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 16),
    _HzOduPrimaryUserConfiguredShutdownMonitorTime_Type()
)
hzOduPrimaryUserConfiguredShutdownMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryUserConfiguredShutdownMonitorTime.setStatus("mandatory")
_HzOduPrimaryActualShutdownMonitorTime_Type = Integer32
_HzOduPrimaryActualShutdownMonitorTime_Object = MibScalar
hzOduPrimaryActualShutdownMonitorTime = _HzOduPrimaryActualShutdownMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 14, 2, 9, 17),
    _HzOduPrimaryActualShutdownMonitorTime_Type()
)
hzOduPrimaryActualShutdownMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduPrimaryActualShutdownMonitorTime.setStatus("mandatory")
_HzOduSntp_ObjectIdentity = ObjectIdentity
hzOduSntp = _HzOduSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 15)
)


class _HzOduSntpEnable_Type(Integer32):
    """Custom type hzOduSntpEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduSntpEnable_Type.__name__ = "Integer32"
_HzOduSntpEnable_Object = MibScalar
hzOduSntpEnable = _HzOduSntpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 15, 1),
    _HzOduSntpEnable_Type()
)
hzOduSntpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduSntpEnable.setStatus("mandatory")


class _HzOduSntpOffset_Type(Integer32):
    """Custom type hzOduSntpOffset based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 140),
    )


_HzOduSntpOffset_Type.__name__ = "Integer32"
_HzOduSntpOffset_Object = MibScalar
hzOduSntpOffset = _HzOduSntpOffset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 15, 2),
    _HzOduSntpOffset_Type()
)
hzOduSntpOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduSntpOffset.setStatus("mandatory")
_HzOduSntpServerTable_Object = MibTable
hzOduSntpServerTable = _HzOduSntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 15, 3)
)
if mibBuilder.loadTexts:
    hzOduSntpServerTable.setStatus("mandatory")
_HzOduSntpServerEntry_Object = MibTableRow
hzOduSntpServerEntry = _HzOduSntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 15, 3, 1)
)
hzOduSntpServerEntry.setIndexNames(
    (0, "HORIZON-ODU-MIB", "hzOduSntpServerIndex"),
)
if mibBuilder.loadTexts:
    hzOduSntpServerEntry.setStatus("mandatory")
_HzOduSntpServerIndex_Type = Integer32
_HzOduSntpServerIndex_Object = MibTableColumn
hzOduSntpServerIndex = _HzOduSntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 15, 3, 1, 1),
    _HzOduSntpServerIndex_Type()
)
hzOduSntpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSntpServerIndex.setStatus("mandatory")
_HzOduSntpServerIpAddress_Type = IpAddress
_HzOduSntpServerIpAddress_Object = MibTableColumn
hzOduSntpServerIpAddress = _HzOduSntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 15, 3, 1, 2),
    _HzOduSntpServerIpAddress_Type()
)
hzOduSntpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduSntpServerIpAddress.setStatus("mandatory")


class _HzOduSntpServerStatus_Type(Integer32):
    """Custom type hzOduSntpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("failed", 2))
    )


_HzOduSntpServerStatus_Type.__name__ = "Integer32"
_HzOduSntpServerStatus_Object = MibTableColumn
hzOduSntpServerStatus = _HzOduSntpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 15, 3, 1, 3),
    _HzOduSntpServerStatus_Type()
)
hzOduSntpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSntpServerStatus.setStatus("mandatory")
_HzOduSntpServerStratum_Type = Integer32
_HzOduSntpServerStratum_Object = MibTableColumn
hzOduSntpServerStratum = _HzOduSntpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 15, 3, 1, 4),
    _HzOduSntpServerStratum_Type()
)
hzOduSntpServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduSntpServerStratum.setStatus("mandatory")
_HzOduLogs_ObjectIdentity = ObjectIdentity
hzOduLogs = _HzOduLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 16)
)


class _HzOduEventLogEnable_Type(Integer32):
    """Custom type hzOduEventLogEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduEventLogEnable_Type.__name__ = "Integer32"
_HzOduEventLogEnable_Object = MibScalar
hzOduEventLogEnable = _HzOduEventLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 16, 1),
    _HzOduEventLogEnable_Type()
)
hzOduEventLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduEventLogEnable.setStatus("mandatory")


class _HzOduPerfmLogEnable_Type(Integer32):
    """Custom type hzOduPerfmLogEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzOduPerfmLogEnable_Type.__name__ = "Integer32"
_HzOduPerfmLogEnable_Object = MibScalar
hzOduPerfmLogEnable = _HzOduPerfmLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 16, 2),
    _HzOduPerfmLogEnable_Type()
)
hzOduPerfmLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPerfmLogEnable.setStatus("mandatory")


class _HzOduPerfmLogInterval_Type(DisplayString):
    """Custom type hzOduPerfmLogInterval based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HzOduPerfmLogInterval_Type.__name__ = "DisplayString"
_HzOduPerfmLogInterval_Object = MibScalar
hzOduPerfmLogInterval = _HzOduPerfmLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 16, 3),
    _HzOduPerfmLogInterval_Type()
)
hzOduPerfmLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduPerfmLogInterval.setStatus("mandatory")
_HzOduRadius_ObjectIdentity = ObjectIdentity
hzOduRadius = _HzOduRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 17)
)


class _HzOduRadiusSuperUserAuthentication_Type(Integer32):
    """Custom type hzOduRadiusSuperUserAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzOduRadiusSuperUserAuthentication_Type.__name__ = "Integer32"
_HzOduRadiusSuperUserAuthentication_Object = MibScalar
hzOduRadiusSuperUserAuthentication = _HzOduRadiusSuperUserAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 17, 1),
    _HzOduRadiusSuperUserAuthentication_Type()
)
hzOduRadiusSuperUserAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRadiusSuperUserAuthentication.setStatus("mandatory")


class _HzOduRadiusServerTimeOut_Type(Integer32):
    """Custom type hzOduRadiusServerTimeOut based on Integer32"""
    defaultValue = 0


_HzOduRadiusServerTimeOut_Type.__name__ = "Integer32"
_HzOduRadiusServerTimeOut_Object = MibScalar
hzOduRadiusServerTimeOut = _HzOduRadiusServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 17, 2),
    _HzOduRadiusServerTimeOut_Type()
)
hzOduRadiusServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadiusServerTimeOut.setStatus("mandatory")


class _HzOduRadiusServerDeadTime_Type(Integer32):
    """Custom type hzOduRadiusServerDeadTime based on Integer32"""
    defaultValue = 0


_HzOduRadiusServerDeadTime_Type.__name__ = "Integer32"
_HzOduRadiusServerDeadTime_Object = MibScalar
hzOduRadiusServerDeadTime = _HzOduRadiusServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 17, 3),
    _HzOduRadiusServerDeadTime_Type()
)
hzOduRadiusServerDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadiusServerDeadTime.setStatus("mandatory")


class _HzOduRadiusServerReTransmit_Type(Integer32):
    """Custom type hzOduRadiusServerReTransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("notstrict", 2))
    )


_HzOduRadiusServerReTransmit_Type.__name__ = "Integer32"
_HzOduRadiusServerReTransmit_Object = MibScalar
hzOduRadiusServerReTransmit = _HzOduRadiusServerReTransmit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 17, 4),
    _HzOduRadiusServerReTransmit_Type()
)
hzOduRadiusServerReTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadiusServerReTransmit.setStatus("mandatory")
_HzOduRadiusServerTable_Object = MibTable
hzOduRadiusServerTable = _HzOduRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 17, 5)
)
if mibBuilder.loadTexts:
    hzOduRadiusServerTable.setStatus("mandatory")
_HzOduRadiusServerEntry_Object = MibTableRow
hzOduRadiusServerEntry = _HzOduRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 17, 5, 1)
)
hzOduRadiusServerEntry.setIndexNames(
    (0, "HORIZON-ODU-MIB", "hzOduRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    hzOduRadiusServerEntry.setStatus("mandatory")
_HzOduRadiusServerIndex_Type = Integer32
_HzOduRadiusServerIndex_Object = MibTableColumn
hzOduRadiusServerIndex = _HzOduRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 17, 5, 1, 1),
    _HzOduRadiusServerIndex_Type()
)
hzOduRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadiusServerIndex.setStatus("mandatory")
_HzOduRadiusCfgdHostIpAddress_Type = IpAddress
_HzOduRadiusCfgdHostIpAddress_Object = MibTableColumn
hzOduRadiusCfgdHostIpAddress = _HzOduRadiusCfgdHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 17, 5, 1, 2),
    _HzOduRadiusCfgdHostIpAddress_Type()
)
hzOduRadiusCfgdHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzOduRadiusCfgdHostIpAddress.setStatus("mandatory")
_HzOduRadiusActiveHostIpAddress_Type = IpAddress
_HzOduRadiusActiveHostIpAddress_Object = MibTableColumn
hzOduRadiusActiveHostIpAddress = _HzOduRadiusActiveHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 17, 5, 1, 3),
    _HzOduRadiusActiveHostIpAddress_Type()
)
hzOduRadiusActiveHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzOduRadiusActiveHostIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 0)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 1)
)
linkDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        ""
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 2)
)
linkUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        ""
    )

hzOduExplicitAuthenticationFailureV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 3)
)
if mibBuilder.loadTexts:
    hzOduExplicitAuthenticationFailureV1Trap.setStatus(
        ""
    )

hzOduExplicitAuthenticationFailureClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 4)
)
if mibBuilder.loadTexts:
    hzOduExplicitAuthenticationFailureClearedV1Trap.setStatus(
        ""
    )

hzOduAamConfigMisMatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 5)
)
if mibBuilder.loadTexts:
    hzOduAamConfigMisMatchV1Trap.setStatus(
        ""
    )

hzOduAamConfigMisMatchClearV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 6)
)
if mibBuilder.loadTexts:
    hzOduAamConfigMisMatchClearV1Trap.setStatus(
        ""
    )

hzOduAamActiveV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 7)
)
if mibBuilder.loadTexts:
    hzOduAamActiveV1Trap.setStatus(
        ""
    )

hzOduAamActiveClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 8)
)
if mibBuilder.loadTexts:
    hzOduAamActiveClearedV1Trap.setStatus(
        ""
    )

hzOduAtpcConfigMismatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 9)
)
if mibBuilder.loadTexts:
    hzOduAtpcConfigMismatchV1Trap.setStatus(
        ""
    )

hzOduAtpcConfigMismatchClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 10)
)
if mibBuilder.loadTexts:
    hzOduAtpcConfigMismatchClearedV1Trap.setStatus(
        ""
    )

hzOduSntpServersUnreachableV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 11)
)
if mibBuilder.loadTexts:
    hzOduSntpServersUnreachableV1Trap.setStatus(
        ""
    )

hzOduSntpServersUnreachableClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 12)
)
if mibBuilder.loadTexts:
    hzOduSntpServersUnreachableClearedV1Trap.setStatus(
        ""
    )

hzOduFrequencyFileInvalidV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 13)
)
if mibBuilder.loadTexts:
    hzOduFrequencyFileInvalidV1Trap.setStatus(
        ""
    )

hzOduEnetPort1DroppedFramesThresholdExceededV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 14)
)
if mibBuilder.loadTexts:
    hzOduEnetPort1DroppedFramesThresholdExceededV1Trap.setStatus(
        ""
    )

hzOduEnetPort1DroppedFramesThresholdExceededClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 15)
)
if mibBuilder.loadTexts:
    hzOduEnetPort1DroppedFramesThresholdExceededClearedV1Trap.setStatus(
        ""
    )

hzOduEnetPort1BwUtilizationThresholdExceededV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 16)
)
if mibBuilder.loadTexts:
    hzOduEnetPort1BwUtilizationThresholdExceededV1Trap.setStatus(
        ""
    )

hzOduEnetPort1BwUtilizationThresholdExceededClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 17)
)
if mibBuilder.loadTexts:
    hzOduEnetPort1BwUtilizationThresholdExceededClearedV1Trap.setStatus(
        ""
    )

hzOduEnetPort1RlsMismatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 18)
)
if mibBuilder.loadTexts:
    hzOduEnetPort1RlsMismatchV1Trap.setStatus(
        ""
    )

hzOduEnetPort1RlsMismatchClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 19)
)
if mibBuilder.loadTexts:
    hzOduEnetPort1RlsMismatchClearedV1Trap.setStatus(
        ""
    )

hzOduEnetPort1RlsShutdownActivatedv1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 20)
)
if mibBuilder.loadTexts:
    hzOduEnetPort1RlsShutdownActivatedv1Trap.setStatus(
        ""
    )

hzOduEnetPort1RlsShutdownActivatedClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 21)
)
if mibBuilder.loadTexts:
    hzOduEnetPort1RlsShutdownActivatedClearedV1Trap.setStatus(
        ""
    )

hzOduModem1RxLossOfSignalLockV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 22)
)
if mibBuilder.loadTexts:
    hzOduModem1RxLossOfSignalLockV1Trap.setStatus(
        ""
    )

hzOduModem1RxLossOfSignalLockClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 23)
)
if mibBuilder.loadTexts:
    hzOduModem1RxLossOfSignalLockClearedV1Trap.setStatus(
        ""
    )

hzOduModem1TxLossOfSyncV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 24)
)
if mibBuilder.loadTexts:
    hzOduModem1TxLossOfSyncV1Trap.setStatus(
        ""
    )

hzOduModem1TxLossOfSyncClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 25)
)
if mibBuilder.loadTexts:
    hzOduModem1TxLossOfSyncClearedV1Trap.setStatus(
        ""
    )

hzOduModem1SnrBelowThresholdV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 26)
)
if mibBuilder.loadTexts:
    hzOduModem1SnrBelowThresholdV1Trap.setStatus(
        ""
    )

hzOduModem1SnrBelowThresholdClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 27)
)
if mibBuilder.loadTexts:
    hzOduModem1SnrBelowThresholdClearedV1Trap.setStatus(
        ""
    )

hzOduModem1EqualizerStressExceedThresholdV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 28)
)
if mibBuilder.loadTexts:
    hzOduModem1EqualizerStressExceedThresholdV1Trap.setStatus(
        ""
    )

hzOduModem1EqualizerStressExceedThresholdClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 29)
)
if mibBuilder.loadTexts:
    hzOduModem1EqualizerStressExceedThresholdClearedV1Trap.setStatus(
        ""
    )

hzOduEnetPort1ChannelizedRslBelowThresholdV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 30)
)
if mibBuilder.loadTexts:
    hzOduEnetPort1ChannelizedRslBelowThresholdV1Trap.setStatus(
        ""
    )

hzOduEnetPort1ChannelizedRslBelowThresholdClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 31)
)
if mibBuilder.loadTexts:
    hzOduEnetPort1ChannelizedRslBelowThresholdClearedV1Trap.setStatus(
        ""
    )

hzOduModem1HardwareFaultV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 32)
)
if mibBuilder.loadTexts:
    hzOduModem1HardwareFaultV1Trap.setStatus(
        ""
    )

hzOduModem1HardwareFaultClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 33)
)
if mibBuilder.loadTexts:
    hzOduModem1HardwareFaultClearedV1Trap.setStatus(
        ""
    )

hzOduModem1ProgrammingErrorV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 34)
)
if mibBuilder.loadTexts:
    hzOduModem1ProgrammingErrorV1Trap.setStatus(
        ""
    )

hzOduModem1ProgrammingErrorClearedrV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 35)
)
if mibBuilder.loadTexts:
    hzOduModem1ProgrammingErrorClearedrV1Trap.setStatus(
        ""
    )

hzOduRadio1SynthLostLockV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 36)
)
if mibBuilder.loadTexts:
    hzOduRadio1SynthLostLockV1Trap.setStatus(
        ""
    )

hzOduRadio1SynthLostLockClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 37)
)
if mibBuilder.loadTexts:
    hzOduRadio1SynthLostLockClearedV1Trap.setStatus(
        ""
    )

hzOduRadio1TempCompCalTableNotAvailableV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 38)
)
if mibBuilder.loadTexts:
    hzOduRadio1TempCompCalTableNotAvailableV1Trap.setStatus(
        ""
    )

hzOduRadio1TempCompCalTableNotAvailableClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 39)
)
if mibBuilder.loadTexts:
    hzOduRadio1TempCompCalTableNotAvailableClearedV1Trap.setStatus(
        ""
    )

hzOduRadio1TxDetectorPwrBelowThreshV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 40)
)
if mibBuilder.loadTexts:
    hzOduRadio1TxDetectorPwrBelowThreshV1Trap.setStatus(
        ""
    )

hzOduRadio1TxDetectorPwrBelowThreshClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 41)
)
if mibBuilder.loadTexts:
    hzOduRadio1TxDetectorPwrBelowThreshClearedV1Trap.setStatus(
        ""
    )

hzOduRadio1DrainCurrentOutOfLimitV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 42)
)
if mibBuilder.loadTexts:
    hzOduRadio1DrainCurrentOutOfLimitV1Trap.setStatus(
        ""
    )

hzOduRadio1DrainCurrentOutOfLimitClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 43)
)
if mibBuilder.loadTexts:
    hzOduRadio1DrainCurrentOutOfLimitClearedV1Trap.setStatus(
        ""
    )

hzOduRadio1TemperatureOutOfLimitV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 44)
)
if mibBuilder.loadTexts:
    hzOduRadio1TemperatureOutOfLimitV1Trap.setStatus(
        ""
    )

hzOduRadio1TemperatureOutOfLimitClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 45)
)
if mibBuilder.loadTexts:
    hzOduRadio1TemperatureOutOfLimitClearedV1Trap.setStatus(
        ""
    )

hzOduTtySessionCommencedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 46)
)
hzOduTtySessionCommencedV1Trap.setObjects(
      *(("HORIZON-ODU-MIB", "hzOduTtySessionUserName"),
        ("HORIZON-ODU-MIB", "hzOduTtySessionUserConnectionType"))
)
if mibBuilder.loadTexts:
    hzOduTtySessionCommencedV1Trap.setStatus(
        ""
    )

hzOduTtySessionTerminatedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 47)
)
hzOduTtySessionTerminatedV1Trap.setObjects(
      *(("HORIZON-ODU-MIB", "hzOduTtySessionUserName"),
        ("HORIZON-ODU-MIB", "hzOduTtySessionUserConnectionType"))
)
if mibBuilder.loadTexts:
    hzOduTtySessionTerminatedV1Trap.setStatus(
        ""
    )

hzOduAtpcTxAtCoordinatedPwrV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 48)
)
if mibBuilder.loadTexts:
    hzOduAtpcTxAtCoordinatedPwrV1Trap.setStatus(
        ""
    )

hzOduAtpcTxAtCoordinatedPwrClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 49)
)
if mibBuilder.loadTexts:
    hzOduAtpcTxAtCoordinatedPwrClearedV1Trap.setStatus(
        ""
    )

hzOduPartnerRedundancyModeMismatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 50)
)
if mibBuilder.loadTexts:
    hzOduPartnerRedundancyModeMismatchV1Trap.setStatus(
        ""
    )

hzOduPartnerRedundancyModeMismatchClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 51)
)
if mibBuilder.loadTexts:
    hzOduPartnerRedundancyModeMismatchClearedV1Trap.setStatus(
        ""
    )

hzOduPartnerConfigurationMismatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 52)
)
if mibBuilder.loadTexts:
    hzOduPartnerConfigurationMismatchV1Trap.setStatus(
        ""
    )

hzOduPartnerConfigurationMismatchClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 53)
)
if mibBuilder.loadTexts:
    hzOduPartnerConfigurationMismatchClearedV1Trap.setStatus(
        ""
    )

hzOduHsbActiveOnSecondaryV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 54)
)
if mibBuilder.loadTexts:
    hzOduHsbActiveOnSecondaryV1Trap.setStatus(
        ""
    )

hzOduHsbActiveOnSecondaryClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 55)
)
if mibBuilder.loadTexts:
    hzOduHsbActiveOnSecondaryClearedV1Trap.setStatus(
        ""
    )

hzOduHsbOverrideByUserV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 56)
)
if mibBuilder.loadTexts:
    hzOduHsbOverrideByUserV1Trap.setStatus(
        ""
    )

hzOduHsbOverrideByUserClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 57)
)
if mibBuilder.loadTexts:
    hzOduHsbOverrideByUserClearedV1Trap.setStatus(
        ""
    )

hzOduHsbCrossLinkV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 58)
)
if mibBuilder.loadTexts:
    hzOduHsbCrossLinkV1Trap.setStatus(
        ""
    )

hzOduHsbCrossLinkClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 59)
)
if mibBuilder.loadTexts:
    hzOduHsbCrossLinkClearedV1Trap.setStatus(
        ""
    )

hzOduHsbActiveOnPrimaryV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 60)
)
if mibBuilder.loadTexts:
    hzOduHsbActiveOnPrimaryV1Trap.setStatus(
        ""
    )

hzOduHsbActiveOnPrimaryClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 2, 9, 0, 61)
)
if mibBuilder.loadTexts:
    hzOduHsbActiveOnPrimaryClearedV1Trap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HORIZON-ODU-MIB",
    **{"PhysAddress": PhysAddress,
       "DisplayString": DisplayString,
       "coldStart": coldStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "horizonOdu": horizonOdu,
       "hzOduSystem": hzOduSystem,
       "hzOduSysGeneral": hzOduSysGeneral,
       "hzOduResetSystem": hzOduResetSystem,
       "hzOduSaveMIB": hzOduSaveMIB,
       "hzOduOperStatus": hzOduOperStatus,
       "hzOduAirInterfaceEncryption": hzOduAirInterfaceEncryption,
       "hzOduSystemRedundancy": hzOduSystemRedundancy,
       "hzOduSysSpeed": hzOduSysSpeed,
       "hzOduSystemCurrentSpeed": hzOduSystemCurrentSpeed,
       "hzOduSystemLicensedSpeed": hzOduSystemLicensedSpeed,
       "hzOduSystemMode": hzOduSystemMode,
       "hzOduUpgradeLicensedSpeed": hzOduUpgradeLicensedSpeed,
       "hzOduInventory": hzOduInventory,
       "hzOduHwInventory": hzOduHwInventory,
       "hzOduUnitSerialNo": hzOduUnitSerialNo,
       "hzOduUnitAssemblylNo": hzOduUnitAssemblylNo,
       "hzOduIfSerialNo": hzOduIfSerialNo,
       "hzOduIfAssemblylNo": hzOduIfAssemblylNo,
       "hzOduRfSerialNo": hzOduRfSerialNo,
       "hzOduRfAssemblylNo": hzOduRfAssemblylNo,
       "hzOduNccSerialNo": hzOduNccSerialNo,
       "hzOduNccAssemblylNo": hzOduNccAssemblylNo,
       "hzOduDiplexerSerialNo": hzOduDiplexerSerialNo,
       "hzOduDiplexerAssemblylNo": hzOduDiplexerAssemblylNo,
       "hzOduSwInventory": hzOduSwInventory,
       "hzOduSystemOmniVersionNo": hzOduSystemOmniVersionNo,
       "hzOduModemOmniVersionNo": hzOduModemOmniVersionNo,
       "hzOduFrequencyFileVersionNo": hzOduFrequencyFileVersionNo,
       "hzOduMibVersionNo": hzOduMibVersionNo,
       "hzOduAtpc": hzOduAtpc,
       "hzOduAtpcEnable": hzOduAtpcEnable,
       "hzOduAtpcCoordinatedPowerDbm": hzOduAtpcCoordinatedPowerDbm,
       "hzOduAam": hzOduAam,
       "hzOduAamEnable": hzOduAamEnable,
       "hzOduPeerSysInfo": hzOduPeerSysInfo,
       "hzOduPeerMacAddress": hzOduPeerMacAddress,
       "hzOduPeerIpAddress": hzOduPeerIpAddress,
       "hzOduPeerSubnetMask": hzOduPeerSubnetMask,
       "hzOduSysRedundancy": hzOduSysRedundancy,
       "hzOduSystemRedundancyMode": hzOduSystemRedundancyMode,
       "hzOduSystemRedundancyOverride": hzOduSystemRedundancyOverride,
       "hzOduSystemRedundancyLinkStatus": hzOduSystemRedundancyLinkStatus,
       "hzOduSystemRedundancyStandbyEnetState": hzOduSystemRedundancyStandbyEnetState,
       "hzOduSystemRedundancyStateSwitch": hzOduSystemRedundancyStateSwitch,
       "hzOduAuthentication": hzOduAuthentication,
       "hzOduUniquePeerAuthenticationKey": hzOduUniquePeerAuthenticationKey,
       "hzOduPeerDetectedSerialNumber": hzOduPeerDetectedSerialNumber,
       "hzOduAuthenticationMode": hzOduAuthenticationMode,
       "hzOduAuthenticationFailureAction": hzOduAuthenticationFailureAction,
       "hzOduPeerAuthenticationStatus": hzOduPeerAuthenticationStatus,
       "hzOduNetworkManagement": hzOduNetworkManagement,
       "hzOduMacAddress": hzOduMacAddress,
       "hzOduNetworkManagementInterface": hzOduNetworkManagementInterface,
       "hzOduIpAddress": hzOduIpAddress,
       "hzOduSubnetMask": hzOduSubnetMask,
       "hzOduDefaultGateway": hzOduDefaultGateway,
       "hzOduTelnetAccessMode": hzOduTelnetAccessMode,
       "hzOduSshAccessMode": hzOduSshAccessMode,
       "hzOduVlanTagEnable": hzOduVlanTagEnable,
       "hzOduVlanTagId": hzOduVlanTagId,
       "hzOduVlanTagPriority": hzOduVlanTagPriority,
       "hzOduNetworkInterface": hzOduNetworkInterface,
       "hzOduEnetPort1": hzOduEnetPort1,
       "hzOduEnetPort1Description": hzOduEnetPort1Description,
       "hzOduEnetPort1Config": hzOduEnetPort1Config,
       "hzOduEnetPort1AutoNegotiation": hzOduEnetPort1AutoNegotiation,
       "hzOduEnetPort1Speed": hzOduEnetPort1Speed,
       "hzOduEnetPort1Duplex": hzOduEnetPort1Duplex,
       "hzOduEnetPort1Media": hzOduEnetPort1Media,
       "hzOduEnetPort1AdminState": hzOduEnetPort1AdminState,
       "hzOduEnetPort1OpticalTransceiverState": hzOduEnetPort1OpticalTransceiverState,
       "hzOduEnetPort1PauseFrameEnable": hzOduEnetPort1PauseFrameEnable,
       "hzOduEnetPort1MaxFrameSize": hzOduEnetPort1MaxFrameSize,
       "hzOduEnetPort1DroppedEnetFramesThresholdParameters": hzOduEnetPort1DroppedEnetFramesThresholdParameters,
       "hzOduEnetPort1BandwidthUtilizationThresholdParameters": hzOduEnetPort1BandwidthUtilizationThresholdParameters,
       "hzOduEnetPort1Status": hzOduEnetPort1Status,
       "hzOduEnetPort1LinkStatus": hzOduEnetPort1LinkStatus,
       "hzOduEnetPort1AutoNegotiationStatus": hzOduEnetPort1AutoNegotiationStatus,
       "hzOduEnetPort1SpeedStatus": hzOduEnetPort1SpeedStatus,
       "hzOduEnetPort1DuplexStatus": hzOduEnetPort1DuplexStatus,
       "hzOduEnetPort1MediaStatus": hzOduEnetPort1MediaStatus,
       "hzOduEnetPort1Stats": hzOduEnetPort1Stats,
       "hzOduEnetPort1TxFrames": hzOduEnetPort1TxFrames,
       "hzOduEnetPort1TxBytes": hzOduEnetPort1TxBytes,
       "hzOduEnetPort1RxFrames": hzOduEnetPort1RxFrames,
       "hzOduEnetPort1RxBytes": hzOduEnetPort1RxBytes,
       "hzOduEnetPort1RxFramesInError": hzOduEnetPort1RxFramesInError,
       "hzOduEnetPort1RxFramesCRCError": hzOduEnetPort1RxFramesCRCError,
       "hzOduEnetPort1BWUtilization": hzOduEnetPort1BWUtilization,
       "hzOduEnetPort1IngressDataRate": hzOduEnetPort1IngressDataRate,
       "hzOduEnetPort1EgressDataRate": hzOduEnetPort1EgressDataRate,
       "hzOduEnetPort1FramesInQueue1": hzOduEnetPort1FramesInQueue1,
       "hzOduEnetPort1FramesInQueue2": hzOduEnetPort1FramesInQueue2,
       "hzOduEnetPort1FramesInQueue3": hzOduEnetPort1FramesInQueue3,
       "hzOduEnetPort1FramesInQueue4": hzOduEnetPort1FramesInQueue4,
       "hzOduEnetPort1FramesInQueue1Discarded": hzOduEnetPort1FramesInQueue1Discarded,
       "hzOduEnetPort1FramesInQueue2Discarded": hzOduEnetPort1FramesInQueue2Discarded,
       "hzOduEnetPort1FramesInQueue3Discarded": hzOduEnetPort1FramesInQueue3Discarded,
       "hzOduEnetPort1FramesInQueue4Discarded": hzOduEnetPort1FramesInQueue4Discarded,
       "hzOduEnetPort2": hzOduEnetPort2,
       "hzOduEnetPort2Description": hzOduEnetPort2Description,
       "hzOduEnetPort2Config": hzOduEnetPort2Config,
       "hzOduEnetPort2AutoNegotiation": hzOduEnetPort2AutoNegotiation,
       "hzOduEnetPort2Speed": hzOduEnetPort2Speed,
       "hzOduEnetPort2Duplex": hzOduEnetPort2Duplex,
       "hzOduEnetPort2AdminState": hzOduEnetPort2AdminState,
       "hzOduEnetPort2Status": hzOduEnetPort2Status,
       "hzOduEnetPort2LinkStatus": hzOduEnetPort2LinkStatus,
       "hzOduEnetPort2AutoNegotiationStatus": hzOduEnetPort2AutoNegotiationStatus,
       "hzOduEnetPort2SpeedStatus": hzOduEnetPort2SpeedStatus,
       "hzOduEnetPort2DuplexStatus": hzOduEnetPort2DuplexStatus,
       "hzOduEnetPort2MediaStatus": hzOduEnetPort2MediaStatus,
       "hzOduEnetPort2Stats": hzOduEnetPort2Stats,
       "hzOduEnetPort2TxFrames": hzOduEnetPort2TxFrames,
       "hzOduEnetPort2TxBytes": hzOduEnetPort2TxBytes,
       "hzOduEnetPort2RxFrames": hzOduEnetPort2RxFrames,
       "hzOduEnetPort2RxBytes": hzOduEnetPort2RxBytes,
       "hzOduEnetPort2RxFramesInError": hzOduEnetPort2RxFramesInError,
       "hzOduEnetPort2RxFramesCrcError": hzOduEnetPort2RxFramesCrcError,
       "hzOduWirelessInterface": hzOduWirelessInterface,
       "hzOduWirelessPort1": hzOduWirelessPort1,
       "hzOduWirelessPort1Description": hzOduWirelessPort1Description,
       "hzOduModem1": hzOduModem1,
       "hzOduModem1AdminStatus": hzOduModem1AdminStatus,
       "hzOduModem1OperStatus": hzOduModem1OperStatus,
       "hzOduModem1Reset": hzOduModem1Reset,
       "hzOduModem1ChannelizedRSL": hzOduModem1ChannelizedRSL,
       "hzOduModem1ModulationType": hzOduModem1ModulationType,
       "hzOduModem1CurrentRxSpeed": hzOduModem1CurrentRxSpeed,
       "hzOduModem1CurrentTxSpeed": hzOduModem1CurrentTxSpeed,
       "hzOduModem1SNR": hzOduModem1SNR,
       "hzOduModem1EbToNoiseRatio": hzOduModem1EbToNoiseRatio,
       "hzOduModem1EqualizerStress": hzOduModem1EqualizerStress,
       "hzOduModem1SNRThresholdParameters": hzOduModem1SNRThresholdParameters,
       "hzOduModem1ChannelizedRslBelowThresholdParameters": hzOduModem1ChannelizedRslBelowThresholdParameters,
       "hzOduModem1LastChange": hzOduModem1LastChange,
       "hzOduModem1ChannelizedRSLUnsignedInt": hzOduModem1ChannelizedRSLUnsignedInt,
       "hzOduModem1Statistics": hzOduModem1Statistics,
       "hzOduModem1TxFrames": hzOduModem1TxFrames,
       "hzOduModem1RxFramesOK": hzOduModem1RxFramesOK,
       "hzOduModem1RxFramesError": hzOduModem1RxFramesError,
       "hzOduModem1RxFramesQueueDiscarded": hzOduModem1RxFramesQueueDiscarded,
       "hzOduModem1TxBlocks": hzOduModem1TxBlocks,
       "hzOduModem1RxBlocksOK": hzOduModem1RxBlocksOK,
       "hzOduModem1RxBlocksError": hzOduModem1RxBlocksError,
       "hzOduRadio1": hzOduRadio1,
       "hzOduRadio1OperStatus": hzOduRadio1OperStatus,
       "hzOduRadio1TransmitPowerDbm": hzOduRadio1TransmitPowerDbm,
       "hzOduRadio1ProgrammedAntennaDiameter": hzOduRadio1ProgrammedAntennaDiameter,
       "hzOduRadio1PowerOption": hzOduRadio1PowerOption,
       "hzOduRadio1TxState": hzOduRadio1TxState,
       "hzOduRadio1Temperature": hzOduRadio1Temperature,
       "hzOduFrequencies": hzOduFrequencies,
       "hzOduRadioBand": hzOduRadioBand,
       "hzOduFreqGroupSelected": hzOduFreqGroupSelected,
       "hzOduTxHighFreqTable": hzOduTxHighFreqTable,
       "hzOduTxHighFreqEntry": hzOduTxHighFreqEntry,
       "hzOduTxHighFreqIndex": hzOduTxHighFreqIndex,
       "hzOduTxHighFreqChannelIndex": hzOduTxHighFreqChannelIndex,
       "hzOduTxHighFreqTransmitRfFrequency": hzOduTxHighFreqTransmitRfFrequency,
       "hzOduTxHighFreqReceiveRfFrequency": hzOduTxHighFreqReceiveRfFrequency,
       "hzOduTxHighFreqProgrammed": hzOduTxHighFreqProgrammed,
       "hzOduTxLowFreqTable": hzOduTxLowFreqTable,
       "hzOduTxLowFreqEntry": hzOduTxLowFreqEntry,
       "hzOduTxLowFreqIndex": hzOduTxLowFreqIndex,
       "hzOduTxLowFreqChannelIndex": hzOduTxLowFreqChannelIndex,
       "hzOduTxLowFreqTransmitRfFrequency": hzOduTxLowFreqTransmitRfFrequency,
       "hzOduTxLowFreqReceiveRfFrequency": hzOduTxLowFreqReceiveRfFrequency,
       "hzOduTxLowFreqProgrammed": hzOduTxLowFreqProgrammed,
       "hzOduProgrammedFrequency": hzOduProgrammedFrequency,
       "hzOduProgrammedFrequencyChannel": hzOduProgrammedFrequencyChannel,
       "hzOduProgrammedFrequencyTxRf": hzOduProgrammedFrequencyTxRf,
       "hzOduProgrammedFrequencyRxRf": hzOduProgrammedFrequencyRxRf,
       "hzOduCalendar": hzOduCalendar,
       "hzOduDate": hzOduDate,
       "hzOduTime": hzOduTime,
       "hzOduAlarms": hzOduAlarms,
       "hzOduClearAlarmCounters": hzOduClearAlarmCounters,
       "hzOduSystemAlarms": hzOduSystemAlarms,
       "hzOduExplicitAuthenticationFailure": hzOduExplicitAuthenticationFailure,
       "hzOduExplicitAuthenticationFailureCount": hzOduExplicitAuthenticationFailureCount,
       "hzOduAamConfigMismatch": hzOduAamConfigMismatch,
       "hzOduAamConfigMismatchCount": hzOduAamConfigMismatchCount,
       "hzOduAamActive": hzOduAamActive,
       "hzOduAamActiveCount": hzOduAamActiveCount,
       "hzOduAtpcConfigMismatch": hzOduAtpcConfigMismatch,
       "hzOduAtpcConfigMismatchCount": hzOduAtpcConfigMismatchCount,
       "hzOduSntpServerUnavailableAlarm": hzOduSntpServerUnavailableAlarm,
       "hzOduSntpServerUnavailableAlarmCount": hzOduSntpServerUnavailableAlarmCount,
       "hzOduFrequencyFileInvalid": hzOduFrequencyFileInvalid,
       "hzOduFrequencyFileInvalidCount": hzOduFrequencyFileInvalidCount,
       "hzOduAtpcAutoDisabled": hzOduAtpcAutoDisabled,
       "hzOduAtpcAutoDisabledCount": hzOduAtpcAutoDisabledCount,
       "hzOduPartnerRedundancyModeMismatch": hzOduPartnerRedundancyModeMismatch,
       "hzOduPartnerRedundancyModeMismatchCount": hzOduPartnerRedundancyModeMismatchCount,
       "hzOduPartnerConfigurationMismatch": hzOduPartnerConfigurationMismatch,
       "hzOduPartnerConfigurationMismatchCount": hzOduPartnerConfigurationMismatchCount,
       "hzOduHsbActiveOnSecondary": hzOduHsbActiveOnSecondary,
       "hzOduHsbActiveOnSecondaryCount": hzOduHsbActiveOnSecondaryCount,
       "hzOduHsbOverrideByUser": hzOduHsbOverrideByUser,
       "hzOduHsbOverrideByUserCount": hzOduHsbOverrideByUserCount,
       "hzOduHsbCrossLinkActive": hzOduHsbCrossLinkActive,
       "hzOduHsbCrossLinkActiveCount": hzOduHsbCrossLinkActiveCount,
       "hzOduNetworkInterfaceAlarms": hzOduNetworkInterfaceAlarms,
       "hzOduEnetPort1Alarms": hzOduEnetPort1Alarms,
       "hzOduEnetPort1DroppedEnetFramesThresholdExceeded": hzOduEnetPort1DroppedEnetFramesThresholdExceeded,
       "hzOduEnetPort1DroppedEnetFramesThresholdCount": hzOduEnetPort1DroppedEnetFramesThresholdCount,
       "hzOduEnetPort1BandwidthUtilizationThresholdExceeded": hzOduEnetPort1BandwidthUtilizationThresholdExceeded,
       "hzOduEnetPort1BandwidthUtilizationThresholdCount": hzOduEnetPort1BandwidthUtilizationThresholdCount,
       "hzOduEnetPort1RlsMismatch": hzOduEnetPort1RlsMismatch,
       "hzOduEnetPort1RlsMismatchCount": hzOduEnetPort1RlsMismatchCount,
       "hzOduEnetPort1RLSShutdownActivated": hzOduEnetPort1RLSShutdownActivated,
       "hzOduEnetPort1RLSShutdownActivatedCount": hzOduEnetPort1RLSShutdownActivatedCount,
       "hzOduEnetPort1EthernetLinkDown": hzOduEnetPort1EthernetLinkDown,
       "hzOduEnetPort1EthernetLinkDownActivatedCount": hzOduEnetPort1EthernetLinkDownActivatedCount,
       "hzOduEnetPort2Alarms": hzOduEnetPort2Alarms,
       "hzOduEnetPort2EthernetLinkDown": hzOduEnetPort2EthernetLinkDown,
       "hzOduEnetPort2EthernetLinkDownActivatedCount": hzOduEnetPort2EthernetLinkDownActivatedCount,
       "hzOduWirelessInterfaceAlarms": hzOduWirelessInterfaceAlarms,
       "hzOduModem1Alarms": hzOduModem1Alarms,
       "hzOduModem1RxLossOfSignal": hzOduModem1RxLossOfSignal,
       "hzOduModem1RxLossOfSignalCount": hzOduModem1RxLossOfSignalCount,
       "hzOduModem1TxLossOfSync": hzOduModem1TxLossOfSync,
       "hzOduModem1TxLossOfSyncCount": hzOduModem1TxLossOfSyncCount,
       "hzOduModem1SnrBelowThreshold": hzOduModem1SnrBelowThreshold,
       "hzOduModem1SnrBelowThresholdCount": hzOduModem1SnrBelowThresholdCount,
       "hzOduModem1EqualizerStressExceedThreshold": hzOduModem1EqualizerStressExceedThreshold,
       "hzOduModem1EquilizerStressExceedThresholdCount": hzOduModem1EquilizerStressExceedThresholdCount,
       "hzOduModem1HardwareFault": hzOduModem1HardwareFault,
       "hzOduModem1HardwareFaultCount": hzOduModem1HardwareFaultCount,
       "hzOduModem1ProgrammingError": hzOduModem1ProgrammingError,
       "hzOduModem1ProgrammingErrorCount": hzOduModem1ProgrammingErrorCount,
       "hzOduRadio1Alarms": hzOduRadio1Alarms,
       "hzOduRadio1SynthLostLock": hzOduRadio1SynthLostLock,
       "hzOduRadio1SynthLostLockCount": hzOduRadio1SynthLostLockCount,
       "hzOduRadio1TempCompCalTableNotAvail": hzOduRadio1TempCompCalTableNotAvail,
       "hzOduRadio1TempCompCalTableNotAvailCount": hzOduRadio1TempCompCalTableNotAvailCount,
       "hzOduRadio1TxDetectorPwrBelowThresh": hzOduRadio1TxDetectorPwrBelowThresh,
       "hzOduRadio1TxDetectorPwrBelowThreshCount": hzOduRadio1TxDetectorPwrBelowThreshCount,
       "hzOduRadio1DrainCurrentOutOfLimit": hzOduRadio1DrainCurrentOutOfLimit,
       "hzOduRadio1DrainCurrentOutOfLimitCount": hzOduRadio1DrainCurrentOutOfLimitCount,
       "hzOduRadio1TemperatureOutOfLimit": hzOduRadio1TemperatureOutOfLimit,
       "hzOduRadio1TemperatureOutOfLimitCount": hzOduRadio1TemperatureOutOfLimitCount,
       "hzOduTraps": hzOduTraps,
       "hzOduExplicitAuthenticationFailureV1Trap": hzOduExplicitAuthenticationFailureV1Trap,
       "hzOduExplicitAuthenticationFailureClearedV1Trap": hzOduExplicitAuthenticationFailureClearedV1Trap,
       "hzOduAamConfigMisMatchV1Trap": hzOduAamConfigMisMatchV1Trap,
       "hzOduAamConfigMisMatchClearV1Trap": hzOduAamConfigMisMatchClearV1Trap,
       "hzOduAamActiveV1Trap": hzOduAamActiveV1Trap,
       "hzOduAamActiveClearedV1Trap": hzOduAamActiveClearedV1Trap,
       "hzOduAtpcConfigMismatchV1Trap": hzOduAtpcConfigMismatchV1Trap,
       "hzOduAtpcConfigMismatchClearedV1Trap": hzOduAtpcConfigMismatchClearedV1Trap,
       "hzOduSntpServersUnreachableV1Trap": hzOduSntpServersUnreachableV1Trap,
       "hzOduSntpServersUnreachableClearedV1Trap": hzOduSntpServersUnreachableClearedV1Trap,
       "hzOduFrequencyFileInvalidV1Trap": hzOduFrequencyFileInvalidV1Trap,
       "hzOduEnetPort1DroppedFramesThresholdExceededV1Trap": hzOduEnetPort1DroppedFramesThresholdExceededV1Trap,
       "hzOduEnetPort1DroppedFramesThresholdExceededClearedV1Trap": hzOduEnetPort1DroppedFramesThresholdExceededClearedV1Trap,
       "hzOduEnetPort1BwUtilizationThresholdExceededV1Trap": hzOduEnetPort1BwUtilizationThresholdExceededV1Trap,
       "hzOduEnetPort1BwUtilizationThresholdExceededClearedV1Trap": hzOduEnetPort1BwUtilizationThresholdExceededClearedV1Trap,
       "hzOduEnetPort1RlsMismatchV1Trap": hzOduEnetPort1RlsMismatchV1Trap,
       "hzOduEnetPort1RlsMismatchClearedV1Trap": hzOduEnetPort1RlsMismatchClearedV1Trap,
       "hzOduEnetPort1RlsShutdownActivatedv1Trap": hzOduEnetPort1RlsShutdownActivatedv1Trap,
       "hzOduEnetPort1RlsShutdownActivatedClearedV1Trap": hzOduEnetPort1RlsShutdownActivatedClearedV1Trap,
       "hzOduModem1RxLossOfSignalLockV1Trap": hzOduModem1RxLossOfSignalLockV1Trap,
       "hzOduModem1RxLossOfSignalLockClearedV1Trap": hzOduModem1RxLossOfSignalLockClearedV1Trap,
       "hzOduModem1TxLossOfSyncV1Trap": hzOduModem1TxLossOfSyncV1Trap,
       "hzOduModem1TxLossOfSyncClearedV1Trap": hzOduModem1TxLossOfSyncClearedV1Trap,
       "hzOduModem1SnrBelowThresholdV1Trap": hzOduModem1SnrBelowThresholdV1Trap,
       "hzOduModem1SnrBelowThresholdClearedV1Trap": hzOduModem1SnrBelowThresholdClearedV1Trap,
       "hzOduModem1EqualizerStressExceedThresholdV1Trap": hzOduModem1EqualizerStressExceedThresholdV1Trap,
       "hzOduModem1EqualizerStressExceedThresholdClearedV1Trap": hzOduModem1EqualizerStressExceedThresholdClearedV1Trap,
       "hzOduEnetPort1ChannelizedRslBelowThresholdV1Trap": hzOduEnetPort1ChannelizedRslBelowThresholdV1Trap,
       "hzOduEnetPort1ChannelizedRslBelowThresholdClearedV1Trap": hzOduEnetPort1ChannelizedRslBelowThresholdClearedV1Trap,
       "hzOduModem1HardwareFaultV1Trap": hzOduModem1HardwareFaultV1Trap,
       "hzOduModem1HardwareFaultClearedV1Trap": hzOduModem1HardwareFaultClearedV1Trap,
       "hzOduModem1ProgrammingErrorV1Trap": hzOduModem1ProgrammingErrorV1Trap,
       "hzOduModem1ProgrammingErrorClearedrV1Trap": hzOduModem1ProgrammingErrorClearedrV1Trap,
       "hzOduRadio1SynthLostLockV1Trap": hzOduRadio1SynthLostLockV1Trap,
       "hzOduRadio1SynthLostLockClearedV1Trap": hzOduRadio1SynthLostLockClearedV1Trap,
       "hzOduRadio1TempCompCalTableNotAvailableV1Trap": hzOduRadio1TempCompCalTableNotAvailableV1Trap,
       "hzOduRadio1TempCompCalTableNotAvailableClearedV1Trap": hzOduRadio1TempCompCalTableNotAvailableClearedV1Trap,
       "hzOduRadio1TxDetectorPwrBelowThreshV1Trap": hzOduRadio1TxDetectorPwrBelowThreshV1Trap,
       "hzOduRadio1TxDetectorPwrBelowThreshClearedV1Trap": hzOduRadio1TxDetectorPwrBelowThreshClearedV1Trap,
       "hzOduRadio1DrainCurrentOutOfLimitV1Trap": hzOduRadio1DrainCurrentOutOfLimitV1Trap,
       "hzOduRadio1DrainCurrentOutOfLimitClearedV1Trap": hzOduRadio1DrainCurrentOutOfLimitClearedV1Trap,
       "hzOduRadio1TemperatureOutOfLimitV1Trap": hzOduRadio1TemperatureOutOfLimitV1Trap,
       "hzOduRadio1TemperatureOutOfLimitClearedV1Trap": hzOduRadio1TemperatureOutOfLimitClearedV1Trap,
       "hzOduTtySessionCommencedV1Trap": hzOduTtySessionCommencedV1Trap,
       "hzOduTtySessionTerminatedV1Trap": hzOduTtySessionTerminatedV1Trap,
       "hzOduAtpcTxAtCoordinatedPwrV1Trap": hzOduAtpcTxAtCoordinatedPwrV1Trap,
       "hzOduAtpcTxAtCoordinatedPwrClearedV1Trap": hzOduAtpcTxAtCoordinatedPwrClearedV1Trap,
       "hzOduPartnerRedundancyModeMismatchV1Trap": hzOduPartnerRedundancyModeMismatchV1Trap,
       "hzOduPartnerRedundancyModeMismatchClearedV1Trap": hzOduPartnerRedundancyModeMismatchClearedV1Trap,
       "hzOduPartnerConfigurationMismatchV1Trap": hzOduPartnerConfigurationMismatchV1Trap,
       "hzOduPartnerConfigurationMismatchClearedV1Trap": hzOduPartnerConfigurationMismatchClearedV1Trap,
       "hzOduHsbActiveOnSecondaryV1Trap": hzOduHsbActiveOnSecondaryV1Trap,
       "hzOduHsbActiveOnSecondaryClearedV1Trap": hzOduHsbActiveOnSecondaryClearedV1Trap,
       "hzOduHsbOverrideByUserV1Trap": hzOduHsbOverrideByUserV1Trap,
       "hzOduHsbOverrideByUserClearedV1Trap": hzOduHsbOverrideByUserClearedV1Trap,
       "hzOduHsbCrossLinkV1Trap": hzOduHsbCrossLinkV1Trap,
       "hzOduHsbCrossLinkClearedV1Trap": hzOduHsbCrossLinkClearedV1Trap,
       "hzOduHsbActiveOnPrimaryV1Trap": hzOduHsbActiveOnPrimaryV1Trap,
       "hzOduHsbActiveOnPrimaryClearedV1Trap": hzOduHsbActiveOnPrimaryClearedV1Trap,
       "hzOduSnmpTrapHostTable": hzOduSnmpTrapHostTable,
       "hzOduSnmpTrapHostEntry": hzOduSnmpTrapHostEntry,
       "hzOduSnmpTrapHostIndex": hzOduSnmpTrapHostIndex,
       "hzOduSnmpTrapHostMode": hzOduSnmpTrapHostMode,
       "hzOduSnmpTrapHostIpAddress": hzOduSnmpTrapHostIpAddress,
       "hzOduSnmpTrapHostCommunityName": hzOduSnmpTrapHostCommunityName,
       "hzOduSnmpTrapHostActivated": hzOduSnmpTrapHostActivated,
       "hzOduSnmpV3TrapHostsTable": hzOduSnmpV3TrapHostsTable,
       "hzOduSnmpV3TrapHostsEntry": hzOduSnmpV3TrapHostsEntry,
       "hzOduSnmpV3TrapHostsIndex": hzOduSnmpV3TrapHostsIndex,
       "snmpV3TrapHostIpAddress": snmpV3TrapHostIpAddress,
       "snmpV3TrapHostUserName": snmpV3TrapHostUserName,
       "snmpV3TrapHostAuthProtocol": snmpV3TrapHostAuthProtocol,
       "snmpV3TrapHostAuthPassword": snmpV3TrapHostAuthPassword,
       "snmpV3TrapHostPrivProtocol": snmpV3TrapHostPrivProtocol,
       "snmpV3TrapHostPrivPassword": snmpV3TrapHostPrivPassword,
       "snmpV3TrapHostActivated": snmpV3TrapHostActivated,
       "hzOduColdStartTrap": hzOduColdStartTrap,
       "hzOduLinkDownTrap": hzOduLinkDownTrap,
       "hzOduLinkUpTrap": hzOduLinkUpTrap,
       "hzOduExplicitAuthenticationFailureTrap": hzOduExplicitAuthenticationFailureTrap,
       "hzOduAamConfigMismatchTrap": hzOduAamConfigMismatchTrap,
       "hzOduAamActiveTrap": hzOduAamActiveTrap,
       "hzOduAtpcConfigMismatchTrap": hzOduAtpcConfigMismatchTrap,
       "hzOduSntpServersUnreachableTrap": hzOduSntpServersUnreachableTrap,
       "hzOduFrequencyFileInvalidTrap": hzOduFrequencyFileInvalidTrap,
       "hzOduEnetPort1DroppedFramesThresholdExceedTrap": hzOduEnetPort1DroppedFramesThresholdExceedTrap,
       "hzOduEnetPort1BandwidthUtilizationThresholdExceedTrap": hzOduEnetPort1BandwidthUtilizationThresholdExceedTrap,
       "hzOduEnetPort1RlsMismatchTrap": hzOduEnetPort1RlsMismatchTrap,
       "hzOduEnetPort1RLSShutdownActivatedTrap": hzOduEnetPort1RLSShutdownActivatedTrap,
       "hzOduModem1RxLossOfSignalLockTrap": hzOduModem1RxLossOfSignalLockTrap,
       "hzOduModem1TxLossOfSyncTrap": hzOduModem1TxLossOfSyncTrap,
       "hzOduModem1SnrBelowThresholdTrap": hzOduModem1SnrBelowThresholdTrap,
       "hzOduModem1EqualizerStressExceedThresholdTrap": hzOduModem1EqualizerStressExceedThresholdTrap,
       "hzOduModem1ChannelizedRslBelowThresholdTrap": hzOduModem1ChannelizedRslBelowThresholdTrap,
       "hzOduModem1HardwareFaultTrap": hzOduModem1HardwareFaultTrap,
       "hzOduModem1ProgrammingErrorTrap": hzOduModem1ProgrammingErrorTrap,
       "hzOduRadio1SynthLostLockTrap": hzOduRadio1SynthLostLockTrap,
       "hzOduRadio1TempCompCalTableNotAvailTrap": hzOduRadio1TempCompCalTableNotAvailTrap,
       "hzOduRadio1TxDetectorPwrBelowThreshTrap": hzOduRadio1TxDetectorPwrBelowThreshTrap,
       "hzOduRadio1DrainCurrentOutOfLimitTrap": hzOduRadio1DrainCurrentOutOfLimitTrap,
       "hzOduRadio1TemperatureOutOfLimitTrap": hzOduRadio1TemperatureOutOfLimitTrap,
       "hzOduTtyManagementSessionCommencedTrap": hzOduTtyManagementSessionCommencedTrap,
       "hzOduTtyManagementSessionTerminatedTrap": hzOduTtyManagementSessionTerminatedTrap,
       "hzOduAtpcAutoDisabledTrap": hzOduAtpcAutoDisabledTrap,
       "hzOduPartnerRedundancyModeMismatchTrap": hzOduPartnerRedundancyModeMismatchTrap,
       "hzOduPartnerConfigurationMismatchTrap": hzOduPartnerConfigurationMismatchTrap,
       "hzOduHsbActiveOnSecondaryTrap": hzOduHsbActiveOnSecondaryTrap,
       "hzOduHsbOverrideByUserTrap": hzOduHsbOverrideByUserTrap,
       "hzOduHsbCrossLinkTrap": hzOduHsbCrossLinkTrap,
       "hzOduHsbActiveOnPrimaryTrap": hzOduHsbActiveOnPrimaryTrap,
       "hzOduSnmp": hzOduSnmp,
       "hzOduSnmpUserAccess": hzOduSnmpUserAccess,
       "hzOduSnmpManagerAnyCommunityName": hzOduSnmpManagerAnyCommunityName,
       "hzOduSnmpSetRequests": hzOduSnmpSetRequests,
       "hzOduSnmpManagersTable": hzOduSnmpManagersTable,
       "hzOduSnmpManagersEntry": hzOduSnmpManagersEntry,
       "hzOduSnmpManagersIndex": hzOduSnmpManagersIndex,
       "hzOduSnmpManagerIpAddress": hzOduSnmpManagerIpAddress,
       "hzOduSnmpManagerCommunityName": hzOduSnmpManagerCommunityName,
       "hzOduSnmpManagerActivated": hzOduSnmpManagerActivated,
       "hzOduSnmpV3ManagersTable": hzOduSnmpV3ManagersTable,
       "hzOduSnmpV3ManagersEntry": hzOduSnmpV3ManagersEntry,
       "hzOduSnmpV3ManagersIndex": hzOduSnmpV3ManagersIndex,
       "hzOduSnmpV3ManagerUserName": hzOduSnmpV3ManagerUserName,
       "hzOduSnmpV3ManagerAuthProtocol": hzOduSnmpV3ManagerAuthProtocol,
       "hzOduSnmpV3ManagerAuthPassword": hzOduSnmpV3ManagerAuthPassword,
       "hzOduSnmpV3ManagerPrivProtocol": hzOduSnmpV3ManagerPrivProtocol,
       "hzOduSnmpV3ManagerPrivPassword": hzOduSnmpV3ManagerPrivPassword,
       "hzOduSnmpV3ManagerActivated": hzOduSnmpV3ManagerActivated,
       "hzOduManagementSessions": hzOduManagementSessions,
       "hzOduTtySessionUser1": hzOduTtySessionUser1,
       "hzOduTtySessionUser1Name": hzOduTtySessionUser1Name,
       "hzOduTtySessionUser1ConnectionType": hzOduTtySessionUser1ConnectionType,
       "hzOduTtySessionUser1State": hzOduTtySessionUser1State,
       "hzOduTtySessionUser2": hzOduTtySessionUser2,
       "hzOduTtySessionUser2Name": hzOduTtySessionUser2Name,
       "hzOduTtySessionUser2ConnectionType": hzOduTtySessionUser2ConnectionType,
       "hzOduTtySessionUser2State": hzOduTtySessionUser2State,
       "hzOduTtySessionUser3": hzOduTtySessionUser3,
       "hzOduTtySessionUser3Name": hzOduTtySessionUser3Name,
       "hzOduTtySessionUser3ConnectionType": hzOduTtySessionUser3ConnectionType,
       "hzOduTtySessionUser3State": hzOduTtySessionUser3State,
       "hzOduTtySessionUser4": hzOduTtySessionUser4,
       "hzOduTtySessionUser4Name": hzOduTtySessionUser4Name,
       "hzOduTtySessionUser4ConnectionType": hzOduTtySessionUser4ConnectionType,
       "hzOduTtySessionUser4State": hzOduTtySessionUser4State,
       "hzOduTtySessionUser5": hzOduTtySessionUser5,
       "hzOduTtySessionUser5Name": hzOduTtySessionUser5Name,
       "hzOduTtySessionUser5ConnectionType": hzOduTtySessionUser5ConnectionType,
       "hzOduTtySessionUser5State": hzOduTtySessionUser5State,
       "hzOduTtySessionUser6": hzOduTtySessionUser6,
       "hzOduTtySessionUser6Name": hzOduTtySessionUser6Name,
       "hzOduTtySessionUser6ConnectionType": hzOduTtySessionUser6ConnectionType,
       "hzOduTtySessionUser6State": hzOduTtySessionUser6State,
       "hzOduSessionUserInformation": hzOduSessionUserInformation,
       "hzOduTtySessionUserName": hzOduTtySessionUserName,
       "hzOduTtySessionUserConnectionType": hzOduTtySessionUserConnectionType,
       "hzOduHttp": hzOduHttp,
       "hzOduHttpEnable": hzOduHttpEnable,
       "hzOduHttpSecure": hzOduHttpSecure,
       "hzOduHttpSecureCertificateStatus": hzOduHttpSecureCertificateStatus,
       "hzOduHttpSecureAccessForAdminUsers": hzOduHttpSecureAccessForAdminUsers,
       "hzOduHttpSecureAccessForNocUsers": hzOduHttpSecureAccessForNocUsers,
       "hzOduHttpSecureAccessForSuperUsers": hzOduHttpSecureAccessForSuperUsers,
       "hzOduQos": hzOduQos,
       "hzOduQosEnable": hzOduQosEnable,
       "hzOduCosType": hzOduCosType,
       "hzOduCoSQinQiTag": hzOduCoSQinQiTag,
       "hzOduCoSQinQoTag": hzOduCoSQinQoTag,
       "hzOduCosQueueMapping": hzOduCosQueueMapping,
       "hzOduCosExpediteQueue": hzOduCosExpediteQueue,
       "hzOduCosQueueCIR": hzOduCosQueueCIR,
       "hzOduCosQueueCBS": hzOduCosQueueCBS,
       "hzOduCosDefaultValue": hzOduCosDefaultValue,
       "hzOduCutThroughProcessing": hzOduCutThroughProcessing,
       "hzOduRapidLinkShutdown": hzOduRapidLinkShutdown,
       "hzOduRapidLinkShutdownVer1": hzOduRapidLinkShutdownVer1,
       "hzOduRlsEnable": hzOduRlsEnable,
       "hzOduAutomaticLinkReestablish": hzOduAutomaticLinkReestablish,
       "hzOduManualLinkReestablish": hzOduManualLinkReestablish,
       "hzOduHysterisisErredFramesPerMilliSecond": hzOduHysterisisErredFramesPerMilliSecond,
       "hzOduHysterisisErredMilliSeconds": hzOduHysterisisErredMilliSeconds,
       "hzOduHysterisisUnerredFramesPerMilliSecond": hzOduHysterisisUnerredFramesPerMilliSecond,
       "hzOduHysterisisUnerredMilliSeconds": hzOduHysterisisUnerredMilliSeconds,
       "hzOduWriteRlsMonitorParametersToSystem": hzOduWriteRlsMonitorParametersToSystem,
       "hzOduRlsSampleTimeInMilliSeconds": hzOduRlsSampleTimeInMilliSeconds,
       "hzOduRapidLinkShutdownVer2": hzOduRapidLinkShutdownVer2,
       "hzOduPrimaryRlsEnable": hzOduPrimaryRlsEnable,
       "hzOduPrimaryRlsHardFaultMonitor": hzOduPrimaryRlsHardFaultMonitor,
       "hzOduPrimaryAutomaticLinkReestablish": hzOduPrimaryAutomaticLinkReestablish,
       "hzOduPrimaryManualLinkReestablish": hzOduPrimaryManualLinkReestablish,
       "hzOduWritePrimaryRlsMonitorParametersToSystem": hzOduWritePrimaryRlsMonitorParametersToSystem,
       "hzOduPrimarySoftFaultMonitor": hzOduPrimarySoftFaultMonitor,
       "hzOduPrimaryEstablishErredFrameThreshold": hzOduPrimaryEstablishErredFrameThreshold,
       "hzOduPrimaryShutdownErredFrameThreshold": hzOduPrimaryShutdownErredFrameThreshold,
       "hzOduPrimaryEstablishNumberOfSamples": hzOduPrimaryEstablishNumberOfSamples,
       "hzOduPrimaryShutdownNumberOfSamples": hzOduPrimaryShutdownNumberOfSamples,
       "hzOduPrimaryEstablishSamplePeriod": hzOduPrimaryEstablishSamplePeriod,
       "hzOduPrimaryShutdownSamplePeriod": hzOduPrimaryShutdownSamplePeriod,
       "hzOduPrimaryQuickShutdownSamplePeriod": hzOduPrimaryQuickShutdownSamplePeriod,
       "hzOduPrimaryHardFaultMonitor": hzOduPrimaryHardFaultMonitor,
       "hzOduPrimaryFaultSamplePeriod": hzOduPrimaryFaultSamplePeriod,
       "hzOduPrimaryFaultThreshold": hzOduPrimaryFaultThreshold,
       "hzOduPrimaryReceiveSignalLevelMonitor": hzOduPrimaryReceiveSignalLevelMonitor,
       "hzOduPrimaryRlsMakeRslMonitorRslValue": hzOduPrimaryRlsMakeRslMonitorRslValue,
       "hzOduPrimaryRlsMakeRslMonitorPeriod": hzOduPrimaryRlsMakeRslMonitorPeriod,
       "hzOduPrimaryRlsStatus": hzOduPrimaryRlsStatus,
       "hzOduPrimaryRlsOption": hzOduPrimaryRlsOption,
       "hzOduPrimaryRlsState": hzOduPrimaryRlsState,
       "hzOduPrimaryRlsMismatchState": hzOduPrimaryRlsMismatchState,
       "hzOduPrimaryDegradeMonitorState": hzOduPrimaryDegradeMonitorState,
       "hzOduPrimaryHardFaultMonitorState": hzOduPrimaryHardFaultMonitorState,
       "hzOduPrimaryMakeRslThresholdState": hzOduPrimaryMakeRslThresholdState,
       "hzOduPrimaryPeerRslState": hzOduPrimaryPeerRslState,
       "hzOduPrimaryRadioInterfaceState": hzOduPrimaryRadioInterfaceState,
       "hzOduPrimaryNetworkInterfaceState": hzOduPrimaryNetworkInterfaceState,
       "hzOduPrimaryUserConfiguredEstablishFer": hzOduPrimaryUserConfiguredEstablishFer,
       "hzOduPrimaryMinimumAchievableEstablishFer": hzOduPrimaryMinimumAchievableEstablishFer,
       "hzOduPrimaryUserConfiguredShutdownFer": hzOduPrimaryUserConfiguredShutdownFer,
       "hzOduPrimaryMinimumAchievableShutdownFer": hzOduPrimaryMinimumAchievableShutdownFer,
       "hzOduPrimaryUserConfiguredEstablishMonitorTime": hzOduPrimaryUserConfiguredEstablishMonitorTime,
       "hzOduPrimaryActualEstablishMonitorTime": hzOduPrimaryActualEstablishMonitorTime,
       "hzOduPrimaryUserConfiguredShutdownMonitorTime": hzOduPrimaryUserConfiguredShutdownMonitorTime,
       "hzOduPrimaryActualShutdownMonitorTime": hzOduPrimaryActualShutdownMonitorTime,
       "hzOduSntp": hzOduSntp,
       "hzOduSntpEnable": hzOduSntpEnable,
       "hzOduSntpOffset": hzOduSntpOffset,
       "hzOduSntpServerTable": hzOduSntpServerTable,
       "hzOduSntpServerEntry": hzOduSntpServerEntry,
       "hzOduSntpServerIndex": hzOduSntpServerIndex,
       "hzOduSntpServerIpAddress": hzOduSntpServerIpAddress,
       "hzOduSntpServerStatus": hzOduSntpServerStatus,
       "hzOduSntpServerStratum": hzOduSntpServerStratum,
       "hzOduLogs": hzOduLogs,
       "hzOduEventLogEnable": hzOduEventLogEnable,
       "hzOduPerfmLogEnable": hzOduPerfmLogEnable,
       "hzOduPerfmLogInterval": hzOduPerfmLogInterval,
       "hzOduRadius": hzOduRadius,
       "hzOduRadiusSuperUserAuthentication": hzOduRadiusSuperUserAuthentication,
       "hzOduRadiusServerTimeOut": hzOduRadiusServerTimeOut,
       "hzOduRadiusServerDeadTime": hzOduRadiusServerDeadTime,
       "hzOduRadiusServerReTransmit": hzOduRadiusServerReTransmit,
       "hzOduRadiusServerTable": hzOduRadiusServerTable,
       "hzOduRadiusServerEntry": hzOduRadiusServerEntry,
       "hzOduRadiusServerIndex": hzOduRadiusServerIndex,
       "hzOduRadiusCfgdHostIpAddress": hzOduRadiusCfgdHostIpAddress,
       "hzOduRadiusActiveHostIpAddress": hzOduRadiusActiveHostIpAddress}
)
