# SNMP MIB module (DLINK-ID-REC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINK-ID-REC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:32 2025
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



class AgentNotifyLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("warning", 1),
          ("information", 2),
          ("emergency", 3),
          ("alert", 4),
          ("error", 5),
          ("notice", 6),
          ("debug", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Dlink_products_ObjectIdentity = ObjectIdentity
dlink_products = _Dlink_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10)
)
_Dlink_mgmt_ObjectIdentity = ObjectIdentity
dlink_mgmt = _Dlink_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11)
)
_Dlink_common_mgmt_ObjectIdentity = ObjectIdentity
dlink_common_mgmt = _Dlink_common_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12)
)
_DlinkIndustrialCommon_ObjectIdentity = ObjectIdentity
dlinkIndustrialCommon = _DlinkIndustrialCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14)
)
_Dlink_broadband_products_ObjectIdentity = ObjectIdentity
dlink_broadband_products = _Dlink_broadband_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 30)
)
_Dlink_broadband_mgmt_ObjectIdentity = ObjectIdentity
dlink_broadband_mgmt = _Dlink_broadband_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 31)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-ID-REC-MIB",
    **{"AgentNotifyLevel": AgentNotifyLevel,
       "dlink": dlink,
       "dlink-products": dlink_products,
       "dlink-mgmt": dlink_mgmt,
       "dlink-common-mgmt": dlink_common_mgmt,
       "dlinkIndustrialCommon": dlinkIndustrialCommon,
       "dlink-broadband-products": dlink_broadband_products,
       "dlink-broadband-mgmt": dlink_broadband_mgmt}
)
