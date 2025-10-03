# SNMP MIB module (DRAGONWAVE-HORIZON-IDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dragonwave\DRAGONWAVE-HORIZON-IDU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:27 2025
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

_HorizonIdu_ObjectIdentity = ObjectIdentity
horizonIdu = _HorizonIdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3)
)
_HzIduSystem_ObjectIdentity = ObjectIdentity
hzIduSystem = _HzIduSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1)
)
_HzIduSysGeneral_ObjectIdentity = ObjectIdentity
hzIduSysGeneral = _HzIduSysGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 1)
)


class _HzIduResetSystem_Type(Integer32):
    """Custom type hzIduResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HzIduResetSystem_Type.__name__ = "Integer32"
_HzIduResetSystem_Object = MibScalar
hzIduResetSystem = _HzIduResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 1, 1),
    _HzIduResetSystem_Type()
)
hzIduResetSystem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduResetSystem.setStatus("mandatory")


class _HzIduSaveMIB_Type(Integer32):
    """Custom type hzIduSaveMIB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_HzIduSaveMIB_Type.__name__ = "Integer32"
_HzIduSaveMIB_Object = MibScalar
hzIduSaveMIB = _HzIduSaveMIB_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 1, 2),
    _HzIduSaveMIB_Type()
)
hzIduSaveMIB.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduSaveMIB.setStatus("mandatory")


class _HzIduOperStatus_Type(Integer32):
    """Custom type hzIduOperStatus based on Integer32"""
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


_HzIduOperStatus_Type.__name__ = "Integer32"
_HzIduOperStatus_Object = MibScalar
hzIduOperStatus = _HzIduOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 1, 3),
    _HzIduOperStatus_Type()
)
hzIduOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduOperStatus.setStatus("mandatory")


class _HzIduAirInterfaceEncryption_Type(Integer32):
    """Custom type hzIduAirInterfaceEncryption based on Integer32"""
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


_HzIduAirInterfaceEncryption_Type.__name__ = "Integer32"
_HzIduAirInterfaceEncryption_Object = MibScalar
hzIduAirInterfaceEncryption = _HzIduAirInterfaceEncryption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 1, 4),
    _HzIduAirInterfaceEncryption_Type()
)
hzIduAirInterfaceEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAirInterfaceEncryption.setStatus("mandatory")


class _HzIduSystemCapacityOption_Type(Integer32):
    """Custom type hzIduSystemCapacityOption based on Integer32"""
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
        *(("singleModem-singleRadio", 1),
          ("multiModem-singleRadio", 2),
          ("multiModem-multiRadio", 3),
          ("singleModem-redundancy", 4))
    )


_HzIduSystemCapacityOption_Type.__name__ = "Integer32"
_HzIduSystemCapacityOption_Object = MibScalar
hzIduSystemCapacityOption = _HzIduSystemCapacityOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 1, 5),
    _HzIduSystemCapacityOption_Type()
)
hzIduSystemCapacityOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduSystemCapacityOption.setStatus("mandatory")
_HzIduSysUpgradeSpeed_ObjectIdentity = ObjectIdentity
hzIduSysUpgradeSpeed = _HzIduSysUpgradeSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 2)
)
_HzIduLicensedSpeedUpgradeSpeedAndKey_Type = DisplayString
_HzIduLicensedSpeedUpgradeSpeedAndKey_Object = MibScalar
hzIduLicensedSpeedUpgradeSpeedAndKey = _HzIduLicensedSpeedUpgradeSpeedAndKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 2, 1),
    _HzIduLicensedSpeedUpgradeSpeedAndKey_Type()
)
hzIduLicensedSpeedUpgradeSpeedAndKey.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduLicensedSpeedUpgradeSpeedAndKey.setStatus("mandatory")
_HzIduLicensedSpeedChanges_Type = Integer32
_HzIduLicensedSpeedChanges_Object = MibScalar
hzIduLicensedSpeedChanges = _HzIduLicensedSpeedChanges_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 2, 2),
    _HzIduLicensedSpeedChanges_Type()
)
hzIduLicensedSpeedChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduLicensedSpeedChanges.setStatus("mandatory")
_HzIduSysDowngradeSpeed_ObjectIdentity = ObjectIdentity
hzIduSysDowngradeSpeed = _HzIduSysDowngradeSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 3)
)
_HzIduLicensedSpeedDowngradeSpeed_Type = Integer32
_HzIduLicensedSpeedDowngradeSpeed_Object = MibScalar
hzIduLicensedSpeedDowngradeSpeed = _HzIduLicensedSpeedDowngradeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 3, 1),
    _HzIduLicensedSpeedDowngradeSpeed_Type()
)
hzIduLicensedSpeedDowngradeSpeed.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduLicensedSpeedDowngradeSpeed.setStatus("mandatory")
_HzIduLicensedSpeedCountUsedForKey_Type = Integer32
_HzIduLicensedSpeedCountUsedForKey_Object = MibScalar
hzIduLicensedSpeedCountUsedForKey = _HzIduLicensedSpeedCountUsedForKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 3, 2),
    _HzIduLicensedSpeedCountUsedForKey_Type()
)
hzIduLicensedSpeedCountUsedForKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduLicensedSpeedCountUsedForKey.setStatus("mandatory")
_HzIduLicensedSpeedDowngradeKey_Type = DisplayString
_HzIduLicensedSpeedDowngradeKey_Object = MibScalar
hzIduLicensedSpeedDowngradeKey = _HzIduLicensedSpeedDowngradeKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 3, 3),
    _HzIduLicensedSpeedDowngradeKey_Type()
)
hzIduLicensedSpeedDowngradeKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduLicensedSpeedDowngradeKey.setStatus("mandatory")
_HzIduSysUpgradeWirelessPorts_ObjectIdentity = ObjectIdentity
hzIduSysUpgradeWirelessPorts = _HzIduSysUpgradeWirelessPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 4)
)
_HzIduLicensedWirelessPortsUpgradeKey_Type = DisplayString
_HzIduLicensedWirelessPortsUpgradeKey_Object = MibScalar
hzIduLicensedWirelessPortsUpgradeKey = _HzIduLicensedWirelessPortsUpgradeKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 4, 1),
    _HzIduLicensedWirelessPortsUpgradeKey_Type()
)
hzIduLicensedWirelessPortsUpgradeKey.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduLicensedWirelessPortsUpgradeKey.setStatus("mandatory")
_HzIduLicensedWirelessPortsChanges_Type = Counter32
_HzIduLicensedWirelessPortsChanges_Object = MibScalar
hzIduLicensedWirelessPortsChanges = _HzIduLicensedWirelessPortsChanges_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 4, 2),
    _HzIduLicensedWirelessPortsChanges_Type()
)
hzIduLicensedWirelessPortsChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduLicensedWirelessPortsChanges.setStatus("mandatory")
_HzIduSysSpeed_ObjectIdentity = ObjectIdentity
hzIduSysSpeed = _HzIduSysSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 5)
)


class _HzIduSystemCurrentSpeed_Type(Integer32):
    """Custom type hzIduSystemCurrentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HzIduSystemCurrentSpeed_Type.__name__ = "Integer32"
_HzIduSystemCurrentSpeed_Object = MibScalar
hzIduSystemCurrentSpeed = _HzIduSystemCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 5, 1),
    _HzIduSystemCurrentSpeed_Type()
)
hzIduSystemCurrentSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduSystemCurrentSpeed.setStatus("mandatory")


class _HzIduSystemLicensedSpeed_Type(Integer32):
    """Custom type hzIduSystemLicensedSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HzIduSystemLicensedSpeed_Type.__name__ = "Integer32"
_HzIduSystemLicensedSpeed_Object = MibScalar
hzIduSystemLicensedSpeed = _HzIduSystemLicensedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 5, 2),
    _HzIduSystemLicensedSpeed_Type()
)
hzIduSystemLicensedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSystemLicensedSpeed.setStatus("mandatory")


class _HzIduSystemMode_Type(Integer32):
    """Custom type hzIduSystemMode based on Integer32"""
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
              40)
        )
    )
    namedValues = NamedValues(
        *(("cw-test", 1),
          ("hz50-67-qpsk", 5),
          ("hz50-110-16qam", 6),
          ("hz50-171-32qam", 7),
          ("hz50-215-64qam", 8),
          ("hz50-271-128qam", 9),
          ("hz50-322-256qam", 10),
          ("hz50-371-256qam", 11),
          ("hz56-65-qpsk", 12),
          ("hz56-111-16qam", 13),
          ("hz56-216-32qam", 14),
          ("hz56-290-128qam", 15),
          ("hz56-385-256qam", 16),
          ("hz28-37-qpsk", 17),
          ("hz28-48-qpsk", 18),
          ("hz28-71-16qam", 19),
          ("hz28-100-32qam", 20),
          ("hz28-144-128qam", 21),
          ("hz28-190-256qam", 22),
          ("hz14-23-qpsk", 23),
          ("hz14-36-16qam", 24),
          ("hz14-47-32qam", 25),
          ("hz14-70-128qam", 26),
          ("hz14-95-256qam", 27),
          ("hz40-57-qpsk", 28),
          ("hz40-58-qpsk", 29),
          ("hz40-110-32qam", 30),
          ("hz40-111-16qam", 31),
          ("hz40-142-32qam", 32),
          ("hz40-181-64qam", 33),
          ("hz40-200-128qam", 34),
          ("hz40-212-128qam", 35),
          ("hz40-277-256qam", 36),
          ("hz30-107-32qam", 37),
          ("hz30-165-128qam", 38),
          ("hz30-212-256qam", 39),
          ("hz50-364-256qam", 40))
    )


_HzIduSystemMode_Type.__name__ = "Integer32"
_HzIduSystemMode_Object = MibScalar
hzIduSystemMode = _HzIduSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 5, 3),
    _HzIduSystemMode_Type()
)
hzIduSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduSystemMode.setStatus("mandatory")
_HzIduInventory_ObjectIdentity = ObjectIdentity
hzIduInventory = _HzIduInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6)
)
_HzIduHwInventory_ObjectIdentity = ObjectIdentity
hzIduHwInventory = _HzIduHwInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1)
)
_HzIduFrequencyFilePartNumber_Type = DisplayString
_HzIduFrequencyFilePartNumber_Object = MibScalar
hzIduFrequencyFilePartNumber = _HzIduFrequencyFilePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 1),
    _HzIduFrequencyFilePartNumber_Type()
)
hzIduFrequencyFilePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFrequencyFilePartNumber.setStatus("mandatory")
_HzIduUnitSerialNo_Type = DisplayString
_HzIduUnitSerialNo_Object = MibScalar
hzIduUnitSerialNo = _HzIduUnitSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 2),
    _HzIduUnitSerialNo_Type()
)
hzIduUnitSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduUnitSerialNo.setStatus("mandatory")
_HzIduUnitAssemblylNo_Type = DisplayString
_HzIduUnitAssemblylNo_Object = MibScalar
hzIduUnitAssemblylNo = _HzIduUnitAssemblylNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 3),
    _HzIduUnitAssemblylNo_Type()
)
hzIduUnitAssemblylNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduUnitAssemblylNo.setStatus("mandatory")
_HzIduIfSerialNo1_Type = DisplayString
_HzIduIfSerialNo1_Object = MibScalar
hzIduIfSerialNo1 = _HzIduIfSerialNo1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 4),
    _HzIduIfSerialNo1_Type()
)
hzIduIfSerialNo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduIfSerialNo1.setStatus("mandatory")
_HzIduIfSerialNo2_Type = DisplayString
_HzIduIfSerialNo2_Object = MibScalar
hzIduIfSerialNo2 = _HzIduIfSerialNo2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 5),
    _HzIduIfSerialNo2_Type()
)
hzIduIfSerialNo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduIfSerialNo2.setStatus("mandatory")
_HzIduIfAssemblylNo1_Type = DisplayString
_HzIduIfAssemblylNo1_Object = MibScalar
hzIduIfAssemblylNo1 = _HzIduIfAssemblylNo1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 6),
    _HzIduIfAssemblylNo1_Type()
)
hzIduIfAssemblylNo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduIfAssemblylNo1.setStatus("mandatory")
_HzIduIfAssemblylNo2_Type = DisplayString
_HzIduIfAssemblylNo2_Object = MibScalar
hzIduIfAssemblylNo2 = _HzIduIfAssemblylNo2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 7),
    _HzIduIfAssemblylNo2_Type()
)
hzIduIfAssemblylNo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduIfAssemblylNo2.setStatus("mandatory")
_HzIduNccSerialNo_Type = DisplayString
_HzIduNccSerialNo_Object = MibScalar
hzIduNccSerialNo = _HzIduNccSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 10),
    _HzIduNccSerialNo_Type()
)
hzIduNccSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduNccSerialNo.setStatus("mandatory")
_HzIduNccAssemblylNo_Type = DisplayString
_HzIduNccAssemblylNo_Object = MibScalar
hzIduNccAssemblylNo = _HzIduNccAssemblylNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 11),
    _HzIduNccAssemblylNo_Type()
)
hzIduNccAssemblylNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduNccAssemblylNo.setStatus("mandatory")
_HzIduRadio1SerialNo_Type = DisplayString
_HzIduRadio1SerialNo_Object = MibScalar
hzIduRadio1SerialNo = _HzIduRadio1SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 12),
    _HzIduRadio1SerialNo_Type()
)
hzIduRadio1SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1SerialNo.setStatus("mandatory")
_HzIduRadio2SerialNo_Type = DisplayString
_HzIduRadio2SerialNo_Object = MibScalar
hzIduRadio2SerialNo = _HzIduRadio2SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 13),
    _HzIduRadio2SerialNo_Type()
)
hzIduRadio2SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2SerialNo.setStatus("mandatory")
_HzIduRadio1HardwareId_Type = DisplayString
_HzIduRadio1HardwareId_Object = MibScalar
hzIduRadio1HardwareId = _HzIduRadio1HardwareId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 14),
    _HzIduRadio1HardwareId_Type()
)
hzIduRadio1HardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1HardwareId.setStatus("mandatory")
_HzIduRadio2HardwareId_Type = DisplayString
_HzIduRadio2HardwareId_Object = MibScalar
hzIduRadio2HardwareId = _HzIduRadio2HardwareId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 15),
    _HzIduRadio2HardwareId_Type()
)
hzIduRadio2HardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2HardwareId.setStatus("mandatory")


class _HzIduInternalIFCouplerPresent_Type(Integer32):
    """Custom type hzIduInternalIFCouplerPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 1),
          ("present", 2))
    )


_HzIduInternalIFCouplerPresent_Type.__name__ = "Integer32"
_HzIduInternalIFCouplerPresent_Object = MibScalar
hzIduInternalIFCouplerPresent = _HzIduInternalIFCouplerPresent_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 16),
    _HzIduInternalIFCouplerPresent_Type()
)
hzIduInternalIFCouplerPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduInternalIFCouplerPresent.setStatus("mandatory")


class _HzIduHwWirelessPortsLicensed_Type(Integer32):
    """Custom type hzIduHwWirelessPortsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HzIduHwWirelessPortsLicensed_Type.__name__ = "Integer32"
_HzIduHwWirelessPortsLicensed_Object = MibScalar
hzIduHwWirelessPortsLicensed = _HzIduHwWirelessPortsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 1, 17),
    _HzIduHwWirelessPortsLicensed_Type()
)
hzIduHwWirelessPortsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduHwWirelessPortsLicensed.setStatus("mandatory")
_HzIduSwInventory_ObjectIdentity = ObjectIdentity
hzIduSwInventory = _HzIduSwInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 2)
)
_HzIduSwInvSystemOmniVersionNo_Type = DisplayString
_HzIduSwInvSystemOmniVersionNo_Object = MibScalar
hzIduSwInvSystemOmniVersionNo = _HzIduSwInvSystemOmniVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 2, 1),
    _HzIduSwInvSystemOmniVersionNo_Type()
)
hzIduSwInvSystemOmniVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSwInvSystemOmniVersionNo.setStatus("mandatory")
_HzIduSwInvModemOmniVersionNo_Type = DisplayString
_HzIduSwInvModemOmniVersionNo_Object = MibScalar
hzIduSwInvModemOmniVersionNo = _HzIduSwInvModemOmniVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 2, 2),
    _HzIduSwInvModemOmniVersionNo_Type()
)
hzIduSwInvModemOmniVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSwInvModemOmniVersionNo.setStatus("mandatory")
_HzIduSwInvFrequencyFileVersionNo_Type = DisplayString
_HzIduSwInvFrequencyFileVersionNo_Object = MibScalar
hzIduSwInvFrequencyFileVersionNo = _HzIduSwInvFrequencyFileVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 2, 3),
    _HzIduSwInvFrequencyFileVersionNo_Type()
)
hzIduSwInvFrequencyFileVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSwInvFrequencyFileVersionNo.setStatus("mandatory")
_HzIduSwInvMibVersionNo_Type = DisplayString
_HzIduSwInvMibVersionNo_Object = MibScalar
hzIduSwInvMibVersionNo = _HzIduSwInvMibVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 2, 4),
    _HzIduSwInvMibVersionNo_Type()
)
hzIduSwInvMibVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSwInvMibVersionNo.setStatus("mandatory")
_HzIduSwInvRadio1FirmwareVersionNo_Type = DisplayString
_HzIduSwInvRadio1FirmwareVersionNo_Object = MibScalar
hzIduSwInvRadio1FirmwareVersionNo = _HzIduSwInvRadio1FirmwareVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 2, 5),
    _HzIduSwInvRadio1FirmwareVersionNo_Type()
)
hzIduSwInvRadio1FirmwareVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSwInvRadio1FirmwareVersionNo.setStatus("mandatory")
_HzIduSwInvRadio2FirmwareVersionNo_Type = DisplayString
_HzIduSwInvRadio2FirmwareVersionNo_Object = MibScalar
hzIduSwInvRadio2FirmwareVersionNo = _HzIduSwInvRadio2FirmwareVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 6, 2, 6),
    _HzIduSwInvRadio2FirmwareVersionNo_Type()
)
hzIduSwInvRadio2FirmwareVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSwInvRadio2FirmwareVersionNo.setStatus("mandatory")
_HzIduAtpc_ObjectIdentity = ObjectIdentity
hzIduAtpc = _HzIduAtpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 7)
)


class _HzIduAtpcEnable_Type(Integer32):
    """Custom type hzIduAtpcEnable based on Integer32"""
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


_HzIduAtpcEnable_Type.__name__ = "Integer32"
_HzIduAtpcEnable_Object = MibScalar
hzIduAtpcEnable = _HzIduAtpcEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 7, 1),
    _HzIduAtpcEnable_Type()
)
hzIduAtpcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduAtpcEnable.setStatus("mandatory")
_HzIduAtpcStatus_Type = DisplayString
_HzIduAtpcStatus_Object = MibScalar
hzIduAtpcStatus = _HzIduAtpcStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 7, 2),
    _HzIduAtpcStatus_Type()
)
hzIduAtpcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAtpcStatus.setStatus("mandatory")
_HzIduAtpcCoordinatedPower_Type = DisplayString
_HzIduAtpcCoordinatedPower_Object = MibScalar
hzIduAtpcCoordinatedPower = _HzIduAtpcCoordinatedPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 7, 3),
    _HzIduAtpcCoordinatedPower_Type()
)
hzIduAtpcCoordinatedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduAtpcCoordinatedPower.setStatus("mandatory")
_HzIduAam_ObjectIdentity = ObjectIdentity
hzIduAam = _HzIduAam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 8)
)


class _HzIduAamStatus_Type(Integer32):
    """Custom type hzIduAamStatus based on Integer32"""
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


_HzIduAamStatus_Type.__name__ = "Integer32"
_HzIduAamStatus_Object = MibScalar
hzIduAamStatus = _HzIduAamStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 8, 1),
    _HzIduAamStatus_Type()
)
hzIduAamStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduAamStatus.setStatus("mandatory")
_HzIduAamDiagnostics_ObjectIdentity = ObjectIdentity
hzIduAamDiagnostics = _HzIduAamDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 8, 2)
)


class _HzIduAamDiagnose_Type(Integer32):
    """Custom type hzIduAamDiagnose based on Integer32"""
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


_HzIduAamDiagnose_Type.__name__ = "Integer32"
_HzIduAamDiagnose_Object = MibScalar
hzIduAamDiagnose = _HzIduAamDiagnose_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 8, 2, 1),
    _HzIduAamDiagnose_Type()
)
hzIduAamDiagnose.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduAamDiagnose.setStatus("mandatory")
_HzIduAamDiagnosticResult_Type = DisplayString
_HzIduAamDiagnosticResult_Object = MibScalar
hzIduAamDiagnosticResult = _HzIduAamDiagnosticResult_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 8, 2, 2),
    _HzIduAamDiagnosticResult_Type()
)
hzIduAamDiagnosticResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAamDiagnosticResult.setStatus("mandatory")
_HzIduPeerSysInfo_ObjectIdentity = ObjectIdentity
hzIduPeerSysInfo = _HzIduPeerSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 9)
)
_HzIduPeerMacAddress_Type = DisplayString
_HzIduPeerMacAddress_Object = MibScalar
hzIduPeerMacAddress = _HzIduPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 9, 1),
    _HzIduPeerMacAddress_Type()
)
hzIduPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduPeerMacAddress.setStatus("mandatory")
_HzIduPeerIpAddress_Type = IpAddress
_HzIduPeerIpAddress_Object = MibScalar
hzIduPeerIpAddress = _HzIduPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 9, 2),
    _HzIduPeerIpAddress_Type()
)
hzIduPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduPeerIpAddress.setStatus("mandatory")
_HzIduPeerSubnetMask_Type = IpAddress
_HzIduPeerSubnetMask_Object = MibScalar
hzIduPeerSubnetMask = _HzIduPeerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 1, 9, 3),
    _HzIduPeerSubnetMask_Type()
)
hzIduPeerSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduPeerSubnetMask.setStatus("mandatory")
_HzIduAuthentication_ObjectIdentity = ObjectIdentity
hzIduAuthentication = _HzIduAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 2)
)


class _HzIduUniquePeerAuthenticationKey_Type(DisplayString):
    """Custom type hzIduUniquePeerAuthenticationKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_HzIduUniquePeerAuthenticationKey_Type.__name__ = "DisplayString"
_HzIduUniquePeerAuthenticationKey_Object = MibScalar
hzIduUniquePeerAuthenticationKey = _HzIduUniquePeerAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 2, 1),
    _HzIduUniquePeerAuthenticationKey_Type()
)
hzIduUniquePeerAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduUniquePeerAuthenticationKey.setStatus("mandatory")
_HzIduPeerDetectedSerialNumber_Type = DisplayString
_HzIduPeerDetectedSerialNumber_Object = MibScalar
hzIduPeerDetectedSerialNumber = _HzIduPeerDetectedSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 2, 2),
    _HzIduPeerDetectedSerialNumber_Type()
)
hzIduPeerDetectedSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduPeerDetectedSerialNumber.setStatus("mandatory")


class _HzIduAuthenticationMode_Type(Integer32):
    """Custom type hzIduAuthenticationMode based on Integer32"""
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


_HzIduAuthenticationMode_Type.__name__ = "Integer32"
_HzIduAuthenticationMode_Object = MibScalar
hzIduAuthenticationMode = _HzIduAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 2, 3),
    _HzIduAuthenticationMode_Type()
)
hzIduAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduAuthenticationMode.setStatus("mandatory")


class _HzIduAuthenticationFailureAction_Type(Integer32):
    """Custom type hzIduAuthenticationFailureAction based on Integer32"""
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


_HzIduAuthenticationFailureAction_Type.__name__ = "Integer32"
_HzIduAuthenticationFailureAction_Object = MibScalar
hzIduAuthenticationFailureAction = _HzIduAuthenticationFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 2, 4),
    _HzIduAuthenticationFailureAction_Type()
)
hzIduAuthenticationFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduAuthenticationFailureAction.setStatus("mandatory")


class _HzIduPeerAuthenticationStatus_Type(Integer32):
    """Custom type hzIduPeerAuthenticationStatus based on Integer32"""
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


_HzIduPeerAuthenticationStatus_Type.__name__ = "Integer32"
_HzIduPeerAuthenticationStatus_Object = MibScalar
hzIduPeerAuthenticationStatus = _HzIduPeerAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 2, 5),
    _HzIduPeerAuthenticationStatus_Type()
)
hzIduPeerAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduPeerAuthenticationStatus.setStatus("mandatory")
_HzIduNetworkManagement_ObjectIdentity = ObjectIdentity
hzIduNetworkManagement = _HzIduNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3)
)
_HzIduMacAddress_Type = DisplayString
_HzIduMacAddress_Object = MibScalar
hzIduMacAddress = _HzIduMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3, 1),
    _HzIduMacAddress_Type()
)
hzIduMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduMacAddress.setStatus("mandatory")


class _HzIduNetworkManagementInterface_Type(Integer32):
    """Custom type hzIduNetworkManagementInterface based on Integer32"""
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


_HzIduNetworkManagementInterface_Type.__name__ = "Integer32"
_HzIduNetworkManagementInterface_Object = MibScalar
hzIduNetworkManagementInterface = _HzIduNetworkManagementInterface_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3, 2),
    _HzIduNetworkManagementInterface_Type()
)
hzIduNetworkManagementInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduNetworkManagementInterface.setStatus("mandatory")
_HzIduIpAddress_Type = IpAddress
_HzIduIpAddress_Object = MibScalar
hzIduIpAddress = _HzIduIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3, 3),
    _HzIduIpAddress_Type()
)
hzIduIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduIpAddress.setStatus("mandatory")
_HzIduSubnetMask_Type = IpAddress
_HzIduSubnetMask_Object = MibScalar
hzIduSubnetMask = _HzIduSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3, 4),
    _HzIduSubnetMask_Type()
)
hzIduSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSubnetMask.setStatus("mandatory")
_HzIduDefaultGateway_Type = IpAddress
_HzIduDefaultGateway_Object = MibScalar
hzIduDefaultGateway = _HzIduDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3, 5),
    _HzIduDefaultGateway_Type()
)
hzIduDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduDefaultGateway.setStatus("mandatory")


class _HzIduTelnetAccessMode_Type(Integer32):
    """Custom type hzIduTelnetAccessMode based on Integer32"""
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


_HzIduTelnetAccessMode_Type.__name__ = "Integer32"
_HzIduTelnetAccessMode_Object = MibScalar
hzIduTelnetAccessMode = _HzIduTelnetAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3, 6),
    _HzIduTelnetAccessMode_Type()
)
hzIduTelnetAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduTelnetAccessMode.setStatus("mandatory")


class _HzIduSshAccessMode_Type(Integer32):
    """Custom type hzIduSshAccessMode based on Integer32"""
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


_HzIduSshAccessMode_Type.__name__ = "Integer32"
_HzIduSshAccessMode_Object = MibScalar
hzIduSshAccessMode = _HzIduSshAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3, 7),
    _HzIduSshAccessMode_Type()
)
hzIduSshAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduSshAccessMode.setStatus("mandatory")


class _HzIduVlanTagEnable_Type(Integer32):
    """Custom type hzIduVlanTagEnable based on Integer32"""
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


_HzIduVlanTagEnable_Type.__name__ = "Integer32"
_HzIduVlanTagEnable_Object = MibScalar
hzIduVlanTagEnable = _HzIduVlanTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3, 8),
    _HzIduVlanTagEnable_Type()
)
hzIduVlanTagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduVlanTagEnable.setStatus("mandatory")


class _HzIduVlanTagId_Type(Integer32):
    """Custom type hzIduVlanTagId based on Integer32"""
    defaultValue = 0


_HzIduVlanTagId_Type.__name__ = "Integer32"
_HzIduVlanTagId_Object = MibScalar
hzIduVlanTagId = _HzIduVlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3, 9),
    _HzIduVlanTagId_Type()
)
hzIduVlanTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduVlanTagId.setStatus("mandatory")


class _HzIduVlanTagPriority_Type(Integer32):
    """Custom type hzIduVlanTagPriority based on Integer32"""
    defaultValue = 0


_HzIduVlanTagPriority_Type.__name__ = "Integer32"
_HzIduVlanTagPriority_Object = MibScalar
hzIduVlanTagPriority = _HzIduVlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 3, 10),
    _HzIduVlanTagPriority_Type()
)
hzIduVlanTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduVlanTagPriority.setStatus("mandatory")
_HzIduNetworkInterface_ObjectIdentity = ObjectIdentity
hzIduNetworkInterface = _HzIduNetworkInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4)
)
_HzIduEnetPort1_ObjectIdentity = ObjectIdentity
hzIduEnetPort1 = _HzIduEnetPort1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1)
)
_HzIduEnetPort1Description_Type = DisplayString
_HzIduEnetPort1Description_Object = MibScalar
hzIduEnetPort1Description = _HzIduEnetPort1Description_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 1),
    _HzIduEnetPort1Description_Type()
)
hzIduEnetPort1Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1Description.setStatus("mandatory")
_HzIduEnetPort1Config_ObjectIdentity = ObjectIdentity
hzIduEnetPort1Config = _HzIduEnetPort1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2)
)


class _HzIduEnetPort1AutoNegotiation_Type(Integer32):
    """Custom type hzIduEnetPort1AutoNegotiation based on Integer32"""
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


_HzIduEnetPort1AutoNegotiation_Type.__name__ = "Integer32"
_HzIduEnetPort1AutoNegotiation_Object = MibScalar
hzIduEnetPort1AutoNegotiation = _HzIduEnetPort1AutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2, 1),
    _HzIduEnetPort1AutoNegotiation_Type()
)
hzIduEnetPort1AutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort1AutoNegotiation.setStatus("mandatory")


class _HzIduEnetPort1Speed_Type(Integer32):
    """Custom type hzIduEnetPort1Speed based on Integer32"""
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


_HzIduEnetPort1Speed_Type.__name__ = "Integer32"
_HzIduEnetPort1Speed_Object = MibScalar
hzIduEnetPort1Speed = _HzIduEnetPort1Speed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2, 2),
    _HzIduEnetPort1Speed_Type()
)
hzIduEnetPort1Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort1Speed.setStatus("mandatory")


class _HzIduEnetPort1Duplex_Type(Integer32):
    """Custom type hzIduEnetPort1Duplex based on Integer32"""
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


_HzIduEnetPort1Duplex_Type.__name__ = "Integer32"
_HzIduEnetPort1Duplex_Object = MibScalar
hzIduEnetPort1Duplex = _HzIduEnetPort1Duplex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2, 3),
    _HzIduEnetPort1Duplex_Type()
)
hzIduEnetPort1Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1Duplex.setStatus("mandatory")


class _HzIduEnetPort1Media_Type(Integer32):
    """Custom type hzIduEnetPort1Media based on Integer32"""
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


_HzIduEnetPort1Media_Type.__name__ = "Integer32"
_HzIduEnetPort1Media_Object = MibScalar
hzIduEnetPort1Media = _HzIduEnetPort1Media_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2, 4),
    _HzIduEnetPort1Media_Type()
)
hzIduEnetPort1Media.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort1Media.setStatus("mandatory")


class _HzIduEnetPort1AdminState_Type(Integer32):
    """Custom type hzIduEnetPort1AdminState based on Integer32"""
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


_HzIduEnetPort1AdminState_Type.__name__ = "Integer32"
_HzIduEnetPort1AdminState_Object = MibScalar
hzIduEnetPort1AdminState = _HzIduEnetPort1AdminState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2, 5),
    _HzIduEnetPort1AdminState_Type()
)
hzIduEnetPort1AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort1AdminState.setStatus("mandatory")


class _HzIduEnetPort1OpticalTransceiverState_Type(Integer32):
    """Custom type hzIduEnetPort1OpticalTransceiverState based on Integer32"""
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


_HzIduEnetPort1OpticalTransceiverState_Type.__name__ = "Integer32"
_HzIduEnetPort1OpticalTransceiverState_Object = MibScalar
hzIduEnetPort1OpticalTransceiverState = _HzIduEnetPort1OpticalTransceiverState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2, 6),
    _HzIduEnetPort1OpticalTransceiverState_Type()
)
hzIduEnetPort1OpticalTransceiverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort1OpticalTransceiverState.setStatus("mandatory")


class _HzIduEnetPort1PauseFrameEnable_Type(Integer32):
    """Custom type hzIduEnetPort1PauseFrameEnable based on Integer32"""
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


_HzIduEnetPort1PauseFrameEnable_Type.__name__ = "Integer32"
_HzIduEnetPort1PauseFrameEnable_Object = MibScalar
hzIduEnetPort1PauseFrameEnable = _HzIduEnetPort1PauseFrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2, 7),
    _HzIduEnetPort1PauseFrameEnable_Type()
)
hzIduEnetPort1PauseFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort1PauseFrameEnable.setStatus("mandatory")


class _HzIduEnetPort1MaxFrameSize_Type(Integer32):
    """Custom type hzIduEnetPort1MaxFrameSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1600, 9600),
    )


_HzIduEnetPort1MaxFrameSize_Type.__name__ = "Integer32"
_HzIduEnetPort1MaxFrameSize_Object = MibScalar
hzIduEnetPort1MaxFrameSize = _HzIduEnetPort1MaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2, 8),
    _HzIduEnetPort1MaxFrameSize_Type()
)
hzIduEnetPort1MaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort1MaxFrameSize.setStatus("mandatory")


class _HzIduEnetPort1DroppedEnetFramesThresholdParameters_Type(DisplayString):
    """Custom type hzIduEnetPort1DroppedEnetFramesThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduEnetPort1DroppedEnetFramesThresholdParameters_Type.__name__ = "DisplayString"
_HzIduEnetPort1DroppedEnetFramesThresholdParameters_Object = MibScalar
hzIduEnetPort1DroppedEnetFramesThresholdParameters = _HzIduEnetPort1DroppedEnetFramesThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2, 9),
    _HzIduEnetPort1DroppedEnetFramesThresholdParameters_Type()
)
hzIduEnetPort1DroppedEnetFramesThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort1DroppedEnetFramesThresholdParameters.setStatus("mandatory")


class _HzIduEnetPort1BandwidthUtilizationThresholdParameters_Type(DisplayString):
    """Custom type hzIduEnetPort1BandwidthUtilizationThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduEnetPort1BandwidthUtilizationThresholdParameters_Type.__name__ = "DisplayString"
_HzIduEnetPort1BandwidthUtilizationThresholdParameters_Object = MibScalar
hzIduEnetPort1BandwidthUtilizationThresholdParameters = _HzIduEnetPort1BandwidthUtilizationThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 2, 10),
    _HzIduEnetPort1BandwidthUtilizationThresholdParameters_Type()
)
hzIduEnetPort1BandwidthUtilizationThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort1BandwidthUtilizationThresholdParameters.setStatus("mandatory")
_HzIduEnetPort1Status_ObjectIdentity = ObjectIdentity
hzIduEnetPort1Status = _HzIduEnetPort1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 3)
)


class _HzIduEnetPort1LinkStatus_Type(Integer32):
    """Custom type hzIduEnetPort1LinkStatus based on Integer32"""
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


_HzIduEnetPort1LinkStatus_Type.__name__ = "Integer32"
_HzIduEnetPort1LinkStatus_Object = MibScalar
hzIduEnetPort1LinkStatus = _HzIduEnetPort1LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 3, 1),
    _HzIduEnetPort1LinkStatus_Type()
)
hzIduEnetPort1LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1LinkStatus.setStatus("mandatory")


class _HzIduEnetPort1AutoNegotiationStatus_Type(Integer32):
    """Custom type hzIduEnetPort1AutoNegotiationStatus based on Integer32"""
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


_HzIduEnetPort1AutoNegotiationStatus_Type.__name__ = "Integer32"
_HzIduEnetPort1AutoNegotiationStatus_Object = MibScalar
hzIduEnetPort1AutoNegotiationStatus = _HzIduEnetPort1AutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 3, 2),
    _HzIduEnetPort1AutoNegotiationStatus_Type()
)
hzIduEnetPort1AutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1AutoNegotiationStatus.setStatus("mandatory")


class _HzIduEnetPort1SpeedStatus_Type(Integer32):
    """Custom type hzIduEnetPort1SpeedStatus based on Integer32"""
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


_HzIduEnetPort1SpeedStatus_Type.__name__ = "Integer32"
_HzIduEnetPort1SpeedStatus_Object = MibScalar
hzIduEnetPort1SpeedStatus = _HzIduEnetPort1SpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 3, 3),
    _HzIduEnetPort1SpeedStatus_Type()
)
hzIduEnetPort1SpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1SpeedStatus.setStatus("mandatory")


class _HzIduEnetPort1DuplexStatus_Type(Integer32):
    """Custom type hzIduEnetPort1DuplexStatus based on Integer32"""
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


_HzIduEnetPort1DuplexStatus_Type.__name__ = "Integer32"
_HzIduEnetPort1DuplexStatus_Object = MibScalar
hzIduEnetPort1DuplexStatus = _HzIduEnetPort1DuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 3, 4),
    _HzIduEnetPort1DuplexStatus_Type()
)
hzIduEnetPort1DuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1DuplexStatus.setStatus("mandatory")


class _HzIduEnetPort1MediaStatus_Type(Integer32):
    """Custom type hzIduEnetPort1MediaStatus based on Integer32"""
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


_HzIduEnetPort1MediaStatus_Type.__name__ = "Integer32"
_HzIduEnetPort1MediaStatus_Object = MibScalar
hzIduEnetPort1MediaStatus = _HzIduEnetPort1MediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 3, 5),
    _HzIduEnetPort1MediaStatus_Type()
)
hzIduEnetPort1MediaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1MediaStatus.setStatus("mandatory")
_HzIduEnetPort1Stats_ObjectIdentity = ObjectIdentity
hzIduEnetPort1Stats = _HzIduEnetPort1Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4)
)
_HzIduEnetPort1TxFrames_Type = Counter32
_HzIduEnetPort1TxFrames_Object = MibScalar
hzIduEnetPort1TxFrames = _HzIduEnetPort1TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 1),
    _HzIduEnetPort1TxFrames_Type()
)
hzIduEnetPort1TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1TxFrames.setStatus("mandatory")
_HzIduEnetPort1TxBytes_Type = Counter32
_HzIduEnetPort1TxBytes_Object = MibScalar
hzIduEnetPort1TxBytes = _HzIduEnetPort1TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 2),
    _HzIduEnetPort1TxBytes_Type()
)
hzIduEnetPort1TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1TxBytes.setStatus("mandatory")
_HzIduEnetPort1RxFrames_Type = Counter32
_HzIduEnetPort1RxFrames_Object = MibScalar
hzIduEnetPort1RxFrames = _HzIduEnetPort1RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 3),
    _HzIduEnetPort1RxFrames_Type()
)
hzIduEnetPort1RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1RxFrames.setStatus("mandatory")
_HzIduEnetPort1RxBytes_Type = Counter32
_HzIduEnetPort1RxBytes_Object = MibScalar
hzIduEnetPort1RxBytes = _HzIduEnetPort1RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 4),
    _HzIduEnetPort1RxBytes_Type()
)
hzIduEnetPort1RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1RxBytes.setStatus("mandatory")
_HzIduEnetPort1RxFramesInErrors_Type = Counter32
_HzIduEnetPort1RxFramesInErrors_Object = MibScalar
hzIduEnetPort1RxFramesInErrors = _HzIduEnetPort1RxFramesInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 5),
    _HzIduEnetPort1RxFramesInErrors_Type()
)
hzIduEnetPort1RxFramesInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1RxFramesInErrors.setStatus("mandatory")
_HzIduEnetPort1RxFramesCRCErrors_Type = Counter32
_HzIduEnetPort1RxFramesCRCErrors_Object = MibScalar
hzIduEnetPort1RxFramesCRCErrors = _HzIduEnetPort1RxFramesCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 6),
    _HzIduEnetPort1RxFramesCRCErrors_Type()
)
hzIduEnetPort1RxFramesCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1RxFramesCRCErrors.setStatus("mandatory")
_HzIduEnetPort1BWUtilization_Type = Integer32
_HzIduEnetPort1BWUtilization_Object = MibScalar
hzIduEnetPort1BWUtilization = _HzIduEnetPort1BWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 7),
    _HzIduEnetPort1BWUtilization_Type()
)
hzIduEnetPort1BWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1BWUtilization.setStatus("mandatory")
_HzIduEnetPort1IngressDataRate_Type = Integer32
_HzIduEnetPort1IngressDataRate_Object = MibScalar
hzIduEnetPort1IngressDataRate = _HzIduEnetPort1IngressDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 8),
    _HzIduEnetPort1IngressDataRate_Type()
)
hzIduEnetPort1IngressDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1IngressDataRate.setStatus("mandatory")
_HzIduEnetPort1EgressDataRate_Type = Integer32
_HzIduEnetPort1EgressDataRate_Object = MibScalar
hzIduEnetPort1EgressDataRate = _HzIduEnetPort1EgressDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 9),
    _HzIduEnetPort1EgressDataRate_Type()
)
hzIduEnetPort1EgressDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1EgressDataRate.setStatus("mandatory")
_HzIduEnetPort1FramesInQueue1s_Type = Counter32
_HzIduEnetPort1FramesInQueue1s_Object = MibScalar
hzIduEnetPort1FramesInQueue1s = _HzIduEnetPort1FramesInQueue1s_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 10),
    _HzIduEnetPort1FramesInQueue1s_Type()
)
hzIduEnetPort1FramesInQueue1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1FramesInQueue1s.setStatus("mandatory")
_HzIduEnetPort1FramesInQueue2s_Type = Counter32
_HzIduEnetPort1FramesInQueue2s_Object = MibScalar
hzIduEnetPort1FramesInQueue2s = _HzIduEnetPort1FramesInQueue2s_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 11),
    _HzIduEnetPort1FramesInQueue2s_Type()
)
hzIduEnetPort1FramesInQueue2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1FramesInQueue2s.setStatus("mandatory")
_HzIduEnetPort1FramesInQueue3s_Type = Counter32
_HzIduEnetPort1FramesInQueue3s_Object = MibScalar
hzIduEnetPort1FramesInQueue3s = _HzIduEnetPort1FramesInQueue3s_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 12),
    _HzIduEnetPort1FramesInQueue3s_Type()
)
hzIduEnetPort1FramesInQueue3s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1FramesInQueue3s.setStatus("mandatory")
_HzIduEnetPort1FramesInQueue4s_Type = Counter32
_HzIduEnetPort1FramesInQueue4s_Object = MibScalar
hzIduEnetPort1FramesInQueue4s = _HzIduEnetPort1FramesInQueue4s_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 13),
    _HzIduEnetPort1FramesInQueue4s_Type()
)
hzIduEnetPort1FramesInQueue4s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1FramesInQueue4s.setStatus("mandatory")
_HzIduEnetPort1FramesInQueue1Discardeds_Type = Counter32
_HzIduEnetPort1FramesInQueue1Discardeds_Object = MibScalar
hzIduEnetPort1FramesInQueue1Discardeds = _HzIduEnetPort1FramesInQueue1Discardeds_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 14),
    _HzIduEnetPort1FramesInQueue1Discardeds_Type()
)
hzIduEnetPort1FramesInQueue1Discardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1FramesInQueue1Discardeds.setStatus("mandatory")
_HzIduEnetPort1FramesInQueue2Discardeds_Type = Counter32
_HzIduEnetPort1FramesInQueue2Discardeds_Object = MibScalar
hzIduEnetPort1FramesInQueue2Discardeds = _HzIduEnetPort1FramesInQueue2Discardeds_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 15),
    _HzIduEnetPort1FramesInQueue2Discardeds_Type()
)
hzIduEnetPort1FramesInQueue2Discardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1FramesInQueue2Discardeds.setStatus("mandatory")
_HzIduEnetPort1FramesInQueue3Discardeds_Type = Counter32
_HzIduEnetPort1FramesInQueue3Discardeds_Object = MibScalar
hzIduEnetPort1FramesInQueue3Discardeds = _HzIduEnetPort1FramesInQueue3Discardeds_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 16),
    _HzIduEnetPort1FramesInQueue3Discardeds_Type()
)
hzIduEnetPort1FramesInQueue3Discardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1FramesInQueue3Discardeds.setStatus("mandatory")
_HzIduEnetPort1FramesInQueue4Discardeds_Type = Counter32
_HzIduEnetPort1FramesInQueue4Discardeds_Object = MibScalar
hzIduEnetPort1FramesInQueue4Discardeds = _HzIduEnetPort1FramesInQueue4Discardeds_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 1, 4, 17),
    _HzIduEnetPort1FramesInQueue4Discardeds_Type()
)
hzIduEnetPort1FramesInQueue4Discardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1FramesInQueue4Discardeds.setStatus("mandatory")
_HzIduEnetPort2_ObjectIdentity = ObjectIdentity
hzIduEnetPort2 = _HzIduEnetPort2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2)
)
_HzIduEnetPort2Description_Type = DisplayString
_HzIduEnetPort2Description_Object = MibScalar
hzIduEnetPort2Description = _HzIduEnetPort2Description_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 1),
    _HzIduEnetPort2Description_Type()
)
hzIduEnetPort2Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2Description.setStatus("mandatory")
_HzIduEnetPort2Config_ObjectIdentity = ObjectIdentity
hzIduEnetPort2Config = _HzIduEnetPort2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 2)
)


class _HzIduEnetPort2AutoNegotiation_Type(Integer32):
    """Custom type hzIduEnetPort2AutoNegotiation based on Integer32"""
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


_HzIduEnetPort2AutoNegotiation_Type.__name__ = "Integer32"
_HzIduEnetPort2AutoNegotiation_Object = MibScalar
hzIduEnetPort2AutoNegotiation = _HzIduEnetPort2AutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 2, 1),
    _HzIduEnetPort2AutoNegotiation_Type()
)
hzIduEnetPort2AutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort2AutoNegotiation.setStatus("mandatory")


class _HzIduEnetPort2Speed_Type(Integer32):
    """Custom type hzIduEnetPort2Speed based on Integer32"""
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


_HzIduEnetPort2Speed_Type.__name__ = "Integer32"
_HzIduEnetPort2Speed_Object = MibScalar
hzIduEnetPort2Speed = _HzIduEnetPort2Speed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 2, 2),
    _HzIduEnetPort2Speed_Type()
)
hzIduEnetPort2Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPort2Speed.setStatus("mandatory")


class _HzIduEnetPort2Duplex_Type(Integer32):
    """Custom type hzIduEnetPort2Duplex based on Integer32"""
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


_HzIduEnetPort2Duplex_Type.__name__ = "Integer32"
_HzIduEnetPort2Duplex_Object = MibScalar
hzIduEnetPort2Duplex = _HzIduEnetPort2Duplex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 2, 3),
    _HzIduEnetPort2Duplex_Type()
)
hzIduEnetPort2Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2Duplex.setStatus("mandatory")


class _HzIduEnetPort2AdminState_Type(Integer32):
    """Custom type hzIduEnetPort2AdminState based on Integer32"""
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


_HzIduEnetPort2AdminState_Type.__name__ = "Integer32"
_HzIduEnetPort2AdminState_Object = MibScalar
hzIduEnetPort2AdminState = _HzIduEnetPort2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 2, 4),
    _HzIduEnetPort2AdminState_Type()
)
hzIduEnetPort2AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2AdminState.setStatus("mandatory")
_HzIduEnetPort2Status_ObjectIdentity = ObjectIdentity
hzIduEnetPort2Status = _HzIduEnetPort2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 3)
)


class _HzIduEnetPort2LinkStatus_Type(Integer32):
    """Custom type hzIduEnetPort2LinkStatus based on Integer32"""
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


_HzIduEnetPort2LinkStatus_Type.__name__ = "Integer32"
_HzIduEnetPort2LinkStatus_Object = MibScalar
hzIduEnetPort2LinkStatus = _HzIduEnetPort2LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 3, 1),
    _HzIduEnetPort2LinkStatus_Type()
)
hzIduEnetPort2LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2LinkStatus.setStatus("mandatory")


class _HzIduEnetPort2AutoNegotiationStatus_Type(Integer32):
    """Custom type hzIduEnetPort2AutoNegotiationStatus based on Integer32"""
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


_HzIduEnetPort2AutoNegotiationStatus_Type.__name__ = "Integer32"
_HzIduEnetPort2AutoNegotiationStatus_Object = MibScalar
hzIduEnetPort2AutoNegotiationStatus = _HzIduEnetPort2AutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 3, 2),
    _HzIduEnetPort2AutoNegotiationStatus_Type()
)
hzIduEnetPort2AutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2AutoNegotiationStatus.setStatus("mandatory")


class _HzIduEnetPort2SpeedStatus_Type(Integer32):
    """Custom type hzIduEnetPort2SpeedStatus based on Integer32"""
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


_HzIduEnetPort2SpeedStatus_Type.__name__ = "Integer32"
_HzIduEnetPort2SpeedStatus_Object = MibScalar
hzIduEnetPort2SpeedStatus = _HzIduEnetPort2SpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 3, 3),
    _HzIduEnetPort2SpeedStatus_Type()
)
hzIduEnetPort2SpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2SpeedStatus.setStatus("mandatory")


class _HzIduEnetPort2DuplexStatus_Type(Integer32):
    """Custom type hzIduEnetPort2DuplexStatus based on Integer32"""
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


_HzIduEnetPort2DuplexStatus_Type.__name__ = "Integer32"
_HzIduEnetPort2DuplexStatus_Object = MibScalar
hzIduEnetPort2DuplexStatus = _HzIduEnetPort2DuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 3, 4),
    _HzIduEnetPort2DuplexStatus_Type()
)
hzIduEnetPort2DuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2DuplexStatus.setStatus("mandatory")
_HzIduEnetPort2Stats_ObjectIdentity = ObjectIdentity
hzIduEnetPort2Stats = _HzIduEnetPort2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 4)
)
_HzIduEnetPort2TxFrames_Type = Counter32
_HzIduEnetPort2TxFrames_Object = MibScalar
hzIduEnetPort2TxFrames = _HzIduEnetPort2TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 4, 1),
    _HzIduEnetPort2TxFrames_Type()
)
hzIduEnetPort2TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2TxFrames.setStatus("mandatory")
_HzIduEnetPort2TxBytes_Type = Counter32
_HzIduEnetPort2TxBytes_Object = MibScalar
hzIduEnetPort2TxBytes = _HzIduEnetPort2TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 4, 2),
    _HzIduEnetPort2TxBytes_Type()
)
hzIduEnetPort2TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2TxBytes.setStatus("mandatory")
_HzIduEnetPort2RxFrames_Type = Counter32
_HzIduEnetPort2RxFrames_Object = MibScalar
hzIduEnetPort2RxFrames = _HzIduEnetPort2RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 4, 3),
    _HzIduEnetPort2RxFrames_Type()
)
hzIduEnetPort2RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2RxFrames.setStatus("mandatory")
_HzIduEnetPort2RxBytes_Type = Counter32
_HzIduEnetPort2RxBytes_Object = MibScalar
hzIduEnetPort2RxBytes = _HzIduEnetPort2RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 4, 4),
    _HzIduEnetPort2RxBytes_Type()
)
hzIduEnetPort2RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2RxBytes.setStatus("mandatory")
_HzIduEnetPort2RxFramesInErrors_Type = Counter32
_HzIduEnetPort2RxFramesInErrors_Object = MibScalar
hzIduEnetPort2RxFramesInErrors = _HzIduEnetPort2RxFramesInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 4, 5),
    _HzIduEnetPort2RxFramesInErrors_Type()
)
hzIduEnetPort2RxFramesInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2RxFramesInErrors.setStatus("mandatory")
_HzIduEnetPort2RxFramesCrcErrors_Type = Counter32
_HzIduEnetPort2RxFramesCrcErrors_Object = MibScalar
hzIduEnetPort2RxFramesCrcErrors = _HzIduEnetPort2RxFramesCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 4, 2, 4, 6),
    _HzIduEnetPort2RxFramesCrcErrors_Type()
)
hzIduEnetPort2RxFramesCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2RxFramesCrcErrors.setStatus("mandatory")
_HzIduWirelessInterface_ObjectIdentity = ObjectIdentity
hzIduWirelessInterface = _HzIduWirelessInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5)
)
_HzIduWirelessInterfaceNames_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceNames = _HzIduWirelessInterfaceNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 1)
)
_HzIduWirelessInterfaceNameTable_Object = MibTable
hzIduWirelessInterfaceNameTable = _HzIduWirelessInterfaceNameTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceNameTable.setStatus("mandatory")
_HzIduWirelessInterfaceNameEntry_Object = MibTableRow
hzIduWirelessInterfaceNameEntry = _HzIduWirelessInterfaceNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 1, 1, 1)
)
hzIduWirelessInterfaceNameEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduWirelessInterfaceNameIndex"),
)
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceNameEntry.setStatus("mandatory")


class _HzIduWirelessInterfaceNameIndex_Type(Integer32):
    """Custom type hzIduWirelessInterfaceNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduWirelessInterfaceNameIndex_Type.__name__ = "Integer32"
_HzIduWirelessInterfaceNameIndex_Object = MibTableColumn
hzIduWirelessInterfaceNameIndex = _HzIduWirelessInterfaceNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 1, 1, 1, 1),
    _HzIduWirelessInterfaceNameIndex_Type()
)
hzIduWirelessInterfaceNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceNameIndex.setStatus("mandatory")
_HzIduWirelessInterfaceName_Type = DisplayString
_HzIduWirelessInterfaceName_Object = MibTableColumn
hzIduWirelessInterfaceName = _HzIduWirelessInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 1, 1, 1, 2),
    _HzIduWirelessInterfaceName_Type()
)
hzIduWirelessInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceName.setStatus("mandatory")
_HzIduWirelessInterfaceModems_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceModems = _HzIduWirelessInterfaceModems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2)
)
_HzIduAggregatedWirelessPortStats_ObjectIdentity = ObjectIdentity
hzIduAggregatedWirelessPortStats = _HzIduAggregatedWirelessPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 1)
)
_HzIduAggregatedWirelessPortTxFrames_Type = Counter32
_HzIduAggregatedWirelessPortTxFrames_Object = MibScalar
hzIduAggregatedWirelessPortTxFrames = _HzIduAggregatedWirelessPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 1, 1),
    _HzIduAggregatedWirelessPortTxFrames_Type()
)
hzIduAggregatedWirelessPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAggregatedWirelessPortTxFrames.setStatus("mandatory")
_HzIduAggregatedWirelessPortRxFramesOKs_Type = Counter32
_HzIduAggregatedWirelessPortRxFramesOKs_Object = MibScalar
hzIduAggregatedWirelessPortRxFramesOKs = _HzIduAggregatedWirelessPortRxFramesOKs_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 1, 2),
    _HzIduAggregatedWirelessPortRxFramesOKs_Type()
)
hzIduAggregatedWirelessPortRxFramesOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAggregatedWirelessPortRxFramesOKs.setStatus("mandatory")
_HzIduAggregatedWirelessPortRxFrameErrors_Type = Counter32
_HzIduAggregatedWirelessPortRxFrameErrors_Object = MibScalar
hzIduAggregatedWirelessPortRxFrameErrors = _HzIduAggregatedWirelessPortRxFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 1, 3),
    _HzIduAggregatedWirelessPortRxFrameErrors_Type()
)
hzIduAggregatedWirelessPortRxFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAggregatedWirelessPortRxFrameErrors.setStatus("mandatory")
_HzIduAggregatedWirelessPortRxFramesQueueDiscards_Type = Counter32
_HzIduAggregatedWirelessPortRxFramesQueueDiscards_Object = MibScalar
hzIduAggregatedWirelessPortRxFramesQueueDiscards = _HzIduAggregatedWirelessPortRxFramesQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 1, 4),
    _HzIduAggregatedWirelessPortRxFramesQueueDiscards_Type()
)
hzIduAggregatedWirelessPortRxFramesQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAggregatedWirelessPortRxFramesQueueDiscards.setStatus("mandatory")
_HzIduModemTable_Object = MibTable
hzIduModemTable = _HzIduModemTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hzIduModemTable.setStatus("mandatory")
_HzIduModemEntry_Object = MibTableRow
hzIduModemEntry = _HzIduModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1)
)
hzIduModemEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemIndex"),
)
if mibBuilder.loadTexts:
    hzIduModemEntry.setStatus("mandatory")


class _HzIduModemIndex_Type(Integer32):
    """Custom type hzIduModemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduModemIndex_Type.__name__ = "Integer32"
_HzIduModemIndex_Object = MibTableColumn
hzIduModemIndex = _HzIduModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 1),
    _HzIduModemIndex_Type()
)
hzIduModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemIndex.setStatus("mandatory")


class _HzIduModemOperStatus_Type(Integer32):
    """Custom type hzIduModemOperStatus based on Integer32"""
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


_HzIduModemOperStatus_Type.__name__ = "Integer32"
_HzIduModemOperStatus_Object = MibTableColumn
hzIduModemOperStatus = _HzIduModemOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 2),
    _HzIduModemOperStatus_Type()
)
hzIduModemOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemOperStatus.setStatus("mandatory")


class _HzIduModemReset_Type(Integer32):
    """Custom type hzIduModemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HzIduModemReset_Type.__name__ = "Integer32"
_HzIduModemReset_Object = MibTableColumn
hzIduModemReset = _HzIduModemReset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 3),
    _HzIduModemReset_Type()
)
hzIduModemReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduModemReset.setStatus("mandatory")
_HzIduModemChannelizedRSL_Type = Integer32
_HzIduModemChannelizedRSL_Object = MibTableColumn
hzIduModemChannelizedRSL = _HzIduModemChannelizedRSL_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 4),
    _HzIduModemChannelizedRSL_Type()
)
hzIduModemChannelizedRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemChannelizedRSL.setStatus("mandatory")
_HzIduModemChannelizedRSLUnsignedInt_Type = Integer32
_HzIduModemChannelizedRSLUnsignedInt_Object = MibTableColumn
hzIduModemChannelizedRSLUnsignedInt = _HzIduModemChannelizedRSLUnsignedInt_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 5),
    _HzIduModemChannelizedRSLUnsignedInt_Type()
)
hzIduModemChannelizedRSLUnsignedInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemChannelizedRSLUnsignedInt.setStatus("mandatory")


class _HzIduModemModulationType_Type(Integer32):
    """Custom type hzIduModemModulationType based on Integer32"""
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


_HzIduModemModulationType_Type.__name__ = "Integer32"
_HzIduModemModulationType_Object = MibTableColumn
hzIduModemModulationType = _HzIduModemModulationType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 6),
    _HzIduModemModulationType_Type()
)
hzIduModemModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemModulationType.setStatus("mandatory")
_HzIduModemRxSpeed_Type = Integer32
_HzIduModemRxSpeed_Object = MibTableColumn
hzIduModemRxSpeed = _HzIduModemRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 7),
    _HzIduModemRxSpeed_Type()
)
hzIduModemRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemRxSpeed.setStatus("mandatory")
_HzIduModemTxSpeed_Type = Integer32
_HzIduModemTxSpeed_Object = MibTableColumn
hzIduModemTxSpeed = _HzIduModemTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 8),
    _HzIduModemTxSpeed_Type()
)
hzIduModemTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemTxSpeed.setStatus("mandatory")
_HzIduModemSNR_Type = Integer32
_HzIduModemSNR_Object = MibTableColumn
hzIduModemSNR = _HzIduModemSNR_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 9),
    _HzIduModemSNR_Type()
)
hzIduModemSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemSNR.setStatus("mandatory")
_HzIduModemEbToNoiseRatio_Type = Integer32
_HzIduModemEbToNoiseRatio_Object = MibTableColumn
hzIduModemEbToNoiseRatio = _HzIduModemEbToNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 10),
    _HzIduModemEbToNoiseRatio_Type()
)
hzIduModemEbToNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemEbToNoiseRatio.setStatus("mandatory")
_HzIduModemEqualizerStress_Type = Integer32
_HzIduModemEqualizerStress_Object = MibTableColumn
hzIduModemEqualizerStress = _HzIduModemEqualizerStress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 11),
    _HzIduModemEqualizerStress_Type()
)
hzIduModemEqualizerStress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemEqualizerStress.setStatus("mandatory")


class _HzIduModemSNRThresholdParameters_Type(DisplayString):
    """Custom type hzIduModemSNRThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduModemSNRThresholdParameters_Type.__name__ = "DisplayString"
_HzIduModemSNRThresholdParameters_Object = MibTableColumn
hzIduModemSNRThresholdParameters = _HzIduModemSNRThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 12),
    _HzIduModemSNRThresholdParameters_Type()
)
hzIduModemSNRThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduModemSNRThresholdParameters.setStatus("mandatory")


class _HzIduModemChannelizedRslBelowThresholdParameters_Type(DisplayString):
    """Custom type hzIduModemChannelizedRslBelowThresholdParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduModemChannelizedRslBelowThresholdParameters_Type.__name__ = "DisplayString"
_HzIduModemChannelizedRslBelowThresholdParameters_Object = MibTableColumn
hzIduModemChannelizedRslBelowThresholdParameters = _HzIduModemChannelizedRslBelowThresholdParameters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 2, 1, 13),
    _HzIduModemChannelizedRslBelowThresholdParameters_Type()
)
hzIduModemChannelizedRslBelowThresholdParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduModemChannelizedRslBelowThresholdParameters.setStatus("mandatory")
_HzIduModemStatsTable_Object = MibTable
hzIduModemStatsTable = _HzIduModemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hzIduModemStatsTable.setStatus("mandatory")
_HzIduModemStatsEntry_Object = MibTableRow
hzIduModemStatsEntry = _HzIduModemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 3, 1)
)
hzIduModemStatsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemStatsIndex"),
)
if mibBuilder.loadTexts:
    hzIduModemStatsEntry.setStatus("mandatory")


class _HzIduModemStatsIndex_Type(Integer32):
    """Custom type hzIduModemStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduModemStatsIndex_Type.__name__ = "Integer32"
_HzIduModemStatsIndex_Object = MibTableColumn
hzIduModemStatsIndex = _HzIduModemStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 3, 1, 1),
    _HzIduModemStatsIndex_Type()
)
hzIduModemStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemStatsIndex.setStatus("mandatory")
_HzIduModemTxBlocks_Type = Counter32
_HzIduModemTxBlocks_Object = MibTableColumn
hzIduModemTxBlocks = _HzIduModemTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 3, 1, 2),
    _HzIduModemTxBlocks_Type()
)
hzIduModemTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemTxBlocks.setStatus("mandatory")
_HzIduModemRxBlocksOKs_Type = Counter32
_HzIduModemRxBlocksOKs_Object = MibTableColumn
hzIduModemRxBlocksOKs = _HzIduModemRxBlocksOKs_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 3, 1, 3),
    _HzIduModemRxBlocksOKs_Type()
)
hzIduModemRxBlocksOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemRxBlocksOKs.setStatus("mandatory")
_HzIduModemRxBlocksErrors_Type = Counter32
_HzIduModemRxBlocksErrors_Object = MibTableColumn
hzIduModemRxBlocksErrors = _HzIduModemRxBlocksErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 2, 3, 1, 4),
    _HzIduModemRxBlocksErrors_Type()
)
hzIduModemRxBlocksErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemRxBlocksErrors.setStatus("mandatory")
_HzIduWirelessInterfaceIFCards_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceIFCards = _HzIduWirelessInterfaceIFCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 3)
)
_HzIduIntermediateFrequencyCardTable_Object = MibTable
hzIduIntermediateFrequencyCardTable = _HzIduIntermediateFrequencyCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    hzIduIntermediateFrequencyCardTable.setStatus("mandatory")
_HzIduIntermediateFrequencyCardEntry_Object = MibTableRow
hzIduIntermediateFrequencyCardEntry = _HzIduIntermediateFrequencyCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 3, 1, 1)
)
hzIduIntermediateFrequencyCardEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduIFCardIndex"),
)
if mibBuilder.loadTexts:
    hzIduIntermediateFrequencyCardEntry.setStatus("mandatory")


class _HzIduIFCardIndex_Type(Integer32):
    """Custom type hzIduIFCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduIFCardIndex_Type.__name__ = "Integer32"
_HzIduIFCardIndex_Object = MibTableColumn
hzIduIFCardIndex = _HzIduIFCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 3, 1, 1, 1),
    _HzIduIFCardIndex_Type()
)
hzIduIFCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduIFCardIndex.setStatus("mandatory")


class _HzIduIFCardTxSynthesizerLock_Type(Integer32):
    """Custom type hzIduIFCardTxSynthesizerLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("locked", 2))
    )


_HzIduIFCardTxSynthesizerLock_Type.__name__ = "Integer32"
_HzIduIFCardTxSynthesizerLock_Object = MibTableColumn
hzIduIFCardTxSynthesizerLock = _HzIduIFCardTxSynthesizerLock_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 3, 1, 1, 2),
    _HzIduIFCardTxSynthesizerLock_Type()
)
hzIduIFCardTxSynthesizerLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduIFCardTxSynthesizerLock.setStatus("mandatory")


class _HzIduIFCardRxSynthesizerLock_Type(Integer32):
    """Custom type hzIduIFCardRxSynthesizerLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("locked", 2))
    )


_HzIduIFCardRxSynthesizerLock_Type.__name__ = "Integer32"
_HzIduIFCardRxSynthesizerLock_Object = MibTableColumn
hzIduIFCardRxSynthesizerLock = _HzIduIFCardRxSynthesizerLock_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 3, 1, 1, 3),
    _HzIduIFCardRxSynthesizerLock_Type()
)
hzIduIFCardRxSynthesizerLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduIFCardRxSynthesizerLock.setStatus("mandatory")
_HzIduWirelessInterfaceRadios_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceRadios = _HzIduWirelessInterfaceRadios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4)
)
_HzIduRadioTable_Object = MibTable
hzIduRadioTable = _HzIduRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    hzIduRadioTable.setStatus("mandatory")
_HzIduRadioEntry_Object = MibTableRow
hzIduRadioEntry = _HzIduRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1)
)
hzIduRadioEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioIndex"),
)
if mibBuilder.loadTexts:
    hzIduRadioEntry.setStatus("mandatory")


class _HzIduRadioIndex_Type(Integer32):
    """Custom type hzIduRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduRadioIndex_Type.__name__ = "Integer32"
_HzIduRadioIndex_Object = MibTableColumn
hzIduRadioIndex = _HzIduRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 1),
    _HzIduRadioIndex_Type()
)
hzIduRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioIndex.setStatus("mandatory")
_HzIduRadioDescription_Type = DisplayString
_HzIduRadioDescription_Object = MibTableColumn
hzIduRadioDescription = _HzIduRadioDescription_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 2),
    _HzIduRadioDescription_Type()
)
hzIduRadioDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioDescription.setStatus("mandatory")


class _HzIduRadioOperStatus_Type(Integer32):
    """Custom type hzIduRadioOperStatus based on Integer32"""
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


_HzIduRadioOperStatus_Type.__name__ = "Integer32"
_HzIduRadioOperStatus_Object = MibTableColumn
hzIduRadioOperStatus = _HzIduRadioOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 3),
    _HzIduRadioOperStatus_Type()
)
hzIduRadioOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioOperStatus.setStatus("mandatory")
_HzIduRadioLastChanged_Type = TimeTicks
_HzIduRadioLastChanged_Object = MibTableColumn
hzIduRadioLastChanged = _HzIduRadioLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 4),
    _HzIduRadioLastChanged_Type()
)
hzIduRadioLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioLastChanged.setStatus("mandatory")
_HzIduRadioReceiveSignalLevel_Type = Integer32
_HzIduRadioReceiveSignalLevel_Object = MibTableColumn
hzIduRadioReceiveSignalLevel = _HzIduRadioReceiveSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 5),
    _HzIduRadioReceiveSignalLevel_Type()
)
hzIduRadioReceiveSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioReceiveSignalLevel.setStatus("mandatory")
_HzIduRadioReceiveSignalLevelUnsigned_Type = Integer32
_HzIduRadioReceiveSignalLevelUnsigned_Object = MibTableColumn
hzIduRadioReceiveSignalLevelUnsigned = _HzIduRadioReceiveSignalLevelUnsigned_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 6),
    _HzIduRadioReceiveSignalLevelUnsigned_Type()
)
hzIduRadioReceiveSignalLevelUnsigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioReceiveSignalLevelUnsigned.setStatus("mandatory")
_HzIduRadioTxGain_Type = Integer32
_HzIduRadioTxGain_Object = MibTableColumn
hzIduRadioTxGain = _HzIduRadioTxGain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 7),
    _HzIduRadioTxGain_Type()
)
hzIduRadioTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioTxGain.setStatus("mandatory")
_HzIduRadioRxGain_Type = Integer32
_HzIduRadioRxGain_Object = MibTableColumn
hzIduRadioRxGain = _HzIduRadioRxGain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 8),
    _HzIduRadioRxGain_Type()
)
hzIduRadioRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioRxGain.setStatus("mandatory")
_HzIduRadioReset_Type = Integer32
_HzIduRadioReset_Object = MibTableColumn
hzIduRadioReset = _HzIduRadioReset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 9),
    _HzIduRadioReset_Type()
)
hzIduRadioReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduRadioReset.setStatus("mandatory")


class _HzIduRadioTransmitPowerdBm_Type(Integer32):
    """Custom type hzIduRadioTransmitPowerdBm based on Integer32"""
    defaultValue = 0


_HzIduRadioTransmitPowerdBm_Type.__name__ = "Integer32"
_HzIduRadioTransmitPowerdBm_Object = MibTableColumn
hzIduRadioTransmitPowerdBm = _HzIduRadioTransmitPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 10),
    _HzIduRadioTransmitPowerdBm_Type()
)
hzIduRadioTransmitPowerdBm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadioTransmitPowerdBm.setStatus("mandatory")


class _HzIduRadioPowerOption_Type(Integer32):
    """Custom type hzIduRadioPowerOption based on Integer32"""
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


_HzIduRadioPowerOption_Type.__name__ = "Integer32"
_HzIduRadioPowerOption_Object = MibTableColumn
hzIduRadioPowerOption = _HzIduRadioPowerOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 11),
    _HzIduRadioPowerOption_Type()
)
hzIduRadioPowerOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioPowerOption.setStatus("mandatory")


class _HzIduRadioTxState_Type(Integer32):
    """Custom type hzIduRadioTxState based on Integer32"""
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


_HzIduRadioTxState_Type.__name__ = "Integer32"
_HzIduRadioTxState_Object = MibTableColumn
hzIduRadioTxState = _HzIduRadioTxState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 12),
    _HzIduRadioTxState_Type()
)
hzIduRadioTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioTxState.setStatus("mandatory")
_HzIduRadioTemperature_Type = Integer32
_HzIduRadioTemperature_Object = MibTableColumn
hzIduRadioTemperature = _HzIduRadioTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 13),
    _HzIduRadioTemperature_Type()
)
hzIduRadioTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioTemperature.setStatus("mandatory")
_HzIduRadioRxCableLoss_Type = DisplayString
_HzIduRadioRxCableLoss_Object = MibTableColumn
hzIduRadioRxCableLoss = _HzIduRadioRxCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 14),
    _HzIduRadioRxCableLoss_Type()
)
hzIduRadioRxCableLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioRxCableLoss.setStatus("mandatory")
_HzIduRadioTxCableLoss_Type = DisplayString
_HzIduRadioTxCableLoss_Object = MibTableColumn
hzIduRadioTxCableLoss = _HzIduRadioTxCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 15),
    _HzIduRadioTxCableLoss_Type()
)
hzIduRadioTxCableLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioTxCableLoss.setStatus("mandatory")
_HzIduRadioTxCableLossChange_Type = DisplayString
_HzIduRadioTxCableLossChange_Object = MibTableColumn
hzIduRadioTxCableLossChange = _HzIduRadioTxCableLossChange_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 4, 1, 1, 16),
    _HzIduRadioTxCableLossChange_Type()
)
hzIduRadioTxCableLossChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioTxCableLossChange.setStatus("mandatory")
_HzIduWirelessInterfaceRadioFrequencies_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceRadioFrequencies = _HzIduWirelessInterfaceRadioFrequencies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5)
)
_HzIduWirelessInterfaceRadio1Frequencies_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceRadio1Frequencies = _HzIduWirelessInterfaceRadio1Frequencies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1)
)


class _HzIduRadio1Band_Type(Integer32):
    """Custom type hzIduRadio1Band based on Integer32"""
    defaultValue = 1

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
        *(("freqNone", 1),
          ("fcc11-1-40", 2),
          ("fcc11-1-30", 3),
          ("fcc18-2-40", 4),
          ("fcc18-2-50", 5),
          ("fcc23-3-50", 6))
    )


_HzIduRadio1Band_Type.__name__ = "Integer32"
_HzIduRadio1Band_Object = MibScalar
hzIduRadio1Band = _HzIduRadio1Band_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 1),
    _HzIduRadio1Band_Type()
)
hzIduRadio1Band.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadio1Band.setStatus("mandatory")


class _HzIduRadio1FreqGroupSelected_Type(Integer32):
    """Custom type hzIduRadio1FreqGroupSelected based on Integer32"""
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


_HzIduRadio1FreqGroupSelected_Type.__name__ = "Integer32"
_HzIduRadio1FreqGroupSelected_Object = MibScalar
hzIduRadio1FreqGroupSelected = _HzIduRadio1FreqGroupSelected_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 2),
    _HzIduRadio1FreqGroupSelected_Type()
)
hzIduRadio1FreqGroupSelected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadio1FreqGroupSelected.setStatus("mandatory")
_HzIduRadio1TxHighFreqTable_Object = MibTable
hzIduRadio1TxHighFreqTable = _HzIduRadio1TxHighFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hzIduRadio1TxHighFreqTable.setStatus("mandatory")
_HzIduRadio1TxHighFreqEntry_Object = MibTableRow
hzIduRadio1TxHighFreqEntry = _HzIduRadio1TxHighFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 3, 1)
)
hzIduRadio1TxHighFreqEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadio1TxHighFreqIndex"),
)
if mibBuilder.loadTexts:
    hzIduRadio1TxHighFreqEntry.setStatus("mandatory")
_HzIduRadio1TxHighFreqIndex_Type = Integer32
_HzIduRadio1TxHighFreqIndex_Object = MibTableColumn
hzIduRadio1TxHighFreqIndex = _HzIduRadio1TxHighFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 3, 1, 1),
    _HzIduRadio1TxHighFreqIndex_Type()
)
hzIduRadio1TxHighFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1TxHighFreqIndex.setStatus("mandatory")
_HzIduRadio1TxHighFreqChannelIndex_Type = DisplayString
_HzIduRadio1TxHighFreqChannelIndex_Object = MibTableColumn
hzIduRadio1TxHighFreqChannelIndex = _HzIduRadio1TxHighFreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 3, 1, 2),
    _HzIduRadio1TxHighFreqChannelIndex_Type()
)
hzIduRadio1TxHighFreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1TxHighFreqChannelIndex.setStatus("mandatory")
_HzIduRadio1TxHighFreqTransmitRfFrequency_Type = Integer32
_HzIduRadio1TxHighFreqTransmitRfFrequency_Object = MibTableColumn
hzIduRadio1TxHighFreqTransmitRfFrequency = _HzIduRadio1TxHighFreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 3, 1, 3),
    _HzIduRadio1TxHighFreqTransmitRfFrequency_Type()
)
hzIduRadio1TxHighFreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1TxHighFreqTransmitRfFrequency.setStatus("mandatory")
_HzIduRadio1TxHighFreqReceiveRfFrequency_Type = Integer32
_HzIduRadio1TxHighFreqReceiveRfFrequency_Object = MibTableColumn
hzIduRadio1TxHighFreqReceiveRfFrequency = _HzIduRadio1TxHighFreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 3, 1, 4),
    _HzIduRadio1TxHighFreqReceiveRfFrequency_Type()
)
hzIduRadio1TxHighFreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1TxHighFreqReceiveRfFrequency.setStatus("mandatory")


class _HzIduRadio1TxHighFreqProgrammed_Type(Integer32):
    """Custom type hzIduRadio1TxHighFreqProgrammed based on Integer32"""
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


_HzIduRadio1TxHighFreqProgrammed_Type.__name__ = "Integer32"
_HzIduRadio1TxHighFreqProgrammed_Object = MibTableColumn
hzIduRadio1TxHighFreqProgrammed = _HzIduRadio1TxHighFreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 3, 1, 5),
    _HzIduRadio1TxHighFreqProgrammed_Type()
)
hzIduRadio1TxHighFreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadio1TxHighFreqProgrammed.setStatus("mandatory")
_HzIduRadio1TxLowFreqTable_Object = MibTable
hzIduRadio1TxLowFreqTable = _HzIduRadio1TxLowFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hzIduRadio1TxLowFreqTable.setStatus("mandatory")
_HzIduRadio1TxLowFreqEntry_Object = MibTableRow
hzIduRadio1TxLowFreqEntry = _HzIduRadio1TxLowFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 4, 1)
)
hzIduRadio1TxLowFreqEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadio1TxLowFreqIndex"),
)
if mibBuilder.loadTexts:
    hzIduRadio1TxLowFreqEntry.setStatus("mandatory")
_HzIduRadio1TxLowFreqIndex_Type = Integer32
_HzIduRadio1TxLowFreqIndex_Object = MibTableColumn
hzIduRadio1TxLowFreqIndex = _HzIduRadio1TxLowFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 4, 1, 1),
    _HzIduRadio1TxLowFreqIndex_Type()
)
hzIduRadio1TxLowFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1TxLowFreqIndex.setStatus("mandatory")
_HzIduRadio1TxLowFreqChannelIndex_Type = DisplayString
_HzIduRadio1TxLowFreqChannelIndex_Object = MibTableColumn
hzIduRadio1TxLowFreqChannelIndex = _HzIduRadio1TxLowFreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 4, 1, 2),
    _HzIduRadio1TxLowFreqChannelIndex_Type()
)
hzIduRadio1TxLowFreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1TxLowFreqChannelIndex.setStatus("mandatory")
_HzIduRadio1TxLowFreqTransmitRfFrequency_Type = Integer32
_HzIduRadio1TxLowFreqTransmitRfFrequency_Object = MibTableColumn
hzIduRadio1TxLowFreqTransmitRfFrequency = _HzIduRadio1TxLowFreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 4, 1, 3),
    _HzIduRadio1TxLowFreqTransmitRfFrequency_Type()
)
hzIduRadio1TxLowFreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1TxLowFreqTransmitRfFrequency.setStatus("mandatory")
_HzIduRadio1TxLowFreqReceiveRfFrequency_Type = Integer32
_HzIduRadio1TxLowFreqReceiveRfFrequency_Object = MibTableColumn
hzIduRadio1TxLowFreqReceiveRfFrequency = _HzIduRadio1TxLowFreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 4, 1, 4),
    _HzIduRadio1TxLowFreqReceiveRfFrequency_Type()
)
hzIduRadio1TxLowFreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1TxLowFreqReceiveRfFrequency.setStatus("mandatory")


class _HzIduRadio1TxLowFreqProgrammed_Type(Integer32):
    """Custom type hzIduRadio1TxLowFreqProgrammed based on Integer32"""
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


_HzIduRadio1TxLowFreqProgrammed_Type.__name__ = "Integer32"
_HzIduRadio1TxLowFreqProgrammed_Object = MibTableColumn
hzIduRadio1TxLowFreqProgrammed = _HzIduRadio1TxLowFreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 4, 1, 5),
    _HzIduRadio1TxLowFreqProgrammed_Type()
)
hzIduRadio1TxLowFreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadio1TxLowFreqProgrammed.setStatus("mandatory")
_HzIduRadio1ProgrammedFrequency_ObjectIdentity = ObjectIdentity
hzIduRadio1ProgrammedFrequency = _HzIduRadio1ProgrammedFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 5)
)
_HzIduRadio1ProgrammedFrequencyChannel_Type = DisplayString
_HzIduRadio1ProgrammedFrequencyChannel_Object = MibScalar
hzIduRadio1ProgrammedFrequencyChannel = _HzIduRadio1ProgrammedFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 5, 1),
    _HzIduRadio1ProgrammedFrequencyChannel_Type()
)
hzIduRadio1ProgrammedFrequencyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1ProgrammedFrequencyChannel.setStatus("mandatory")
_HzIduRadio1ProgrammedFrequencyTxRf_Type = Integer32
_HzIduRadio1ProgrammedFrequencyTxRf_Object = MibScalar
hzIduRadio1ProgrammedFrequencyTxRf = _HzIduRadio1ProgrammedFrequencyTxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 5, 2),
    _HzIduRadio1ProgrammedFrequencyTxRf_Type()
)
hzIduRadio1ProgrammedFrequencyTxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1ProgrammedFrequencyTxRf.setStatus("mandatory")
_HzIduRadio1ProgrammedFrequencyRxRf_Type = Integer32
_HzIduRadio1ProgrammedFrequencyRxRf_Object = MibScalar
hzIduRadio1ProgrammedFrequencyRxRf = _HzIduRadio1ProgrammedFrequencyRxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 1, 5, 3),
    _HzIduRadio1ProgrammedFrequencyRxRf_Type()
)
hzIduRadio1ProgrammedFrequencyRxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio1ProgrammedFrequencyRxRf.setStatus("mandatory")
_HzIduWirelessInterfaceRadio2Frequencies_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceRadio2Frequencies = _HzIduWirelessInterfaceRadio2Frequencies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2)
)


class _HzIduRadio2Band_Type(Integer32):
    """Custom type hzIduRadio2Band based on Integer32"""
    defaultValue = 1

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
        *(("freqNone", 1),
          ("fcc11-1-40", 2),
          ("fcc11-1-30", 3),
          ("fcc18-2-40", 4),
          ("fcc18-2-50", 5),
          ("fcc23-3-50", 6))
    )


_HzIduRadio2Band_Type.__name__ = "Integer32"
_HzIduRadio2Band_Object = MibScalar
hzIduRadio2Band = _HzIduRadio2Band_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 1),
    _HzIduRadio2Band_Type()
)
hzIduRadio2Band.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadio2Band.setStatus("mandatory")


class _HzIduRadio2FreqGroupSelected_Type(Integer32):
    """Custom type hzIduRadio2FreqGroupSelected based on Integer32"""
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


_HzIduRadio2FreqGroupSelected_Type.__name__ = "Integer32"
_HzIduRadio2FreqGroupSelected_Object = MibScalar
hzIduRadio2FreqGroupSelected = _HzIduRadio2FreqGroupSelected_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 2),
    _HzIduRadio2FreqGroupSelected_Type()
)
hzIduRadio2FreqGroupSelected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadio2FreqGroupSelected.setStatus("mandatory")
_HzIduRadio2TxHighFreqTable_Object = MibTable
hzIduRadio2TxHighFreqTable = _HzIduRadio2TxHighFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hzIduRadio2TxHighFreqTable.setStatus("mandatory")
_HzIduRadio2TxHighFreqEntry_Object = MibTableRow
hzIduRadio2TxHighFreqEntry = _HzIduRadio2TxHighFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 3, 1)
)
hzIduRadio2TxHighFreqEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadio2TxHighFreqIndex"),
)
if mibBuilder.loadTexts:
    hzIduRadio2TxHighFreqEntry.setStatus("mandatory")
_HzIduRadio2TxHighFreqIndex_Type = Integer32
_HzIduRadio2TxHighFreqIndex_Object = MibTableColumn
hzIduRadio2TxHighFreqIndex = _HzIduRadio2TxHighFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 3, 1, 1),
    _HzIduRadio2TxHighFreqIndex_Type()
)
hzIduRadio2TxHighFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2TxHighFreqIndex.setStatus("mandatory")
_HzIduRadio2TxHighFreqChannelIndex_Type = DisplayString
_HzIduRadio2TxHighFreqChannelIndex_Object = MibTableColumn
hzIduRadio2TxHighFreqChannelIndex = _HzIduRadio2TxHighFreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 3, 1, 2),
    _HzIduRadio2TxHighFreqChannelIndex_Type()
)
hzIduRadio2TxHighFreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2TxHighFreqChannelIndex.setStatus("mandatory")
_HzIduRadio2TxHighFreqTransmitRfFrequency_Type = Integer32
_HzIduRadio2TxHighFreqTransmitRfFrequency_Object = MibTableColumn
hzIduRadio2TxHighFreqTransmitRfFrequency = _HzIduRadio2TxHighFreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 3, 1, 3),
    _HzIduRadio2TxHighFreqTransmitRfFrequency_Type()
)
hzIduRadio2TxHighFreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2TxHighFreqTransmitRfFrequency.setStatus("mandatory")
_HzIduRadio2TxHighFreqReceiveRfFrequency_Type = Integer32
_HzIduRadio2TxHighFreqReceiveRfFrequency_Object = MibTableColumn
hzIduRadio2TxHighFreqReceiveRfFrequency = _HzIduRadio2TxHighFreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 3, 1, 4),
    _HzIduRadio2TxHighFreqReceiveRfFrequency_Type()
)
hzIduRadio2TxHighFreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2TxHighFreqReceiveRfFrequency.setStatus("mandatory")


class _HzIduRadio2TxHighFreqProgrammed_Type(Integer32):
    """Custom type hzIduRadio2TxHighFreqProgrammed based on Integer32"""
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


_HzIduRadio2TxHighFreqProgrammed_Type.__name__ = "Integer32"
_HzIduRadio2TxHighFreqProgrammed_Object = MibTableColumn
hzIduRadio2TxHighFreqProgrammed = _HzIduRadio2TxHighFreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 3, 1, 5),
    _HzIduRadio2TxHighFreqProgrammed_Type()
)
hzIduRadio2TxHighFreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadio2TxHighFreqProgrammed.setStatus("mandatory")
_HzIduRadio2TxLowFreqTable_Object = MibTable
hzIduRadio2TxLowFreqTable = _HzIduRadio2TxLowFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 4)
)
if mibBuilder.loadTexts:
    hzIduRadio2TxLowFreqTable.setStatus("mandatory")
_HzIduRadio2TxLowFreqEntry_Object = MibTableRow
hzIduRadio2TxLowFreqEntry = _HzIduRadio2TxLowFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 4, 1)
)
hzIduRadio2TxLowFreqEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadio2TxLowFreqIndex"),
)
if mibBuilder.loadTexts:
    hzIduRadio2TxLowFreqEntry.setStatus("mandatory")
_HzIduRadio2TxLowFreqIndex_Type = Integer32
_HzIduRadio2TxLowFreqIndex_Object = MibTableColumn
hzIduRadio2TxLowFreqIndex = _HzIduRadio2TxLowFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 4, 1, 1),
    _HzIduRadio2TxLowFreqIndex_Type()
)
hzIduRadio2TxLowFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2TxLowFreqIndex.setStatus("mandatory")
_HzIduRadio2TxLowFreqChannelIndex_Type = DisplayString
_HzIduRadio2TxLowFreqChannelIndex_Object = MibTableColumn
hzIduRadio2TxLowFreqChannelIndex = _HzIduRadio2TxLowFreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 4, 1, 2),
    _HzIduRadio2TxLowFreqChannelIndex_Type()
)
hzIduRadio2TxLowFreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2TxLowFreqChannelIndex.setStatus("mandatory")
_HzIduRadio2TxLowFreqTransmitRfFrequency_Type = Integer32
_HzIduRadio2TxLowFreqTransmitRfFrequency_Object = MibTableColumn
hzIduRadio2TxLowFreqTransmitRfFrequency = _HzIduRadio2TxLowFreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 4, 1, 3),
    _HzIduRadio2TxLowFreqTransmitRfFrequency_Type()
)
hzIduRadio2TxLowFreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2TxLowFreqTransmitRfFrequency.setStatus("mandatory")
_HzIduRadio2TxLowFreqReceiveRfFrequency_Type = Integer32
_HzIduRadio2TxLowFreqReceiveRfFrequency_Object = MibTableColumn
hzIduRadio2TxLowFreqReceiveRfFrequency = _HzIduRadio2TxLowFreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 4, 1, 4),
    _HzIduRadio2TxLowFreqReceiveRfFrequency_Type()
)
hzIduRadio2TxLowFreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2TxLowFreqReceiveRfFrequency.setStatus("mandatory")


class _HzIduRadio2TxLowFreqProgrammed_Type(Integer32):
    """Custom type hzIduRadio2TxLowFreqProgrammed based on Integer32"""
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


_HzIduRadio2TxLowFreqProgrammed_Type.__name__ = "Integer32"
_HzIduRadio2TxLowFreqProgrammed_Object = MibTableColumn
hzIduRadio2TxLowFreqProgrammed = _HzIduRadio2TxLowFreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 4, 1, 5),
    _HzIduRadio2TxLowFreqProgrammed_Type()
)
hzIduRadio2TxLowFreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadio2TxLowFreqProgrammed.setStatus("mandatory")
_HzIduRadio2ProgrammedFrequency_ObjectIdentity = ObjectIdentity
hzIduRadio2ProgrammedFrequency = _HzIduRadio2ProgrammedFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 5)
)
_HzIduRadio2ProgrammedFrequencyChannel_Type = DisplayString
_HzIduRadio2ProgrammedFrequencyChannel_Object = MibScalar
hzIduRadio2ProgrammedFrequencyChannel = _HzIduRadio2ProgrammedFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 5, 1),
    _HzIduRadio2ProgrammedFrequencyChannel_Type()
)
hzIduRadio2ProgrammedFrequencyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2ProgrammedFrequencyChannel.setStatus("mandatory")
_HzIduRadio2ProgrammedFrequencyTxRf_Type = Integer32
_HzIduRadio2ProgrammedFrequencyTxRf_Object = MibScalar
hzIduRadio2ProgrammedFrequencyTxRf = _HzIduRadio2ProgrammedFrequencyTxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 5, 2),
    _HzIduRadio2ProgrammedFrequencyTxRf_Type()
)
hzIduRadio2ProgrammedFrequencyTxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2ProgrammedFrequencyTxRf.setStatus("mandatory")
_HzIduRadio2ProgrammedFrequencyRxRf_Type = Integer32
_HzIduRadio2ProgrammedFrequencyRxRf_Object = MibScalar
hzIduRadio2ProgrammedFrequencyRxRf = _HzIduRadio2ProgrammedFrequencyRxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 5, 2, 5, 3),
    _HzIduRadio2ProgrammedFrequencyRxRf_Type()
)
hzIduRadio2ProgrammedFrequencyRxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadio2ProgrammedFrequencyRxRf.setStatus("mandatory")
_HzIduWirelessInterfaceAntenna_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceAntenna = _HzIduWirelessInterfaceAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 6)
)


class _HzIduAntennaDiameter_Type(Integer32):
    """Custom type hzIduAntennaDiameter based on Integer32"""
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
        *(("antenna12", 1),
          ("antenna24", 2),
          ("antenna36", 3),
          ("antenna48", 4),
          ("antenna72", 5))
    )


_HzIduAntennaDiameter_Type.__name__ = "Integer32"
_HzIduAntennaDiameter_Object = MibScalar
hzIduAntennaDiameter = _HzIduAntennaDiameter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 6, 1),
    _HzIduAntennaDiameter_Type()
)
hzIduAntennaDiameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAntennaDiameter.setStatus("mandatory")
_HzIduWirelessInterfaceRedundancy_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceRedundancy = _HzIduWirelessInterfaceRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 7)
)


class _HzIduWirelessInterfaceRedundancyActiveWirelessPort_Type(Integer32):
    """Custom type hzIduWirelessInterfaceRedundancyActiveWirelessPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduWirelessInterfaceRedundancyActiveWirelessPort_Type.__name__ = "Integer32"
_HzIduWirelessInterfaceRedundancyActiveWirelessPort_Object = MibScalar
hzIduWirelessInterfaceRedundancyActiveWirelessPort = _HzIduWirelessInterfaceRedundancyActiveWirelessPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 7, 1),
    _HzIduWirelessInterfaceRedundancyActiveWirelessPort_Type()
)
hzIduWirelessInterfaceRedundancyActiveWirelessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceRedundancyActiveWirelessPort.setStatus("mandatory")


class _HzIduWirelessInterfaceRedundancyPrimaryWirelessPort_Type(Integer32):
    """Custom type hzIduWirelessInterfaceRedundancyPrimaryWirelessPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduWirelessInterfaceRedundancyPrimaryWirelessPort_Type.__name__ = "Integer32"
_HzIduWirelessInterfaceRedundancyPrimaryWirelessPort_Object = MibScalar
hzIduWirelessInterfaceRedundancyPrimaryWirelessPort = _HzIduWirelessInterfaceRedundancyPrimaryWirelessPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 7, 2),
    _HzIduWirelessInterfaceRedundancyPrimaryWirelessPort_Type()
)
hzIduWirelessInterfaceRedundancyPrimaryWirelessPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceRedundancyPrimaryWirelessPort.setStatus("mandatory")


class _HzIduWirelessInterfaceRedundancySwitchingAlgorithm_Type(Integer32):
    """Custom type hzIduWirelessInterfaceRedundancySwitchingAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("algorithm-based", 2))
    )


_HzIduWirelessInterfaceRedundancySwitchingAlgorithm_Type.__name__ = "Integer32"
_HzIduWirelessInterfaceRedundancySwitchingAlgorithm_Object = MibScalar
hzIduWirelessInterfaceRedundancySwitchingAlgorithm = _HzIduWirelessInterfaceRedundancySwitchingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 7, 3),
    _HzIduWirelessInterfaceRedundancySwitchingAlgorithm_Type()
)
hzIduWirelessInterfaceRedundancySwitchingAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceRedundancySwitchingAlgorithm.setStatus("mandatory")
_HzIduWirelessInterfaceRedundancySwitchCause_Type = DisplayString
_HzIduWirelessInterfaceRedundancySwitchCause_Object = MibScalar
hzIduWirelessInterfaceRedundancySwitchCause = _HzIduWirelessInterfaceRedundancySwitchCause_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 7, 4),
    _HzIduWirelessInterfaceRedundancySwitchCause_Type()
)
hzIduWirelessInterfaceRedundancySwitchCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceRedundancySwitchCause.setStatus("mandatory")


class _HzIduWirelessInterfaceRedundancySwitchRadio_Type(Integer32):
    """Custom type hzIduWirelessInterfaceRedundancySwitchRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("switch", 1)
    )


_HzIduWirelessInterfaceRedundancySwitchRadio_Type.__name__ = "Integer32"
_HzIduWirelessInterfaceRedundancySwitchRadio_Object = MibScalar
hzIduWirelessInterfaceRedundancySwitchRadio = _HzIduWirelessInterfaceRedundancySwitchRadio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 7, 5),
    _HzIduWirelessInterfaceRedundancySwitchRadio_Type()
)
hzIduWirelessInterfaceRedundancySwitchRadio.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceRedundancySwitchRadio.setStatus("mandatory")


class _HzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort_Type(Integer32):
    """Custom type hzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort_Type.__name__ = "Integer32"
_HzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort_Object = MibScalar
hzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort = _HzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 7, 6),
    _HzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort_Type()
)
hzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort.setStatus("mandatory")
_HzIduWirelessInterfaceRedundancyDiagnostics_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceRedundancyDiagnostics = _HzIduWirelessInterfaceRedundancyDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 7, 7)
)


class _HzIduWirelessInterfaceRedundancyDiagnose_Type(Integer32):
    """Custom type hzIduWirelessInterfaceRedundancyDiagnose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("diagnose", 1)
    )


_HzIduWirelessInterfaceRedundancyDiagnose_Type.__name__ = "Integer32"
_HzIduWirelessInterfaceRedundancyDiagnose_Object = MibScalar
hzIduWirelessInterfaceRedundancyDiagnose = _HzIduWirelessInterfaceRedundancyDiagnose_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 7, 7, 1),
    _HzIduWirelessInterfaceRedundancyDiagnose_Type()
)
hzIduWirelessInterfaceRedundancyDiagnose.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceRedundancyDiagnose.setStatus("mandatory")
_HzIduWirelessInterfaceRedundancyDiagnosticResult_Type = DisplayString
_HzIduWirelessInterfaceRedundancyDiagnosticResult_Object = MibScalar
hzIduWirelessInterfaceRedundancyDiagnosticResult = _HzIduWirelessInterfaceRedundancyDiagnosticResult_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 5, 7, 7, 2),
    _HzIduWirelessInterfaceRedundancyDiagnosticResult_Type()
)
hzIduWirelessInterfaceRedundancyDiagnosticResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduWirelessInterfaceRedundancyDiagnosticResult.setStatus("mandatory")
_HzIduCalendar_ObjectIdentity = ObjectIdentity
hzIduCalendar = _HzIduCalendar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 6)
)
_HzIduDate_Type = DisplayString
_HzIduDate_Object = MibScalar
hzIduDate = _HzIduDate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 6, 1),
    _HzIduDate_Type()
)
hzIduDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduDate.setStatus("mandatory")
_HzIduTime_Type = DisplayString
_HzIduTime_Object = MibScalar
hzIduTime = _HzIduTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 6, 2),
    _HzIduTime_Type()
)
hzIduTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduTime.setStatus("mandatory")
_HzIduAlarms_ObjectIdentity = ObjectIdentity
hzIduAlarms = _HzIduAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7)
)


class _HzIduClearAlarmCounters_Type(Integer32):
    """Custom type hzIduClearAlarmCounters based on Integer32"""
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


_HzIduClearAlarmCounters_Type.__name__ = "Integer32"
_HzIduClearAlarmCounters_Object = MibScalar
hzIduClearAlarmCounters = _HzIduClearAlarmCounters_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 1),
    _HzIduClearAlarmCounters_Type()
)
hzIduClearAlarmCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hzIduClearAlarmCounters.setStatus("mandatory")
_HzIduSystemAlarms_ObjectIdentity = ObjectIdentity
hzIduSystemAlarms = _HzIduSystemAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2)
)


class _HzIduExplicitAuthenticationFailure_Type(Integer32):
    """Custom type hzIduExplicitAuthenticationFailure based on Integer32"""
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


_HzIduExplicitAuthenticationFailure_Type.__name__ = "Integer32"
_HzIduExplicitAuthenticationFailure_Object = MibScalar
hzIduExplicitAuthenticationFailure = _HzIduExplicitAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 1),
    _HzIduExplicitAuthenticationFailure_Type()
)
hzIduExplicitAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduExplicitAuthenticationFailure.setStatus("mandatory")
_HzIduExplicitAuthenticationFailureCounts_Type = Counter32
_HzIduExplicitAuthenticationFailureCounts_Object = MibScalar
hzIduExplicitAuthenticationFailureCounts = _HzIduExplicitAuthenticationFailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 2),
    _HzIduExplicitAuthenticationFailureCounts_Type()
)
hzIduExplicitAuthenticationFailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduExplicitAuthenticationFailureCounts.setStatus("mandatory")


class _HzIduAamConfigMismatch_Type(Integer32):
    """Custom type hzIduAamConfigMismatch based on Integer32"""
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


_HzIduAamConfigMismatch_Type.__name__ = "Integer32"
_HzIduAamConfigMismatch_Object = MibScalar
hzIduAamConfigMismatch = _HzIduAamConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 3),
    _HzIduAamConfigMismatch_Type()
)
hzIduAamConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAamConfigMismatch.setStatus("mandatory")
_HzIduAamConfigMismatchCounts_Type = Counter32
_HzIduAamConfigMismatchCounts_Object = MibScalar
hzIduAamConfigMismatchCounts = _HzIduAamConfigMismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 4),
    _HzIduAamConfigMismatchCounts_Type()
)
hzIduAamConfigMismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAamConfigMismatchCounts.setStatus("mandatory")


class _HzIduAamActive_Type(Integer32):
    """Custom type hzIduAamActive based on Integer32"""
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


_HzIduAamActive_Type.__name__ = "Integer32"
_HzIduAamActive_Object = MibScalar
hzIduAamActive = _HzIduAamActive_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 5),
    _HzIduAamActive_Type()
)
hzIduAamActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAamActive.setStatus("mandatory")
_HzIduAamActiveCounts_Type = Counter32
_HzIduAamActiveCounts_Object = MibScalar
hzIduAamActiveCounts = _HzIduAamActiveCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 6),
    _HzIduAamActiveCounts_Type()
)
hzIduAamActiveCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduAamActiveCounts.setStatus("mandatory")


class _HzIduSntpServerUnavailableAlarm_Type(Integer32):
    """Custom type hzIduSntpServerUnavailableAlarm based on Integer32"""
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


_HzIduSntpServerUnavailableAlarm_Type.__name__ = "Integer32"
_HzIduSntpServerUnavailableAlarm_Object = MibScalar
hzIduSntpServerUnavailableAlarm = _HzIduSntpServerUnavailableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 7),
    _HzIduSntpServerUnavailableAlarm_Type()
)
hzIduSntpServerUnavailableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSntpServerUnavailableAlarm.setStatus("mandatory")
_HzIduSntpServerUnavailableAlarmCounts_Type = Counter32
_HzIduSntpServerUnavailableAlarmCounts_Object = MibScalar
hzIduSntpServerUnavailableAlarmCounts = _HzIduSntpServerUnavailableAlarmCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 8),
    _HzIduSntpServerUnavailableAlarmCounts_Type()
)
hzIduSntpServerUnavailableAlarmCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSntpServerUnavailableAlarmCounts.setStatus("mandatory")


class _HzIduFrequencyFileInvalid_Type(Integer32):
    """Custom type hzIduFrequencyFileInvalid based on Integer32"""
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


_HzIduFrequencyFileInvalid_Type.__name__ = "Integer32"
_HzIduFrequencyFileInvalid_Object = MibScalar
hzIduFrequencyFileInvalid = _HzIduFrequencyFileInvalid_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 9),
    _HzIduFrequencyFileInvalid_Type()
)
hzIduFrequencyFileInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFrequencyFileInvalid.setStatus("mandatory")
_HzIduFrequencyFileInvalidCounts_Type = Counter32
_HzIduFrequencyFileInvalidCounts_Object = MibScalar
hzIduFrequencyFileInvalidCounts = _HzIduFrequencyFileInvalidCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 10),
    _HzIduFrequencyFileInvalidCounts_Type()
)
hzIduFrequencyFileInvalidCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFrequencyFileInvalidCounts.setStatus("mandatory")


class _HzIduFan1Failure_Type(Integer32):
    """Custom type hzIduFan1Failure based on Integer32"""
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


_HzIduFan1Failure_Type.__name__ = "Integer32"
_HzIduFan1Failure_Object = MibScalar
hzIduFan1Failure = _HzIduFan1Failure_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 11),
    _HzIduFan1Failure_Type()
)
hzIduFan1Failure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFan1Failure.setStatus("mandatory")
_HzIduFan1FailureCounts_Type = Counter32
_HzIduFan1FailureCounts_Object = MibScalar
hzIduFan1FailureCounts = _HzIduFan1FailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 12),
    _HzIduFan1FailureCounts_Type()
)
hzIduFan1FailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFan1FailureCounts.setStatus("mandatory")


class _HzIduFan2Failure_Type(Integer32):
    """Custom type hzIduFan2Failure based on Integer32"""
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


_HzIduFan2Failure_Type.__name__ = "Integer32"
_HzIduFan2Failure_Object = MibScalar
hzIduFan2Failure = _HzIduFan2Failure_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 13),
    _HzIduFan2Failure_Type()
)
hzIduFan2Failure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFan2Failure.setStatus("mandatory")
_HzIduFan2FailureCounts_Type = Counter32
_HzIduFan2FailureCounts_Object = MibScalar
hzIduFan2FailureCounts = _HzIduFan2FailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 14),
    _HzIduFan2FailureCounts_Type()
)
hzIduFan2FailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFan2FailureCounts.setStatus("mandatory")


class _HzIduFan3Failure_Type(Integer32):
    """Custom type hzIduFan3Failure based on Integer32"""
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


_HzIduFan3Failure_Type.__name__ = "Integer32"
_HzIduFan3Failure_Object = MibScalar
hzIduFan3Failure = _HzIduFan3Failure_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 15),
    _HzIduFan3Failure_Type()
)
hzIduFan3Failure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFan3Failure.setStatus("mandatory")
_HzIduFan3FailureCounts_Type = Counter32
_HzIduFan3FailureCounts_Object = MibScalar
hzIduFan3FailureCounts = _HzIduFan3FailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 16),
    _HzIduFan3FailureCounts_Type()
)
hzIduFan3FailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFan3FailureCounts.setStatus("mandatory")


class _HzIduFan4Failure_Type(Integer32):
    """Custom type hzIduFan4Failure based on Integer32"""
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


_HzIduFan4Failure_Type.__name__ = "Integer32"
_HzIduFan4Failure_Object = MibScalar
hzIduFan4Failure = _HzIduFan4Failure_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 17),
    _HzIduFan4Failure_Type()
)
hzIduFan4Failure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFan4Failure.setStatus("mandatory")
_HzIduFan4FailureCounts_Type = Counter32
_HzIduFan4FailureCounts_Object = MibScalar
hzIduFan4FailureCounts = _HzIduFan4FailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 18),
    _HzIduFan4FailureCounts_Type()
)
hzIduFan4FailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduFan4FailureCounts.setStatus("mandatory")


class _HzIduPrimaryPortNotSet_Type(Integer32):
    """Custom type hzIduPrimaryPortNotSet based on Integer32"""
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


_HzIduPrimaryPortNotSet_Type.__name__ = "Integer32"
_HzIduPrimaryPortNotSet_Object = MibScalar
hzIduPrimaryPortNotSet = _HzIduPrimaryPortNotSet_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 19),
    _HzIduPrimaryPortNotSet_Type()
)
hzIduPrimaryPortNotSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduPrimaryPortNotSet.setStatus("mandatory")
_HzIduPrimaryPortNotSetCounts_Type = Counter32
_HzIduPrimaryPortNotSetCounts_Object = MibScalar
hzIduPrimaryPortNotSetCounts = _HzIduPrimaryPortNotSetCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 20),
    _HzIduPrimaryPortNotSetCounts_Type()
)
hzIduPrimaryPortNotSetCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduPrimaryPortNotSetCounts.setStatus("mandatory")


class _HzIduSecondaryPortActive_Type(Integer32):
    """Custom type hzIduSecondaryPortActive based on Integer32"""
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


_HzIduSecondaryPortActive_Type.__name__ = "Integer32"
_HzIduSecondaryPortActive_Object = MibScalar
hzIduSecondaryPortActive = _HzIduSecondaryPortActive_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 21),
    _HzIduSecondaryPortActive_Type()
)
hzIduSecondaryPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSecondaryPortActive.setStatus("mandatory")
_HzIduSecondaryPortActiveCounts_Type = Counter32
_HzIduSecondaryPortActiveCounts_Object = MibScalar
hzIduSecondaryPortActiveCounts = _HzIduSecondaryPortActiveCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 22),
    _HzIduSecondaryPortActiveCounts_Type()
)
hzIduSecondaryPortActiveCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSecondaryPortActiveCounts.setStatus("mandatory")


class _HzIduPrimaryPortFaulty_Type(Integer32):
    """Custom type hzIduPrimaryPortFaulty based on Integer32"""
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


_HzIduPrimaryPortFaulty_Type.__name__ = "Integer32"
_HzIduPrimaryPortFaulty_Object = MibScalar
hzIduPrimaryPortFaulty = _HzIduPrimaryPortFaulty_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 23),
    _HzIduPrimaryPortFaulty_Type()
)
hzIduPrimaryPortFaulty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduPrimaryPortFaulty.setStatus("mandatory")
_HzIduPrimaryPortFaultyCounts_Type = Counter32
_HzIduPrimaryPortFaultyCounts_Object = MibScalar
hzIduPrimaryPortFaultyCounts = _HzIduPrimaryPortFaultyCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 24),
    _HzIduPrimaryPortFaultyCounts_Type()
)
hzIduPrimaryPortFaultyCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduPrimaryPortFaultyCounts.setStatus("mandatory")


class _HzIduSecondaryPortFaulty_Type(Integer32):
    """Custom type hzIduSecondaryPortFaulty based on Integer32"""
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


_HzIduSecondaryPortFaulty_Type.__name__ = "Integer32"
_HzIduSecondaryPortFaulty_Object = MibScalar
hzIduSecondaryPortFaulty = _HzIduSecondaryPortFaulty_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 25),
    _HzIduSecondaryPortFaulty_Type()
)
hzIduSecondaryPortFaulty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSecondaryPortFaulty.setStatus("mandatory")
_HzIduSecondaryPortFaultyCounts_Type = Counter32
_HzIduSecondaryPortFaultyCounts_Object = MibScalar
hzIduSecondaryPortFaultyCounts = _HzIduSecondaryPortFaultyCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 2, 26),
    _HzIduSecondaryPortFaultyCounts_Type()
)
hzIduSecondaryPortFaultyCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSecondaryPortFaultyCounts.setStatus("mandatory")
_HzIduNetworkInterfaceAlarms_ObjectIdentity = ObjectIdentity
hzIduNetworkInterfaceAlarms = _HzIduNetworkInterfaceAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3)
)
_HzIduEnetPort1Alarms_ObjectIdentity = ObjectIdentity
hzIduEnetPort1Alarms = _HzIduEnetPort1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1)
)


class _HzIduEnetPort1DroppedEnetFramesThresholdExceeded_Type(Integer32):
    """Custom type hzIduEnetPort1DroppedEnetFramesThresholdExceeded based on Integer32"""
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


_HzIduEnetPort1DroppedEnetFramesThresholdExceeded_Type.__name__ = "Integer32"
_HzIduEnetPort1DroppedEnetFramesThresholdExceeded_Object = MibScalar
hzIduEnetPort1DroppedEnetFramesThresholdExceeded = _HzIduEnetPort1DroppedEnetFramesThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1, 1),
    _HzIduEnetPort1DroppedEnetFramesThresholdExceeded_Type()
)
hzIduEnetPort1DroppedEnetFramesThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1DroppedEnetFramesThresholdExceeded.setStatus("mandatory")
_HzIduEnetPort1DroppedEnetFramesThresholdCounts_Type = Counter32
_HzIduEnetPort1DroppedEnetFramesThresholdCounts_Object = MibScalar
hzIduEnetPort1DroppedEnetFramesThresholdCounts = _HzIduEnetPort1DroppedEnetFramesThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1, 2),
    _HzIduEnetPort1DroppedEnetFramesThresholdCounts_Type()
)
hzIduEnetPort1DroppedEnetFramesThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1DroppedEnetFramesThresholdCounts.setStatus("mandatory")


class _HzIduEnetPort1BandwidthUtilizationThresholdExceeded_Type(Integer32):
    """Custom type hzIduEnetPort1BandwidthUtilizationThresholdExceeded based on Integer32"""
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


_HzIduEnetPort1BandwidthUtilizationThresholdExceeded_Type.__name__ = "Integer32"
_HzIduEnetPort1BandwidthUtilizationThresholdExceeded_Object = MibScalar
hzIduEnetPort1BandwidthUtilizationThresholdExceeded = _HzIduEnetPort1BandwidthUtilizationThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1, 3),
    _HzIduEnetPort1BandwidthUtilizationThresholdExceeded_Type()
)
hzIduEnetPort1BandwidthUtilizationThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1BandwidthUtilizationThresholdExceeded.setStatus("mandatory")
_HzIduEnetPort1BandwidthUtilizationThresholdCounts_Type = Counter32
_HzIduEnetPort1BandwidthUtilizationThresholdCounts_Object = MibScalar
hzIduEnetPort1BandwidthUtilizationThresholdCounts = _HzIduEnetPort1BandwidthUtilizationThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1, 4),
    _HzIduEnetPort1BandwidthUtilizationThresholdCounts_Type()
)
hzIduEnetPort1BandwidthUtilizationThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1BandwidthUtilizationThresholdCounts.setStatus("mandatory")


class _HzIduEnetPort1RlsMismatch_Type(Integer32):
    """Custom type hzIduEnetPort1RlsMismatch based on Integer32"""
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


_HzIduEnetPort1RlsMismatch_Type.__name__ = "Integer32"
_HzIduEnetPort1RlsMismatch_Object = MibScalar
hzIduEnetPort1RlsMismatch = _HzIduEnetPort1RlsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1, 5),
    _HzIduEnetPort1RlsMismatch_Type()
)
hzIduEnetPort1RlsMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1RlsMismatch.setStatus("mandatory")
_HzIduEnetPort1RlsMismatchCounts_Type = Counter32
_HzIduEnetPort1RlsMismatchCounts_Object = MibScalar
hzIduEnetPort1RlsMismatchCounts = _HzIduEnetPort1RlsMismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1, 6),
    _HzIduEnetPort1RlsMismatchCounts_Type()
)
hzIduEnetPort1RlsMismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1RlsMismatchCounts.setStatus("mandatory")


class _HzIduRLSQueueBasedShutdownActivated_Type(Integer32):
    """Custom type hzIduRLSQueueBasedShutdownActivated based on Integer32"""
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


_HzIduRLSQueueBasedShutdownActivated_Type.__name__ = "Integer32"
_HzIduRLSQueueBasedShutdownActivated_Object = MibScalar
hzIduRLSQueueBasedShutdownActivated = _HzIduRLSQueueBasedShutdownActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1, 7),
    _HzIduRLSQueueBasedShutdownActivated_Type()
)
hzIduRLSQueueBasedShutdownActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRLSQueueBasedShutdownActivated.setStatus("mandatory")
_HzIduRLSQueueBasedShutdownActivatedCounts_Type = Counter32
_HzIduRLSQueueBasedShutdownActivatedCounts_Object = MibScalar
hzIduRLSQueueBasedShutdownActivatedCounts = _HzIduRLSQueueBasedShutdownActivatedCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1, 8),
    _HzIduRLSQueueBasedShutdownActivatedCounts_Type()
)
hzIduRLSQueueBasedShutdownActivatedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRLSQueueBasedShutdownActivatedCounts.setStatus("mandatory")


class _HzIduEnetPort1EthernetLinkDown_Type(Integer32):
    """Custom type hzIduEnetPort1EthernetLinkDown based on Integer32"""
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


_HzIduEnetPort1EthernetLinkDown_Type.__name__ = "Integer32"
_HzIduEnetPort1EthernetLinkDown_Object = MibScalar
hzIduEnetPort1EthernetLinkDown = _HzIduEnetPort1EthernetLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1, 9),
    _HzIduEnetPort1EthernetLinkDown_Type()
)
hzIduEnetPort1EthernetLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1EthernetLinkDown.setStatus("mandatory")
_HzIduEnetPort1EthernetLinkDownActivatedCounts_Type = Counter32
_HzIduEnetPort1EthernetLinkDownActivatedCounts_Object = MibScalar
hzIduEnetPort1EthernetLinkDownActivatedCounts = _HzIduEnetPort1EthernetLinkDownActivatedCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 1, 10),
    _HzIduEnetPort1EthernetLinkDownActivatedCounts_Type()
)
hzIduEnetPort1EthernetLinkDownActivatedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort1EthernetLinkDownActivatedCounts.setStatus("mandatory")
_HzIduEnetPort2Alarms_ObjectIdentity = ObjectIdentity
hzIduEnetPort2Alarms = _HzIduEnetPort2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 2)
)


class _HzIduEnetPort2EthernetLinkDown_Type(Integer32):
    """Custom type hzIduEnetPort2EthernetLinkDown based on Integer32"""
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


_HzIduEnetPort2EthernetLinkDown_Type.__name__ = "Integer32"
_HzIduEnetPort2EthernetLinkDown_Object = MibScalar
hzIduEnetPort2EthernetLinkDown = _HzIduEnetPort2EthernetLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 2, 1),
    _HzIduEnetPort2EthernetLinkDown_Type()
)
hzIduEnetPort2EthernetLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2EthernetLinkDown.setStatus("mandatory")
_HzIduEnetPort2EthernetLinkDownActivatedCounts_Type = Counter32
_HzIduEnetPort2EthernetLinkDownActivatedCounts_Object = MibScalar
hzIduEnetPort2EthernetLinkDownActivatedCounts = _HzIduEnetPort2EthernetLinkDownActivatedCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 3, 2, 2),
    _HzIduEnetPort2EthernetLinkDownActivatedCounts_Type()
)
hzIduEnetPort2EthernetLinkDownActivatedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduEnetPort2EthernetLinkDownActivatedCounts.setStatus("mandatory")
_HzIduWirelessInterfaceAlarms_ObjectIdentity = ObjectIdentity
hzIduWirelessInterfaceAlarms = _HzIduWirelessInterfaceAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4)
)
_HzIduModemAlarms_ObjectIdentity = ObjectIdentity
hzIduModemAlarms = _HzIduModemAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1)
)
_HzIduModemAlarmsTable_Object = MibTable
hzIduModemAlarmsTable = _HzIduModemAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hzIduModemAlarmsTable.setStatus("mandatory")
_HzIduModemAlarmsEntry_Object = MibTableRow
hzIduModemAlarmsEntry = _HzIduModemAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1)
)
hzIduModemAlarmsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex"),
)
if mibBuilder.loadTexts:
    hzIduModemAlarmsEntry.setStatus("mandatory")


class _HzIduModemAlarmsIndex_Type(Integer32):
    """Custom type hzIduModemAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduModemAlarmsIndex_Type.__name__ = "Integer32"
_HzIduModemAlarmsIndex_Object = MibTableColumn
hzIduModemAlarmsIndex = _HzIduModemAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 1),
    _HzIduModemAlarmsIndex_Type()
)
hzIduModemAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemAlarmsIndex.setStatus("mandatory")


class _HzIduModemRxLossOfSignal_Type(Integer32):
    """Custom type hzIduModemRxLossOfSignal based on Integer32"""
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


_HzIduModemRxLossOfSignal_Type.__name__ = "Integer32"
_HzIduModemRxLossOfSignal_Object = MibTableColumn
hzIduModemRxLossOfSignal = _HzIduModemRxLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 2),
    _HzIduModemRxLossOfSignal_Type()
)
hzIduModemRxLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemRxLossOfSignal.setStatus("mandatory")
_HzIduModemRxLossOfSignalCounts_Type = Counter32
_HzIduModemRxLossOfSignalCounts_Object = MibTableColumn
hzIduModemRxLossOfSignalCounts = _HzIduModemRxLossOfSignalCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 3),
    _HzIduModemRxLossOfSignalCounts_Type()
)
hzIduModemRxLossOfSignalCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemRxLossOfSignalCounts.setStatus("mandatory")


class _HzIduModemTxLossOfSync_Type(Integer32):
    """Custom type hzIduModemTxLossOfSync based on Integer32"""
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


_HzIduModemTxLossOfSync_Type.__name__ = "Integer32"
_HzIduModemTxLossOfSync_Object = MibTableColumn
hzIduModemTxLossOfSync = _HzIduModemTxLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 4),
    _HzIduModemTxLossOfSync_Type()
)
hzIduModemTxLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemTxLossOfSync.setStatus("mandatory")
_HzIduModemTxLossOfSyncCounts_Type = Counter32
_HzIduModemTxLossOfSyncCounts_Object = MibTableColumn
hzIduModemTxLossOfSyncCounts = _HzIduModemTxLossOfSyncCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 5),
    _HzIduModemTxLossOfSyncCounts_Type()
)
hzIduModemTxLossOfSyncCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemTxLossOfSyncCounts.setStatus("mandatory")


class _HzIduModemSnrBelowThreshold_Type(Integer32):
    """Custom type hzIduModemSnrBelowThreshold based on Integer32"""
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


_HzIduModemSnrBelowThreshold_Type.__name__ = "Integer32"
_HzIduModemSnrBelowThreshold_Object = MibTableColumn
hzIduModemSnrBelowThreshold = _HzIduModemSnrBelowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 6),
    _HzIduModemSnrBelowThreshold_Type()
)
hzIduModemSnrBelowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemSnrBelowThreshold.setStatus("mandatory")
_HzIduModemSnrBelowThresholdCounts_Type = Counter32
_HzIduModemSnrBelowThresholdCounts_Object = MibTableColumn
hzIduModemSnrBelowThresholdCounts = _HzIduModemSnrBelowThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 7),
    _HzIduModemSnrBelowThresholdCounts_Type()
)
hzIduModemSnrBelowThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemSnrBelowThresholdCounts.setStatus("mandatory")


class _HzIduModemEqualizerStressExceedThreshold_Type(Integer32):
    """Custom type hzIduModemEqualizerStressExceedThreshold based on Integer32"""
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


_HzIduModemEqualizerStressExceedThreshold_Type.__name__ = "Integer32"
_HzIduModemEqualizerStressExceedThreshold_Object = MibTableColumn
hzIduModemEqualizerStressExceedThreshold = _HzIduModemEqualizerStressExceedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 8),
    _HzIduModemEqualizerStressExceedThreshold_Type()
)
hzIduModemEqualizerStressExceedThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemEqualizerStressExceedThreshold.setStatus("mandatory")
_HzIduModemEquilizerStressExceedThresholdCounts_Type = Counter32
_HzIduModemEquilizerStressExceedThresholdCounts_Object = MibTableColumn
hzIduModemEquilizerStressExceedThresholdCounts = _HzIduModemEquilizerStressExceedThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 9),
    _HzIduModemEquilizerStressExceedThresholdCounts_Type()
)
hzIduModemEquilizerStressExceedThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemEquilizerStressExceedThresholdCounts.setStatus("mandatory")


class _HzIduModemHardwareFault_Type(Integer32):
    """Custom type hzIduModemHardwareFault based on Integer32"""
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


_HzIduModemHardwareFault_Type.__name__ = "Integer32"
_HzIduModemHardwareFault_Object = MibTableColumn
hzIduModemHardwareFault = _HzIduModemHardwareFault_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 10),
    _HzIduModemHardwareFault_Type()
)
hzIduModemHardwareFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemHardwareFault.setStatus("mandatory")
_HzIduModemHardwareFaultCounts_Type = Counter32
_HzIduModemHardwareFaultCounts_Object = MibTableColumn
hzIduModemHardwareFaultCounts = _HzIduModemHardwareFaultCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 11),
    _HzIduModemHardwareFaultCounts_Type()
)
hzIduModemHardwareFaultCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemHardwareFaultCounts.setStatus("mandatory")


class _HzIduModemProgrammingError_Type(Integer32):
    """Custom type hzIduModemProgrammingError based on Integer32"""
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


_HzIduModemProgrammingError_Type.__name__ = "Integer32"
_HzIduModemProgrammingError_Object = MibTableColumn
hzIduModemProgrammingError = _HzIduModemProgrammingError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 12),
    _HzIduModemProgrammingError_Type()
)
hzIduModemProgrammingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemProgrammingError.setStatus("mandatory")
_HzIduModemProgrammingErrorCounts_Type = Counter32
_HzIduModemProgrammingErrorCounts_Object = MibTableColumn
hzIduModemProgrammingErrorCounts = _HzIduModemProgrammingErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 13),
    _HzIduModemProgrammingErrorCounts_Type()
)
hzIduModemProgrammingErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduModemProgrammingErrorCounts.setStatus("mandatory")


class _HzIduRLSShutdownActivated_Type(Integer32):
    """Custom type hzIduRLSShutdownActivated based on Integer32"""
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


_HzIduRLSShutdownActivated_Type.__name__ = "Integer32"
_HzIduRLSShutdownActivated_Object = MibTableColumn
hzIduRLSShutdownActivated = _HzIduRLSShutdownActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 14),
    _HzIduRLSShutdownActivated_Type()
)
hzIduRLSShutdownActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRLSShutdownActivated.setStatus("mandatory")
_HzIduRLSShutdownActivatedCounts_Type = Counter32
_HzIduRLSShutdownActivatedCounts_Object = MibTableColumn
hzIduRLSShutdownActivatedCounts = _HzIduRLSShutdownActivatedCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 1, 1, 1, 15),
    _HzIduRLSShutdownActivatedCounts_Type()
)
hzIduRLSShutdownActivatedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRLSShutdownActivatedCounts.setStatus("mandatory")
_HzIduRadioAlarms_ObjectIdentity = ObjectIdentity
hzIduRadioAlarms = _HzIduRadioAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2)
)
_HzIduRadioAlarmsTable_Object = MibTable
hzIduRadioAlarmsTable = _HzIduRadioAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hzIduRadioAlarmsTable.setStatus("mandatory")
_HzIduRadioAlarmsEntry_Object = MibTableRow
hzIduRadioAlarmsEntry = _HzIduRadioAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1)
)
hzIduRadioAlarmsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex"),
)
if mibBuilder.loadTexts:
    hzIduRadioAlarmsEntry.setStatus("mandatory")


class _HzIduRadioAlarmsIndex_Type(Integer32):
    """Custom type hzIduRadioAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduRadioAlarmsIndex_Type.__name__ = "Integer32"
_HzIduRadioAlarmsIndex_Object = MibTableColumn
hzIduRadioAlarmsIndex = _HzIduRadioAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 1),
    _HzIduRadioAlarmsIndex_Type()
)
hzIduRadioAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioAlarmsIndex.setStatus("mandatory")


class _HzIduRadioPLDROLostLock_Type(Integer32):
    """Custom type hzIduRadioPLDROLostLock based on Integer32"""
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


_HzIduRadioPLDROLostLock_Type.__name__ = "Integer32"
_HzIduRadioPLDROLostLock_Object = MibTableColumn
hzIduRadioPLDROLostLock = _HzIduRadioPLDROLostLock_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 2),
    _HzIduRadioPLDROLostLock_Type()
)
hzIduRadioPLDROLostLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioPLDROLostLock.setStatus("mandatory")
_HzIduRadioPLDROLostLockCounts_Type = Counter32
_HzIduRadioPLDROLostLockCounts_Object = MibTableColumn
hzIduRadioPLDROLostLockCounts = _HzIduRadioPLDROLostLockCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 3),
    _HzIduRadioPLDROLostLockCounts_Type()
)
hzIduRadioPLDROLostLockCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioPLDROLostLockCounts.setStatus("mandatory")


class _HzIduRadioLostCommunication_Type(Integer32):
    """Custom type hzIduRadioLostCommunication based on Integer32"""
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


_HzIduRadioLostCommunication_Type.__name__ = "Integer32"
_HzIduRadioLostCommunication_Object = MibTableColumn
hzIduRadioLostCommunication = _HzIduRadioLostCommunication_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 4),
    _HzIduRadioLostCommunication_Type()
)
hzIduRadioLostCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioLostCommunication.setStatus("mandatory")
_HzIduRadioLostCommunicationCounts_Type = Counter32
_HzIduRadioLostCommunicationCounts_Object = MibTableColumn
hzIduRadioLostCommunicationCounts = _HzIduRadioLostCommunicationCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 5),
    _HzIduRadioLostCommunicationCounts_Type()
)
hzIduRadioLostCommunicationCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioLostCommunicationCounts.setStatus("mandatory")


class _HzIduRadioMismatch_Type(Integer32):
    """Custom type hzIduRadioMismatch based on Integer32"""
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


_HzIduRadioMismatch_Type.__name__ = "Integer32"
_HzIduRadioMismatch_Object = MibTableColumn
hzIduRadioMismatch = _HzIduRadioMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 6),
    _HzIduRadioMismatch_Type()
)
hzIduRadioMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioMismatch.setStatus("mandatory")
_HzIduRadioMismatchCounts_Type = Counter32
_HzIduRadioMismatchCounts_Object = MibTableColumn
hzIduRadioMismatchCounts = _HzIduRadioMismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 7),
    _HzIduRadioMismatchCounts_Type()
)
hzIduRadioMismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioMismatchCounts.setStatus("mandatory")


class _HzIduRadioPowerAmp_Type(Integer32):
    """Custom type hzIduRadioPowerAmp based on Integer32"""
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


_HzIduRadioPowerAmp_Type.__name__ = "Integer32"
_HzIduRadioPowerAmp_Object = MibTableColumn
hzIduRadioPowerAmp = _HzIduRadioPowerAmp_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 8),
    _HzIduRadioPowerAmp_Type()
)
hzIduRadioPowerAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioPowerAmp.setStatus("mandatory")
_HzIduRadioPowerAmpCounts_Type = Counter32
_HzIduRadioPowerAmpCounts_Object = MibTableColumn
hzIduRadioPowerAmpCounts = _HzIduRadioPowerAmpCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 9),
    _HzIduRadioPowerAmpCounts_Type()
)
hzIduRadioPowerAmpCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioPowerAmpCounts.setStatus("mandatory")


class _HzIduRadioExcessiveTxCableLoss_Type(Integer32):
    """Custom type hzIduRadioExcessiveTxCableLoss based on Integer32"""
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


_HzIduRadioExcessiveTxCableLoss_Type.__name__ = "Integer32"
_HzIduRadioExcessiveTxCableLoss_Object = MibTableColumn
hzIduRadioExcessiveTxCableLoss = _HzIduRadioExcessiveTxCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 10),
    _HzIduRadioExcessiveTxCableLoss_Type()
)
hzIduRadioExcessiveTxCableLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioExcessiveTxCableLoss.setStatus("mandatory")
_HzIduRadioExcessiveTxCableLossCounts_Type = Counter32
_HzIduRadioExcessiveTxCableLossCounts_Object = MibTableColumn
hzIduRadioExcessiveTxCableLossCounts = _HzIduRadioExcessiveTxCableLossCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 11),
    _HzIduRadioExcessiveTxCableLossCounts_Type()
)
hzIduRadioExcessiveTxCableLossCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioExcessiveTxCableLossCounts.setStatus("mandatory")


class _HzIduRadioRslBelowThreshold_Type(Integer32):
    """Custom type hzIduRadioRslBelowThreshold based on Integer32"""
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


_HzIduRadioRslBelowThreshold_Type.__name__ = "Integer32"
_HzIduRadioRslBelowThreshold_Object = MibTableColumn
hzIduRadioRslBelowThreshold = _HzIduRadioRslBelowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 12),
    _HzIduRadioRslBelowThreshold_Type()
)
hzIduRadioRslBelowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioRslBelowThreshold.setStatus("mandatory")
_HzIduRadioRslBelowThresholdCounts_Type = Counter32
_HzIduRadioRslBelowThresholdCounts_Object = MibTableColumn
hzIduRadioRslBelowThresholdCounts = _HzIduRadioRslBelowThresholdCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 13),
    _HzIduRadioRslBelowThresholdCounts_Type()
)
hzIduRadioRslBelowThresholdCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioRslBelowThresholdCounts.setStatus("mandatory")


class _HzIduRadioHighPowerOptionM1_Type(Integer32):
    """Custom type hzIduRadioHighPowerOptionM1 based on Integer32"""
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


_HzIduRadioHighPowerOptionM1_Type.__name__ = "Integer32"
_HzIduRadioHighPowerOptionM1_Object = MibTableColumn
hzIduRadioHighPowerOptionM1 = _HzIduRadioHighPowerOptionM1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 14),
    _HzIduRadioHighPowerOptionM1_Type()
)
hzIduRadioHighPowerOptionM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioHighPowerOptionM1.setStatus("mandatory")
_HzIduRadioHighPowerOptionM1Counts_Type = Counter32
_HzIduRadioHighPowerOptionM1Counts_Object = MibTableColumn
hzIduRadioHighPowerOptionM1Counts = _HzIduRadioHighPowerOptionM1Counts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 15),
    _HzIduRadioHighPowerOptionM1Counts_Type()
)
hzIduRadioHighPowerOptionM1Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioHighPowerOptionM1Counts.setStatus("mandatory")


class _HzIduRadioHighPowerOptionM2_Type(Integer32):
    """Custom type hzIduRadioHighPowerOptionM2 based on Integer32"""
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


_HzIduRadioHighPowerOptionM2_Type.__name__ = "Integer32"
_HzIduRadioHighPowerOptionM2_Object = MibTableColumn
hzIduRadioHighPowerOptionM2 = _HzIduRadioHighPowerOptionM2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 16),
    _HzIduRadioHighPowerOptionM2_Type()
)
hzIduRadioHighPowerOptionM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioHighPowerOptionM2.setStatus("mandatory")
_HzIduRadioHighPowerOptionM2Counts_Type = Counter32
_HzIduRadioHighPowerOptionM2Counts_Object = MibTableColumn
hzIduRadioHighPowerOptionM2Counts = _HzIduRadioHighPowerOptionM2Counts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 17),
    _HzIduRadioHighPowerOptionM2Counts_Type()
)
hzIduRadioHighPowerOptionM2Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioHighPowerOptionM2Counts.setStatus("mandatory")


class _HzIduRadioHighPowerTxDetector_Type(Integer32):
    """Custom type hzIduRadioHighPowerTxDetector based on Integer32"""
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


_HzIduRadioHighPowerTxDetector_Type.__name__ = "Integer32"
_HzIduRadioHighPowerTxDetector_Object = MibTableColumn
hzIduRadioHighPowerTxDetector = _HzIduRadioHighPowerTxDetector_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 18),
    _HzIduRadioHighPowerTxDetector_Type()
)
hzIduRadioHighPowerTxDetector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioHighPowerTxDetector.setStatus("mandatory")
_HzIduRadioHighPowerTxDetectorCounts_Type = Counter32
_HzIduRadioHighPowerTxDetectorCounts_Object = MibTableColumn
hzIduRadioHighPowerTxDetectorCounts = _HzIduRadioHighPowerTxDetectorCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 19),
    _HzIduRadioHighPowerTxDetectorCounts_Type()
)
hzIduRadioHighPowerTxDetectorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioHighPowerTxDetectorCounts.setStatus("mandatory")


class _HzIduRadioAtpcConfigMismatch_Type(Integer32):
    """Custom type hzIduRadioAtpcConfigMismatch based on Integer32"""
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


_HzIduRadioAtpcConfigMismatch_Type.__name__ = "Integer32"
_HzIduRadioAtpcConfigMismatch_Object = MibTableColumn
hzIduRadioAtpcConfigMismatch = _HzIduRadioAtpcConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 20),
    _HzIduRadioAtpcConfigMismatch_Type()
)
hzIduRadioAtpcConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioAtpcConfigMismatch.setStatus("mandatory")
_HzIduRadioAtpcConfigMismatchCounts_Type = Counter32
_HzIduRadioAtpcConfigMismatchCounts_Object = MibTableColumn
hzIduRadioAtpcConfigMismatchCounts = _HzIduRadioAtpcConfigMismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 21),
    _HzIduRadioAtpcConfigMismatchCounts_Type()
)
hzIduRadioAtpcConfigMismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioAtpcConfigMismatchCounts.setStatus("mandatory")


class _HzIduRadioRedundancySerialNumMismatch_Type(Integer32):
    """Custom type hzIduRadioRedundancySerialNumMismatch based on Integer32"""
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


_HzIduRadioRedundancySerialNumMismatch_Type.__name__ = "Integer32"
_HzIduRadioRedundancySerialNumMismatch_Object = MibTableColumn
hzIduRadioRedundancySerialNumMismatch = _HzIduRadioRedundancySerialNumMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 22),
    _HzIduRadioRedundancySerialNumMismatch_Type()
)
hzIduRadioRedundancySerialNumMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioRedundancySerialNumMismatch.setStatus("mandatory")
_HzIduRadioRedundancySerialNumMismatchCounts_Type = Counter32
_HzIduRadioRedundancySerialNumMismatchCounts_Object = MibTableColumn
hzIduRadioRedundancySerialNumMismatchCounts = _HzIduRadioRedundancySerialNumMismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 23),
    _HzIduRadioRedundancySerialNumMismatchCounts_Type()
)
hzIduRadioRedundancySerialNumMismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioRedundancySerialNumMismatchCounts.setStatus("mandatory")


class _HzIduRadioExcessiveTxCableLossChange_Type(Integer32):
    """Custom type hzIduRadioExcessiveTxCableLossChange based on Integer32"""
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


_HzIduRadioExcessiveTxCableLossChange_Type.__name__ = "Integer32"
_HzIduRadioExcessiveTxCableLossChange_Object = MibTableColumn
hzIduRadioExcessiveTxCableLossChange = _HzIduRadioExcessiveTxCableLossChange_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 24),
    _HzIduRadioExcessiveTxCableLossChange_Type()
)
hzIduRadioExcessiveTxCableLossChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioExcessiveTxCableLossChange.setStatus("mandatory")
_HzIduRadioExcessiveTxCableLossChangeCounts_Type = Counter32
_HzIduRadioExcessiveTxCableLossChangeCounts_Object = MibTableColumn
hzIduRadioExcessiveTxCableLossChangeCounts = _HzIduRadioExcessiveTxCableLossChangeCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 25),
    _HzIduRadioExcessiveTxCableLossChangeCounts_Type()
)
hzIduRadioExcessiveTxCableLossChangeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioExcessiveTxCableLossChangeCounts.setStatus("mandatory")


class _HzIduRadioExcessiveRxCableLoss_Type(Integer32):
    """Custom type hzIduRadioExcessiveRxCableLoss based on Integer32"""
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


_HzIduRadioExcessiveRxCableLoss_Type.__name__ = "Integer32"
_HzIduRadioExcessiveRxCableLoss_Object = MibTableColumn
hzIduRadioExcessiveRxCableLoss = _HzIduRadioExcessiveRxCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 26),
    _HzIduRadioExcessiveRxCableLoss_Type()
)
hzIduRadioExcessiveRxCableLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioExcessiveRxCableLoss.setStatus("mandatory")
_HzIduRadioExcessiveRxCableLossCounts_Type = Counter32
_HzIduRadioExcessiveRxCableLossCounts_Object = MibTableColumn
hzIduRadioExcessiveRxCableLossCounts = _HzIduRadioExcessiveRxCableLossCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 27),
    _HzIduRadioExcessiveRxCableLossCounts_Type()
)
hzIduRadioExcessiveRxCableLossCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioExcessiveRxCableLossCounts.setStatus("mandatory")


class _HzIduRadioAtpcTxAtMaxPower_Type(Integer32):
    """Custom type hzIduRadioAtpcTxAtMaxPower based on Integer32"""
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


_HzIduRadioAtpcTxAtMaxPower_Type.__name__ = "Integer32"
_HzIduRadioAtpcTxAtMaxPower_Object = MibTableColumn
hzIduRadioAtpcTxAtMaxPower = _HzIduRadioAtpcTxAtMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 28),
    _HzIduRadioAtpcTxAtMaxPower_Type()
)
hzIduRadioAtpcTxAtMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioAtpcTxAtMaxPower.setStatus("mandatory")
_HzIduRadioAtpcTxAtMaxPowerCounts_Type = Counter32
_HzIduRadioAtpcTxAtMaxPowerCounts_Object = MibTableColumn
hzIduRadioAtpcTxAtMaxPowerCounts = _HzIduRadioAtpcTxAtMaxPowerCounts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 7, 4, 2, 1, 1, 29),
    _HzIduRadioAtpcTxAtMaxPowerCounts_Type()
)
hzIduRadioAtpcTxAtMaxPowerCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioAtpcTxAtMaxPowerCounts.setStatus("mandatory")
_HzIduTrapConfig_ObjectIdentity = ObjectIdentity
hzIduTrapConfig = _HzIduTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8)
)
_HzIduSnmpTrapHostTable_Object = MibTable
hzIduSnmpTrapHostTable = _HzIduSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 1)
)
if mibBuilder.loadTexts:
    hzIduSnmpTrapHostTable.setStatus("mandatory")
_HzIduSnmpTrapHostEntry_Object = MibTableRow
hzIduSnmpTrapHostEntry = _HzIduSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 1, 1)
)
hzIduSnmpTrapHostEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduSnmpTrapHostIndex"),
)
if mibBuilder.loadTexts:
    hzIduSnmpTrapHostEntry.setStatus("mandatory")
_HzIduSnmpTrapHostIndex_Type = Integer32
_HzIduSnmpTrapHostIndex_Object = MibTableColumn
hzIduSnmpTrapHostIndex = _HzIduSnmpTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 1, 1, 1),
    _HzIduSnmpTrapHostIndex_Type()
)
hzIduSnmpTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpTrapHostIndex.setStatus("mandatory")


class _HzIduSnmpTrapHostMode_Type(Integer32):
    """Custom type hzIduSnmpTrapHostMode based on Integer32"""
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


_HzIduSnmpTrapHostMode_Type.__name__ = "Integer32"
_HzIduSnmpTrapHostMode_Object = MibTableColumn
hzIduSnmpTrapHostMode = _HzIduSnmpTrapHostMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 1, 1, 2),
    _HzIduSnmpTrapHostMode_Type()
)
hzIduSnmpTrapHostMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpTrapHostMode.setStatus("mandatory")
_HzIduSnmpTrapHostIpAddress_Type = IpAddress
_HzIduSnmpTrapHostIpAddress_Object = MibTableColumn
hzIduSnmpTrapHostIpAddress = _HzIduSnmpTrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 1, 1, 3),
    _HzIduSnmpTrapHostIpAddress_Type()
)
hzIduSnmpTrapHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpTrapHostIpAddress.setStatus("mandatory")


class _HzIduSnmpTrapHostCommunityName_Type(DisplayString):
    """Custom type hzIduSnmpTrapHostCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduSnmpTrapHostCommunityName_Type.__name__ = "DisplayString"
_HzIduSnmpTrapHostCommunityName_Object = MibTableColumn
hzIduSnmpTrapHostCommunityName = _HzIduSnmpTrapHostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 1, 1, 4),
    _HzIduSnmpTrapHostCommunityName_Type()
)
hzIduSnmpTrapHostCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpTrapHostCommunityName.setStatus("mandatory")


class _HzIduSnmpTrapHostActivated_Type(Integer32):
    """Custom type hzIduSnmpTrapHostActivated based on Integer32"""
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


_HzIduSnmpTrapHostActivated_Type.__name__ = "Integer32"
_HzIduSnmpTrapHostActivated_Object = MibTableColumn
hzIduSnmpTrapHostActivated = _HzIduSnmpTrapHostActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 1, 1, 5),
    _HzIduSnmpTrapHostActivated_Type()
)
hzIduSnmpTrapHostActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpTrapHostActivated.setStatus("mandatory")
_HzIduSnmpV3TrapHostsTable_Object = MibTable
hzIduSnmpV3TrapHostsTable = _HzIduSnmpV3TrapHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 2)
)
if mibBuilder.loadTexts:
    hzIduSnmpV3TrapHostsTable.setStatus("mandatory")
_HzIduSnmpV3TrapHostsEntry_Object = MibTableRow
hzIduSnmpV3TrapHostsEntry = _HzIduSnmpV3TrapHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 2, 1)
)
hzIduSnmpV3TrapHostsEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduSnmpV3TrapHostsIndex"),
)
if mibBuilder.loadTexts:
    hzIduSnmpV3TrapHostsEntry.setStatus("mandatory")


class _HzIduSnmpV3TrapHostsIndex_Type(Integer32):
    """Custom type hzIduSnmpV3TrapHostsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HzIduSnmpV3TrapHostsIndex_Type.__name__ = "Integer32"
_HzIduSnmpV3TrapHostsIndex_Object = MibTableColumn
hzIduSnmpV3TrapHostsIndex = _HzIduSnmpV3TrapHostsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 2, 1, 1),
    _HzIduSnmpV3TrapHostsIndex_Type()
)
hzIduSnmpV3TrapHostsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpV3TrapHostsIndex.setStatus("mandatory")
_SnmpV3TrapHostIpAddress_Type = IpAddress
_SnmpV3TrapHostIpAddress_Object = MibTableColumn
snmpV3TrapHostIpAddress = _SnmpV3TrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 2, 1, 8),
    _SnmpV3TrapHostActivated_Type()
)
snmpV3TrapHostActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3TrapHostActivated.setStatus("mandatory")
_HzIduTrapEnable_ObjectIdentity = ObjectIdentity
hzIduTrapEnable = _HzIduTrapEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3)
)


class _HzIduColdStartTrap_Type(Integer32):
    """Custom type hzIduColdStartTrap based on Integer32"""
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


_HzIduColdStartTrap_Type.__name__ = "Integer32"
_HzIduColdStartTrap_Object = MibScalar
hzIduColdStartTrap = _HzIduColdStartTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 1),
    _HzIduColdStartTrap_Type()
)
hzIduColdStartTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduColdStartTrap.setStatus("mandatory")


class _HzIduLinkDownTrap_Type(Integer32):
    """Custom type hzIduLinkDownTrap based on Integer32"""
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


_HzIduLinkDownTrap_Type.__name__ = "Integer32"
_HzIduLinkDownTrap_Object = MibScalar
hzIduLinkDownTrap = _HzIduLinkDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 2),
    _HzIduLinkDownTrap_Type()
)
hzIduLinkDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduLinkDownTrap.setStatus("mandatory")


class _HzIduLinkUpTrap_Type(Integer32):
    """Custom type hzIduLinkUpTrap based on Integer32"""
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


_HzIduLinkUpTrap_Type.__name__ = "Integer32"
_HzIduLinkUpTrap_Object = MibScalar
hzIduLinkUpTrap = _HzIduLinkUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 3),
    _HzIduLinkUpTrap_Type()
)
hzIduLinkUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduLinkUpTrap.setStatus("mandatory")


class _HzIduExplicitAuthenticationFailureTrap_Type(Integer32):
    """Custom type hzIduExplicitAuthenticationFailureTrap based on Integer32"""
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


_HzIduExplicitAuthenticationFailureTrap_Type.__name__ = "Integer32"
_HzIduExplicitAuthenticationFailureTrap_Object = MibScalar
hzIduExplicitAuthenticationFailureTrap = _HzIduExplicitAuthenticationFailureTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 4),
    _HzIduExplicitAuthenticationFailureTrap_Type()
)
hzIduExplicitAuthenticationFailureTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduExplicitAuthenticationFailureTrap.setStatus("mandatory")


class _HzIduAamConfigMismatchTrap_Type(Integer32):
    """Custom type hzIduAamConfigMismatchTrap based on Integer32"""
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


_HzIduAamConfigMismatchTrap_Type.__name__ = "Integer32"
_HzIduAamConfigMismatchTrap_Object = MibScalar
hzIduAamConfigMismatchTrap = _HzIduAamConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 5),
    _HzIduAamConfigMismatchTrap_Type()
)
hzIduAamConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduAamConfigMismatchTrap.setStatus("mandatory")


class _HzIduAamActiveTrap_Type(Integer32):
    """Custom type hzIduAamActiveTrap based on Integer32"""
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


_HzIduAamActiveTrap_Type.__name__ = "Integer32"
_HzIduAamActiveTrap_Object = MibScalar
hzIduAamActiveTrap = _HzIduAamActiveTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 6),
    _HzIduAamActiveTrap_Type()
)
hzIduAamActiveTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduAamActiveTrap.setStatus("mandatory")


class _HzIduAtpcConfigMismatchTrap_Type(Integer32):
    """Custom type hzIduAtpcConfigMismatchTrap based on Integer32"""
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


_HzIduAtpcConfigMismatchTrap_Type.__name__ = "Integer32"
_HzIduAtpcConfigMismatchTrap_Object = MibScalar
hzIduAtpcConfigMismatchTrap = _HzIduAtpcConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 7),
    _HzIduAtpcConfigMismatchTrap_Type()
)
hzIduAtpcConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduAtpcConfigMismatchTrap.setStatus("mandatory")


class _HzIduSntpServersUnreachableTrap_Type(Integer32):
    """Custom type hzIduSntpServersUnreachableTrap based on Integer32"""
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


_HzIduSntpServersUnreachableTrap_Type.__name__ = "Integer32"
_HzIduSntpServersUnreachableTrap_Object = MibScalar
hzIduSntpServersUnreachableTrap = _HzIduSntpServersUnreachableTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 8),
    _HzIduSntpServersUnreachableTrap_Type()
)
hzIduSntpServersUnreachableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduSntpServersUnreachableTrap.setStatus("mandatory")


class _HzIduFrequencyFileInvalidTrap_Type(Integer32):
    """Custom type hzIduFrequencyFileInvalidTrap based on Integer32"""
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


_HzIduFrequencyFileInvalidTrap_Type.__name__ = "Integer32"
_HzIduFrequencyFileInvalidTrap_Object = MibScalar
hzIduFrequencyFileInvalidTrap = _HzIduFrequencyFileInvalidTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 9),
    _HzIduFrequencyFileInvalidTrap_Type()
)
hzIduFrequencyFileInvalidTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduFrequencyFileInvalidTrap.setStatus("mandatory")


class _HzIduEnetPortDroppedFramesThresholdExceedTrap_Type(Integer32):
    """Custom type hzIduEnetPortDroppedFramesThresholdExceedTrap based on Integer32"""
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


_HzIduEnetPortDroppedFramesThresholdExceedTrap_Type.__name__ = "Integer32"
_HzIduEnetPortDroppedFramesThresholdExceedTrap_Object = MibScalar
hzIduEnetPortDroppedFramesThresholdExceedTrap = _HzIduEnetPortDroppedFramesThresholdExceedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 10),
    _HzIduEnetPortDroppedFramesThresholdExceedTrap_Type()
)
hzIduEnetPortDroppedFramesThresholdExceedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPortDroppedFramesThresholdExceedTrap.setStatus("mandatory")


class _HzIduEnetPortBandwidthUtilizationThresholdExceedTrap_Type(Integer32):
    """Custom type hzIduEnetPortBandwidthUtilizationThresholdExceedTrap based on Integer32"""
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


_HzIduEnetPortBandwidthUtilizationThresholdExceedTrap_Type.__name__ = "Integer32"
_HzIduEnetPortBandwidthUtilizationThresholdExceedTrap_Object = MibScalar
hzIduEnetPortBandwidthUtilizationThresholdExceedTrap = _HzIduEnetPortBandwidthUtilizationThresholdExceedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 11),
    _HzIduEnetPortBandwidthUtilizationThresholdExceedTrap_Type()
)
hzIduEnetPortBandwidthUtilizationThresholdExceedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPortBandwidthUtilizationThresholdExceedTrap.setStatus("mandatory")


class _HzIduEnetPortRlsMismatchTrap_Type(Integer32):
    """Custom type hzIduEnetPortRlsMismatchTrap based on Integer32"""
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


_HzIduEnetPortRlsMismatchTrap_Type.__name__ = "Integer32"
_HzIduEnetPortRlsMismatchTrap_Object = MibScalar
hzIduEnetPortRlsMismatchTrap = _HzIduEnetPortRlsMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 12),
    _HzIduEnetPortRlsMismatchTrap_Type()
)
hzIduEnetPortRlsMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEnetPortRlsMismatchTrap.setStatus("mandatory")


class _HzIduRLSQueueBasedShutdownActivatedTrap_Type(Integer32):
    """Custom type hzIduRLSQueueBasedShutdownActivatedTrap based on Integer32"""
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


_HzIduRLSQueueBasedShutdownActivatedTrap_Type.__name__ = "Integer32"
_HzIduRLSQueueBasedShutdownActivatedTrap_Object = MibScalar
hzIduRLSQueueBasedShutdownActivatedTrap = _HzIduRLSQueueBasedShutdownActivatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 13),
    _HzIduRLSQueueBasedShutdownActivatedTrap_Type()
)
hzIduRLSQueueBasedShutdownActivatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRLSQueueBasedShutdownActivatedTrap.setStatus("mandatory")


class _HzIduModemRxLossOfSignalLockTrap_Type(Integer32):
    """Custom type hzIduModemRxLossOfSignalLockTrap based on Integer32"""
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


_HzIduModemRxLossOfSignalLockTrap_Type.__name__ = "Integer32"
_HzIduModemRxLossOfSignalLockTrap_Object = MibScalar
hzIduModemRxLossOfSignalLockTrap = _HzIduModemRxLossOfSignalLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 14),
    _HzIduModemRxLossOfSignalLockTrap_Type()
)
hzIduModemRxLossOfSignalLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduModemRxLossOfSignalLockTrap.setStatus("mandatory")


class _HzIduModemTxLossOfSyncTrap_Type(Integer32):
    """Custom type hzIduModemTxLossOfSyncTrap based on Integer32"""
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


_HzIduModemTxLossOfSyncTrap_Type.__name__ = "Integer32"
_HzIduModemTxLossOfSyncTrap_Object = MibScalar
hzIduModemTxLossOfSyncTrap = _HzIduModemTxLossOfSyncTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 15),
    _HzIduModemTxLossOfSyncTrap_Type()
)
hzIduModemTxLossOfSyncTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduModemTxLossOfSyncTrap.setStatus("mandatory")


class _HzIduModemSnrBelowThresholdTrap_Type(Integer32):
    """Custom type hzIduModemSnrBelowThresholdTrap based on Integer32"""
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


_HzIduModemSnrBelowThresholdTrap_Type.__name__ = "Integer32"
_HzIduModemSnrBelowThresholdTrap_Object = MibScalar
hzIduModemSnrBelowThresholdTrap = _HzIduModemSnrBelowThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 16),
    _HzIduModemSnrBelowThresholdTrap_Type()
)
hzIduModemSnrBelowThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduModemSnrBelowThresholdTrap.setStatus("mandatory")


class _HzIduModemEqualizerStressExceedThresholdTrap_Type(Integer32):
    """Custom type hzIduModemEqualizerStressExceedThresholdTrap based on Integer32"""
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


_HzIduModemEqualizerStressExceedThresholdTrap_Type.__name__ = "Integer32"
_HzIduModemEqualizerStressExceedThresholdTrap_Object = MibScalar
hzIduModemEqualizerStressExceedThresholdTrap = _HzIduModemEqualizerStressExceedThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 17),
    _HzIduModemEqualizerStressExceedThresholdTrap_Type()
)
hzIduModemEqualizerStressExceedThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduModemEqualizerStressExceedThresholdTrap.setStatus("mandatory")


class _HzIduModemChannelizedRslBelowThresholdTrap_Type(Integer32):
    """Custom type hzIduModemChannelizedRslBelowThresholdTrap based on Integer32"""
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


_HzIduModemChannelizedRslBelowThresholdTrap_Type.__name__ = "Integer32"
_HzIduModemChannelizedRslBelowThresholdTrap_Object = MibScalar
hzIduModemChannelizedRslBelowThresholdTrap = _HzIduModemChannelizedRslBelowThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 18),
    _HzIduModemChannelizedRslBelowThresholdTrap_Type()
)
hzIduModemChannelizedRslBelowThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduModemChannelizedRslBelowThresholdTrap.setStatus("mandatory")


class _HzIduModemHardwareFaultTrap_Type(Integer32):
    """Custom type hzIduModemHardwareFaultTrap based on Integer32"""
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


_HzIduModemHardwareFaultTrap_Type.__name__ = "Integer32"
_HzIduModemHardwareFaultTrap_Object = MibScalar
hzIduModemHardwareFaultTrap = _HzIduModemHardwareFaultTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 19),
    _HzIduModemHardwareFaultTrap_Type()
)
hzIduModemHardwareFaultTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduModemHardwareFaultTrap.setStatus("mandatory")


class _HzIduModemProgrammingErrorTrap_Type(Integer32):
    """Custom type hzIduModemProgrammingErrorTrap based on Integer32"""
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


_HzIduModemProgrammingErrorTrap_Type.__name__ = "Integer32"
_HzIduModemProgrammingErrorTrap_Object = MibScalar
hzIduModemProgrammingErrorTrap = _HzIduModemProgrammingErrorTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 20),
    _HzIduModemProgrammingErrorTrap_Type()
)
hzIduModemProgrammingErrorTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduModemProgrammingErrorTrap.setStatus("mandatory")


class _HzIduTtyManagementSessionCommencedTrap_Type(Integer32):
    """Custom type hzIduTtyManagementSessionCommencedTrap based on Integer32"""
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


_HzIduTtyManagementSessionCommencedTrap_Type.__name__ = "Integer32"
_HzIduTtyManagementSessionCommencedTrap_Object = MibScalar
hzIduTtyManagementSessionCommencedTrap = _HzIduTtyManagementSessionCommencedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 21),
    _HzIduTtyManagementSessionCommencedTrap_Type()
)
hzIduTtyManagementSessionCommencedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduTtyManagementSessionCommencedTrap.setStatus("mandatory")


class _HzIduTtyManagementSessionTerminatedTrap_Type(Integer32):
    """Custom type hzIduTtyManagementSessionTerminatedTrap based on Integer32"""
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


_HzIduTtyManagementSessionTerminatedTrap_Type.__name__ = "Integer32"
_HzIduTtyManagementSessionTerminatedTrap_Object = MibScalar
hzIduTtyManagementSessionTerminatedTrap = _HzIduTtyManagementSessionTerminatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 22),
    _HzIduTtyManagementSessionTerminatedTrap_Type()
)
hzIduTtyManagementSessionTerminatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduTtyManagementSessionTerminatedTrap.setStatus("mandatory")


class _HzIduAtpcTxAtMaxPwrTrap_Type(Integer32):
    """Custom type hzIduAtpcTxAtMaxPwrTrap based on Integer32"""
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


_HzIduAtpcTxAtMaxPwrTrap_Type.__name__ = "Integer32"
_HzIduAtpcTxAtMaxPwrTrap_Object = MibScalar
hzIduAtpcTxAtMaxPwrTrap = _HzIduAtpcTxAtMaxPwrTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 23),
    _HzIduAtpcTxAtMaxPwrTrap_Type()
)
hzIduAtpcTxAtMaxPwrTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduAtpcTxAtMaxPwrTrap.setStatus("mandatory")


class _HzIduRadioPLDROLostLockTrap_Type(Integer32):
    """Custom type hzIduRadioPLDROLostLockTrap based on Integer32"""
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


_HzIduRadioPLDROLostLockTrap_Type.__name__ = "Integer32"
_HzIduRadioPLDROLostLockTrap_Object = MibScalar
hzIduRadioPLDROLostLockTrap = _HzIduRadioPLDROLostLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 24),
    _HzIduRadioPLDROLostLockTrap_Type()
)
hzIduRadioPLDROLostLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadioPLDROLostLockTrap.setStatus("mandatory")


class _HzIduRadioLostCommunicationTrap_Type(Integer32):
    """Custom type hzIduRadioLostCommunicationTrap based on Integer32"""
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


_HzIduRadioLostCommunicationTrap_Type.__name__ = "Integer32"
_HzIduRadioLostCommunicationTrap_Object = MibScalar
hzIduRadioLostCommunicationTrap = _HzIduRadioLostCommunicationTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 25),
    _HzIduRadioLostCommunicationTrap_Type()
)
hzIduRadioLostCommunicationTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadioLostCommunicationTrap.setStatus("mandatory")


class _HzIduRadioMismatchTrap_Type(Integer32):
    """Custom type hzIduRadioMismatchTrap based on Integer32"""
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


_HzIduRadioMismatchTrap_Type.__name__ = "Integer32"
_HzIduRadioMismatchTrap_Object = MibScalar
hzIduRadioMismatchTrap = _HzIduRadioMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 26),
    _HzIduRadioMismatchTrap_Type()
)
hzIduRadioMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadioMismatchTrap.setStatus("mandatory")


class _HzIduRadioPowerAmpTrap_Type(Integer32):
    """Custom type hzIduRadioPowerAmpTrap based on Integer32"""
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


_HzIduRadioPowerAmpTrap_Type.__name__ = "Integer32"
_HzIduRadioPowerAmpTrap_Object = MibScalar
hzIduRadioPowerAmpTrap = _HzIduRadioPowerAmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 27),
    _HzIduRadioPowerAmpTrap_Type()
)
hzIduRadioPowerAmpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadioPowerAmpTrap.setStatus("mandatory")


class _HzIduRadioExcessiveTxCableLossTrap_Type(Integer32):
    """Custom type hzIduRadioExcessiveTxCableLossTrap based on Integer32"""
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


_HzIduRadioExcessiveTxCableLossTrap_Type.__name__ = "Integer32"
_HzIduRadioExcessiveTxCableLossTrap_Object = MibScalar
hzIduRadioExcessiveTxCableLossTrap = _HzIduRadioExcessiveTxCableLossTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 28),
    _HzIduRadioExcessiveTxCableLossTrap_Type()
)
hzIduRadioExcessiveTxCableLossTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadioExcessiveTxCableLossTrap.setStatus("mandatory")


class _HzIduHiPowerRadioDrainM1Trap_Type(Integer32):
    """Custom type hzIduHiPowerRadioDrainM1Trap based on Integer32"""
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


_HzIduHiPowerRadioDrainM1Trap_Type.__name__ = "Integer32"
_HzIduHiPowerRadioDrainM1Trap_Object = MibScalar
hzIduHiPowerRadioDrainM1Trap = _HzIduHiPowerRadioDrainM1Trap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 29),
    _HzIduHiPowerRadioDrainM1Trap_Type()
)
hzIduHiPowerRadioDrainM1Trap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduHiPowerRadioDrainM1Trap.setStatus("mandatory")


class _HzIduHiPowerRadioDrainM2Trap_Type(Integer32):
    """Custom type hzIduHiPowerRadioDrainM2Trap based on Integer32"""
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


_HzIduHiPowerRadioDrainM2Trap_Type.__name__ = "Integer32"
_HzIduHiPowerRadioDrainM2Trap_Object = MibScalar
hzIduHiPowerRadioDrainM2Trap = _HzIduHiPowerRadioDrainM2Trap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 30),
    _HzIduHiPowerRadioDrainM2Trap_Type()
)
hzIduHiPowerRadioDrainM2Trap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduHiPowerRadioDrainM2Trap.setStatus("mandatory")


class _HzIduHiPowerRadioTxDetectorTrap_Type(Integer32):
    """Custom type hzIduHiPowerRadioTxDetectorTrap based on Integer32"""
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


_HzIduHiPowerRadioTxDetectorTrap_Type.__name__ = "Integer32"
_HzIduHiPowerRadioTxDetectorTrap_Object = MibScalar
hzIduHiPowerRadioTxDetectorTrap = _HzIduHiPowerRadioTxDetectorTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 31),
    _HzIduHiPowerRadioTxDetectorTrap_Type()
)
hzIduHiPowerRadioTxDetectorTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduHiPowerRadioTxDetectorTrap.setStatus("mandatory")


class _HzIduSecondaryRadioIsActiveTrap_Type(Integer32):
    """Custom type hzIduSecondaryRadioIsActiveTrap based on Integer32"""
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


_HzIduSecondaryRadioIsActiveTrap_Type.__name__ = "Integer32"
_HzIduSecondaryRadioIsActiveTrap_Object = MibScalar
hzIduSecondaryRadioIsActiveTrap = _HzIduSecondaryRadioIsActiveTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 32),
    _HzIduSecondaryRadioIsActiveTrap_Type()
)
hzIduSecondaryRadioIsActiveTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduSecondaryRadioIsActiveTrap.setStatus("mandatory")


class _HzIduRedundancySerialNumberMisMatchTrap_Type(Integer32):
    """Custom type hzIduRedundancySerialNumberMisMatchTrap based on Integer32"""
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


_HzIduRedundancySerialNumberMisMatchTrap_Type.__name__ = "Integer32"
_HzIduRedundancySerialNumberMisMatchTrap_Object = MibScalar
hzIduRedundancySerialNumberMisMatchTrap = _HzIduRedundancySerialNumberMisMatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 33),
    _HzIduRedundancySerialNumberMisMatchTrap_Type()
)
hzIduRedundancySerialNumberMisMatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRedundancySerialNumberMisMatchTrap.setStatus("mandatory")


class _HzIduRadioFirmwareMismatchTrap_Type(Integer32):
    """Custom type hzIduRadioFirmwareMismatchTrap based on Integer32"""
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


_HzIduRadioFirmwareMismatchTrap_Type.__name__ = "Integer32"
_HzIduRadioFirmwareMismatchTrap_Object = MibScalar
hzIduRadioFirmwareMismatchTrap = _HzIduRadioFirmwareMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 34),
    _HzIduRadioFirmwareMismatchTrap_Type()
)
hzIduRadioFirmwareMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadioFirmwareMismatchTrap.setStatus("mandatory")


class _HzIduSecondaryRadioNotdetectedTrap_Type(Integer32):
    """Custom type hzIduSecondaryRadioNotdetectedTrap based on Integer32"""
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


_HzIduSecondaryRadioNotdetectedTrap_Type.__name__ = "Integer32"
_HzIduSecondaryRadioNotdetectedTrap_Object = MibScalar
hzIduSecondaryRadioNotdetectedTrap = _HzIduSecondaryRadioNotdetectedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 35),
    _HzIduSecondaryRadioNotdetectedTrap_Type()
)
hzIduSecondaryRadioNotdetectedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduSecondaryRadioNotdetectedTrap.setStatus("mandatory")


class _HzIduPrimaryRadioNotdetectedTrap_Type(Integer32):
    """Custom type hzIduPrimaryRadioNotdetectedTrap based on Integer32"""
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


_HzIduPrimaryRadioNotdetectedTrap_Type.__name__ = "Integer32"
_HzIduPrimaryRadioNotdetectedTrap_Object = MibScalar
hzIduPrimaryRadioNotdetectedTrap = _HzIduPrimaryRadioNotdetectedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 36),
    _HzIduPrimaryRadioNotdetectedTrap_Type()
)
hzIduPrimaryRadioNotdetectedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduPrimaryRadioNotdetectedTrap.setStatus("mandatory")


class _HzIduFaultyPrimaryRadioTrap_Type(Integer32):
    """Custom type hzIduFaultyPrimaryRadioTrap based on Integer32"""
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


_HzIduFaultyPrimaryRadioTrap_Type.__name__ = "Integer32"
_HzIduFaultyPrimaryRadioTrap_Object = MibScalar
hzIduFaultyPrimaryRadioTrap = _HzIduFaultyPrimaryRadioTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 37),
    _HzIduFaultyPrimaryRadioTrap_Type()
)
hzIduFaultyPrimaryRadioTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduFaultyPrimaryRadioTrap.setStatus("mandatory")


class _HzIduRadioExcessiveTxCableLossChangeTrap_Type(Integer32):
    """Custom type hzIduRadioExcessiveTxCableLossChangeTrap based on Integer32"""
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


_HzIduRadioExcessiveTxCableLossChangeTrap_Type.__name__ = "Integer32"
_HzIduRadioExcessiveTxCableLossChangeTrap_Object = MibScalar
hzIduRadioExcessiveTxCableLossChangeTrap = _HzIduRadioExcessiveTxCableLossChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 38),
    _HzIduRadioExcessiveTxCableLossChangeTrap_Type()
)
hzIduRadioExcessiveTxCableLossChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadioExcessiveTxCableLossChangeTrap.setStatus("mandatory")


class _HzIduRadioExcessiveRxCableLossTrap_Type(Integer32):
    """Custom type hzIduRadioExcessiveRxCableLossTrap based on Integer32"""
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


_HzIduRadioExcessiveRxCableLossTrap_Type.__name__ = "Integer32"
_HzIduRadioExcessiveRxCableLossTrap_Object = MibScalar
hzIduRadioExcessiveRxCableLossTrap = _HzIduRadioExcessiveRxCableLossTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 39),
    _HzIduRadioExcessiveRxCableLossTrap_Type()
)
hzIduRadioExcessiveRxCableLossTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadioExcessiveRxCableLossTrap.setStatus("mandatory")


class _HzIduRedundancyPrimaryPortNotSetTrap_Type(Integer32):
    """Custom type hzIduRedundancyPrimaryPortNotSetTrap based on Integer32"""
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


_HzIduRedundancyPrimaryPortNotSetTrap_Type.__name__ = "Integer32"
_HzIduRedundancyPrimaryPortNotSetTrap_Object = MibScalar
hzIduRedundancyPrimaryPortNotSetTrap = _HzIduRedundancyPrimaryPortNotSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 40),
    _HzIduRedundancyPrimaryPortNotSetTrap_Type()
)
hzIduRedundancyPrimaryPortNotSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRedundancyPrimaryPortNotSetTrap.setStatus("mandatory")


class _HzIduRedundancySecondaryPortIsActiveTrap_Type(Integer32):
    """Custom type hzIduRedundancySecondaryPortIsActiveTrap based on Integer32"""
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


_HzIduRedundancySecondaryPortIsActiveTrap_Type.__name__ = "Integer32"
_HzIduRedundancySecondaryPortIsActiveTrap_Object = MibScalar
hzIduRedundancySecondaryPortIsActiveTrap = _HzIduRedundancySecondaryPortIsActiveTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 41),
    _HzIduRedundancySecondaryPortIsActiveTrap_Type()
)
hzIduRedundancySecondaryPortIsActiveTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRedundancySecondaryPortIsActiveTrap.setStatus("mandatory")


class _HzIduRedundancyPrimaryPortFaultyTrap_Type(Integer32):
    """Custom type hzIduRedundancyPrimaryPortFaultyTrap based on Integer32"""
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


_HzIduRedundancyPrimaryPortFaultyTrap_Type.__name__ = "Integer32"
_HzIduRedundancyPrimaryPortFaultyTrap_Object = MibScalar
hzIduRedundancyPrimaryPortFaultyTrap = _HzIduRedundancyPrimaryPortFaultyTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 42),
    _HzIduRedundancyPrimaryPortFaultyTrap_Type()
)
hzIduRedundancyPrimaryPortFaultyTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRedundancyPrimaryPortFaultyTrap.setStatus("mandatory")


class _HzIduRedundancySecondaryPortFaultyTrap_Type(Integer32):
    """Custom type hzIduRedundancySecondaryPortFaultyTrap based on Integer32"""
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


_HzIduRedundancySecondaryPortFaultyTrap_Type.__name__ = "Integer32"
_HzIduRedundancySecondaryPortFaultyTrap_Object = MibScalar
hzIduRedundancySecondaryPortFaultyTrap = _HzIduRedundancySecondaryPortFaultyTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 43),
    _HzIduRedundancySecondaryPortFaultyTrap_Type()
)
hzIduRedundancySecondaryPortFaultyTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRedundancySecondaryPortFaultyTrap.setStatus("mandatory")


class _HzIduFan1FailedTrap_Type(Integer32):
    """Custom type hzIduFan1FailedTrap based on Integer32"""
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


_HzIduFan1FailedTrap_Type.__name__ = "Integer32"
_HzIduFan1FailedTrap_Object = MibScalar
hzIduFan1FailedTrap = _HzIduFan1FailedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 44),
    _HzIduFan1FailedTrap_Type()
)
hzIduFan1FailedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduFan1FailedTrap.setStatus("mandatory")


class _HzIduFan2FailedTrap_Type(Integer32):
    """Custom type hzIduFan2FailedTrap based on Integer32"""
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


_HzIduFan2FailedTrap_Type.__name__ = "Integer32"
_HzIduFan2FailedTrap_Object = MibScalar
hzIduFan2FailedTrap = _HzIduFan2FailedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 45),
    _HzIduFan2FailedTrap_Type()
)
hzIduFan2FailedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduFan2FailedTrap.setStatus("mandatory")


class _HzIduFan3FailedTrap_Type(Integer32):
    """Custom type hzIduFan3FailedTrap based on Integer32"""
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


_HzIduFan3FailedTrap_Type.__name__ = "Integer32"
_HzIduFan3FailedTrap_Object = MibScalar
hzIduFan3FailedTrap = _HzIduFan3FailedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 46),
    _HzIduFan3FailedTrap_Type()
)
hzIduFan3FailedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduFan3FailedTrap.setStatus("mandatory")


class _HzIduFan4FailedTrap_Type(Integer32):
    """Custom type hzIduFan4FailedTrap based on Integer32"""
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


_HzIduFan4FailedTrap_Type.__name__ = "Integer32"
_HzIduFan4FailedTrap_Object = MibScalar
hzIduFan4FailedTrap = _HzIduFan4FailedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 47),
    _HzIduFan4FailedTrap_Type()
)
hzIduFan4FailedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduFan4FailedTrap.setStatus("mandatory")


class _HzIduPortRLSShutdownActivatedTrap_Type(Integer32):
    """Custom type hzIduPortRLSShutdownActivatedTrap based on Integer32"""
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


_HzIduPortRLSShutdownActivatedTrap_Type.__name__ = "Integer32"
_HzIduPortRLSShutdownActivatedTrap_Object = MibScalar
hzIduPortRLSShutdownActivatedTrap = _HzIduPortRLSShutdownActivatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 3, 48),
    _HzIduPortRLSShutdownActivatedTrap_Type()
)
hzIduPortRLSShutdownActivatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduPortRLSShutdownActivatedTrap.setStatus("mandatory")
_HzIduSnmp_ObjectIdentity = ObjectIdentity
hzIduSnmp = _HzIduSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9)
)


class _HzIduSnmpUserAccess_Type(Integer32):
    """Custom type hzIduSnmpUserAccess based on Integer32"""
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


_HzIduSnmpUserAccess_Type.__name__ = "Integer32"
_HzIduSnmpUserAccess_Object = MibScalar
hzIduSnmpUserAccess = _HzIduSnmpUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 1),
    _HzIduSnmpUserAccess_Type()
)
hzIduSnmpUserAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpUserAccess.setStatus("mandatory")


class _HzIduSnmpManagerAnyCommunityName_Type(DisplayString):
    """Custom type hzIduSnmpManagerAnyCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduSnmpManagerAnyCommunityName_Type.__name__ = "DisplayString"
_HzIduSnmpManagerAnyCommunityName_Object = MibScalar
hzIduSnmpManagerAnyCommunityName = _HzIduSnmpManagerAnyCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 2),
    _HzIduSnmpManagerAnyCommunityName_Type()
)
hzIduSnmpManagerAnyCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpManagerAnyCommunityName.setStatus("mandatory")


class _HzIduSnmpSetRequests_Type(Integer32):
    """Custom type hzIduSnmpSetRequests based on Integer32"""
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


_HzIduSnmpSetRequests_Type.__name__ = "Integer32"
_HzIduSnmpSetRequests_Object = MibScalar
hzIduSnmpSetRequests = _HzIduSnmpSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 3),
    _HzIduSnmpSetRequests_Type()
)
hzIduSnmpSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpSetRequests.setStatus("mandatory")
_HzIduSnmpManagersTable_Object = MibTable
hzIduSnmpManagersTable = _HzIduSnmpManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 4)
)
if mibBuilder.loadTexts:
    hzIduSnmpManagersTable.setStatus("mandatory")
_HzIduSnmpManagersEntry_Object = MibTableRow
hzIduSnmpManagersEntry = _HzIduSnmpManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 4, 1)
)
hzIduSnmpManagersEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduSnmpManagersIndex"),
)
if mibBuilder.loadTexts:
    hzIduSnmpManagersEntry.setStatus("mandatory")
_HzIduSnmpManagersIndex_Type = Integer32
_HzIduSnmpManagersIndex_Object = MibTableColumn
hzIduSnmpManagersIndex = _HzIduSnmpManagersIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 4, 1, 1),
    _HzIduSnmpManagersIndex_Type()
)
hzIduSnmpManagersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpManagersIndex.setStatus("mandatory")
_HzIduSnmpManagerIpAddress_Type = IpAddress
_HzIduSnmpManagerIpAddress_Object = MibTableColumn
hzIduSnmpManagerIpAddress = _HzIduSnmpManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 4, 1, 2),
    _HzIduSnmpManagerIpAddress_Type()
)
hzIduSnmpManagerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpManagerIpAddress.setStatus("mandatory")


class _HzIduSnmpManagerCommunityName_Type(DisplayString):
    """Custom type hzIduSnmpManagerCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduSnmpManagerCommunityName_Type.__name__ = "DisplayString"
_HzIduSnmpManagerCommunityName_Object = MibTableColumn
hzIduSnmpManagerCommunityName = _HzIduSnmpManagerCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 4, 1, 3),
    _HzIduSnmpManagerCommunityName_Type()
)
hzIduSnmpManagerCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpManagerCommunityName.setStatus("mandatory")


class _HzIduSnmpManagerActivated_Type(Integer32):
    """Custom type hzIduSnmpManagerActivated based on Integer32"""
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


_HzIduSnmpManagerActivated_Type.__name__ = "Integer32"
_HzIduSnmpManagerActivated_Object = MibTableColumn
hzIduSnmpManagerActivated = _HzIduSnmpManagerActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 4, 1, 4),
    _HzIduSnmpManagerActivated_Type()
)
hzIduSnmpManagerActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpManagerActivated.setStatus("mandatory")
_HzIduSnmpV3ManagersTable_Object = MibTable
hzIduSnmpV3ManagersTable = _HzIduSnmpV3ManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 5)
)
if mibBuilder.loadTexts:
    hzIduSnmpV3ManagersTable.setStatus("mandatory")
_HzIduSnmpV3ManagersEntry_Object = MibTableRow
hzIduSnmpV3ManagersEntry = _HzIduSnmpV3ManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 5, 1)
)
hzIduSnmpV3ManagersEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduSnmpV3ManagersIndex"),
)
if mibBuilder.loadTexts:
    hzIduSnmpV3ManagersEntry.setStatus("mandatory")
_HzIduSnmpV3ManagersIndex_Type = Integer32
_HzIduSnmpV3ManagersIndex_Object = MibTableColumn
hzIduSnmpV3ManagersIndex = _HzIduSnmpV3ManagersIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 5, 1, 1),
    _HzIduSnmpV3ManagersIndex_Type()
)
hzIduSnmpV3ManagersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpV3ManagersIndex.setStatus("mandatory")


class _HzIduSnmpV3ManagerUserName_Type(DisplayString):
    """Custom type hzIduSnmpV3ManagerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduSnmpV3ManagerUserName_Type.__name__ = "DisplayString"
_HzIduSnmpV3ManagerUserName_Object = MibTableColumn
hzIduSnmpV3ManagerUserName = _HzIduSnmpV3ManagerUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 5, 1, 2),
    _HzIduSnmpV3ManagerUserName_Type()
)
hzIduSnmpV3ManagerUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpV3ManagerUserName.setStatus("mandatory")


class _HzIduSnmpV3ManagerAuthProtocol_Type(Integer32):
    """Custom type hzIduSnmpV3ManagerAuthProtocol based on Integer32"""
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


_HzIduSnmpV3ManagerAuthProtocol_Type.__name__ = "Integer32"
_HzIduSnmpV3ManagerAuthProtocol_Object = MibTableColumn
hzIduSnmpV3ManagerAuthProtocol = _HzIduSnmpV3ManagerAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 5, 1, 3),
    _HzIduSnmpV3ManagerAuthProtocol_Type()
)
hzIduSnmpV3ManagerAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpV3ManagerAuthProtocol.setStatus("mandatory")


class _HzIduSnmpV3ManagerAuthPassword_Type(DisplayString):
    """Custom type hzIduSnmpV3ManagerAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduSnmpV3ManagerAuthPassword_Type.__name__ = "DisplayString"
_HzIduSnmpV3ManagerAuthPassword_Object = MibTableColumn
hzIduSnmpV3ManagerAuthPassword = _HzIduSnmpV3ManagerAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 5, 1, 4),
    _HzIduSnmpV3ManagerAuthPassword_Type()
)
hzIduSnmpV3ManagerAuthPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpV3ManagerAuthPassword.setStatus("mandatory")


class _HzIduSnmpV3ManagerPrivProtocol_Type(Integer32):
    """Custom type hzIduSnmpV3ManagerPrivProtocol based on Integer32"""
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


_HzIduSnmpV3ManagerPrivProtocol_Type.__name__ = "Integer32"
_HzIduSnmpV3ManagerPrivProtocol_Object = MibTableColumn
hzIduSnmpV3ManagerPrivProtocol = _HzIduSnmpV3ManagerPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 5, 1, 5),
    _HzIduSnmpV3ManagerPrivProtocol_Type()
)
hzIduSnmpV3ManagerPrivProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpV3ManagerPrivProtocol.setStatus("mandatory")


class _HzIduSnmpV3ManagerPrivPassword_Type(DisplayString):
    """Custom type hzIduSnmpV3ManagerPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduSnmpV3ManagerPrivPassword_Type.__name__ = "DisplayString"
_HzIduSnmpV3ManagerPrivPassword_Object = MibTableColumn
hzIduSnmpV3ManagerPrivPassword = _HzIduSnmpV3ManagerPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 5, 1, 6),
    _HzIduSnmpV3ManagerPrivPassword_Type()
)
hzIduSnmpV3ManagerPrivPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpV3ManagerPrivPassword.setStatus("mandatory")


class _HzIduSnmpV3ManagerActivated_Type(Integer32):
    """Custom type hzIduSnmpV3ManagerActivated based on Integer32"""
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


_HzIduSnmpV3ManagerActivated_Type.__name__ = "Integer32"
_HzIduSnmpV3ManagerActivated_Object = MibTableColumn
hzIduSnmpV3ManagerActivated = _HzIduSnmpV3ManagerActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 9, 5, 1, 7),
    _HzIduSnmpV3ManagerActivated_Type()
)
hzIduSnmpV3ManagerActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSnmpV3ManagerActivated.setStatus("mandatory")
_HzIduManagementSessions_ObjectIdentity = ObjectIdentity
hzIduManagementSessions = _HzIduManagementSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 10)
)
_HzIduTtySessionUserTable_Object = MibTable
hzIduTtySessionUserTable = _HzIduTtySessionUserTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 10, 1)
)
if mibBuilder.loadTexts:
    hzIduTtySessionUserTable.setStatus("mandatory")
_HzIduTtySessionUserEntry_Object = MibTableRow
hzIduTtySessionUserEntry = _HzIduTtySessionUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 10, 1, 1)
)
hzIduTtySessionUserEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduTtySessionUserIndex"),
)
if mibBuilder.loadTexts:
    hzIduTtySessionUserEntry.setStatus("mandatory")


class _HzIduTtySessionUserIndex_Type(Integer32):
    """Custom type hzIduTtySessionUserIndex based on Integer32"""
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
        *(("user1", 1),
          ("user2", 2),
          ("user3", 3),
          ("user4", 4),
          ("user5", 5),
          ("user6", 6))
    )


_HzIduTtySessionUserIndex_Type.__name__ = "Integer32"
_HzIduTtySessionUserIndex_Object = MibTableColumn
hzIduTtySessionUserIndex = _HzIduTtySessionUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 10, 1, 1, 1),
    _HzIduTtySessionUserIndex_Type()
)
hzIduTtySessionUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduTtySessionUserIndex.setStatus("mandatory")


class _HzIduTtySessionUserName_Type(DisplayString):
    """Custom type hzIduTtySessionUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzIduTtySessionUserName_Type.__name__ = "DisplayString"
_HzIduTtySessionUserName_Object = MibTableColumn
hzIduTtySessionUserName = _HzIduTtySessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 10, 1, 1, 2),
    _HzIduTtySessionUserName_Type()
)
hzIduTtySessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduTtySessionUserName.setStatus("mandatory")


class _HzIduTtySessionUserConnectionType_Type(Integer32):
    """Custom type hzIduTtySessionUserConnectionType based on Integer32"""
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


_HzIduTtySessionUserConnectionType_Type.__name__ = "Integer32"
_HzIduTtySessionUserConnectionType_Object = MibTableColumn
hzIduTtySessionUserConnectionType = _HzIduTtySessionUserConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 10, 1, 1, 3),
    _HzIduTtySessionUserConnectionType_Type()
)
hzIduTtySessionUserConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduTtySessionUserConnectionType.setStatus("mandatory")


class _HzIduTtySessionUserState_Type(Integer32):
    """Custom type hzIduTtySessionUserState based on Integer32"""
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


_HzIduTtySessionUserState_Type.__name__ = "Integer32"
_HzIduTtySessionUserState_Object = MibTableColumn
hzIduTtySessionUserState = _HzIduTtySessionUserState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 10, 1, 1, 4),
    _HzIduTtySessionUserState_Type()
)
hzIduTtySessionUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduTtySessionUserState.setStatus("mandatory")
_HzIduHttp_ObjectIdentity = ObjectIdentity
hzIduHttp = _HzIduHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 11)
)


class _HzIduHttpEnable_Type(Integer32):
    """Custom type hzIduHttpEnable based on Integer32"""
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


_HzIduHttpEnable_Type.__name__ = "Integer32"
_HzIduHttpEnable_Object = MibScalar
hzIduHttpEnable = _HzIduHttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 11, 1),
    _HzIduHttpEnable_Type()
)
hzIduHttpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduHttpEnable.setStatus("mandatory")
_HzIduHttpSecure_ObjectIdentity = ObjectIdentity
hzIduHttpSecure = _HzIduHttpSecure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 11, 2)
)


class _HzIduHttpSecureCertificateStatus_Type(DisplayString):
    """Custom type hzIduHttpSecureCertificateStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HzIduHttpSecureCertificateStatus_Type.__name__ = "DisplayString"
_HzIduHttpSecureCertificateStatus_Object = MibScalar
hzIduHttpSecureCertificateStatus = _HzIduHttpSecureCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 11, 2, 1),
    _HzIduHttpSecureCertificateStatus_Type()
)
hzIduHttpSecureCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduHttpSecureCertificateStatus.setStatus("mandatory")


class _HzIduHttpSecureAccessForAdminUsers_Type(Integer32):
    """Custom type hzIduHttpSecureAccessForAdminUsers based on Integer32"""
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


_HzIduHttpSecureAccessForAdminUsers_Type.__name__ = "Integer32"
_HzIduHttpSecureAccessForAdminUsers_Object = MibScalar
hzIduHttpSecureAccessForAdminUsers = _HzIduHttpSecureAccessForAdminUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 11, 2, 2),
    _HzIduHttpSecureAccessForAdminUsers_Type()
)
hzIduHttpSecureAccessForAdminUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduHttpSecureAccessForAdminUsers.setStatus("mandatory")


class _HzIduHttpSecureAccessForNocUsers_Type(Integer32):
    """Custom type hzIduHttpSecureAccessForNocUsers based on Integer32"""
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


_HzIduHttpSecureAccessForNocUsers_Type.__name__ = "Integer32"
_HzIduHttpSecureAccessForNocUsers_Object = MibScalar
hzIduHttpSecureAccessForNocUsers = _HzIduHttpSecureAccessForNocUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 11, 2, 3),
    _HzIduHttpSecureAccessForNocUsers_Type()
)
hzIduHttpSecureAccessForNocUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduHttpSecureAccessForNocUsers.setStatus("mandatory")


class _HzIduHttpSecureAccessForSuperUsers_Type(Integer32):
    """Custom type hzIduHttpSecureAccessForSuperUsers based on Integer32"""
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


_HzIduHttpSecureAccessForSuperUsers_Type.__name__ = "Integer32"
_HzIduHttpSecureAccessForSuperUsers_Object = MibScalar
hzIduHttpSecureAccessForSuperUsers = _HzIduHttpSecureAccessForSuperUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 11, 2, 4),
    _HzIduHttpSecureAccessForSuperUsers_Type()
)
hzIduHttpSecureAccessForSuperUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduHttpSecureAccessForSuperUsers.setStatus("mandatory")
_HzIduQos_ObjectIdentity = ObjectIdentity
hzIduQos = _HzIduQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12)
)


class _HzIduQosEnable_Type(Integer32):
    """Custom type hzIduQosEnable based on Integer32"""
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


_HzIduQosEnable_Type.__name__ = "Integer32"
_HzIduQosEnable_Object = MibScalar
hzIduQosEnable = _HzIduQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 1),
    _HzIduQosEnable_Type()
)
hzIduQosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduQosEnable.setStatus("mandatory")


class _HzIduCosType_Type(Integer32):
    """Custom type hzIduCosType based on Integer32"""
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
        *(("cosVlan", 1),
          ("cosQinQiTag", 2),
          ("cosQinQoTag", 3))
    )


_HzIduCosType_Type.__name__ = "Integer32"
_HzIduCosType_Object = MibScalar
hzIduCosType = _HzIduCosType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 2),
    _HzIduCosType_Type()
)
hzIduCosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduCosType.setStatus("mandatory")
_HzIduCoSQinQiTag_Type = DisplayString
_HzIduCoSQinQiTag_Object = MibScalar
hzIduCoSQinQiTag = _HzIduCoSQinQiTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 3),
    _HzIduCoSQinQiTag_Type()
)
hzIduCoSQinQiTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduCoSQinQiTag.setStatus("mandatory")
_HzIduCoSQinQoTag_Type = DisplayString
_HzIduCoSQinQoTag_Object = MibScalar
hzIduCoSQinQoTag = _HzIduCoSQinQoTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 4),
    _HzIduCoSQinQoTag_Type()
)
hzIduCoSQinQoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduCoSQinQoTag.setStatus("mandatory")


class _HzIduCosQueueMapping_Type(DisplayString):
    """Custom type hzIduCosQueueMapping based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 32),
    )


_HzIduCosQueueMapping_Type.__name__ = "DisplayString"
_HzIduCosQueueMapping_Object = MibScalar
hzIduCosQueueMapping = _HzIduCosQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 5),
    _HzIduCosQueueMapping_Type()
)
hzIduCosQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduCosQueueMapping.setStatus("mandatory")


class _HzIduCosExpediteQueue_Type(Integer32):
    """Custom type hzIduCosExpediteQueue based on Integer32"""
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


_HzIduCosExpediteQueue_Type.__name__ = "Integer32"
_HzIduCosExpediteQueue_Object = MibScalar
hzIduCosExpediteQueue = _HzIduCosExpediteQueue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 6),
    _HzIduCosExpediteQueue_Type()
)
hzIduCosExpediteQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduCosExpediteQueue.setStatus("mandatory")


class _HzIduCosQueueCIR_Type(DisplayString):
    """Custom type hzIduCosQueueCIR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzIduCosQueueCIR_Type.__name__ = "DisplayString"
_HzIduCosQueueCIR_Object = MibScalar
hzIduCosQueueCIR = _HzIduCosQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 7),
    _HzIduCosQueueCIR_Type()
)
hzIduCosQueueCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduCosQueueCIR.setStatus("mandatory")


class _HzIduCosQueueCBS_Type(DisplayString):
    """Custom type hzIduCosQueueCBS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzIduCosQueueCBS_Type.__name__ = "DisplayString"
_HzIduCosQueueCBS_Object = MibScalar
hzIduCosQueueCBS = _HzIduCosQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 8),
    _HzIduCosQueueCBS_Type()
)
hzIduCosQueueCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduCosQueueCBS.setStatus("mandatory")


class _HzIduCosDefaultValue_Type(Integer32):
    """Custom type hzIduCosDefaultValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HzIduCosDefaultValue_Type.__name__ = "Integer32"
_HzIduCosDefaultValue_Object = MibScalar
hzIduCosDefaultValue = _HzIduCosDefaultValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 9),
    _HzIduCosDefaultValue_Type()
)
hzIduCosDefaultValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduCosDefaultValue.setStatus("mandatory")


class _HzIduCutThroughProcessing_Type(Integer32):
    """Custom type hzIduCutThroughProcessing based on Integer32"""
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


_HzIduCutThroughProcessing_Type.__name__ = "Integer32"
_HzIduCutThroughProcessing_Object = MibScalar
hzIduCutThroughProcessing = _HzIduCutThroughProcessing_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 10),
    _HzIduCutThroughProcessing_Type()
)
hzIduCutThroughProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduCutThroughProcessing.setStatus("mandatory")


class _HzIduQosPolicy_Type(Integer32):
    """Custom type hzIduQosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict-priority", 1),
          ("wfq", 2))
    )


_HzIduQosPolicy_Type.__name__ = "Integer32"
_HzIduQosPolicy_Object = MibScalar
hzIduQosPolicy = _HzIduQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 11),
    _HzIduQosPolicy_Type()
)
hzIduQosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduQosPolicy.setStatus("mandatory")


class _HzIduCosWfqWeight_Type(DisplayString):
    """Custom type hzIduCosWfqWeight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzIduCosWfqWeight_Type.__name__ = "DisplayString"
_HzIduCosWfqWeight_Object = MibScalar
hzIduCosWfqWeight = _HzIduCosWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 12, 12),
    _HzIduCosWfqWeight_Type()
)
hzIduCosWfqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduCosWfqWeight.setStatus("mandatory")
_HzIduRapidLinkShutdown_ObjectIdentity = ObjectIdentity
hzIduRapidLinkShutdown = _HzIduRapidLinkShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13)
)


class _HzIduRlsEnable_Type(Integer32):
    """Custom type hzIduRlsEnable based on Integer32"""
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


_HzIduRlsEnable_Type.__name__ = "Integer32"
_HzIduRlsEnable_Object = MibScalar
hzIduRlsEnable = _HzIduRlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 1),
    _HzIduRlsEnable_Type()
)
hzIduRlsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsEnable.setStatus("mandatory")


class _HzIduRlsHardFaultMonitor_Type(Integer32):
    """Custom type hzIduRlsHardFaultMonitor based on Integer32"""
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


_HzIduRlsHardFaultMonitor_Type.__name__ = "Integer32"
_HzIduRlsHardFaultMonitor_Object = MibScalar
hzIduRlsHardFaultMonitor = _HzIduRlsHardFaultMonitor_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 2),
    _HzIduRlsHardFaultMonitor_Type()
)
hzIduRlsHardFaultMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsHardFaultMonitor.setStatus("mandatory")


class _HzIduRlsWirelessPortOption_Type(Integer32):
    """Custom type hzIduRlsWirelessPortOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anyport", 1),
          ("bothports", 2))
    )


_HzIduRlsWirelessPortOption_Type.__name__ = "Integer32"
_HzIduRlsWirelessPortOption_Object = MibScalar
hzIduRlsWirelessPortOption = _HzIduRlsWirelessPortOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 3),
    _HzIduRlsWirelessPortOption_Type()
)
hzIduRlsWirelessPortOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsWirelessPortOption.setStatus("mandatory")


class _HzIduRlsAutomaticLinkReestablish_Type(Integer32):
    """Custom type hzIduRlsAutomaticLinkReestablish based on Integer32"""
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


_HzIduRlsAutomaticLinkReestablish_Type.__name__ = "Integer32"
_HzIduRlsAutomaticLinkReestablish_Object = MibScalar
hzIduRlsAutomaticLinkReestablish = _HzIduRlsAutomaticLinkReestablish_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 4),
    _HzIduRlsAutomaticLinkReestablish_Type()
)
hzIduRlsAutomaticLinkReestablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsAutomaticLinkReestablish.setStatus("mandatory")


class _HzIduRlsManualLinkReestablish_Type(Integer32):
    """Custom type hzIduRlsManualLinkReestablish based on Integer32"""
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


_HzIduRlsManualLinkReestablish_Type.__name__ = "Integer32"
_HzIduRlsManualLinkReestablish_Object = MibScalar
hzIduRlsManualLinkReestablish = _HzIduRlsManualLinkReestablish_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 5),
    _HzIduRlsManualLinkReestablish_Type()
)
hzIduRlsManualLinkReestablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsManualLinkReestablish.setStatus("mandatory")


class _HzIduWriteRlsMonitorParametersToSystem_Type(Integer32):
    """Custom type hzIduWriteRlsMonitorParametersToSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_HzIduWriteRlsMonitorParametersToSystem_Type.__name__ = "Integer32"
_HzIduWriteRlsMonitorParametersToSystem_Object = MibScalar
hzIduWriteRlsMonitorParametersToSystem = _HzIduWriteRlsMonitorParametersToSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 6),
    _HzIduWriteRlsMonitorParametersToSystem_Type()
)
hzIduWriteRlsMonitorParametersToSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduWriteRlsMonitorParametersToSystem.setStatus("mandatory")


class _HzIduRlsDroppedFramesThresholdOverride_Type(Integer32):
    """Custom type hzIduRlsDroppedFramesThresholdOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_HzIduRlsDroppedFramesThresholdOverride_Type.__name__ = "Integer32"
_HzIduRlsDroppedFramesThresholdOverride_Object = MibScalar
hzIduRlsDroppedFramesThresholdOverride = _HzIduRlsDroppedFramesThresholdOverride_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 7),
    _HzIduRlsDroppedFramesThresholdOverride_Type()
)
hzIduRlsDroppedFramesThresholdOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsDroppedFramesThresholdOverride.setStatus("mandatory")
_HzIduRlsDroppedFramesThresholdTable_Object = MibTable
hzIduRlsDroppedFramesThresholdTable = _HzIduRlsDroppedFramesThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 8)
)
if mibBuilder.loadTexts:
    hzIduRlsDroppedFramesThresholdTable.setStatus("mandatory")
_HzIduRlsDroppedFramesThresholdEntry_Object = MibTableRow
hzIduRlsDroppedFramesThresholdEntry = _HzIduRlsDroppedFramesThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 8, 1)
)
hzIduRlsDroppedFramesThresholdEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRlsDroppedFramesThresholdIndex"),
)
if mibBuilder.loadTexts:
    hzIduRlsDroppedFramesThresholdEntry.setStatus("mandatory")


class _HzIduRlsDroppedFramesThresholdIndex_Type(Integer32):
    """Custom type hzIduRlsDroppedFramesThresholdIndex based on Integer32"""
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
        *(("queue-1", 1),
          ("queue-2", 2),
          ("queue-3", 3),
          ("queue-4", 4))
    )


_HzIduRlsDroppedFramesThresholdIndex_Type.__name__ = "Integer32"
_HzIduRlsDroppedFramesThresholdIndex_Object = MibTableColumn
hzIduRlsDroppedFramesThresholdIndex = _HzIduRlsDroppedFramesThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 8, 1, 1),
    _HzIduRlsDroppedFramesThresholdIndex_Type()
)
hzIduRlsDroppedFramesThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsDroppedFramesThresholdIndex.setStatus("mandatory")
_HzIduRlsAllowedDroppedFrameRateValue_Type = DisplayString
_HzIduRlsAllowedDroppedFrameRateValue_Object = MibTableColumn
hzIduRlsAllowedDroppedFrameRateValue = _HzIduRlsAllowedDroppedFrameRateValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 8, 1, 2),
    _HzIduRlsAllowedDroppedFrameRateValue_Type()
)
hzIduRlsAllowedDroppedFrameRateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsAllowedDroppedFrameRateValue.setStatus("mandatory")
_HzIduRlsDroppedFrameMonitorPeriod_Type = Integer32
_HzIduRlsDroppedFrameMonitorPeriod_Object = MibTableColumn
hzIduRlsDroppedFrameMonitorPeriod = _HzIduRlsDroppedFrameMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 8, 1, 3),
    _HzIduRlsDroppedFrameMonitorPeriod_Type()
)
hzIduRlsDroppedFrameMonitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsDroppedFrameMonitorPeriod.setStatus("mandatory")
_HzIduRlsSoftFaultMonitorTable_Object = MibTable
hzIduRlsSoftFaultMonitorTable = _HzIduRlsSoftFaultMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 9)
)
if mibBuilder.loadTexts:
    hzIduRlsSoftFaultMonitorTable.setStatus("mandatory")
_HzIduRlsSoftFaultMonitorEntry_Object = MibTableRow
hzIduRlsSoftFaultMonitorEntry = _HzIduRlsSoftFaultMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 9, 1)
)
hzIduRlsSoftFaultMonitorEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRlsSoftFaultMonitorIndex"),
)
if mibBuilder.loadTexts:
    hzIduRlsSoftFaultMonitorEntry.setStatus("mandatory")


class _HzIduRlsSoftFaultMonitorIndex_Type(Integer32):
    """Custom type hzIduRlsSoftFaultMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduRlsSoftFaultMonitorIndex_Type.__name__ = "Integer32"
_HzIduRlsSoftFaultMonitorIndex_Object = MibTableColumn
hzIduRlsSoftFaultMonitorIndex = _HzIduRlsSoftFaultMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 9, 1, 1),
    _HzIduRlsSoftFaultMonitorIndex_Type()
)
hzIduRlsSoftFaultMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsSoftFaultMonitorIndex.setStatus("mandatory")
_HzIduRlsEstablishErredFrameThreshold_Type = Integer32
_HzIduRlsEstablishErredFrameThreshold_Object = MibTableColumn
hzIduRlsEstablishErredFrameThreshold = _HzIduRlsEstablishErredFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 9, 1, 2),
    _HzIduRlsEstablishErredFrameThreshold_Type()
)
hzIduRlsEstablishErredFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsEstablishErredFrameThreshold.setStatus("mandatory")
_HzIduRlsShutdownErredFrameThreshold_Type = Integer32
_HzIduRlsShutdownErredFrameThreshold_Object = MibTableColumn
hzIduRlsShutdownErredFrameThreshold = _HzIduRlsShutdownErredFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 9, 1, 3),
    _HzIduRlsShutdownErredFrameThreshold_Type()
)
hzIduRlsShutdownErredFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsShutdownErredFrameThreshold.setStatus("mandatory")
_HzIduRlsEstablishNumberOfSamples_Type = Integer32
_HzIduRlsEstablishNumberOfSamples_Object = MibTableColumn
hzIduRlsEstablishNumberOfSamples = _HzIduRlsEstablishNumberOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 9, 1, 4),
    _HzIduRlsEstablishNumberOfSamples_Type()
)
hzIduRlsEstablishNumberOfSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsEstablishNumberOfSamples.setStatus("mandatory")
_HzIduRlsShutdownNumberOfSamples_Type = Integer32
_HzIduRlsShutdownNumberOfSamples_Object = MibTableColumn
hzIduRlsShutdownNumberOfSamples = _HzIduRlsShutdownNumberOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 9, 1, 5),
    _HzIduRlsShutdownNumberOfSamples_Type()
)
hzIduRlsShutdownNumberOfSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsShutdownNumberOfSamples.setStatus("mandatory")
_HzIduRlsEstablishSamplePeriod_Type = Integer32
_HzIduRlsEstablishSamplePeriod_Object = MibTableColumn
hzIduRlsEstablishSamplePeriod = _HzIduRlsEstablishSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 9, 1, 6),
    _HzIduRlsEstablishSamplePeriod_Type()
)
hzIduRlsEstablishSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsEstablishSamplePeriod.setStatus("mandatory")
_HzIduRlsShutdownSamplePeriod_Type = Integer32
_HzIduRlsShutdownSamplePeriod_Object = MibTableColumn
hzIduRlsShutdownSamplePeriod = _HzIduRlsShutdownSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 9, 1, 7),
    _HzIduRlsShutdownSamplePeriod_Type()
)
hzIduRlsShutdownSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsShutdownSamplePeriod.setStatus("mandatory")
_HzIduRlsQuickShutdownSamplePeriod_Type = Integer32
_HzIduRlsQuickShutdownSamplePeriod_Object = MibTableColumn
hzIduRlsQuickShutdownSamplePeriod = _HzIduRlsQuickShutdownSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 9, 1, 8),
    _HzIduRlsQuickShutdownSamplePeriod_Type()
)
hzIduRlsQuickShutdownSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsQuickShutdownSamplePeriod.setStatus("mandatory")
_HzIduHardFaultMonitorTable_Object = MibTable
hzIduHardFaultMonitorTable = _HzIduHardFaultMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 10)
)
if mibBuilder.loadTexts:
    hzIduHardFaultMonitorTable.setStatus("mandatory")
_HzIduHardFaultMonitorEntry_Object = MibTableRow
hzIduHardFaultMonitorEntry = _HzIduHardFaultMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 10, 1)
)
hzIduHardFaultMonitorEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduHardFaultMonitorIndex"),
)
if mibBuilder.loadTexts:
    hzIduHardFaultMonitorEntry.setStatus("mandatory")


class _HzIduHardFaultMonitorIndex_Type(Integer32):
    """Custom type hzIduHardFaultMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduHardFaultMonitorIndex_Type.__name__ = "Integer32"
_HzIduHardFaultMonitorIndex_Object = MibTableColumn
hzIduHardFaultMonitorIndex = _HzIduHardFaultMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 10, 1, 1),
    _HzIduHardFaultMonitorIndex_Type()
)
hzIduHardFaultMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduHardFaultMonitorIndex.setStatus("mandatory")
_HzIduRlsHardFaultSamplePeriod_Type = Integer32
_HzIduRlsHardFaultSamplePeriod_Object = MibTableColumn
hzIduRlsHardFaultSamplePeriod = _HzIduRlsHardFaultSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 10, 1, 2),
    _HzIduRlsHardFaultSamplePeriod_Type()
)
hzIduRlsHardFaultSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsHardFaultSamplePeriod.setStatus("mandatory")
_HzIduRlsHardFaultThreshold_Type = Integer32
_HzIduRlsHardFaultThreshold_Object = MibTableColumn
hzIduRlsHardFaultThreshold = _HzIduRlsHardFaultThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 10, 1, 3),
    _HzIduRlsHardFaultThreshold_Type()
)
hzIduRlsHardFaultThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsHardFaultThreshold.setStatus("mandatory")
_HzIduRlsReceiveSignalLevelMonitorTable_Object = MibTable
hzIduRlsReceiveSignalLevelMonitorTable = _HzIduRlsReceiveSignalLevelMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 11)
)
if mibBuilder.loadTexts:
    hzIduRlsReceiveSignalLevelMonitorTable.setStatus("mandatory")
_HzIduRlsReceiveSignalLevelMonitorEntry_Object = MibTableRow
hzIduRlsReceiveSignalLevelMonitorEntry = _HzIduRlsReceiveSignalLevelMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 11, 1)
)
hzIduRlsReceiveSignalLevelMonitorEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRlsReceiveSignalLevelMonitorIndex"),
)
if mibBuilder.loadTexts:
    hzIduRlsReceiveSignalLevelMonitorEntry.setStatus("mandatory")


class _HzIduRlsReceiveSignalLevelMonitorIndex_Type(Integer32):
    """Custom type hzIduRlsReceiveSignalLevelMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduRlsReceiveSignalLevelMonitorIndex_Type.__name__ = "Integer32"
_HzIduRlsReceiveSignalLevelMonitorIndex_Object = MibTableColumn
hzIduRlsReceiveSignalLevelMonitorIndex = _HzIduRlsReceiveSignalLevelMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 11, 1, 1),
    _HzIduRlsReceiveSignalLevelMonitorIndex_Type()
)
hzIduRlsReceiveSignalLevelMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsReceiveSignalLevelMonitorIndex.setStatus("mandatory")


class _HzIduRlsMakeRslMonitorRslValue_Type(DisplayString):
    """Custom type hzIduRlsMakeRslMonitorRslValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzIduRlsMakeRslMonitorRslValue_Type.__name__ = "DisplayString"
_HzIduRlsMakeRslMonitorRslValue_Object = MibTableColumn
hzIduRlsMakeRslMonitorRslValue = _HzIduRlsMakeRslMonitorRslValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 11, 1, 2),
    _HzIduRlsMakeRslMonitorRslValue_Type()
)
hzIduRlsMakeRslMonitorRslValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsMakeRslMonitorRslValue.setStatus("mandatory")
_HzIduRlsMakeRslMonitorPeriod_Type = Integer32
_HzIduRlsMakeRslMonitorPeriod_Object = MibTableColumn
hzIduRlsMakeRslMonitorPeriod = _HzIduRlsMakeRslMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 11, 1, 3),
    _HzIduRlsMakeRslMonitorPeriod_Type()
)
hzIduRlsMakeRslMonitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRlsMakeRslMonitorPeriod.setStatus("mandatory")
_HzIduRlsStatus_ObjectIdentity = ObjectIdentity
hzIduRlsStatus = _HzIduRlsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12)
)
_HzIduRlsCurrentDroppedFramesTable_Object = MibTable
hzIduRlsCurrentDroppedFramesTable = _HzIduRlsCurrentDroppedFramesTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 1)
)
if mibBuilder.loadTexts:
    hzIduRlsCurrentDroppedFramesTable.setStatus("mandatory")
_HzIduRlsCurrentDroppedFramesEntry_Object = MibTableRow
hzIduRlsCurrentDroppedFramesEntry = _HzIduRlsCurrentDroppedFramesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 1, 1)
)
hzIduRlsCurrentDroppedFramesEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRlsCurrentDroppedFramesIndex"),
)
if mibBuilder.loadTexts:
    hzIduRlsCurrentDroppedFramesEntry.setStatus("mandatory")


class _HzIduRlsCurrentDroppedFramesIndex_Type(Integer32):
    """Custom type hzIduRlsCurrentDroppedFramesIndex based on Integer32"""
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
        *(("queue-1", 1),
          ("queue-2", 2),
          ("queue-3", 3),
          ("queue-4", 4))
    )


_HzIduRlsCurrentDroppedFramesIndex_Type.__name__ = "Integer32"
_HzIduRlsCurrentDroppedFramesIndex_Object = MibTableColumn
hzIduRlsCurrentDroppedFramesIndex = _HzIduRlsCurrentDroppedFramesIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 1, 1, 1),
    _HzIduRlsCurrentDroppedFramesIndex_Type()
)
hzIduRlsCurrentDroppedFramesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsCurrentDroppedFramesIndex.setStatus("mandatory")
_HzIduRlsCurrentDroppedFramesRateValue_Type = DisplayString
_HzIduRlsCurrentDroppedFramesRateValue_Object = MibTableColumn
hzIduRlsCurrentDroppedFramesRateValue = _HzIduRlsCurrentDroppedFramesRateValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 1, 1, 2),
    _HzIduRlsCurrentDroppedFramesRateValue_Type()
)
hzIduRlsCurrentDroppedFramesRateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsCurrentDroppedFramesRateValue.setStatus("mandatory")
_HzIduRlsCurrentDroppedFrameMonitorPeriod_Type = Integer32
_HzIduRlsCurrentDroppedFrameMonitorPeriod_Object = MibTableColumn
hzIduRlsCurrentDroppedFrameMonitorPeriod = _HzIduRlsCurrentDroppedFrameMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 1, 1, 3),
    _HzIduRlsCurrentDroppedFrameMonitorPeriod_Type()
)
hzIduRlsCurrentDroppedFrameMonitorPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsCurrentDroppedFrameMonitorPeriod.setStatus("mandatory")
_HzIduRlsCurrentQueueStatus_Type = DisplayString
_HzIduRlsCurrentQueueStatus_Object = MibTableColumn
hzIduRlsCurrentQueueStatus = _HzIduRlsCurrentQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 1, 1, 4),
    _HzIduRlsCurrentQueueStatus_Type()
)
hzIduRlsCurrentQueueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsCurrentQueueStatus.setStatus("mandatory")
_HzIduRlsStatusTable_Object = MibTable
hzIduRlsStatusTable = _HzIduRlsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2)
)
if mibBuilder.loadTexts:
    hzIduRlsStatusTable.setStatus("mandatory")
_HzIduRlsStatusEntry_Object = MibTableRow
hzIduRlsStatusEntry = _HzIduRlsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1)
)
hzIduRlsStatusEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRlsStatusIndex"),
)
if mibBuilder.loadTexts:
    hzIduRlsStatusEntry.setStatus("mandatory")


class _HzIduRlsStatusIndex_Type(Integer32):
    """Custom type hzIduRlsStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzIduRlsStatusIndex_Type.__name__ = "Integer32"
_HzIduRlsStatusIndex_Object = MibTableColumn
hzIduRlsStatusIndex = _HzIduRlsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 1),
    _HzIduRlsStatusIndex_Type()
)
hzIduRlsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsStatusIndex.setStatus("mandatory")
_HzIduRlsOption_Type = DisplayString
_HzIduRlsOption_Object = MibTableColumn
hzIduRlsOption = _HzIduRlsOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 2),
    _HzIduRlsOption_Type()
)
hzIduRlsOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsOption.setStatus("mandatory")
_HzIduRlsState_Type = DisplayString
_HzIduRlsState_Object = MibTableColumn
hzIduRlsState = _HzIduRlsState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 3),
    _HzIduRlsState_Type()
)
hzIduRlsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsState.setStatus("mandatory")
_HzIduRlsMismatchState_Type = DisplayString
_HzIduRlsMismatchState_Object = MibTableColumn
hzIduRlsMismatchState = _HzIduRlsMismatchState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 4),
    _HzIduRlsMismatchState_Type()
)
hzIduRlsMismatchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRlsMismatchState.setStatus("mandatory")
_HzIduDegradeMonitorState_Type = DisplayString
_HzIduDegradeMonitorState_Object = MibTableColumn
hzIduDegradeMonitorState = _HzIduDegradeMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 5),
    _HzIduDegradeMonitorState_Type()
)
hzIduDegradeMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduDegradeMonitorState.setStatus("mandatory")
_HzIduHardFaultMonitorState_Type = DisplayString
_HzIduHardFaultMonitorState_Object = MibTableColumn
hzIduHardFaultMonitorState = _HzIduHardFaultMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 6),
    _HzIduHardFaultMonitorState_Type()
)
hzIduHardFaultMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduHardFaultMonitorState.setStatus("mandatory")
_HzIduMakeRslThresholdState_Type = DisplayString
_HzIduMakeRslThresholdState_Object = MibTableColumn
hzIduMakeRslThresholdState = _HzIduMakeRslThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 7),
    _HzIduMakeRslThresholdState_Type()
)
hzIduMakeRslThresholdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduMakeRslThresholdState.setStatus("mandatory")
_HzIduPeerRlsState_Type = DisplayString
_HzIduPeerRlsState_Object = MibTableColumn
hzIduPeerRlsState = _HzIduPeerRlsState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 8),
    _HzIduPeerRlsState_Type()
)
hzIduPeerRlsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduPeerRlsState.setStatus("mandatory")
_HzIduRadioInterfaceState_Type = DisplayString
_HzIduRadioInterfaceState_Object = MibTableColumn
hzIduRadioInterfaceState = _HzIduRadioInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 9),
    _HzIduRadioInterfaceState_Type()
)
hzIduRadioInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadioInterfaceState.setStatus("mandatory")
_HzIduNetworkInterfaceState_Type = DisplayString
_HzIduNetworkInterfaceState_Object = MibTableColumn
hzIduNetworkInterfaceState = _HzIduNetworkInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 10),
    _HzIduNetworkInterfaceState_Type()
)
hzIduNetworkInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduNetworkInterfaceState.setStatus("mandatory")
_HzIduUserConfiguredEstablishFer_Type = DisplayString
_HzIduUserConfiguredEstablishFer_Object = MibTableColumn
hzIduUserConfiguredEstablishFer = _HzIduUserConfiguredEstablishFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 11),
    _HzIduUserConfiguredEstablishFer_Type()
)
hzIduUserConfiguredEstablishFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduUserConfiguredEstablishFer.setStatus("mandatory")
_HzIduMinimumAchievableEstablishFer_Type = DisplayString
_HzIduMinimumAchievableEstablishFer_Object = MibTableColumn
hzIduMinimumAchievableEstablishFer = _HzIduMinimumAchievableEstablishFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 12),
    _HzIduMinimumAchievableEstablishFer_Type()
)
hzIduMinimumAchievableEstablishFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduMinimumAchievableEstablishFer.setStatus("mandatory")
_HzIduUserConfiguredShutdownFer_Type = DisplayString
_HzIduUserConfiguredShutdownFer_Object = MibTableColumn
hzIduUserConfiguredShutdownFer = _HzIduUserConfiguredShutdownFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 13),
    _HzIduUserConfiguredShutdownFer_Type()
)
hzIduUserConfiguredShutdownFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduUserConfiguredShutdownFer.setStatus("mandatory")
_HzIduMinimumAchievableShutdownFer_Type = DisplayString
_HzIduMinimumAchievableShutdownFer_Object = MibTableColumn
hzIduMinimumAchievableShutdownFer = _HzIduMinimumAchievableShutdownFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 14),
    _HzIduMinimumAchievableShutdownFer_Type()
)
hzIduMinimumAchievableShutdownFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduMinimumAchievableShutdownFer.setStatus("mandatory")
_HzIduUserConfiguredEstablishMonitorTime_Type = Integer32
_HzIduUserConfiguredEstablishMonitorTime_Object = MibTableColumn
hzIduUserConfiguredEstablishMonitorTime = _HzIduUserConfiguredEstablishMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 15),
    _HzIduUserConfiguredEstablishMonitorTime_Type()
)
hzIduUserConfiguredEstablishMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduUserConfiguredEstablishMonitorTime.setStatus("mandatory")
_HzIduActualEstablishMonitorTime_Type = Integer32
_HzIduActualEstablishMonitorTime_Object = MibTableColumn
hzIduActualEstablishMonitorTime = _HzIduActualEstablishMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 16),
    _HzIduActualEstablishMonitorTime_Type()
)
hzIduActualEstablishMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduActualEstablishMonitorTime.setStatus("mandatory")
_HzIduUserConfiguredShutdownMonitorTime_Type = Integer32
_HzIduUserConfiguredShutdownMonitorTime_Object = MibTableColumn
hzIduUserConfiguredShutdownMonitorTime = _HzIduUserConfiguredShutdownMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 17),
    _HzIduUserConfiguredShutdownMonitorTime_Type()
)
hzIduUserConfiguredShutdownMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduUserConfiguredShutdownMonitorTime.setStatus("mandatory")
_HzIduActualShutdownMonitorTime_Type = Integer32
_HzIduActualShutdownMonitorTime_Object = MibTableColumn
hzIduActualShutdownMonitorTime = _HzIduActualShutdownMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 13, 12, 2, 1, 18),
    _HzIduActualShutdownMonitorTime_Type()
)
hzIduActualShutdownMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduActualShutdownMonitorTime.setStatus("mandatory")
_HzIduSntp_ObjectIdentity = ObjectIdentity
hzIduSntp = _HzIduSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 14)
)


class _HzIduSntpEnable_Type(Integer32):
    """Custom type hzIduSntpEnable based on Integer32"""
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


_HzIduSntpEnable_Type.__name__ = "Integer32"
_HzIduSntpEnable_Object = MibScalar
hzIduSntpEnable = _HzIduSntpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 14, 1),
    _HzIduSntpEnable_Type()
)
hzIduSntpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduSntpEnable.setStatus("mandatory")


class _HzIduSntpOffset_Type(Integer32):
    """Custom type hzIduSntpOffset based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 140),
    )


_HzIduSntpOffset_Type.__name__ = "Integer32"
_HzIduSntpOffset_Object = MibScalar
hzIduSntpOffset = _HzIduSntpOffset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 14, 2),
    _HzIduSntpOffset_Type()
)
hzIduSntpOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduSntpOffset.setStatus("mandatory")
_HzIduSntpServerTable_Object = MibTable
hzIduSntpServerTable = _HzIduSntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 14, 3)
)
if mibBuilder.loadTexts:
    hzIduSntpServerTable.setStatus("mandatory")
_HzIduSntpServerEntry_Object = MibTableRow
hzIduSntpServerEntry = _HzIduSntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 14, 3, 1)
)
hzIduSntpServerEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduSntpServerIndex"),
)
if mibBuilder.loadTexts:
    hzIduSntpServerEntry.setStatus("mandatory")
_HzIduSntpServerIndex_Type = Integer32
_HzIduSntpServerIndex_Object = MibTableColumn
hzIduSntpServerIndex = _HzIduSntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 14, 3, 1, 1),
    _HzIduSntpServerIndex_Type()
)
hzIduSntpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSntpServerIndex.setStatus("mandatory")
_HzIduSntpServerIpAddress_Type = IpAddress
_HzIduSntpServerIpAddress_Object = MibTableColumn
hzIduSntpServerIpAddress = _HzIduSntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 14, 3, 1, 2),
    _HzIduSntpServerIpAddress_Type()
)
hzIduSntpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduSntpServerIpAddress.setStatus("mandatory")


class _HzIduSntpServerStatus_Type(Integer32):
    """Custom type hzIduSntpServerStatus based on Integer32"""
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


_HzIduSntpServerStatus_Type.__name__ = "Integer32"
_HzIduSntpServerStatus_Object = MibTableColumn
hzIduSntpServerStatus = _HzIduSntpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 14, 3, 1, 3),
    _HzIduSntpServerStatus_Type()
)
hzIduSntpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSntpServerStatus.setStatus("mandatory")
_HzIduSntpServerStratum_Type = Integer32
_HzIduSntpServerStratum_Object = MibTableColumn
hzIduSntpServerStratum = _HzIduSntpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 14, 3, 1, 4),
    _HzIduSntpServerStratum_Type()
)
hzIduSntpServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduSntpServerStratum.setStatus("mandatory")
_HzIduLogs_ObjectIdentity = ObjectIdentity
hzIduLogs = _HzIduLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 15)
)


class _HzIduEventLogEnable_Type(Integer32):
    """Custom type hzIduEventLogEnable based on Integer32"""
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


_HzIduEventLogEnable_Type.__name__ = "Integer32"
_HzIduEventLogEnable_Object = MibScalar
hzIduEventLogEnable = _HzIduEventLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 15, 1),
    _HzIduEventLogEnable_Type()
)
hzIduEventLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduEventLogEnable.setStatus("mandatory")


class _HzIduPerfmLogEnable_Type(Integer32):
    """Custom type hzIduPerfmLogEnable based on Integer32"""
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


_HzIduPerfmLogEnable_Type.__name__ = "Integer32"
_HzIduPerfmLogEnable_Object = MibScalar
hzIduPerfmLogEnable = _HzIduPerfmLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 15, 2),
    _HzIduPerfmLogEnable_Type()
)
hzIduPerfmLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduPerfmLogEnable.setStatus("mandatory")


class _HzIduPerfmLogInterval_Type(DisplayString):
    """Custom type hzIduPerfmLogInterval based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HzIduPerfmLogInterval_Type.__name__ = "DisplayString"
_HzIduPerfmLogInterval_Object = MibScalar
hzIduPerfmLogInterval = _HzIduPerfmLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 15, 3),
    _HzIduPerfmLogInterval_Type()
)
hzIduPerfmLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduPerfmLogInterval.setStatus("mandatory")
_HzIduRadius_ObjectIdentity = ObjectIdentity
hzIduRadius = _HzIduRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 16)
)


class _HzIduRadiusSuperUserAuthentication_Type(Integer32):
    """Custom type hzIduRadiusSuperUserAuthentication based on Integer32"""
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


_HzIduRadiusSuperUserAuthentication_Type.__name__ = "Integer32"
_HzIduRadiusSuperUserAuthentication_Object = MibScalar
hzIduRadiusSuperUserAuthentication = _HzIduRadiusSuperUserAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 16, 1),
    _HzIduRadiusSuperUserAuthentication_Type()
)
hzIduRadiusSuperUserAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadiusSuperUserAuthentication.setStatus("mandatory")


class _HzIduRadiusServerTimeOut_Type(Integer32):
    """Custom type hzIduRadiusServerTimeOut based on Integer32"""
    defaultValue = 0


_HzIduRadiusServerTimeOut_Type.__name__ = "Integer32"
_HzIduRadiusServerTimeOut_Object = MibScalar
hzIduRadiusServerTimeOut = _HzIduRadiusServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 16, 2),
    _HzIduRadiusServerTimeOut_Type()
)
hzIduRadiusServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadiusServerTimeOut.setStatus("mandatory")


class _HzIduRadiusServerDeadTime_Type(Integer32):
    """Custom type hzIduRadiusServerDeadTime based on Integer32"""
    defaultValue = 0


_HzIduRadiusServerDeadTime_Type.__name__ = "Integer32"
_HzIduRadiusServerDeadTime_Object = MibScalar
hzIduRadiusServerDeadTime = _HzIduRadiusServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 16, 3),
    _HzIduRadiusServerDeadTime_Type()
)
hzIduRadiusServerDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadiusServerDeadTime.setStatus("mandatory")
_HzIduRadiusServerReTransmit_Type = Integer32
_HzIduRadiusServerReTransmit_Object = MibScalar
hzIduRadiusServerReTransmit = _HzIduRadiusServerReTransmit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 16, 4),
    _HzIduRadiusServerReTransmit_Type()
)
hzIduRadiusServerReTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadiusServerReTransmit.setStatus("mandatory")
_HzIduRadiusServerTable_Object = MibTable
hzIduRadiusServerTable = _HzIduRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 16, 5)
)
if mibBuilder.loadTexts:
    hzIduRadiusServerTable.setStatus("mandatory")
_HzIduRadiusServerEntry_Object = MibTableRow
hzIduRadiusServerEntry = _HzIduRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 16, 5, 1)
)
hzIduRadiusServerEntry.setIndexNames(
    (0, "DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    hzIduRadiusServerEntry.setStatus("mandatory")
_HzIduRadiusServerIndex_Type = Integer32
_HzIduRadiusServerIndex_Object = MibTableColumn
hzIduRadiusServerIndex = _HzIduRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 16, 5, 1, 1),
    _HzIduRadiusServerIndex_Type()
)
hzIduRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadiusServerIndex.setStatus("mandatory")
_HzIduRadiusCfgdHostIpAddress_Type = IpAddress
_HzIduRadiusCfgdHostIpAddress_Object = MibTableColumn
hzIduRadiusCfgdHostIpAddress = _HzIduRadiusCfgdHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 16, 5, 1, 2),
    _HzIduRadiusCfgdHostIpAddress_Type()
)
hzIduRadiusCfgdHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzIduRadiusCfgdHostIpAddress.setStatus("mandatory")
_HzIduRadiusActiveHostIpAddress_Type = IpAddress
_HzIduRadiusActiveHostIpAddress_Object = MibTableColumn
hzIduRadiusActiveHostIpAddress = _HzIduRadiusActiveHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 16, 5, 1, 3),
    _HzIduRadiusActiveHostIpAddress_Type()
)
hzIduRadiusActiveHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzIduRadiusActiveHostIpAddress.setStatus("mandatory")

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

hzIduExplicitAuthenticationFailureV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 3)
)
if mibBuilder.loadTexts:
    hzIduExplicitAuthenticationFailureV1Trap.setStatus(
        ""
    )

hzIduExplicitAuthenticationFailureClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 4)
)
if mibBuilder.loadTexts:
    hzIduExplicitAuthenticationFailureClearedV1Trap.setStatus(
        ""
    )

hzIduAamConfigMisMatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 5)
)
hzIduAamConfigMisMatchV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduAamConfigMisMatchV1Trap.setStatus(
        ""
    )

hzIduAamConfigMisMatchClearV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 6)
)
hzIduAamConfigMisMatchClearV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduAamConfigMisMatchClearV1Trap.setStatus(
        ""
    )

hzIduAamActiveV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 7)
)
if mibBuilder.loadTexts:
    hzIduAamActiveV1Trap.setStatus(
        ""
    )

hzIduAamActiveClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 8)
)
if mibBuilder.loadTexts:
    hzIduAamActiveClearedV1Trap.setStatus(
        ""
    )

hzIduAtpcConfigMismatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 9)
)
if mibBuilder.loadTexts:
    hzIduAtpcConfigMismatchV1Trap.setStatus(
        ""
    )

hzIduAtpcConfigMismatchClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 10)
)
if mibBuilder.loadTexts:
    hzIduAtpcConfigMismatchClearedV1Trap.setStatus(
        ""
    )

hzIduSntpServersUnreachableV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 11)
)
if mibBuilder.loadTexts:
    hzIduSntpServersUnreachableV1Trap.setStatus(
        ""
    )

hzIduSntpServersUnreachableClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 12)
)
if mibBuilder.loadTexts:
    hzIduSntpServersUnreachableClearedV1Trap.setStatus(
        ""
    )

hzIduFrequencyFileInvalidV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 13)
)
if mibBuilder.loadTexts:
    hzIduFrequencyFileInvalidV1Trap.setStatus(
        ""
    )

hzIduEnetPort1DroppedFramesThresholdExceededV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 14)
)
if mibBuilder.loadTexts:
    hzIduEnetPort1DroppedFramesThresholdExceededV1Trap.setStatus(
        ""
    )

hzIduEnetPort1DroppedFramesThresholdExceededClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 15)
)
if mibBuilder.loadTexts:
    hzIduEnetPort1DroppedFramesThresholdExceededClearedV1Trap.setStatus(
        ""
    )

hzIduEnetPort1BwUtilizationThresholdExceededV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 16)
)
if mibBuilder.loadTexts:
    hzIduEnetPort1BwUtilizationThresholdExceededV1Trap.setStatus(
        ""
    )

hzIduEnetPort1BwUtilizationThresholdExceededClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 17)
)
if mibBuilder.loadTexts:
    hzIduEnetPort1BwUtilizationThresholdExceededClearedV1Trap.setStatus(
        ""
    )

hzIduEnetPort1RlsMismatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 18)
)
if mibBuilder.loadTexts:
    hzIduEnetPort1RlsMismatchV1Trap.setStatus(
        ""
    )

hzIduEnetPort1RlsMismatchClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 19)
)
if mibBuilder.loadTexts:
    hzIduEnetPort1RlsMismatchClearedV1Trap.setStatus(
        ""
    )

hzIduRlsQueueBasedShutdownActivatedv1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 20)
)
if mibBuilder.loadTexts:
    hzIduRlsQueueBasedShutdownActivatedv1Trap.setStatus(
        ""
    )

hzIduRlsQueueBasedShutdownActivatedClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 21)
)
if mibBuilder.loadTexts:
    hzIduRlsQueueBasedShutdownActivatedClearedV1Trap.setStatus(
        ""
    )

hzIduModemRxLossOfSignalLockV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 22)
)
hzIduModemRxLossOfSignalLockV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemRxLossOfSignalLockV1Trap.setStatus(
        ""
    )

hzIduModemRxLossOfSignalLockClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 23)
)
hzIduModemRxLossOfSignalLockClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemRxLossOfSignalLockClearedV1Trap.setStatus(
        ""
    )

hzIduModemTxLossOfSyncV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 24)
)
hzIduModemTxLossOfSyncV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemTxLossOfSyncV1Trap.setStatus(
        ""
    )

hzIduModemTxLossOfSyncClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 25)
)
hzIduModemTxLossOfSyncClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemTxLossOfSyncClearedV1Trap.setStatus(
        ""
    )

hzIduModemSnrBelowThresholdV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 26)
)
hzIduModemSnrBelowThresholdV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemSnrBelowThresholdV1Trap.setStatus(
        ""
    )

hzIduModemSnrBelowThresholdClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 27)
)
hzIduModemSnrBelowThresholdClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemSnrBelowThresholdClearedV1Trap.setStatus(
        ""
    )

hzIduModemEqualizerStressExceedThresholdV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 28)
)
hzIduModemEqualizerStressExceedThresholdV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemEqualizerStressExceedThresholdV1Trap.setStatus(
        ""
    )

hzIduModemEqualizerStressExceedThresholdClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 29)
)
hzIduModemEqualizerStressExceedThresholdClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemEqualizerStressExceedThresholdClearedV1Trap.setStatus(
        ""
    )

hzIduEnetPort1ChannelizedRslBelowThresholdV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 30)
)
if mibBuilder.loadTexts:
    hzIduEnetPort1ChannelizedRslBelowThresholdV1Trap.setStatus(
        ""
    )

hzIduEnetPort1ChannelizedRslBelowThresholdClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 31)
)
if mibBuilder.loadTexts:
    hzIduEnetPort1ChannelizedRslBelowThresholdClearedV1Trap.setStatus(
        ""
    )

hzIduModemHardwareFaultV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 32)
)
hzIduModemHardwareFaultV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemHardwareFaultV1Trap.setStatus(
        ""
    )

hzIduModemHardwareFaultClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 33)
)
hzIduModemHardwareFaultClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemHardwareFaultClearedV1Trap.setStatus(
        ""
    )

hzIduModemProgrammingErrorV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 34)
)
hzIduModemProgrammingErrorV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemProgrammingErrorV1Trap.setStatus(
        ""
    )

hzIduModemProgrammingErrorClearedrV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 35)
)
hzIduModemProgrammingErrorClearedrV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduModemProgrammingErrorClearedrV1Trap.setStatus(
        ""
    )

hzIduTtySessionCommencedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 36)
)
hzIduTtySessionCommencedV1Trap.setObjects(
      *(("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduTtySessionUserName"),
        ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduTtySessionUserConnectionType"))
)
if mibBuilder.loadTexts:
    hzIduTtySessionCommencedV1Trap.setStatus(
        ""
    )

hzIduTtySessionTerminatedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 37)
)
hzIduTtySessionTerminatedV1Trap.setObjects(
      *(("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduTtySessionUserName"),
        ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduTtySessionUserConnectionType"))
)
if mibBuilder.loadTexts:
    hzIduTtySessionTerminatedV1Trap.setStatus(
        ""
    )

hzIduAtpcTxAtMaxPwrV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 38)
)
hzIduAtpcTxAtMaxPwrV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduAtpcTxAtMaxPwrV1Trap.setStatus(
        ""
    )

hzIduAtpcTxAtMaxPwrClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 39)
)
hzIduAtpcTxAtMaxPwrClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduAtpcTxAtMaxPwrClearedV1Trap.setStatus(
        ""
    )

hzIduRadioPLDROLostLockV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 40)
)
hzIduRadioPLDROLostLockV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioPLDROLostLockV1Trap.setStatus(
        ""
    )

hzIduRadioPLDROLostLockClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 41)
)
hzIduRadioPLDROLostLockClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioPLDROLostLockClearedV1Trap.setStatus(
        ""
    )

hzIduRadioLostCommunicationV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 42)
)
hzIduRadioLostCommunicationV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioLostCommunicationV1Trap.setStatus(
        ""
    )

hzIduRadioLostCommunicationClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 43)
)
hzIduRadioLostCommunicationClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioLostCommunicationClearedV1Trap.setStatus(
        ""
    )

hzIduRadioMismatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 44)
)
hzIduRadioMismatchV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioMismatchV1Trap.setStatus(
        ""
    )

hzIduRadioMismatchClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 45)
)
hzIduRadioMismatchClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioMismatchClearedV1Trap.setStatus(
        ""
    )

hzIduRadioPowerAmpV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 46)
)
hzIduRadioPowerAmpV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioPowerAmpV1Trap.setStatus(
        ""
    )

hzIduRadioPowerAmpClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 47)
)
hzIduRadioPowerAmpClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioPowerAmpClearedV1Trap.setStatus(
        ""
    )

hzIduRadioExcessiveTxCableLossV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 48)
)
hzIduRadioExcessiveTxCableLossV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioExcessiveTxCableLossV1Trap.setStatus(
        ""
    )

hzIduRadioExcessiveTxCableLossClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 49)
)
hzIduRadioExcessiveTxCableLossClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioExcessiveTxCableLossClearedV1Trap.setStatus(
        ""
    )

hzIduHiPowerRadioDrainM1V1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 50)
)
hzIduHiPowerRadioDrainM1V1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduHiPowerRadioDrainM1V1Trap.setStatus(
        ""
    )

hzIduHiPowerRadioDrainM1ClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 51)
)
hzIduHiPowerRadioDrainM1ClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduHiPowerRadioDrainM1ClearedV1Trap.setStatus(
        ""
    )

hzIduHiPowerRadioDrainM2V1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 52)
)
hzIduHiPowerRadioDrainM2V1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduHiPowerRadioDrainM2V1Trap.setStatus(
        ""
    )

hzIduHiPowerRadioDrainM2ClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 53)
)
hzIduHiPowerRadioDrainM2ClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduHiPowerRadioDrainM2ClearedV1Trap.setStatus(
        ""
    )

hzIduHiPowerRadioTxDetectorV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 54)
)
hzIduHiPowerRadioTxDetectorV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduHiPowerRadioTxDetectorV1Trap.setStatus(
        ""
    )

hzIduHiPowerRadioTxDetectorClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 55)
)
hzIduHiPowerRadioTxDetectorClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduHiPowerRadioTxDetectorClearedV1Trap.setStatus(
        ""
    )

hzIduSecondaryRadioIsActiveV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 56)
)
hzIduSecondaryRadioIsActiveV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduSecondaryRadioIsActiveV1Trap.setStatus(
        ""
    )

hzIduSecondaryRadioIsActiveClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 57)
)
hzIduSecondaryRadioIsActiveClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduSecondaryRadioIsActiveClearedV1Trap.setStatus(
        ""
    )

hzIduRedundancySerialNumberMisMatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 58)
)
hzIduRedundancySerialNumberMisMatchV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRedundancySerialNumberMisMatchV1Trap.setStatus(
        ""
    )

hzIduRedundancySerialNumberMisMatchClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 59)
)
hzIduRedundancySerialNumberMisMatchClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRedundancySerialNumberMisMatchClearedV1Trap.setStatus(
        ""
    )

hzIduRadioFirmwareMismatchV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 60)
)
hzIduRadioFirmwareMismatchV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioFirmwareMismatchV1Trap.setStatus(
        ""
    )

hzIduRadioFirmwareMismatchClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 61)
)
hzIduRadioFirmwareMismatchClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioFirmwareMismatchClearedV1Trap.setStatus(
        ""
    )

hzIduSecondaryRadioNotdetectedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 62)
)
hzIduSecondaryRadioNotdetectedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduSecondaryRadioNotdetectedV1Trap.setStatus(
        ""
    )

hzIduSecondaryRadioNotdetectedClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 63)
)
hzIduSecondaryRadioNotdetectedClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduSecondaryRadioNotdetectedClearedV1Trap.setStatus(
        ""
    )

hzIduPrimaryRadioNotdetectedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 64)
)
hzIduPrimaryRadioNotdetectedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduPrimaryRadioNotdetectedV1Trap.setStatus(
        ""
    )

hzIduPrimaryRadioNotdetectedClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 65)
)
hzIduPrimaryRadioNotdetectedClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduPrimaryRadioNotdetectedClearedV1Trap.setStatus(
        ""
    )

hzIduFaultyPrimaryRadioV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 66)
)
hzIduFaultyPrimaryRadioV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduFaultyPrimaryRadioV1Trap.setStatus(
        ""
    )

hzIduFaultyPrimaryRadioClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 67)
)
hzIduFaultyPrimaryRadioClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduFaultyPrimaryRadioClearedV1Trap.setStatus(
        ""
    )

hzIduRadioExcessiveTxCableLossChangeV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 68)
)
hzIduRadioExcessiveTxCableLossChangeV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioExcessiveTxCableLossChangeV1Trap.setStatus(
        ""
    )

hzIduRadioExcessiveTxCableLossChangeClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 69)
)
hzIduRadioExcessiveTxCableLossChangeClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRadioExcessiveTxCableLossChangeClearedV1Trap.setStatus(
        ""
    )

hzIduExcessiveRxCableLossV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 70)
)
hzIduExcessiveRxCableLossV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduExcessiveRxCableLossV1Trap.setStatus(
        ""
    )

hzIduExcessiveRxCableLossClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 71)
)
hzIduExcessiveRxCableLossClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduRadioAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduExcessiveRxCableLossClearedV1Trap.setStatus(
        ""
    )

hzIduRedundancyPrimaryPortNotSetV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 72)
)
if mibBuilder.loadTexts:
    hzIduRedundancyPrimaryPortNotSetV1Trap.setStatus(
        ""
    )

hzIduRedundancyPrimaryPortNotSetClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 73)
)
if mibBuilder.loadTexts:
    hzIduRedundancyPrimaryPortNotSetClearedV1Trap.setStatus(
        ""
    )

hzIduRedundancySecondaryPortIsActiveV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 74)
)
if mibBuilder.loadTexts:
    hzIduRedundancySecondaryPortIsActiveV1Trap.setStatus(
        ""
    )

hzIduRedundancySecondaryPortIsActiveClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 75)
)
if mibBuilder.loadTexts:
    hzIduRedundancySecondaryPortIsActiveClearedV1Trap.setStatus(
        ""
    )

hzIduRedundancyPrimaryPortFaultyV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 76)
)
if mibBuilder.loadTexts:
    hzIduRedundancyPrimaryPortFaultyV1Trap.setStatus(
        ""
    )

hzIduRedundancyPrimaryPortFaultyClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 77)
)
if mibBuilder.loadTexts:
    hzIduRedundancyPrimaryPortFaultyClearedV1Trap.setStatus(
        ""
    )

hzIduRedundancySecondaryPortFaultyV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 78)
)
if mibBuilder.loadTexts:
    hzIduRedundancySecondaryPortFaultyV1Trap.setStatus(
        ""
    )

hzIduRedundancySecondaryPortFaultyClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 79)
)
if mibBuilder.loadTexts:
    hzIduRedundancySecondaryPortFaultyClearedV1Trap.setStatus(
        ""
    )

hzIduFan1FailedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 80)
)
if mibBuilder.loadTexts:
    hzIduFan1FailedV1Trap.setStatus(
        ""
    )

hzIduFan1FailureClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 81)
)
if mibBuilder.loadTexts:
    hzIduFan1FailureClearedV1Trap.setStatus(
        ""
    )

hzIduFan2FailedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 82)
)
if mibBuilder.loadTexts:
    hzIduFan2FailedV1Trap.setStatus(
        ""
    )

hzIduFan2FailureClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 83)
)
if mibBuilder.loadTexts:
    hzIduFan2FailureClearedV1Trap.setStatus(
        ""
    )

hzIduFan3FailedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 84)
)
if mibBuilder.loadTexts:
    hzIduFan3FailedV1Trap.setStatus(
        ""
    )

hzIduFan3FailureClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 85)
)
if mibBuilder.loadTexts:
    hzIduFan3FailureClearedV1Trap.setStatus(
        ""
    )

hzIduFan4FailedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 86)
)
if mibBuilder.loadTexts:
    hzIduFan4FailedV1Trap.setStatus(
        ""
    )

hzIduFan4FailureClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 87)
)
if mibBuilder.loadTexts:
    hzIduFan4FailureClearedV1Trap.setStatus(
        ""
    )

hzIduRlsShutdownActivatedv1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 88)
)
hzIduRlsShutdownActivatedv1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRlsShutdownActivatedv1Trap.setStatus(
        ""
    )

hzIduRlsShutdownActivatedClearedV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 3, 8, 0, 89)
)
hzIduRlsShutdownActivatedClearedV1Trap.setObjects(
    ("DRAGONWAVE-HORIZON-IDU-MIB", "hzIduModemAlarmsIndex")
)
if mibBuilder.loadTexts:
    hzIduRlsShutdownActivatedClearedV1Trap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DRAGONWAVE-HORIZON-IDU-MIB",
    **{"PhysAddress": PhysAddress,
       "DisplayString": DisplayString,
       "coldStart": coldStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "horizonIdu": horizonIdu,
       "hzIduSystem": hzIduSystem,
       "hzIduSysGeneral": hzIduSysGeneral,
       "hzIduResetSystem": hzIduResetSystem,
       "hzIduSaveMIB": hzIduSaveMIB,
       "hzIduOperStatus": hzIduOperStatus,
       "hzIduAirInterfaceEncryption": hzIduAirInterfaceEncryption,
       "hzIduSystemCapacityOption": hzIduSystemCapacityOption,
       "hzIduSysUpgradeSpeed": hzIduSysUpgradeSpeed,
       "hzIduLicensedSpeedUpgradeSpeedAndKey": hzIduLicensedSpeedUpgradeSpeedAndKey,
       "hzIduLicensedSpeedChanges": hzIduLicensedSpeedChanges,
       "hzIduSysDowngradeSpeed": hzIduSysDowngradeSpeed,
       "hzIduLicensedSpeedDowngradeSpeed": hzIduLicensedSpeedDowngradeSpeed,
       "hzIduLicensedSpeedCountUsedForKey": hzIduLicensedSpeedCountUsedForKey,
       "hzIduLicensedSpeedDowngradeKey": hzIduLicensedSpeedDowngradeKey,
       "hzIduSysUpgradeWirelessPorts": hzIduSysUpgradeWirelessPorts,
       "hzIduLicensedWirelessPortsUpgradeKey": hzIduLicensedWirelessPortsUpgradeKey,
       "hzIduLicensedWirelessPortsChanges": hzIduLicensedWirelessPortsChanges,
       "hzIduSysSpeed": hzIduSysSpeed,
       "hzIduSystemCurrentSpeed": hzIduSystemCurrentSpeed,
       "hzIduSystemLicensedSpeed": hzIduSystemLicensedSpeed,
       "hzIduSystemMode": hzIduSystemMode,
       "hzIduInventory": hzIduInventory,
       "hzIduHwInventory": hzIduHwInventory,
       "hzIduFrequencyFilePartNumber": hzIduFrequencyFilePartNumber,
       "hzIduUnitSerialNo": hzIduUnitSerialNo,
       "hzIduUnitAssemblylNo": hzIduUnitAssemblylNo,
       "hzIduIfSerialNo1": hzIduIfSerialNo1,
       "hzIduIfSerialNo2": hzIduIfSerialNo2,
       "hzIduIfAssemblylNo1": hzIduIfAssemblylNo1,
       "hzIduIfAssemblylNo2": hzIduIfAssemblylNo2,
       "hzIduNccSerialNo": hzIduNccSerialNo,
       "hzIduNccAssemblylNo": hzIduNccAssemblylNo,
       "hzIduRadio1SerialNo": hzIduRadio1SerialNo,
       "hzIduRadio2SerialNo": hzIduRadio2SerialNo,
       "hzIduRadio1HardwareId": hzIduRadio1HardwareId,
       "hzIduRadio2HardwareId": hzIduRadio2HardwareId,
       "hzIduInternalIFCouplerPresent": hzIduInternalIFCouplerPresent,
       "hzIduHwWirelessPortsLicensed": hzIduHwWirelessPortsLicensed,
       "hzIduSwInventory": hzIduSwInventory,
       "hzIduSwInvSystemOmniVersionNo": hzIduSwInvSystemOmniVersionNo,
       "hzIduSwInvModemOmniVersionNo": hzIduSwInvModemOmniVersionNo,
       "hzIduSwInvFrequencyFileVersionNo": hzIduSwInvFrequencyFileVersionNo,
       "hzIduSwInvMibVersionNo": hzIduSwInvMibVersionNo,
       "hzIduSwInvRadio1FirmwareVersionNo": hzIduSwInvRadio1FirmwareVersionNo,
       "hzIduSwInvRadio2FirmwareVersionNo": hzIduSwInvRadio2FirmwareVersionNo,
       "hzIduAtpc": hzIduAtpc,
       "hzIduAtpcEnable": hzIduAtpcEnable,
       "hzIduAtpcStatus": hzIduAtpcStatus,
       "hzIduAtpcCoordinatedPower": hzIduAtpcCoordinatedPower,
       "hzIduAam": hzIduAam,
       "hzIduAamStatus": hzIduAamStatus,
       "hzIduAamDiagnostics": hzIduAamDiagnostics,
       "hzIduAamDiagnose": hzIduAamDiagnose,
       "hzIduAamDiagnosticResult": hzIduAamDiagnosticResult,
       "hzIduPeerSysInfo": hzIduPeerSysInfo,
       "hzIduPeerMacAddress": hzIduPeerMacAddress,
       "hzIduPeerIpAddress": hzIduPeerIpAddress,
       "hzIduPeerSubnetMask": hzIduPeerSubnetMask,
       "hzIduAuthentication": hzIduAuthentication,
       "hzIduUniquePeerAuthenticationKey": hzIduUniquePeerAuthenticationKey,
       "hzIduPeerDetectedSerialNumber": hzIduPeerDetectedSerialNumber,
       "hzIduAuthenticationMode": hzIduAuthenticationMode,
       "hzIduAuthenticationFailureAction": hzIduAuthenticationFailureAction,
       "hzIduPeerAuthenticationStatus": hzIduPeerAuthenticationStatus,
       "hzIduNetworkManagement": hzIduNetworkManagement,
       "hzIduMacAddress": hzIduMacAddress,
       "hzIduNetworkManagementInterface": hzIduNetworkManagementInterface,
       "hzIduIpAddress": hzIduIpAddress,
       "hzIduSubnetMask": hzIduSubnetMask,
       "hzIduDefaultGateway": hzIduDefaultGateway,
       "hzIduTelnetAccessMode": hzIduTelnetAccessMode,
       "hzIduSshAccessMode": hzIduSshAccessMode,
       "hzIduVlanTagEnable": hzIduVlanTagEnable,
       "hzIduVlanTagId": hzIduVlanTagId,
       "hzIduVlanTagPriority": hzIduVlanTagPriority,
       "hzIduNetworkInterface": hzIduNetworkInterface,
       "hzIduEnetPort1": hzIduEnetPort1,
       "hzIduEnetPort1Description": hzIduEnetPort1Description,
       "hzIduEnetPort1Config": hzIduEnetPort1Config,
       "hzIduEnetPort1AutoNegotiation": hzIduEnetPort1AutoNegotiation,
       "hzIduEnetPort1Speed": hzIduEnetPort1Speed,
       "hzIduEnetPort1Duplex": hzIduEnetPort1Duplex,
       "hzIduEnetPort1Media": hzIduEnetPort1Media,
       "hzIduEnetPort1AdminState": hzIduEnetPort1AdminState,
       "hzIduEnetPort1OpticalTransceiverState": hzIduEnetPort1OpticalTransceiverState,
       "hzIduEnetPort1PauseFrameEnable": hzIduEnetPort1PauseFrameEnable,
       "hzIduEnetPort1MaxFrameSize": hzIduEnetPort1MaxFrameSize,
       "hzIduEnetPort1DroppedEnetFramesThresholdParameters": hzIduEnetPort1DroppedEnetFramesThresholdParameters,
       "hzIduEnetPort1BandwidthUtilizationThresholdParameters": hzIduEnetPort1BandwidthUtilizationThresholdParameters,
       "hzIduEnetPort1Status": hzIduEnetPort1Status,
       "hzIduEnetPort1LinkStatus": hzIduEnetPort1LinkStatus,
       "hzIduEnetPort1AutoNegotiationStatus": hzIduEnetPort1AutoNegotiationStatus,
       "hzIduEnetPort1SpeedStatus": hzIduEnetPort1SpeedStatus,
       "hzIduEnetPort1DuplexStatus": hzIduEnetPort1DuplexStatus,
       "hzIduEnetPort1MediaStatus": hzIduEnetPort1MediaStatus,
       "hzIduEnetPort1Stats": hzIduEnetPort1Stats,
       "hzIduEnetPort1TxFrames": hzIduEnetPort1TxFrames,
       "hzIduEnetPort1TxBytes": hzIduEnetPort1TxBytes,
       "hzIduEnetPort1RxFrames": hzIduEnetPort1RxFrames,
       "hzIduEnetPort1RxBytes": hzIduEnetPort1RxBytes,
       "hzIduEnetPort1RxFramesInErrors": hzIduEnetPort1RxFramesInErrors,
       "hzIduEnetPort1RxFramesCRCErrors": hzIduEnetPort1RxFramesCRCErrors,
       "hzIduEnetPort1BWUtilization": hzIduEnetPort1BWUtilization,
       "hzIduEnetPort1IngressDataRate": hzIduEnetPort1IngressDataRate,
       "hzIduEnetPort1EgressDataRate": hzIduEnetPort1EgressDataRate,
       "hzIduEnetPort1FramesInQueue1s": hzIduEnetPort1FramesInQueue1s,
       "hzIduEnetPort1FramesInQueue2s": hzIduEnetPort1FramesInQueue2s,
       "hzIduEnetPort1FramesInQueue3s": hzIduEnetPort1FramesInQueue3s,
       "hzIduEnetPort1FramesInQueue4s": hzIduEnetPort1FramesInQueue4s,
       "hzIduEnetPort1FramesInQueue1Discardeds": hzIduEnetPort1FramesInQueue1Discardeds,
       "hzIduEnetPort1FramesInQueue2Discardeds": hzIduEnetPort1FramesInQueue2Discardeds,
       "hzIduEnetPort1FramesInQueue3Discardeds": hzIduEnetPort1FramesInQueue3Discardeds,
       "hzIduEnetPort1FramesInQueue4Discardeds": hzIduEnetPort1FramesInQueue4Discardeds,
       "hzIduEnetPort2": hzIduEnetPort2,
       "hzIduEnetPort2Description": hzIduEnetPort2Description,
       "hzIduEnetPort2Config": hzIduEnetPort2Config,
       "hzIduEnetPort2AutoNegotiation": hzIduEnetPort2AutoNegotiation,
       "hzIduEnetPort2Speed": hzIduEnetPort2Speed,
       "hzIduEnetPort2Duplex": hzIduEnetPort2Duplex,
       "hzIduEnetPort2AdminState": hzIduEnetPort2AdminState,
       "hzIduEnetPort2Status": hzIduEnetPort2Status,
       "hzIduEnetPort2LinkStatus": hzIduEnetPort2LinkStatus,
       "hzIduEnetPort2AutoNegotiationStatus": hzIduEnetPort2AutoNegotiationStatus,
       "hzIduEnetPort2SpeedStatus": hzIduEnetPort2SpeedStatus,
       "hzIduEnetPort2DuplexStatus": hzIduEnetPort2DuplexStatus,
       "hzIduEnetPort2Stats": hzIduEnetPort2Stats,
       "hzIduEnetPort2TxFrames": hzIduEnetPort2TxFrames,
       "hzIduEnetPort2TxBytes": hzIduEnetPort2TxBytes,
       "hzIduEnetPort2RxFrames": hzIduEnetPort2RxFrames,
       "hzIduEnetPort2RxBytes": hzIduEnetPort2RxBytes,
       "hzIduEnetPort2RxFramesInErrors": hzIduEnetPort2RxFramesInErrors,
       "hzIduEnetPort2RxFramesCrcErrors": hzIduEnetPort2RxFramesCrcErrors,
       "hzIduWirelessInterface": hzIduWirelessInterface,
       "hzIduWirelessInterfaceNames": hzIduWirelessInterfaceNames,
       "hzIduWirelessInterfaceNameTable": hzIduWirelessInterfaceNameTable,
       "hzIduWirelessInterfaceNameEntry": hzIduWirelessInterfaceNameEntry,
       "hzIduWirelessInterfaceNameIndex": hzIduWirelessInterfaceNameIndex,
       "hzIduWirelessInterfaceName": hzIduWirelessInterfaceName,
       "hzIduWirelessInterfaceModems": hzIduWirelessInterfaceModems,
       "hzIduAggregatedWirelessPortStats": hzIduAggregatedWirelessPortStats,
       "hzIduAggregatedWirelessPortTxFrames": hzIduAggregatedWirelessPortTxFrames,
       "hzIduAggregatedWirelessPortRxFramesOKs": hzIduAggregatedWirelessPortRxFramesOKs,
       "hzIduAggregatedWirelessPortRxFrameErrors": hzIduAggregatedWirelessPortRxFrameErrors,
       "hzIduAggregatedWirelessPortRxFramesQueueDiscards": hzIduAggregatedWirelessPortRxFramesQueueDiscards,
       "hzIduModemTable": hzIduModemTable,
       "hzIduModemEntry": hzIduModemEntry,
       "hzIduModemIndex": hzIduModemIndex,
       "hzIduModemOperStatus": hzIduModemOperStatus,
       "hzIduModemReset": hzIduModemReset,
       "hzIduModemChannelizedRSL": hzIduModemChannelizedRSL,
       "hzIduModemChannelizedRSLUnsignedInt": hzIduModemChannelizedRSLUnsignedInt,
       "hzIduModemModulationType": hzIduModemModulationType,
       "hzIduModemRxSpeed": hzIduModemRxSpeed,
       "hzIduModemTxSpeed": hzIduModemTxSpeed,
       "hzIduModemSNR": hzIduModemSNR,
       "hzIduModemEbToNoiseRatio": hzIduModemEbToNoiseRatio,
       "hzIduModemEqualizerStress": hzIduModemEqualizerStress,
       "hzIduModemSNRThresholdParameters": hzIduModemSNRThresholdParameters,
       "hzIduModemChannelizedRslBelowThresholdParameters": hzIduModemChannelizedRslBelowThresholdParameters,
       "hzIduModemStatsTable": hzIduModemStatsTable,
       "hzIduModemStatsEntry": hzIduModemStatsEntry,
       "hzIduModemStatsIndex": hzIduModemStatsIndex,
       "hzIduModemTxBlocks": hzIduModemTxBlocks,
       "hzIduModemRxBlocksOKs": hzIduModemRxBlocksOKs,
       "hzIduModemRxBlocksErrors": hzIduModemRxBlocksErrors,
       "hzIduWirelessInterfaceIFCards": hzIduWirelessInterfaceIFCards,
       "hzIduIntermediateFrequencyCardTable": hzIduIntermediateFrequencyCardTable,
       "hzIduIntermediateFrequencyCardEntry": hzIduIntermediateFrequencyCardEntry,
       "hzIduIFCardIndex": hzIduIFCardIndex,
       "hzIduIFCardTxSynthesizerLock": hzIduIFCardTxSynthesizerLock,
       "hzIduIFCardRxSynthesizerLock": hzIduIFCardRxSynthesizerLock,
       "hzIduWirelessInterfaceRadios": hzIduWirelessInterfaceRadios,
       "hzIduRadioTable": hzIduRadioTable,
       "hzIduRadioEntry": hzIduRadioEntry,
       "hzIduRadioIndex": hzIduRadioIndex,
       "hzIduRadioDescription": hzIduRadioDescription,
       "hzIduRadioOperStatus": hzIduRadioOperStatus,
       "hzIduRadioLastChanged": hzIduRadioLastChanged,
       "hzIduRadioReceiveSignalLevel": hzIduRadioReceiveSignalLevel,
       "hzIduRadioReceiveSignalLevelUnsigned": hzIduRadioReceiveSignalLevelUnsigned,
       "hzIduRadioTxGain": hzIduRadioTxGain,
       "hzIduRadioRxGain": hzIduRadioRxGain,
       "hzIduRadioReset": hzIduRadioReset,
       "hzIduRadioTransmitPowerdBm": hzIduRadioTransmitPowerdBm,
       "hzIduRadioPowerOption": hzIduRadioPowerOption,
       "hzIduRadioTxState": hzIduRadioTxState,
       "hzIduRadioTemperature": hzIduRadioTemperature,
       "hzIduRadioRxCableLoss": hzIduRadioRxCableLoss,
       "hzIduRadioTxCableLoss": hzIduRadioTxCableLoss,
       "hzIduRadioTxCableLossChange": hzIduRadioTxCableLossChange,
       "hzIduWirelessInterfaceRadioFrequencies": hzIduWirelessInterfaceRadioFrequencies,
       "hzIduWirelessInterfaceRadio1Frequencies": hzIduWirelessInterfaceRadio1Frequencies,
       "hzIduRadio1Band": hzIduRadio1Band,
       "hzIduRadio1FreqGroupSelected": hzIduRadio1FreqGroupSelected,
       "hzIduRadio1TxHighFreqTable": hzIduRadio1TxHighFreqTable,
       "hzIduRadio1TxHighFreqEntry": hzIduRadio1TxHighFreqEntry,
       "hzIduRadio1TxHighFreqIndex": hzIduRadio1TxHighFreqIndex,
       "hzIduRadio1TxHighFreqChannelIndex": hzIduRadio1TxHighFreqChannelIndex,
       "hzIduRadio1TxHighFreqTransmitRfFrequency": hzIduRadio1TxHighFreqTransmitRfFrequency,
       "hzIduRadio1TxHighFreqReceiveRfFrequency": hzIduRadio1TxHighFreqReceiveRfFrequency,
       "hzIduRadio1TxHighFreqProgrammed": hzIduRadio1TxHighFreqProgrammed,
       "hzIduRadio1TxLowFreqTable": hzIduRadio1TxLowFreqTable,
       "hzIduRadio1TxLowFreqEntry": hzIduRadio1TxLowFreqEntry,
       "hzIduRadio1TxLowFreqIndex": hzIduRadio1TxLowFreqIndex,
       "hzIduRadio1TxLowFreqChannelIndex": hzIduRadio1TxLowFreqChannelIndex,
       "hzIduRadio1TxLowFreqTransmitRfFrequency": hzIduRadio1TxLowFreqTransmitRfFrequency,
       "hzIduRadio1TxLowFreqReceiveRfFrequency": hzIduRadio1TxLowFreqReceiveRfFrequency,
       "hzIduRadio1TxLowFreqProgrammed": hzIduRadio1TxLowFreqProgrammed,
       "hzIduRadio1ProgrammedFrequency": hzIduRadio1ProgrammedFrequency,
       "hzIduRadio1ProgrammedFrequencyChannel": hzIduRadio1ProgrammedFrequencyChannel,
       "hzIduRadio1ProgrammedFrequencyTxRf": hzIduRadio1ProgrammedFrequencyTxRf,
       "hzIduRadio1ProgrammedFrequencyRxRf": hzIduRadio1ProgrammedFrequencyRxRf,
       "hzIduWirelessInterfaceRadio2Frequencies": hzIduWirelessInterfaceRadio2Frequencies,
       "hzIduRadio2Band": hzIduRadio2Band,
       "hzIduRadio2FreqGroupSelected": hzIduRadio2FreqGroupSelected,
       "hzIduRadio2TxHighFreqTable": hzIduRadio2TxHighFreqTable,
       "hzIduRadio2TxHighFreqEntry": hzIduRadio2TxHighFreqEntry,
       "hzIduRadio2TxHighFreqIndex": hzIduRadio2TxHighFreqIndex,
       "hzIduRadio2TxHighFreqChannelIndex": hzIduRadio2TxHighFreqChannelIndex,
       "hzIduRadio2TxHighFreqTransmitRfFrequency": hzIduRadio2TxHighFreqTransmitRfFrequency,
       "hzIduRadio2TxHighFreqReceiveRfFrequency": hzIduRadio2TxHighFreqReceiveRfFrequency,
       "hzIduRadio2TxHighFreqProgrammed": hzIduRadio2TxHighFreqProgrammed,
       "hzIduRadio2TxLowFreqTable": hzIduRadio2TxLowFreqTable,
       "hzIduRadio2TxLowFreqEntry": hzIduRadio2TxLowFreqEntry,
       "hzIduRadio2TxLowFreqIndex": hzIduRadio2TxLowFreqIndex,
       "hzIduRadio2TxLowFreqChannelIndex": hzIduRadio2TxLowFreqChannelIndex,
       "hzIduRadio2TxLowFreqTransmitRfFrequency": hzIduRadio2TxLowFreqTransmitRfFrequency,
       "hzIduRadio2TxLowFreqReceiveRfFrequency": hzIduRadio2TxLowFreqReceiveRfFrequency,
       "hzIduRadio2TxLowFreqProgrammed": hzIduRadio2TxLowFreqProgrammed,
       "hzIduRadio2ProgrammedFrequency": hzIduRadio2ProgrammedFrequency,
       "hzIduRadio2ProgrammedFrequencyChannel": hzIduRadio2ProgrammedFrequencyChannel,
       "hzIduRadio2ProgrammedFrequencyTxRf": hzIduRadio2ProgrammedFrequencyTxRf,
       "hzIduRadio2ProgrammedFrequencyRxRf": hzIduRadio2ProgrammedFrequencyRxRf,
       "hzIduWirelessInterfaceAntenna": hzIduWirelessInterfaceAntenna,
       "hzIduAntennaDiameter": hzIduAntennaDiameter,
       "hzIduWirelessInterfaceRedundancy": hzIduWirelessInterfaceRedundancy,
       "hzIduWirelessInterfaceRedundancyActiveWirelessPort": hzIduWirelessInterfaceRedundancyActiveWirelessPort,
       "hzIduWirelessInterfaceRedundancyPrimaryWirelessPort": hzIduWirelessInterfaceRedundancyPrimaryWirelessPort,
       "hzIduWirelessInterfaceRedundancySwitchingAlgorithm": hzIduWirelessInterfaceRedundancySwitchingAlgorithm,
       "hzIduWirelessInterfaceRedundancySwitchCause": hzIduWirelessInterfaceRedundancySwitchCause,
       "hzIduWirelessInterfaceRedundancySwitchRadio": hzIduWirelessInterfaceRedundancySwitchRadio,
       "hzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort": hzIduWirelessInterfaceRedundancyRemoveFaultyWirelessPort,
       "hzIduWirelessInterfaceRedundancyDiagnostics": hzIduWirelessInterfaceRedundancyDiagnostics,
       "hzIduWirelessInterfaceRedundancyDiagnose": hzIduWirelessInterfaceRedundancyDiagnose,
       "hzIduWirelessInterfaceRedundancyDiagnosticResult": hzIduWirelessInterfaceRedundancyDiagnosticResult,
       "hzIduCalendar": hzIduCalendar,
       "hzIduDate": hzIduDate,
       "hzIduTime": hzIduTime,
       "hzIduAlarms": hzIduAlarms,
       "hzIduClearAlarmCounters": hzIduClearAlarmCounters,
       "hzIduSystemAlarms": hzIduSystemAlarms,
       "hzIduExplicitAuthenticationFailure": hzIduExplicitAuthenticationFailure,
       "hzIduExplicitAuthenticationFailureCounts": hzIduExplicitAuthenticationFailureCounts,
       "hzIduAamConfigMismatch": hzIduAamConfigMismatch,
       "hzIduAamConfigMismatchCounts": hzIduAamConfigMismatchCounts,
       "hzIduAamActive": hzIduAamActive,
       "hzIduAamActiveCounts": hzIduAamActiveCounts,
       "hzIduSntpServerUnavailableAlarm": hzIduSntpServerUnavailableAlarm,
       "hzIduSntpServerUnavailableAlarmCounts": hzIduSntpServerUnavailableAlarmCounts,
       "hzIduFrequencyFileInvalid": hzIduFrequencyFileInvalid,
       "hzIduFrequencyFileInvalidCounts": hzIduFrequencyFileInvalidCounts,
       "hzIduFan1Failure": hzIduFan1Failure,
       "hzIduFan1FailureCounts": hzIduFan1FailureCounts,
       "hzIduFan2Failure": hzIduFan2Failure,
       "hzIduFan2FailureCounts": hzIduFan2FailureCounts,
       "hzIduFan3Failure": hzIduFan3Failure,
       "hzIduFan3FailureCounts": hzIduFan3FailureCounts,
       "hzIduFan4Failure": hzIduFan4Failure,
       "hzIduFan4FailureCounts": hzIduFan4FailureCounts,
       "hzIduPrimaryPortNotSet": hzIduPrimaryPortNotSet,
       "hzIduPrimaryPortNotSetCounts": hzIduPrimaryPortNotSetCounts,
       "hzIduSecondaryPortActive": hzIduSecondaryPortActive,
       "hzIduSecondaryPortActiveCounts": hzIduSecondaryPortActiveCounts,
       "hzIduPrimaryPortFaulty": hzIduPrimaryPortFaulty,
       "hzIduPrimaryPortFaultyCounts": hzIduPrimaryPortFaultyCounts,
       "hzIduSecondaryPortFaulty": hzIduSecondaryPortFaulty,
       "hzIduSecondaryPortFaultyCounts": hzIduSecondaryPortFaultyCounts,
       "hzIduNetworkInterfaceAlarms": hzIduNetworkInterfaceAlarms,
       "hzIduEnetPort1Alarms": hzIduEnetPort1Alarms,
       "hzIduEnetPort1DroppedEnetFramesThresholdExceeded": hzIduEnetPort1DroppedEnetFramesThresholdExceeded,
       "hzIduEnetPort1DroppedEnetFramesThresholdCounts": hzIduEnetPort1DroppedEnetFramesThresholdCounts,
       "hzIduEnetPort1BandwidthUtilizationThresholdExceeded": hzIduEnetPort1BandwidthUtilizationThresholdExceeded,
       "hzIduEnetPort1BandwidthUtilizationThresholdCounts": hzIduEnetPort1BandwidthUtilizationThresholdCounts,
       "hzIduEnetPort1RlsMismatch": hzIduEnetPort1RlsMismatch,
       "hzIduEnetPort1RlsMismatchCounts": hzIduEnetPort1RlsMismatchCounts,
       "hzIduRLSQueueBasedShutdownActivated": hzIduRLSQueueBasedShutdownActivated,
       "hzIduRLSQueueBasedShutdownActivatedCounts": hzIduRLSQueueBasedShutdownActivatedCounts,
       "hzIduEnetPort1EthernetLinkDown": hzIduEnetPort1EthernetLinkDown,
       "hzIduEnetPort1EthernetLinkDownActivatedCounts": hzIduEnetPort1EthernetLinkDownActivatedCounts,
       "hzIduEnetPort2Alarms": hzIduEnetPort2Alarms,
       "hzIduEnetPort2EthernetLinkDown": hzIduEnetPort2EthernetLinkDown,
       "hzIduEnetPort2EthernetLinkDownActivatedCounts": hzIduEnetPort2EthernetLinkDownActivatedCounts,
       "hzIduWirelessInterfaceAlarms": hzIduWirelessInterfaceAlarms,
       "hzIduModemAlarms": hzIduModemAlarms,
       "hzIduModemAlarmsTable": hzIduModemAlarmsTable,
       "hzIduModemAlarmsEntry": hzIduModemAlarmsEntry,
       "hzIduModemAlarmsIndex": hzIduModemAlarmsIndex,
       "hzIduModemRxLossOfSignal": hzIduModemRxLossOfSignal,
       "hzIduModemRxLossOfSignalCounts": hzIduModemRxLossOfSignalCounts,
       "hzIduModemTxLossOfSync": hzIduModemTxLossOfSync,
       "hzIduModemTxLossOfSyncCounts": hzIduModemTxLossOfSyncCounts,
       "hzIduModemSnrBelowThreshold": hzIduModemSnrBelowThreshold,
       "hzIduModemSnrBelowThresholdCounts": hzIduModemSnrBelowThresholdCounts,
       "hzIduModemEqualizerStressExceedThreshold": hzIduModemEqualizerStressExceedThreshold,
       "hzIduModemEquilizerStressExceedThresholdCounts": hzIduModemEquilizerStressExceedThresholdCounts,
       "hzIduModemHardwareFault": hzIduModemHardwareFault,
       "hzIduModemHardwareFaultCounts": hzIduModemHardwareFaultCounts,
       "hzIduModemProgrammingError": hzIduModemProgrammingError,
       "hzIduModemProgrammingErrorCounts": hzIduModemProgrammingErrorCounts,
       "hzIduRLSShutdownActivated": hzIduRLSShutdownActivated,
       "hzIduRLSShutdownActivatedCounts": hzIduRLSShutdownActivatedCounts,
       "hzIduRadioAlarms": hzIduRadioAlarms,
       "hzIduRadioAlarmsTable": hzIduRadioAlarmsTable,
       "hzIduRadioAlarmsEntry": hzIduRadioAlarmsEntry,
       "hzIduRadioAlarmsIndex": hzIduRadioAlarmsIndex,
       "hzIduRadioPLDROLostLock": hzIduRadioPLDROLostLock,
       "hzIduRadioPLDROLostLockCounts": hzIduRadioPLDROLostLockCounts,
       "hzIduRadioLostCommunication": hzIduRadioLostCommunication,
       "hzIduRadioLostCommunicationCounts": hzIduRadioLostCommunicationCounts,
       "hzIduRadioMismatch": hzIduRadioMismatch,
       "hzIduRadioMismatchCounts": hzIduRadioMismatchCounts,
       "hzIduRadioPowerAmp": hzIduRadioPowerAmp,
       "hzIduRadioPowerAmpCounts": hzIduRadioPowerAmpCounts,
       "hzIduRadioExcessiveTxCableLoss": hzIduRadioExcessiveTxCableLoss,
       "hzIduRadioExcessiveTxCableLossCounts": hzIduRadioExcessiveTxCableLossCounts,
       "hzIduRadioRslBelowThreshold": hzIduRadioRslBelowThreshold,
       "hzIduRadioRslBelowThresholdCounts": hzIduRadioRslBelowThresholdCounts,
       "hzIduRadioHighPowerOptionM1": hzIduRadioHighPowerOptionM1,
       "hzIduRadioHighPowerOptionM1Counts": hzIduRadioHighPowerOptionM1Counts,
       "hzIduRadioHighPowerOptionM2": hzIduRadioHighPowerOptionM2,
       "hzIduRadioHighPowerOptionM2Counts": hzIduRadioHighPowerOptionM2Counts,
       "hzIduRadioHighPowerTxDetector": hzIduRadioHighPowerTxDetector,
       "hzIduRadioHighPowerTxDetectorCounts": hzIduRadioHighPowerTxDetectorCounts,
       "hzIduRadioAtpcConfigMismatch": hzIduRadioAtpcConfigMismatch,
       "hzIduRadioAtpcConfigMismatchCounts": hzIduRadioAtpcConfigMismatchCounts,
       "hzIduRadioRedundancySerialNumMismatch": hzIduRadioRedundancySerialNumMismatch,
       "hzIduRadioRedundancySerialNumMismatchCounts": hzIduRadioRedundancySerialNumMismatchCounts,
       "hzIduRadioExcessiveTxCableLossChange": hzIduRadioExcessiveTxCableLossChange,
       "hzIduRadioExcessiveTxCableLossChangeCounts": hzIduRadioExcessiveTxCableLossChangeCounts,
       "hzIduRadioExcessiveRxCableLoss": hzIduRadioExcessiveRxCableLoss,
       "hzIduRadioExcessiveRxCableLossCounts": hzIduRadioExcessiveRxCableLossCounts,
       "hzIduRadioAtpcTxAtMaxPower": hzIduRadioAtpcTxAtMaxPower,
       "hzIduRadioAtpcTxAtMaxPowerCounts": hzIduRadioAtpcTxAtMaxPowerCounts,
       "hzIduTrapConfig": hzIduTrapConfig,
       "hzIduExplicitAuthenticationFailureV1Trap": hzIduExplicitAuthenticationFailureV1Trap,
       "hzIduExplicitAuthenticationFailureClearedV1Trap": hzIduExplicitAuthenticationFailureClearedV1Trap,
       "hzIduAamConfigMisMatchV1Trap": hzIduAamConfigMisMatchV1Trap,
       "hzIduAamConfigMisMatchClearV1Trap": hzIduAamConfigMisMatchClearV1Trap,
       "hzIduAamActiveV1Trap": hzIduAamActiveV1Trap,
       "hzIduAamActiveClearedV1Trap": hzIduAamActiveClearedV1Trap,
       "hzIduAtpcConfigMismatchV1Trap": hzIduAtpcConfigMismatchV1Trap,
       "hzIduAtpcConfigMismatchClearedV1Trap": hzIduAtpcConfigMismatchClearedV1Trap,
       "hzIduSntpServersUnreachableV1Trap": hzIduSntpServersUnreachableV1Trap,
       "hzIduSntpServersUnreachableClearedV1Trap": hzIduSntpServersUnreachableClearedV1Trap,
       "hzIduFrequencyFileInvalidV1Trap": hzIduFrequencyFileInvalidV1Trap,
       "hzIduEnetPort1DroppedFramesThresholdExceededV1Trap": hzIduEnetPort1DroppedFramesThresholdExceededV1Trap,
       "hzIduEnetPort1DroppedFramesThresholdExceededClearedV1Trap": hzIduEnetPort1DroppedFramesThresholdExceededClearedV1Trap,
       "hzIduEnetPort1BwUtilizationThresholdExceededV1Trap": hzIduEnetPort1BwUtilizationThresholdExceededV1Trap,
       "hzIduEnetPort1BwUtilizationThresholdExceededClearedV1Trap": hzIduEnetPort1BwUtilizationThresholdExceededClearedV1Trap,
       "hzIduEnetPort1RlsMismatchV1Trap": hzIduEnetPort1RlsMismatchV1Trap,
       "hzIduEnetPort1RlsMismatchClearedV1Trap": hzIduEnetPort1RlsMismatchClearedV1Trap,
       "hzIduRlsQueueBasedShutdownActivatedv1Trap": hzIduRlsQueueBasedShutdownActivatedv1Trap,
       "hzIduRlsQueueBasedShutdownActivatedClearedV1Trap": hzIduRlsQueueBasedShutdownActivatedClearedV1Trap,
       "hzIduModemRxLossOfSignalLockV1Trap": hzIduModemRxLossOfSignalLockV1Trap,
       "hzIduModemRxLossOfSignalLockClearedV1Trap": hzIduModemRxLossOfSignalLockClearedV1Trap,
       "hzIduModemTxLossOfSyncV1Trap": hzIduModemTxLossOfSyncV1Trap,
       "hzIduModemTxLossOfSyncClearedV1Trap": hzIduModemTxLossOfSyncClearedV1Trap,
       "hzIduModemSnrBelowThresholdV1Trap": hzIduModemSnrBelowThresholdV1Trap,
       "hzIduModemSnrBelowThresholdClearedV1Trap": hzIduModemSnrBelowThresholdClearedV1Trap,
       "hzIduModemEqualizerStressExceedThresholdV1Trap": hzIduModemEqualizerStressExceedThresholdV1Trap,
       "hzIduModemEqualizerStressExceedThresholdClearedV1Trap": hzIduModemEqualizerStressExceedThresholdClearedV1Trap,
       "hzIduEnetPort1ChannelizedRslBelowThresholdV1Trap": hzIduEnetPort1ChannelizedRslBelowThresholdV1Trap,
       "hzIduEnetPort1ChannelizedRslBelowThresholdClearedV1Trap": hzIduEnetPort1ChannelizedRslBelowThresholdClearedV1Trap,
       "hzIduModemHardwareFaultV1Trap": hzIduModemHardwareFaultV1Trap,
       "hzIduModemHardwareFaultClearedV1Trap": hzIduModemHardwareFaultClearedV1Trap,
       "hzIduModemProgrammingErrorV1Trap": hzIduModemProgrammingErrorV1Trap,
       "hzIduModemProgrammingErrorClearedrV1Trap": hzIduModemProgrammingErrorClearedrV1Trap,
       "hzIduTtySessionCommencedV1Trap": hzIduTtySessionCommencedV1Trap,
       "hzIduTtySessionTerminatedV1Trap": hzIduTtySessionTerminatedV1Trap,
       "hzIduAtpcTxAtMaxPwrV1Trap": hzIduAtpcTxAtMaxPwrV1Trap,
       "hzIduAtpcTxAtMaxPwrClearedV1Trap": hzIduAtpcTxAtMaxPwrClearedV1Trap,
       "hzIduRadioPLDROLostLockV1Trap": hzIduRadioPLDROLostLockV1Trap,
       "hzIduRadioPLDROLostLockClearedV1Trap": hzIduRadioPLDROLostLockClearedV1Trap,
       "hzIduRadioLostCommunicationV1Trap": hzIduRadioLostCommunicationV1Trap,
       "hzIduRadioLostCommunicationClearedV1Trap": hzIduRadioLostCommunicationClearedV1Trap,
       "hzIduRadioMismatchV1Trap": hzIduRadioMismatchV1Trap,
       "hzIduRadioMismatchClearedV1Trap": hzIduRadioMismatchClearedV1Trap,
       "hzIduRadioPowerAmpV1Trap": hzIduRadioPowerAmpV1Trap,
       "hzIduRadioPowerAmpClearedV1Trap": hzIduRadioPowerAmpClearedV1Trap,
       "hzIduRadioExcessiveTxCableLossV1Trap": hzIduRadioExcessiveTxCableLossV1Trap,
       "hzIduRadioExcessiveTxCableLossClearedV1Trap": hzIduRadioExcessiveTxCableLossClearedV1Trap,
       "hzIduHiPowerRadioDrainM1V1Trap": hzIduHiPowerRadioDrainM1V1Trap,
       "hzIduHiPowerRadioDrainM1ClearedV1Trap": hzIduHiPowerRadioDrainM1ClearedV1Trap,
       "hzIduHiPowerRadioDrainM2V1Trap": hzIduHiPowerRadioDrainM2V1Trap,
       "hzIduHiPowerRadioDrainM2ClearedV1Trap": hzIduHiPowerRadioDrainM2ClearedV1Trap,
       "hzIduHiPowerRadioTxDetectorV1Trap": hzIduHiPowerRadioTxDetectorV1Trap,
       "hzIduHiPowerRadioTxDetectorClearedV1Trap": hzIduHiPowerRadioTxDetectorClearedV1Trap,
       "hzIduSecondaryRadioIsActiveV1Trap": hzIduSecondaryRadioIsActiveV1Trap,
       "hzIduSecondaryRadioIsActiveClearedV1Trap": hzIduSecondaryRadioIsActiveClearedV1Trap,
       "hzIduRedundancySerialNumberMisMatchV1Trap": hzIduRedundancySerialNumberMisMatchV1Trap,
       "hzIduRedundancySerialNumberMisMatchClearedV1Trap": hzIduRedundancySerialNumberMisMatchClearedV1Trap,
       "hzIduRadioFirmwareMismatchV1Trap": hzIduRadioFirmwareMismatchV1Trap,
       "hzIduRadioFirmwareMismatchClearedV1Trap": hzIduRadioFirmwareMismatchClearedV1Trap,
       "hzIduSecondaryRadioNotdetectedV1Trap": hzIduSecondaryRadioNotdetectedV1Trap,
       "hzIduSecondaryRadioNotdetectedClearedV1Trap": hzIduSecondaryRadioNotdetectedClearedV1Trap,
       "hzIduPrimaryRadioNotdetectedV1Trap": hzIduPrimaryRadioNotdetectedV1Trap,
       "hzIduPrimaryRadioNotdetectedClearedV1Trap": hzIduPrimaryRadioNotdetectedClearedV1Trap,
       "hzIduFaultyPrimaryRadioV1Trap": hzIduFaultyPrimaryRadioV1Trap,
       "hzIduFaultyPrimaryRadioClearedV1Trap": hzIduFaultyPrimaryRadioClearedV1Trap,
       "hzIduRadioExcessiveTxCableLossChangeV1Trap": hzIduRadioExcessiveTxCableLossChangeV1Trap,
       "hzIduRadioExcessiveTxCableLossChangeClearedV1Trap": hzIduRadioExcessiveTxCableLossChangeClearedV1Trap,
       "hzIduExcessiveRxCableLossV1Trap": hzIduExcessiveRxCableLossV1Trap,
       "hzIduExcessiveRxCableLossClearedV1Trap": hzIduExcessiveRxCableLossClearedV1Trap,
       "hzIduRedundancyPrimaryPortNotSetV1Trap": hzIduRedundancyPrimaryPortNotSetV1Trap,
       "hzIduRedundancyPrimaryPortNotSetClearedV1Trap": hzIduRedundancyPrimaryPortNotSetClearedV1Trap,
       "hzIduRedundancySecondaryPortIsActiveV1Trap": hzIduRedundancySecondaryPortIsActiveV1Trap,
       "hzIduRedundancySecondaryPortIsActiveClearedV1Trap": hzIduRedundancySecondaryPortIsActiveClearedV1Trap,
       "hzIduRedundancyPrimaryPortFaultyV1Trap": hzIduRedundancyPrimaryPortFaultyV1Trap,
       "hzIduRedundancyPrimaryPortFaultyClearedV1Trap": hzIduRedundancyPrimaryPortFaultyClearedV1Trap,
       "hzIduRedundancySecondaryPortFaultyV1Trap": hzIduRedundancySecondaryPortFaultyV1Trap,
       "hzIduRedundancySecondaryPortFaultyClearedV1Trap": hzIduRedundancySecondaryPortFaultyClearedV1Trap,
       "hzIduFan1FailedV1Trap": hzIduFan1FailedV1Trap,
       "hzIduFan1FailureClearedV1Trap": hzIduFan1FailureClearedV1Trap,
       "hzIduFan2FailedV1Trap": hzIduFan2FailedV1Trap,
       "hzIduFan2FailureClearedV1Trap": hzIduFan2FailureClearedV1Trap,
       "hzIduFan3FailedV1Trap": hzIduFan3FailedV1Trap,
       "hzIduFan3FailureClearedV1Trap": hzIduFan3FailureClearedV1Trap,
       "hzIduFan4FailedV1Trap": hzIduFan4FailedV1Trap,
       "hzIduFan4FailureClearedV1Trap": hzIduFan4FailureClearedV1Trap,
       "hzIduRlsShutdownActivatedv1Trap": hzIduRlsShutdownActivatedv1Trap,
       "hzIduRlsShutdownActivatedClearedV1Trap": hzIduRlsShutdownActivatedClearedV1Trap,
       "hzIduSnmpTrapHostTable": hzIduSnmpTrapHostTable,
       "hzIduSnmpTrapHostEntry": hzIduSnmpTrapHostEntry,
       "hzIduSnmpTrapHostIndex": hzIduSnmpTrapHostIndex,
       "hzIduSnmpTrapHostMode": hzIduSnmpTrapHostMode,
       "hzIduSnmpTrapHostIpAddress": hzIduSnmpTrapHostIpAddress,
       "hzIduSnmpTrapHostCommunityName": hzIduSnmpTrapHostCommunityName,
       "hzIduSnmpTrapHostActivated": hzIduSnmpTrapHostActivated,
       "hzIduSnmpV3TrapHostsTable": hzIduSnmpV3TrapHostsTable,
       "hzIduSnmpV3TrapHostsEntry": hzIduSnmpV3TrapHostsEntry,
       "hzIduSnmpV3TrapHostsIndex": hzIduSnmpV3TrapHostsIndex,
       "snmpV3TrapHostIpAddress": snmpV3TrapHostIpAddress,
       "snmpV3TrapHostUserName": snmpV3TrapHostUserName,
       "snmpV3TrapHostAuthProtocol": snmpV3TrapHostAuthProtocol,
       "snmpV3TrapHostAuthPassword": snmpV3TrapHostAuthPassword,
       "snmpV3TrapHostPrivProtocol": snmpV3TrapHostPrivProtocol,
       "snmpV3TrapHostPrivPassword": snmpV3TrapHostPrivPassword,
       "snmpV3TrapHostActivated": snmpV3TrapHostActivated,
       "hzIduTrapEnable": hzIduTrapEnable,
       "hzIduColdStartTrap": hzIduColdStartTrap,
       "hzIduLinkDownTrap": hzIduLinkDownTrap,
       "hzIduLinkUpTrap": hzIduLinkUpTrap,
       "hzIduExplicitAuthenticationFailureTrap": hzIduExplicitAuthenticationFailureTrap,
       "hzIduAamConfigMismatchTrap": hzIduAamConfigMismatchTrap,
       "hzIduAamActiveTrap": hzIduAamActiveTrap,
       "hzIduAtpcConfigMismatchTrap": hzIduAtpcConfigMismatchTrap,
       "hzIduSntpServersUnreachableTrap": hzIduSntpServersUnreachableTrap,
       "hzIduFrequencyFileInvalidTrap": hzIduFrequencyFileInvalidTrap,
       "hzIduEnetPortDroppedFramesThresholdExceedTrap": hzIduEnetPortDroppedFramesThresholdExceedTrap,
       "hzIduEnetPortBandwidthUtilizationThresholdExceedTrap": hzIduEnetPortBandwidthUtilizationThresholdExceedTrap,
       "hzIduEnetPortRlsMismatchTrap": hzIduEnetPortRlsMismatchTrap,
       "hzIduRLSQueueBasedShutdownActivatedTrap": hzIduRLSQueueBasedShutdownActivatedTrap,
       "hzIduModemRxLossOfSignalLockTrap": hzIduModemRxLossOfSignalLockTrap,
       "hzIduModemTxLossOfSyncTrap": hzIduModemTxLossOfSyncTrap,
       "hzIduModemSnrBelowThresholdTrap": hzIduModemSnrBelowThresholdTrap,
       "hzIduModemEqualizerStressExceedThresholdTrap": hzIduModemEqualizerStressExceedThresholdTrap,
       "hzIduModemChannelizedRslBelowThresholdTrap": hzIduModemChannelizedRslBelowThresholdTrap,
       "hzIduModemHardwareFaultTrap": hzIduModemHardwareFaultTrap,
       "hzIduModemProgrammingErrorTrap": hzIduModemProgrammingErrorTrap,
       "hzIduTtyManagementSessionCommencedTrap": hzIduTtyManagementSessionCommencedTrap,
       "hzIduTtyManagementSessionTerminatedTrap": hzIduTtyManagementSessionTerminatedTrap,
       "hzIduAtpcTxAtMaxPwrTrap": hzIduAtpcTxAtMaxPwrTrap,
       "hzIduRadioPLDROLostLockTrap": hzIduRadioPLDROLostLockTrap,
       "hzIduRadioLostCommunicationTrap": hzIduRadioLostCommunicationTrap,
       "hzIduRadioMismatchTrap": hzIduRadioMismatchTrap,
       "hzIduRadioPowerAmpTrap": hzIduRadioPowerAmpTrap,
       "hzIduRadioExcessiveTxCableLossTrap": hzIduRadioExcessiveTxCableLossTrap,
       "hzIduHiPowerRadioDrainM1Trap": hzIduHiPowerRadioDrainM1Trap,
       "hzIduHiPowerRadioDrainM2Trap": hzIduHiPowerRadioDrainM2Trap,
       "hzIduHiPowerRadioTxDetectorTrap": hzIduHiPowerRadioTxDetectorTrap,
       "hzIduSecondaryRadioIsActiveTrap": hzIduSecondaryRadioIsActiveTrap,
       "hzIduRedundancySerialNumberMisMatchTrap": hzIduRedundancySerialNumberMisMatchTrap,
       "hzIduRadioFirmwareMismatchTrap": hzIduRadioFirmwareMismatchTrap,
       "hzIduSecondaryRadioNotdetectedTrap": hzIduSecondaryRadioNotdetectedTrap,
       "hzIduPrimaryRadioNotdetectedTrap": hzIduPrimaryRadioNotdetectedTrap,
       "hzIduFaultyPrimaryRadioTrap": hzIduFaultyPrimaryRadioTrap,
       "hzIduRadioExcessiveTxCableLossChangeTrap": hzIduRadioExcessiveTxCableLossChangeTrap,
       "hzIduRadioExcessiveRxCableLossTrap": hzIduRadioExcessiveRxCableLossTrap,
       "hzIduRedundancyPrimaryPortNotSetTrap": hzIduRedundancyPrimaryPortNotSetTrap,
       "hzIduRedundancySecondaryPortIsActiveTrap": hzIduRedundancySecondaryPortIsActiveTrap,
       "hzIduRedundancyPrimaryPortFaultyTrap": hzIduRedundancyPrimaryPortFaultyTrap,
       "hzIduRedundancySecondaryPortFaultyTrap": hzIduRedundancySecondaryPortFaultyTrap,
       "hzIduFan1FailedTrap": hzIduFan1FailedTrap,
       "hzIduFan2FailedTrap": hzIduFan2FailedTrap,
       "hzIduFan3FailedTrap": hzIduFan3FailedTrap,
       "hzIduFan4FailedTrap": hzIduFan4FailedTrap,
       "hzIduPortRLSShutdownActivatedTrap": hzIduPortRLSShutdownActivatedTrap,
       "hzIduSnmp": hzIduSnmp,
       "hzIduSnmpUserAccess": hzIduSnmpUserAccess,
       "hzIduSnmpManagerAnyCommunityName": hzIduSnmpManagerAnyCommunityName,
       "hzIduSnmpSetRequests": hzIduSnmpSetRequests,
       "hzIduSnmpManagersTable": hzIduSnmpManagersTable,
       "hzIduSnmpManagersEntry": hzIduSnmpManagersEntry,
       "hzIduSnmpManagersIndex": hzIduSnmpManagersIndex,
       "hzIduSnmpManagerIpAddress": hzIduSnmpManagerIpAddress,
       "hzIduSnmpManagerCommunityName": hzIduSnmpManagerCommunityName,
       "hzIduSnmpManagerActivated": hzIduSnmpManagerActivated,
       "hzIduSnmpV3ManagersTable": hzIduSnmpV3ManagersTable,
       "hzIduSnmpV3ManagersEntry": hzIduSnmpV3ManagersEntry,
       "hzIduSnmpV3ManagersIndex": hzIduSnmpV3ManagersIndex,
       "hzIduSnmpV3ManagerUserName": hzIduSnmpV3ManagerUserName,
       "hzIduSnmpV3ManagerAuthProtocol": hzIduSnmpV3ManagerAuthProtocol,
       "hzIduSnmpV3ManagerAuthPassword": hzIduSnmpV3ManagerAuthPassword,
       "hzIduSnmpV3ManagerPrivProtocol": hzIduSnmpV3ManagerPrivProtocol,
       "hzIduSnmpV3ManagerPrivPassword": hzIduSnmpV3ManagerPrivPassword,
       "hzIduSnmpV3ManagerActivated": hzIduSnmpV3ManagerActivated,
       "hzIduManagementSessions": hzIduManagementSessions,
       "hzIduTtySessionUserTable": hzIduTtySessionUserTable,
       "hzIduTtySessionUserEntry": hzIduTtySessionUserEntry,
       "hzIduTtySessionUserIndex": hzIduTtySessionUserIndex,
       "hzIduTtySessionUserName": hzIduTtySessionUserName,
       "hzIduTtySessionUserConnectionType": hzIduTtySessionUserConnectionType,
       "hzIduTtySessionUserState": hzIduTtySessionUserState,
       "hzIduHttp": hzIduHttp,
       "hzIduHttpEnable": hzIduHttpEnable,
       "hzIduHttpSecure": hzIduHttpSecure,
       "hzIduHttpSecureCertificateStatus": hzIduHttpSecureCertificateStatus,
       "hzIduHttpSecureAccessForAdminUsers": hzIduHttpSecureAccessForAdminUsers,
       "hzIduHttpSecureAccessForNocUsers": hzIduHttpSecureAccessForNocUsers,
       "hzIduHttpSecureAccessForSuperUsers": hzIduHttpSecureAccessForSuperUsers,
       "hzIduQos": hzIduQos,
       "hzIduQosEnable": hzIduQosEnable,
       "hzIduCosType": hzIduCosType,
       "hzIduCoSQinQiTag": hzIduCoSQinQiTag,
       "hzIduCoSQinQoTag": hzIduCoSQinQoTag,
       "hzIduCosQueueMapping": hzIduCosQueueMapping,
       "hzIduCosExpediteQueue": hzIduCosExpediteQueue,
       "hzIduCosQueueCIR": hzIduCosQueueCIR,
       "hzIduCosQueueCBS": hzIduCosQueueCBS,
       "hzIduCosDefaultValue": hzIduCosDefaultValue,
       "hzIduCutThroughProcessing": hzIduCutThroughProcessing,
       "hzIduQosPolicy": hzIduQosPolicy,
       "hzIduCosWfqWeight": hzIduCosWfqWeight,
       "hzIduRapidLinkShutdown": hzIduRapidLinkShutdown,
       "hzIduRlsEnable": hzIduRlsEnable,
       "hzIduRlsHardFaultMonitor": hzIduRlsHardFaultMonitor,
       "hzIduRlsWirelessPortOption": hzIduRlsWirelessPortOption,
       "hzIduRlsAutomaticLinkReestablish": hzIduRlsAutomaticLinkReestablish,
       "hzIduRlsManualLinkReestablish": hzIduRlsManualLinkReestablish,
       "hzIduWriteRlsMonitorParametersToSystem": hzIduWriteRlsMonitorParametersToSystem,
       "hzIduRlsDroppedFramesThresholdOverride": hzIduRlsDroppedFramesThresholdOverride,
       "hzIduRlsDroppedFramesThresholdTable": hzIduRlsDroppedFramesThresholdTable,
       "hzIduRlsDroppedFramesThresholdEntry": hzIduRlsDroppedFramesThresholdEntry,
       "hzIduRlsDroppedFramesThresholdIndex": hzIduRlsDroppedFramesThresholdIndex,
       "hzIduRlsAllowedDroppedFrameRateValue": hzIduRlsAllowedDroppedFrameRateValue,
       "hzIduRlsDroppedFrameMonitorPeriod": hzIduRlsDroppedFrameMonitorPeriod,
       "hzIduRlsSoftFaultMonitorTable": hzIduRlsSoftFaultMonitorTable,
       "hzIduRlsSoftFaultMonitorEntry": hzIduRlsSoftFaultMonitorEntry,
       "hzIduRlsSoftFaultMonitorIndex": hzIduRlsSoftFaultMonitorIndex,
       "hzIduRlsEstablishErredFrameThreshold": hzIduRlsEstablishErredFrameThreshold,
       "hzIduRlsShutdownErredFrameThreshold": hzIduRlsShutdownErredFrameThreshold,
       "hzIduRlsEstablishNumberOfSamples": hzIduRlsEstablishNumberOfSamples,
       "hzIduRlsShutdownNumberOfSamples": hzIduRlsShutdownNumberOfSamples,
       "hzIduRlsEstablishSamplePeriod": hzIduRlsEstablishSamplePeriod,
       "hzIduRlsShutdownSamplePeriod": hzIduRlsShutdownSamplePeriod,
       "hzIduRlsQuickShutdownSamplePeriod": hzIduRlsQuickShutdownSamplePeriod,
       "hzIduHardFaultMonitorTable": hzIduHardFaultMonitorTable,
       "hzIduHardFaultMonitorEntry": hzIduHardFaultMonitorEntry,
       "hzIduHardFaultMonitorIndex": hzIduHardFaultMonitorIndex,
       "hzIduRlsHardFaultSamplePeriod": hzIduRlsHardFaultSamplePeriod,
       "hzIduRlsHardFaultThreshold": hzIduRlsHardFaultThreshold,
       "hzIduRlsReceiveSignalLevelMonitorTable": hzIduRlsReceiveSignalLevelMonitorTable,
       "hzIduRlsReceiveSignalLevelMonitorEntry": hzIduRlsReceiveSignalLevelMonitorEntry,
       "hzIduRlsReceiveSignalLevelMonitorIndex": hzIduRlsReceiveSignalLevelMonitorIndex,
       "hzIduRlsMakeRslMonitorRslValue": hzIduRlsMakeRslMonitorRslValue,
       "hzIduRlsMakeRslMonitorPeriod": hzIduRlsMakeRslMonitorPeriod,
       "hzIduRlsStatus": hzIduRlsStatus,
       "hzIduRlsCurrentDroppedFramesTable": hzIduRlsCurrentDroppedFramesTable,
       "hzIduRlsCurrentDroppedFramesEntry": hzIduRlsCurrentDroppedFramesEntry,
       "hzIduRlsCurrentDroppedFramesIndex": hzIduRlsCurrentDroppedFramesIndex,
       "hzIduRlsCurrentDroppedFramesRateValue": hzIduRlsCurrentDroppedFramesRateValue,
       "hzIduRlsCurrentDroppedFrameMonitorPeriod": hzIduRlsCurrentDroppedFrameMonitorPeriod,
       "hzIduRlsCurrentQueueStatus": hzIduRlsCurrentQueueStatus,
       "hzIduRlsStatusTable": hzIduRlsStatusTable,
       "hzIduRlsStatusEntry": hzIduRlsStatusEntry,
       "hzIduRlsStatusIndex": hzIduRlsStatusIndex,
       "hzIduRlsOption": hzIduRlsOption,
       "hzIduRlsState": hzIduRlsState,
       "hzIduRlsMismatchState": hzIduRlsMismatchState,
       "hzIduDegradeMonitorState": hzIduDegradeMonitorState,
       "hzIduHardFaultMonitorState": hzIduHardFaultMonitorState,
       "hzIduMakeRslThresholdState": hzIduMakeRslThresholdState,
       "hzIduPeerRlsState": hzIduPeerRlsState,
       "hzIduRadioInterfaceState": hzIduRadioInterfaceState,
       "hzIduNetworkInterfaceState": hzIduNetworkInterfaceState,
       "hzIduUserConfiguredEstablishFer": hzIduUserConfiguredEstablishFer,
       "hzIduMinimumAchievableEstablishFer": hzIduMinimumAchievableEstablishFer,
       "hzIduUserConfiguredShutdownFer": hzIduUserConfiguredShutdownFer,
       "hzIduMinimumAchievableShutdownFer": hzIduMinimumAchievableShutdownFer,
       "hzIduUserConfiguredEstablishMonitorTime": hzIduUserConfiguredEstablishMonitorTime,
       "hzIduActualEstablishMonitorTime": hzIduActualEstablishMonitorTime,
       "hzIduUserConfiguredShutdownMonitorTime": hzIduUserConfiguredShutdownMonitorTime,
       "hzIduActualShutdownMonitorTime": hzIduActualShutdownMonitorTime,
       "hzIduSntp": hzIduSntp,
       "hzIduSntpEnable": hzIduSntpEnable,
       "hzIduSntpOffset": hzIduSntpOffset,
       "hzIduSntpServerTable": hzIduSntpServerTable,
       "hzIduSntpServerEntry": hzIduSntpServerEntry,
       "hzIduSntpServerIndex": hzIduSntpServerIndex,
       "hzIduSntpServerIpAddress": hzIduSntpServerIpAddress,
       "hzIduSntpServerStatus": hzIduSntpServerStatus,
       "hzIduSntpServerStratum": hzIduSntpServerStratum,
       "hzIduLogs": hzIduLogs,
       "hzIduEventLogEnable": hzIduEventLogEnable,
       "hzIduPerfmLogEnable": hzIduPerfmLogEnable,
       "hzIduPerfmLogInterval": hzIduPerfmLogInterval,
       "hzIduRadius": hzIduRadius,
       "hzIduRadiusSuperUserAuthentication": hzIduRadiusSuperUserAuthentication,
       "hzIduRadiusServerTimeOut": hzIduRadiusServerTimeOut,
       "hzIduRadiusServerDeadTime": hzIduRadiusServerDeadTime,
       "hzIduRadiusServerReTransmit": hzIduRadiusServerReTransmit,
       "hzIduRadiusServerTable": hzIduRadiusServerTable,
       "hzIduRadiusServerEntry": hzIduRadiusServerEntry,
       "hzIduRadiusServerIndex": hzIduRadiusServerIndex,
       "hzIduRadiusCfgdHostIpAddress": hzIduRadiusCfgdHostIpAddress,
       "hzIduRadiusActiveHostIpAddress": hzIduRadiusActiveHostIpAddress}
)
