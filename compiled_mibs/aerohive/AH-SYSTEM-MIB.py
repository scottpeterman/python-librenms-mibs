# SNMP MIB module (AH-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\aerohive\AH-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:07 2025
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

(ahProduct,) = mibBuilder.importSymbols(
    "AH-SMI-MIB",
    "ahProduct")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ahSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AhSystemName_Type(DisplayString):
    """Custom type ahSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AhSystemName_Type.__name__ = "DisplayString"
_AhSystemName_Object = MibScalar
ahSystemName = _AhSystemName_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 1),
    _AhSystemName_Type()
)
ahSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahSystemName.setStatus("current")


class _AhSystemDescription_Type(DisplayString):
    """Custom type ahSystemDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AhSystemDescription_Type.__name__ = "DisplayString"
_AhSystemDescription_Object = MibScalar
ahSystemDescription = _AhSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 2),
    _AhSystemDescription_Type()
)
ahSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahSystemDescription.setStatus("current")


class _AhCpuUtilization_Type(Integer32):
    """Custom type ahCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AhCpuUtilization_Type.__name__ = "Integer32"
_AhCpuUtilization_Object = MibScalar
ahCpuUtilization = _AhCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 3),
    _AhCpuUtilization_Type()
)
ahCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahCpuUtilization.setStatus("current")


class _AhMemUtilization_Type(Integer32):
    """Custom type ahMemUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AhMemUtilization_Type.__name__ = "Integer32"
_AhMemUtilization_Object = MibScalar
ahMemUtilization = _AhMemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 4),
    _AhMemUtilization_Type()
)
ahMemUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahMemUtilization.setStatus("current")


class _AhSystemSerial_Type(DisplayString):
    """Custom type ahSystemSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AhSystemSerial_Type.__name__ = "DisplayString"
_AhSystemSerial_Object = MibScalar
ahSystemSerial = _AhSystemSerial_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 5),
    _AhSystemSerial_Type()
)
ahSystemSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahSystemSerial.setStatus("current")


class _AhDeviceMode_Type(DisplayString):
    """Custom type ahDeviceMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AhDeviceMode_Type.__name__ = "DisplayString"
_AhDeviceMode_Object = MibScalar
ahDeviceMode = _AhDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 6),
    _AhDeviceMode_Type()
)
ahDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahDeviceMode.setStatus("current")


class _AhUpTime_Type(DisplayString):
    """Custom type ahUpTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AhUpTime_Type.__name__ = "DisplayString"
_AhUpTime_Object = MibScalar
ahUpTime = _AhUpTime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 7),
    _AhUpTime_Type()
)
ahUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahUpTime.setStatus("current")


class _AhHwVersion_Type(DisplayString):
    """Custom type ahHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AhHwVersion_Type.__name__ = "DisplayString"
_AhHwVersion_Object = MibScalar
ahHwVersion = _AhHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 8),
    _AhHwVersion_Type()
)
ahHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahHwVersion.setStatus("current")


class _AhClientCount_Type(Integer32):
    """Custom type ahClientCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AhClientCount_Type.__name__ = "Integer32"
_AhClientCount_Object = MibScalar
ahClientCount = _AhClientCount_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 9),
    _AhClientCount_Type()
)
ahClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientCount.setStatus("current")


class _AhEnvirmentTemp_Type(Integer32):
    """Custom type ahEnvirmentTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AhEnvirmentTemp_Type.__name__ = "Integer32"
_AhEnvirmentTemp_Object = MibScalar
ahEnvirmentTemp = _AhEnvirmentTemp_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 10),
    _AhEnvirmentTemp_Type()
)
ahEnvirmentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahEnvirmentTemp.setStatus("current")


class _AhEnvirmentFan_Type(Integer32):
    """Custom type ahEnvirmentFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AhEnvirmentFan_Type.__name__ = "Integer32"
_AhEnvirmentFan_Object = MibScalar
ahEnvirmentFan = _AhEnvirmentFan_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 11),
    _AhEnvirmentFan_Type()
)
ahEnvirmentFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahEnvirmentFan.setStatus("current")


class _AhFirmwareVersion_Type(DisplayString):
    """Custom type ahFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AhFirmwareVersion_Type.__name__ = "DisplayString"
_AhFirmwareVersion_Object = MibScalar
ahFirmwareVersion = _AhFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 2, 12),
    _AhFirmwareVersion_Type()
)
ahFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahFirmwareVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AH-SYSTEM-MIB",
    **{"ahSystem": ahSystem,
       "ahSystemName": ahSystemName,
       "ahSystemDescription": ahSystemDescription,
       "ahCpuUtilization": ahCpuUtilization,
       "ahMemUtilization": ahMemUtilization,
       "ahSystemSerial": ahSystemSerial,
       "ahDeviceMode": ahDeviceMode,
       "ahUpTime": ahUpTime,
       "ahHwVersion": ahHwVersion,
       "ahClientCount": ahClientCount,
       "ahEnvirmentTemp": ahEnvirmentTemp,
       "ahEnvirmentFan": ahEnvirmentFan,
       "ahFirmwareVersion": ahFirmwareVersion}
)
