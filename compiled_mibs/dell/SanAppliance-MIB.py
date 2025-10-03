# SNMP MIB module (SanAppliance-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\SanAppliance-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:18 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893)
)
_SanRoot_ObjectIdentity = ObjectIdentity
sanRoot = _SanRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2)
)
_SanAppliance_ObjectIdentity = ObjectIdentity
sanAppliance = _SanAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 1)
)


class _SanApplGlobalStatus_Type(Integer32):
    """Custom type sanApplGlobalStatus based on Integer32"""
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
        *(("critical", 1),
          ("warning", 2),
          ("normal", 3),
          ("unknown", 4))
    )


_SanApplGlobalStatus_Type.__name__ = "Integer32"
_SanApplGlobalStatus_Object = MibScalar
sanApplGlobalStatus = _SanApplGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 1),
    _SanApplGlobalStatus_Type()
)
sanApplGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanApplGlobalStatus.setStatus("mandatory")
_SanApplEvts_ObjectIdentity = ObjectIdentity
sanApplEvts = _SanApplEvts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200)
)
_SanApplName_Type = OctetString
_SanApplName_Object = MibScalar
sanApplName = _SanApplName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200, 1),
    _SanApplName_Type()
)
sanApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanApplName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sanApplFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200, 0, 1)
)
sanApplFailed.setObjects(
    ("SanAppliance-MIB", "sanApplName")
)
if mibBuilder.loadTexts:
    sanApplFailed.setStatus(
        ""
    )

sanApplNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200, 0, 2)
)
sanApplNormal.setObjects(
    ("SanAppliance-MIB", "sanApplName")
)
if mibBuilder.loadTexts:
    sanApplNormal.setStatus(
        ""
    )

sanApplStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200, 0, 3)
)
sanApplStarted.setObjects(
    ("SanAppliance-MIB", "sanApplName")
)
if mibBuilder.loadTexts:
    sanApplStarted.setStatus(
        ""
    )

sanApplStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200, 0, 4)
)
sanApplStopped.setObjects(
    ("SanAppliance-MIB", "sanApplName")
)
if mibBuilder.loadTexts:
    sanApplStopped.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SanAppliance-MIB",
    **{"dell": dell,
       "storage": storage,
       "sanRoot": sanRoot,
       "sanAppliance": sanAppliance,
       "sanApplGlobalStatus": sanApplGlobalStatus,
       "sanApplEvts": sanApplEvts,
       "sanApplFailed": sanApplFailed,
       "sanApplNormal": sanApplNormal,
       "sanApplStarted": sanApplStarted,
       "sanApplStopped": sanApplStopped,
       "sanApplName": sanApplName}
)
