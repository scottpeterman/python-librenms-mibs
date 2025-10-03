# SNMP MIB module (BROADCOM-REF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\BROADCOM-REF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:30 2025
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

(dellLan,
 dellLanExtension) = mibBuilder.importSymbols(
    "Dell-Vendor-MIB",
    "dellLan",
    "dellLanExtension")

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

lvl7 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132)
)
if mibBuilder.loadTexts:
    lvl7.setRevisions(
        ("2003-11-21 00:00",
         "2003-02-06 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentPortMask(TextualConvention, OctetString):
    status = "current"
    displayHint = "255x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Dell6224Switch_ObjectIdentity = ObjectIdentity
dell6224Switch = _Dell6224Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3010)
)
_Dell6248Switch_ObjectIdentity = ObjectIdentity
dell6248Switch = _Dell6248Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3011)
)
_Dell6224PSwitch_ObjectIdentity = ObjectIdentity
dell6224PSwitch = _Dell6224PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3012)
)
_Dell6248PSwitch_ObjectIdentity = ObjectIdentity
dell6248PSwitch = _Dell6248PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3013)
)
_Dell6224FSwitch_ObjectIdentity = ObjectIdentity
dell6224FSwitch = _Dell6224FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3014)
)
_DellM6220Switch_ObjectIdentity = ObjectIdentity
dellM6220Switch = _DellM6220Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3015)
)
_Lvl7Products_ObjectIdentity = ObjectIdentity
lvl7Products = _Lvl7Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1)
)
_FastPath_ObjectIdentity = ObjectIdentity
fastPath = _FastPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROADCOM-REF-MIB",
    **{"AgentPortMask": AgentPortMask,
       "dell6224Switch": dell6224Switch,
       "dell6248Switch": dell6248Switch,
       "dell6224PSwitch": dell6224PSwitch,
       "dell6248PSwitch": dell6248PSwitch,
       "dell6224FSwitch": dell6224FSwitch,
       "dellM6220Switch": dellM6220Switch,
       "lvl7": lvl7,
       "lvl7Products": lvl7Products,
       "fastPath": fastPath}
)
