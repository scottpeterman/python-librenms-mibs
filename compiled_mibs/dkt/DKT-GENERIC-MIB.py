# SNMP MIB module (DKT-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dkt\DKT-GENERIC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:28 2025
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

(dkt,) = mibBuilder.importSymbols(
    "DKT-MIB",
    "dkt")

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

genericMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _HwVersion_Type(OctetString):
    """Custom type hwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HwVersion_Type.__name__ = "OctetString"
_HwVersion_Object = MibScalar
hwVersion = _HwVersion_Object(
    (1, 3, 6, 1, 4, 1, 27304, 10, 1),
    _HwVersion_Type()
)
hwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVersion.setStatus("current")


class _SwVersion_Type(OctetString):
    """Custom type swVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SwVersion_Type.__name__ = "OctetString"
_SwVersion_Object = MibScalar
swVersion = _SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 27304, 10, 2),
    _SwVersion_Type()
)
swVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersion.setStatus("current")
_Reboot_Type = Integer32
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 27304, 10, 3),
    _Reboot_Type()
)
reboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    reboot.setStatus("current")

# Managed Objects groups

genericModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27304, 10, 4)
)
genericModuleGroup.setObjects(
      *(("DKT-GENERIC-MIB", "hwVersion"),
        ("DKT-GENERIC-MIB", "swVersion"),
        ("DKT-GENERIC-MIB", "reboot"))
)
if mibBuilder.loadTexts:
    genericModuleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKT-GENERIC-MIB",
    **{"genericMIB": genericMIB,
       "hwVersion": hwVersion,
       "swVersion": swVersion,
       "reboot": reboot,
       "genericModuleGroup": genericModuleGroup}
)
