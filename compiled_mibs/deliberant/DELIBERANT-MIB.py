# SNMP MIB module (DELIBERANT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\deliberant\DELIBERANT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:25 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

deliberant = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32761)
)
if mibBuilder.loadTexts:
    deliberant.setRevisions(
        ("2008-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlbProducts_ObjectIdentity = ObjectIdentity
dlbProducts = _DlbProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 1)
)
_DlbAdmin_ObjectIdentity = ObjectIdentity
dlbAdmin = _DlbAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 2)
)
_DlbMgmt_ObjectIdentity = ObjectIdentity
dlbMgmt = _DlbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3)
)
_DlbExperimental_ObjectIdentity = ObjectIdentity
dlbExperimental = _DlbExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELIBERANT-MIB",
    **{"deliberant": deliberant,
       "dlbProducts": dlbProducts,
       "dlbAdmin": dlbAdmin,
       "dlbMgmt": dlbMgmt,
       "dlbExperimental": dlbExperimental}
)
