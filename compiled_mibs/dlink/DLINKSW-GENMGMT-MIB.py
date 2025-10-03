# SNMP MIB module (DLINKSW-GENMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-GENMGMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:08 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

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

dlinkSwGenMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 165)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DGenMgmtMIBNotifications_ObjectIdentity = ObjectIdentity
dGenMgmtMIBNotifications = _DGenMgmtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 165, 0)
)
_DGenMgmtMIBObjects_ObjectIdentity = ObjectIdentity
dGenMgmtMIBObjects = _DGenMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 165, 1)
)
_DGenMgmtNotifyInfos_ObjectIdentity = ObjectIdentity
dGenMgmtNotifyInfos = _DGenMgmtNotifyInfos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 165, 1, 1)
)


class _DGenMgmtNotifyInfoLoginType_Type(Integer32):
    """Custom type dGenMgmtNotifyInfoLoginType based on Integer32"""
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
        *(("console", 1),
          ("telnet", 2),
          ("ssh", 3),
          ("web", 4))
    )


_DGenMgmtNotifyInfoLoginType_Type.__name__ = "Integer32"
_DGenMgmtNotifyInfoLoginType_Object = MibScalar
dGenMgmtNotifyInfoLoginType = _DGenMgmtNotifyInfoLoginType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 165, 1, 1, 1),
    _DGenMgmtNotifyInfoLoginType_Type()
)
dGenMgmtNotifyInfoLoginType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dGenMgmtNotifyInfoLoginType.setStatus("current")
_DGenMgmtNotifyInfoUserName_Type = DisplayString
_DGenMgmtNotifyInfoUserName_Object = MibScalar
dGenMgmtNotifyInfoUserName = _DGenMgmtNotifyInfoUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 165, 1, 1, 2),
    _DGenMgmtNotifyInfoUserName_Type()
)
dGenMgmtNotifyInfoUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dGenMgmtNotifyInfoUserName.setStatus("current")
_DGenMgmtMIBConformance_ObjectIdentity = ObjectIdentity
dGenMgmtMIBConformance = _DGenMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 165, 2)
)

# Managed Objects groups


# Notification objects

dGenMgmtLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 165, 0, 1)
)
dGenMgmtLoginFail.setObjects(
      *(("DLINKSW-GENMGMT-MIB", "dGenMgmtNotifyInfoLoginType"),
        ("DLINKSW-GENMGMT-MIB", "dGenMgmtNotifyInfoUserName"))
)
if mibBuilder.loadTexts:
    dGenMgmtLoginFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-GENMGMT-MIB",
    **{"dlinkSwGenMgmtMIB": dlinkSwGenMgmtMIB,
       "dGenMgmtMIBNotifications": dGenMgmtMIBNotifications,
       "dGenMgmtLoginFail": dGenMgmtLoginFail,
       "dGenMgmtMIBObjects": dGenMgmtMIBObjects,
       "dGenMgmtNotifyInfos": dGenMgmtNotifyInfos,
       "dGenMgmtNotifyInfoLoginType": dGenMgmtNotifyInfoLoginType,
       "dGenMgmtNotifyInfoUserName": dGenMgmtNotifyInfoUserName,
       "dGenMgmtMIBConformance": dGenMgmtMIBConformance}
)
