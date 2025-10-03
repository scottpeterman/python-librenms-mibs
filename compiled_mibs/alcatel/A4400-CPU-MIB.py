# SNMP MIB module (A4400-CPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alcatel\A4400-CPU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:10 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alcatel_ObjectIdentity = ObjectIdentity
alcatel = _Alcatel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637)
)
_Abs_ObjectIdentity = ObjectIdentity
abs = _Abs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64)
)
_A4400_ObjectIdentity = ObjectIdentity
a4400 = _A4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400)
)
_A4400CPU_ObjectIdentity = ObjectIdentity
a4400CPU = _A4400CPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1)
)
_PbxMibVersion_Type = Integer32
_PbxMibVersion_Object = MibScalar
pbxMibVersion = _PbxMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 0),
    _PbxMibVersion_Type()
)
pbxMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbxMibVersion.setStatus("mandatory")
_PbxAgent_ObjectIdentity = ObjectIdentity
pbxAgent = _PbxAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1)
)
_Linux_ObjectIdentity = ObjectIdentity
linux = _Linux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1, 10)
)
_Unknown_ObjectIdentity = ObjectIdentity
unknown = _Unknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1, 255)
)


class _PbxState_Type(Integer32):
    """Custom type pbxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("normal", 5))
    )


_PbxState_Type.__name__ = "Integer32"
_PbxState_Object = MibScalar
pbxState = _PbxState_Object(
    (1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 2),
    _PbxState_Type()
)
pbxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbxState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A4400-CPU-MIB",
    **{"alcatel": alcatel,
       "abs": abs,
       "a4400": a4400,
       "a4400CPU": a4400CPU,
       "pbxMibVersion": pbxMibVersion,
       "pbxAgent": pbxAgent,
       "linux": linux,
       "unknown": unknown,
       "pbxState": pbxState}
)
