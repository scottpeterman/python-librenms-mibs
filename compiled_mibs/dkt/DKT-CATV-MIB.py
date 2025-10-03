# SNMP MIB module (DKT-CATV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dkt\DKT-CATV-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:26 2025
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

catvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _CatvVersion_Type(OctetString):
    """Custom type catvVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CatvVersion_Type.__name__ = "OctetString"
_CatvVersion_Object = MibScalar
catvVersion = _CatvVersion_Object(
    (1, 3, 6, 1, 4, 1, 27304, 11, 1),
    _CatvVersion_Type()
)
catvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvVersion.setStatus("current")
_CatvSwitch_Type = Integer32
_CatvSwitch_Object = MibScalar
catvSwitch = _CatvSwitch_Object(
    (1, 3, 6, 1, 4, 1, 27304, 11, 2),
    _CatvSwitch_Type()
)
catvSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catvSwitch.setStatus("current")
_CatvSignalDetect_Type = Integer32
_CatvSignalDetect_Object = MibScalar
catvSignalDetect = _CatvSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 27304, 11, 3),
    _CatvSignalDetect_Type()
)
catvSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvSignalDetect.setStatus("current")

# Managed Objects groups

catvModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27304, 11, 4)
)
catvModuleGroup.setObjects(
      *(("DKT-CATV-MIB", "catvVersion"),
        ("DKT-CATV-MIB", "catvSwitch"),
        ("DKT-CATV-MIB", "catvSignalDetect"))
)
if mibBuilder.loadTexts:
    catvModuleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKT-CATV-MIB",
    **{"catvMIB": catvMIB,
       "catvVersion": catvVersion,
       "catvSwitch": catvSwitch,
       "catvSignalDetect": catvSignalDetect,
       "catvModuleGroup": catvModuleGroup}
)
