# SNMP MIB module (IBM-TN3270E-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ibm\IBM-TN3270E-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:00:45 2025
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

(IpAddress,) = mibBuilder.importSymbols(
    "SNMPv2-SMI-v1",
    "IpAddress")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(DisplayString,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibmtn3270eMIB_ObjectIdentity = ObjectIdentity
ibmtn3270eMIB = _Ibmtn3270eMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1)
)
_Ibmtn3270eConnRejectTable_Object = MibTable
ibmtn3270eConnRejectTable = _Ibmtn3270eConnRejectTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1)
)
if mibBuilder.loadTexts:
    ibmtn3270eConnRejectTable.setStatus("mandatory")
_Ibmtn3270eConnRejectEntry_Object = MibTableRow
ibmtn3270eConnRejectEntry = _Ibmtn3270eConnRejectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1)
)
ibmtn3270eConnRejectEntry.setIndexNames(
    (0, "IBM-TN3270E-MIB", "ibmtn3270eConnRejectIndex"),
)
if mibBuilder.loadTexts:
    ibmtn3270eConnRejectEntry.setStatus("mandatory")
_Ibmtn3270eConnRejectIndex_Type = Integer32
_Ibmtn3270eConnRejectIndex_Object = MibTableColumn
ibmtn3270eConnRejectIndex = _Ibmtn3270eConnRejectIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1, 1),
    _Ibmtn3270eConnRejectIndex_Type()
)
ibmtn3270eConnRejectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmtn3270eConnRejectIndex.setStatus("mandatory")


class _Ibmtn3270eConnRejectAddrType_Type(Integer32):
    """Custom type ibmtn3270eConnRejectAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_Ibmtn3270eConnRejectAddrType_Type.__name__ = "Integer32"
_Ibmtn3270eConnRejectAddrType_Object = MibTableColumn
ibmtn3270eConnRejectAddrType = _Ibmtn3270eConnRejectAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1, 2),
    _Ibmtn3270eConnRejectAddrType_Type()
)
ibmtn3270eConnRejectAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtn3270eConnRejectAddrType.setStatus("mandatory")


class _Ibmtn3270eConnRejectClient_Type(OctetString):
    """Custom type ibmtn3270eConnRejectClient based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ibmtn3270eConnRejectClient_Type.__name__ = "OctetString"
_Ibmtn3270eConnRejectClient_Object = MibTableColumn
ibmtn3270eConnRejectClient = _Ibmtn3270eConnRejectClient_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1, 3),
    _Ibmtn3270eConnRejectClient_Type()
)
ibmtn3270eConnRejectClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtn3270eConnRejectClient.setStatus("mandatory")


class _Ibmtn3270eConnRejectReason_Type(Integer32):
    """Custom type ibmtn3270eConnRejectReason based on Integer32"""
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
              40,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("noportinfo", 1),
          ("cliunknown", 2),
          ("clinoauth", 3),
          ("sockblock", 4),
          ("nodeterm", 5),
          ("createfail", 6),
          ("seqnum", 7),
          ("negfailed", 8),
          ("notelquale", 9),
          ("termtypefail", 10),
          ("notypeprtgen", 11),
          ("clirplyfail", 12),
          ("valtelquale", 13),
          ("clisendfail", 14),
          ("failtelquale", 15),
          ("termtypagain", 16),
          ("noportagain", 17),
          ("prtnoluname", 18),
          ("clinoauthent", 19),
          ("clinoauthflt", 20),
          ("noluconf", 21),
          ("noportmore", 22),
          ("noresource", 23),
          ("nameresource", 24),
          ("prtnoluagain", 25),
          ("noimplu", 26),
          ("lunotfound", 27),
          ("valluprt", 28),
          ("vallu", 29),
          ("prtlunofind", 30),
          ("nameinuse", 31),
          ("reqlunofind", 32),
          ("valprtagain", 33),
          ("valluagain", 34),
          ("luprtnofind", 35),
          ("poolluinuse", 36),
          ("poollunofind", 37),
          ("restypnofind", 38),
          ("poolluconf", 39),
          ("lucapreach", 40),
          ("noappnmem", 41),
          ("nomoreconn", 42),
          ("pooldep", 43),
          ("termnorsp", 44))
    )


_Ibmtn3270eConnRejectReason_Type.__name__ = "Integer32"
_Ibmtn3270eConnRejectReason_Object = MibTableColumn
ibmtn3270eConnRejectReason = _Ibmtn3270eConnRejectReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1, 4),
    _Ibmtn3270eConnRejectReason_Type()
)
ibmtn3270eConnRejectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtn3270eConnRejectReason.setStatus("mandatory")
_Ibmtn3270eConnRejectTime_Type = DisplayString
_Ibmtn3270eConnRejectTime_Object = MibTableColumn
ibmtn3270eConnRejectTime = _Ibmtn3270eConnRejectTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18, 1, 1, 1, 5),
    _Ibmtn3270eConnRejectTime_Type()
)
ibmtn3270eConnRejectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtn3270eConnRejectTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-TN3270E-MIB",
    **{"ibmtn3270eMIB": ibmtn3270eMIB,
       "ibmtn3270eConnRejectTable": ibmtn3270eConnRejectTable,
       "ibmtn3270eConnRejectEntry": ibmtn3270eConnRejectEntry,
       "ibmtn3270eConnRejectIndex": ibmtn3270eConnRejectIndex,
       "ibmtn3270eConnRejectAddrType": ibmtn3270eConnRejectAddrType,
       "ibmtn3270eConnRejectClient": ibmtn3270eConnRejectClient,
       "ibmtn3270eConnRejectReason": ibmtn3270eConnRejectReason,
       "ibmtn3270eConnRejectTime": ibmtn3270eConnRejectTime}
)
